# bigDataContest-bytedance

本项目用以记录小队参加2019年字节跳动举办的大数据竞赛的各种模型、数据与相关资料。

比赛官网：https://www.kesci.com/home/competition/5cc51043f71088002c5b8840

正式赛题说明：https://www.kesci.com/home/competition/5cc51043f71088002c5b8840/content/1

Kaggle比赛经验：https://zhuanlan.zhihu.com/p/27424282

特征探索：https://www.kaggle.com/sudalairajkumar/simple-leaky-exploration-notebook-quora?scriptVersionId=1184830

## Dataset

- 数据集样例：参考`./legacy/data/大数据挑战赛_sample.txt`，用以理解数据集。
- 线下训练数据集：参考`./legacy/data/train.csv`，共2万条，用以线下训练模型。
- 线下测试数据集：参考`./legacy/data/test.csv`，仅用于梳理代码。
- 线上训练数据集，共1亿条数据，详细信息参考如下：

  ```bash
  <class 'pandas.core.frame.DataFrame'>
  RangeIndex: 100000000 entries, 0 to 99999999
  Data columns (total 5 columns):
  query_id          int64
  query             object
  query_title_id    int64
  title             object
  label             int64
  dtypes: int64(3), object(2)
  memory usage: 20.0 GB
  ```

- 线上测试数据集：共500万条，没有label信息。

## Code FrameWork

- `Stage1`：产生特征，包含手工特征与深度特征。
- `Stage2`：训练各类模型，如lightGBM、随机森林等。
- `Stage3`：模型整合。

## FrameWork OP

下面记录了一些平台相关的操作。

```bash
# 查看当前挂载的数据集目录
!ls /home/kesci/input/
# 查看数据集
!ls -lh /home/kesci/input/bytedance/first-round/
total 9.0G
-rw-r--r-- 1 kesci 1000 426M May 22 04:05 test.csv
-rw-r--r-- 1 kesci 1000 8.6G May 16 20:15 train.csv
# 查看个人持久化工作区文件
!ls /home/kesci/work/
# 查看当前kernerl下的package
!pip list --format=columns
# 显示cell运行时长
%load_ext klab-autotime
# 提交结果
!wget -nv -O kesci_submit https://www.heywhale.com/kesci_submit&&chmod +x kesci_submit
!./kesci_submit -token 490475a1ae106f67 -file submit.csv
```

## Question wait for solving

- 亿级别数据的处理问题？
  - 随机采样？
  - 顺序批量训练？
- 数据分析
  - 如何清洗和处理？将字符串feature转成数字列表？
  - 根据数据类型可以挖掘什么有用信息？
  - query与title存在什么关系？需要定量描述
  - 同一个query为什么有些title会被点击而其他title不会被点击？
  - 数据中的哪些特征会对标签的预测有帮助？
  - 统计分析：
    - 分析数值类变量的统计特征（如观察Label是否均衡），分析多个数值型变量的关系(相关系数，找到高相关的特征)
    - 文本变量，可以统计词频(TF)，TF-IDF，文本长度

## Data analysis

- 正负样本比例为1:3，分布不平衡不严重
- query与title中的单词数目对结果有一定影响，被点击条目的query单词数均值相比于未被点击的query均值较大（均值取log1p）；title关系则相反(均值取log1p，注：这个关系相比于query并不明显)。
- query与title公共的Unigram对结果影响不大，针对公共unigram的radio，被点击条目的radio整体相比于未点击条目略大（不明显）。
- 注意上面两条都存在离群值情况，需要处理，参考：https://zhuanlan.zhihu.com/p/33468998。
- query与title的出现交集对结果有较大影响，query_freq较小，title_freq较大，被点击的可能性增大。
- **我们应该尽可能多地抽取特征，只要你认为某个特征对解决问题有帮助，它就可以成为一个特征**
- 对于文本数据，有一些常规的Feature。比如，文本长度，Embeddings，TF-IDF，LDA，LSI等，你甚至可以用深度学习提取文本特征（隐藏层）
- 如果你想对数据有更深入的了解，可以通过思考数据集的构造过程来发现一些magic feature，这些特征有可能会大大提升效果。
- 特征选择的方法多种多样，最简单的是相关度系数(Correlation coefficient)，它主要是衡量两个变量之间的线性关系。Feature和Feature、Feature和Label。
- 不同种类的模型，我们用hyperopt的默认策略来搜索参数空间，将中间结果全保留下来。

## 一些心得

- https://zhuanlan.zhihu.com/p/60953933
  - 刚参加一个比赛，需要花点时间了解这个比赛的领域背景，甚至需要查一些资料或阅读一些文献，这对后面构建特征和选择模型很重要。我看到有很多 winners 分享经验说自己构建的大多数特征都是从商业(领域)层面思考得到的，所以领域的先验知识很重要。
  - 排名区，分 public LB 和 private LB。比赛方会将 test 数据集中一部分(比如 30%)拿出来做为 public LB 评分和排名，剩下的部分作为 private LB（也就是最终结果）的评分和排名。
  - 先训练一个baseline model, 然后在这个基础上不断优化、提升。我这里要补充的一个点是“零模型”，就是不用模型去做预测，一般就用全零或者全均值去做提交。GBDT已成为挖掘类比赛的主流算法，现成的包有xgboost、lightgbm、catboost，lightgbm因为速度快、准确度高脱颖而出。
  - 前期也需要尽可能多地尝试其他模型，机器学习领域有一个“没有免费午餐定律”，是说没有那种模型要比其他模型都好，不同的数据集可能适合不同的模型，这个只用通过尝试才知道。所以，打 kaggle 比赛，其实更像是不断地做数据实验。
  - 模型评估体系没建起来，其他任何探索都是盲目的，因为你没法确定好坏。这个很有讲究，你得判断 public LB 和 private LB 的得分是不是一致的或高度相关的。否则你可能在接下来的几个月中“一直努力拟合public LB”，结果却偏离了 private LB，这就是为何大牛一直告诫我们“Trust your CV”的原因。
  - 前期适当做一些调参，获取一组相对可以的参数就可以了，不用太花太多时间调参，因为它起得作用很有限。用这组参数和基模型来输出特征重要性。挑选重要的特征(比如top10)进行分析和构建新特征，然后测试，然后扩大范围(比如top20)重复以上过程。
  - 特征工程和模型融合是打 kaggle 比赛的两大利器，比赛后期基本就是尝试各种模型融合了。对于模型融合，大牛的观点：真正重要的是要有两三个强模型和很多相关性很小的弱模型，模型多样性很重要，弱一点也没关系。幸运的是我们每个人手里都有一个不错的模型，然后我又批量生成了一些弱模型，融合起来，取得了不错的效果。
- 文本相似度：https://blog.csdn.net/qq_28031525/article/details/79596376
- 词向量对比：https://zhuanlan.zhihu.com/p/56382372
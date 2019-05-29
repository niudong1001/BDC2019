# bigDataContest-bytedance

本项目用以记录小队参加2019年字节跳动举办的大数据竞赛的各种模型、数据与相关资料。

比赛官网：https://www.kesci.com/home/competition/5cc51043f71088002c5b8840

正式赛题说明：https://www.kesci.com/home/competition/5cc51043f71088002c5b8840/content/1

## 数据集

- 数据集样例：参考`data/大数据挑战赛_sample.txt`，用以理解数据集。

- 训练数据Sample：参考`data/train_data.csv`，可使用线下训练该数据集，再上传测试。

- 训练数据集：下面是训练数据的类型描述、内存占用等信息，

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

## 模型

- Baseline：参考`models/baseline.ipynb`，使用tfIdf+lr并随机采样1000万条数据建立Baseline模型。

## 平台相关操作

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


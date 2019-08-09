- 将query和title去重再在0维上拼接到一起效果最好
- 不加test部分在测试集上的效果会变差

- 代码片段

```python
# Two
df_train = ReadCSV(train_file, names=train_name, iterator=False)
df_test = ReadCSV(test_file, names=test_name,  iterator=False)
# df_test["title"] = df_test["title"].str.strip()
df_data = pd.concat([df_train[['query', 'title']], df_test[['query', 'title']]], axis=0)
del df_train, df_test; gc.collect()
# corpus =  pd.Series(
#     df_data['query'].unique().tolist() +
#     df_data['title'].unique().tolist()
# ).astype(str)
corpus = []
for i, line in df_data.iterrows():
  corpus.append("{} {}".format(line["query"], line["title"]))
# One
# df_train = ReadCSV(train_file, names=train_name, iterator=False)
# corpus =  pd.Series(
#     df_train['query'].unique().tolist() +
#     df_train['title'].unique().tolist()
# ).astype(str)
# print(corpus.shape)
```

```
if regen_word2vec_sen_vec_sim:
    ExtractFeature1(train_csv=train_file, test_csv=test_file, 
        train_name=train_name, test_name=test_name, 
        process_func=process_word2vec_sen_vec, 
        save_dir=feature_save_dir, 
        prefix=feature_prefix, 
        feature_name=feature_name)
```
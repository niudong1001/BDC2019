- 左右拼接效果较好

- 代码
```python
def PrepareWord2vecSamples(save_file):
    with Timer("prepare corpus"):
        df_train = ReadCSV(train_file, names=train_name, iterator=False)
        df_test = ReadCSV(test_file, names=test_name,  iterator=False)
        df_data = pd.concat([df_train[['query', 'title']], df_test[['query', 'title']]], axis=0)
        del df_train, df_test; gc.collect()
        corpus =  pd.Series(
            df_data['query'].unique().tolist() +
            df_data['title'].unique().tolist()
        ).astype(str)
    # with Timer("prepare corpus"):
    #     df_train = pd.read_csv(train_file, names=train_name)
    #     df_test = pd.read_csv(test_file, names=test_name)
    #     corpus = pd.concat([df_train[['query', 'title']], df_test[['query', 'title']]], axis=0)
    #     del df_train, df_test
    #     gc.collect()
    with Timer("save sentences"):
        with open(save_file, 'w') as f:
            line_count = 0
            # for i, line in corpus.iterrows():
            for i, line in corpus.items():
                # f.write("{} {}\n".format(line["query"], line["title"]))
                f.write("{}\n".format(line))
                line_count += 1
                if line_count % 10000000 == 0: 
                    print(f'Processed {line_count} lines.')
PrepareWord2vecSamples(word2vec_train_sentences)
```
1. 0.54092000
{                                                  
 "bagging_fraction": 0.9,
 "bagging_freq": 6.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.13,
 "max_bin": 1023,
 "min_data_in_leaf": 20.0,
 "num_iterations": 75.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.534976              
[40]	valid's binary_logloss: 0.53418               
[60]	valid's binary_logloss: 0.533889              
[20]	valid's binary_logloss: 0.535177              
[40]	valid's binary_logloss: 0.53439               
[60]	valid's binary_logloss: 0.534092              
[20]	valid's binary_logloss: 0.535119              
[40]	valid's binary_logloss: 0.53433               
[60]	valid's binary_logloss: 0.534042              
[20]	valid's binary_logloss: 0.535111              
[40]	valid's binary_logloss: 0.534289              
[60]	valid's binary_logloss: 0.533984              
[20]	valid's binary_logloss: 0.534924              
[40]	valid's binary_logloss: 0.534139              
[60]	valid's binary_logloss: 0.533875              
feature importance:                                
                                             column  importance
40                        online_testMagic_localCTR          71
36                       online_testWord2vec_cosine          71
1                  online_testTextMining_text_t-len          50
0                  online_testTextMining_text_q-len          47
5              online_testTextMining_unigrams_t-len          47
6       online_testTextMining_unigrams_qt-len-radio          43
16    online_testTextMining_unigrams_edit_set_ratio          31
9         online_testTextMining_text_edit_seq_ratio          28
14        online_testTextMining_unigrams_dice_ratio          28
41                                       query_freq          27
4              online_testTextMining_unigrams_q-len          24
3           online_testTextMining_text_tq-len-radio          24
12         online_testTextMining_text_partial_ratio          20
13      online_testTextMining_text_token_sort_ratio          19
2           online_testTextMining_text_qt-len-radio          17
7       online_testTextMining_unigrams_tq-len-radio          15
20         online_testTextMining_bigrams_dice_ratio          14
33                     online_testWord2vec_canberra          12
30     online_testTextMining_trigrams_partial_ratio          12
32                   online_testWord2vec_braycurtis          11
18     online_testTextMining_unigrams_partial_ratio          10
38                  online_testWord2vec_sqeuclidean           8
21     online_testTextMining_bigrams_edit_seq_ratio           6
24      online_testTextMining_bigrams_partial_ratio           6
19  online_testTextMining_unigrams_token_sort_ratio           6
15    online_testTextMining_unigrams_edit_seq_ratio           4
8             online_testTextMining_text_dice_ratio           4
31  online_testTextMining_trigrams_token_sort_ratio           4
37                    online_testWord2vec_euclidean           3
26        online_testTextMining_trigrams_dice_ratio           3
27    online_testTextMining_trigrams_edit_seq_ratio           2
34                    online_testWord2vec_chebyshev           2
35                    online_testWord2vec_cityblock           2
25   online_testTextMining_bigrams_token_sort_ratio           2
11                 online_testTextMining_text_ratio           1
10        online_testTextMining_text_edit_set_ratio           1
29             online_testTextMining_trigrams_ratio           0
28    online_testTextMining_trigrams_edit_set_ratio           0
23              online_testTextMining_bigrams_ratio           0
22     online_testTextMining_bigrams_edit_set_ratio           0
39                       online_testMagic_globalCTR           0
17             online_testTextMining_unigrams_ratio           0
Valid Loss, AUC: 0.535911 0.668602                 
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561127347_auc0.668602_loss0.535911_std0.004564.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561127347_auc0.668602_loss0.535911_std0.004564.npy

2. 0.54271300
{                                                                            
 "bagging_fraction": 0.8,
 "bagging_freq": 8.0,
 "feature_fraction": 0.9,
 "learning_rate": 0.11,
 "max_bin": 63,
 "min_data_in_leaf": 20.0,
 "num_iterations": 100.0,
 "num_leaves": 30.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.534801                                        
[40]	valid's binary_logloss: 0.533905                                        
[60]	valid's binary_logloss: 0.533573                                        
[80]	valid's binary_logloss: 0.533427                                        
[100]	valid's binary_logloss: 0.53335                                        
[20]	valid's binary_logloss: 0.534998                                        
[40]	valid's binary_logloss: 0.534104                                        
[60]	valid's binary_logloss: 0.533767                                        
[80]	valid's binary_logloss: 0.533603                                        
[100]	valid's binary_logloss: 0.533513                                       
[20]	valid's binary_logloss: 0.534961                                        
[40]	valid's binary_logloss: 0.534056                                        
[60]	valid's binary_logloss: 0.533738                                        
[80]	valid's binary_logloss: 0.533578                                        
[100]	valid's binary_logloss: 0.533507                                       
[20]	valid's binary_logloss: 0.534904                                        
[40]	valid's binary_logloss: 0.533983                                        
[60]	valid's binary_logloss: 0.533619                                        
[80]	valid's binary_logloss: 0.53346                                         
[100]	valid's binary_logloss: 0.533378                                       
[20]	valid's binary_logloss: 0.534766                                        
[40]	valid's binary_logloss: 0.533872                                        
[60]	valid's binary_logloss: 0.533547                                        
[80]	valid's binary_logloss: 0.533398                                        
[100]	valid's binary_logloss: 0.533321                                       
feature importance:                                                          
                                             column  importance              
36                       online_testWord2vec_cosine         260
5              online_testTextMining_unigrams_t-len         235
1                  online_testTextMining_text_t-len         201
40                        online_testMagic_localCTR         180
0                  online_testTextMining_text_q-len         159
14        online_testTextMining_unigrams_dice_ratio         156
6       online_testTextMining_unigrams_qt-len-radio         136
13      online_testTextMining_text_token_sort_ratio         121
4              online_testTextMining_unigrams_q-len         109
16    online_testTextMining_unigrams_edit_set_ratio         100
12         online_testTextMining_text_partial_ratio          91
9         online_testTextMining_text_edit_seq_ratio          89
20         online_testTextMining_bigrams_dice_ratio          77
3           online_testTextMining_text_tq-len-radio          70
30     online_testTextMining_trigrams_partial_ratio          64
15    online_testTextMining_unigrams_edit_seq_ratio          60
18     online_testTextMining_unigrams_partial_ratio          60
32                   online_testWord2vec_braycurtis          59
7       online_testTextMining_unigrams_tq-len-radio          58
38                  online_testWord2vec_sqeuclidean          57
11                 online_testTextMining_text_ratio          55
2           online_testTextMining_text_qt-len-radio          54
35                    online_testWord2vec_cityblock          51
37                    online_testWord2vec_euclidean          47
21     online_testTextMining_bigrams_edit_seq_ratio          38
24      online_testTextMining_bigrams_partial_ratio          37
33                     online_testWord2vec_canberra          34
34                    online_testWord2vec_chebyshev          33
26        online_testTextMining_trigrams_dice_ratio          32
8             online_testTextMining_text_dice_ratio          30
41                                       query_freq          25
22     online_testTextMining_bigrams_edit_set_ratio          18
10        online_testTextMining_text_edit_set_ratio          17
27    online_testTextMining_trigrams_edit_seq_ratio          16
19  online_testTextMining_unigrams_token_sort_ratio          14
25   online_testTextMining_bigrams_token_sort_ratio          13
28    online_testTextMining_trigrams_edit_set_ratio          12
31  online_testTextMining_trigrams_token_sort_ratio          11
23              online_testTextMining_bigrams_ratio           8
29             online_testTextMining_trigrams_ratio           7
17             online_testTextMining_unigrams_ratio           6
39                       online_testMagic_globalCTR           0
Valid Loss, AUC: 0.535256 0.66962                                            
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561128381_auc0.669620_loss0.535256_std0.004450.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561128381_auc0.669620_loss0.535256_std0.004450.npy

{                                                  
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 8.0,
 "feature_fraction": 0.6000000000000001,
 "learning_rate": 0.17,
 "max_bin": 1023,
 "min_data_in_leaf": 10.0,
 "num_iterations": 175.0,
 "num_leaves": 30.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.53416               
[40]	valid's binary_logloss: 0.533586              
[60]	valid's binary_logloss: 0.533414              
[80]	valid's binary_logloss: 0.533356              
[100]	valid's binary_logloss: 0.533321             
[120]	valid's binary_logloss: 0.533299             
[140]	valid's binary_logloss: 0.53328              
[160]	valid's binary_logloss: 0.533273             
[20]	valid's binary_logloss: 0.53436               
[40]	valid's binary_logloss: 0.533767              
[60]	valid's binary_logloss: 0.533562              
[80]	valid's binary_logloss: 0.533495              
[100]	valid's binary_logloss: 0.533462             
[120]	valid's binary_logloss: 0.533436             
[140]	valid's binary_logloss: 0.533419             
[160]	valid's binary_logloss: 0.533412             
[20]	valid's binary_logloss: 0.534309              
[40]	valid's binary_logloss: 0.53376               
[60]	valid's binary_logloss: 0.533564              
[80]	valid's binary_logloss: 0.533495              
[100]	valid's binary_logloss: 0.53346              
[120]	valid's binary_logloss: 0.533441             
[140]	valid's binary_logloss: 0.533431             
[160]	valid's binary_logloss: 0.533427             
[20]	valid's binary_logloss: 0.534264              
[40]	valid's binary_logloss: 0.533681              
[60]	valid's binary_logloss: 0.533459              
[80]	valid's binary_logloss: 0.533381              
[100]	valid's binary_logloss: 0.533342             
[120]	valid's binary_logloss: 0.533315             
[140]	valid's binary_logloss: 0.533301             
[160]	valid's binary_logloss: 0.533281             
[20]	valid's binary_logloss: 0.534152              
[40]	valid's binary_logloss: 0.533607              
[60]	valid's binary_logloss: 0.533416              
[80]	valid's binary_logloss: 0.53335               
[100]	valid's binary_logloss: 0.533323             
[120]	valid's binary_logloss: 0.533297             
[140]	valid's binary_logloss: 0.533288             
[160]	valid's binary_logloss: 0.533271             
feature importance:                                
                                             column  importance
1                  online_testTextMining_text_t-len         277
36                       online_testWord2vec_cosine         273
5              online_testTextMining_unigrams_t-len         203
9         online_testTextMining_text_edit_seq_ratio         199
32                   online_testWord2vec_braycurtis         196
16    online_testTextMining_unigrams_edit_set_ratio         191
0                  online_testTextMining_text_q-len         190
33                     online_testWord2vec_canberra         180
34                    online_testWord2vec_chebyshev         176
14        online_testTextMining_unigrams_dice_ratio         175
2           online_testTextMining_text_qt-len-radio         162
35                    online_testWord2vec_cityblock         155
15    online_testTextMining_unigrams_edit_seq_ratio         149
40                        online_testMagic_localCTR         143
37                    online_testWord2vec_euclidean         142
21     online_testTextMining_bigrams_edit_seq_ratio         138
6       online_testTextMining_unigrams_qt-len-radio         137
13      online_testTextMining_text_token_sort_ratio         133
18     online_testTextMining_unigrams_partial_ratio         129
12         online_testTextMining_text_partial_ratio         122
38                  online_testWord2vec_sqeuclidean         113
30     online_testTextMining_trigrams_partial_ratio         113
22     online_testTextMining_bigrams_edit_set_ratio         109
10        online_testTextMining_text_edit_set_ratio         107
3           online_testTextMining_text_tq-len-radio         102
24      online_testTextMining_bigrams_partial_ratio          97
27    online_testTextMining_trigrams_edit_seq_ratio          96
28    online_testTextMining_trigrams_edit_set_ratio          95
41                                       query_freq          83
25   online_testTextMining_bigrams_token_sort_ratio          82
4              online_testTextMining_unigrams_q-len          82
20         online_testTextMining_bigrams_dice_ratio          79
7       online_testTextMining_unigrams_tq-len-radio          75
31  online_testTextMining_trigrams_token_sort_ratio          59
8             online_testTextMining_text_dice_ratio          58
17             online_testTextMining_unigrams_ratio          54
11                 online_testTextMining_text_ratio          50
19  online_testTextMining_unigrams_token_sort_ratio          45
26        online_testTextMining_trigrams_dice_ratio          42
23              online_testTextMining_bigrams_ratio          36
29             online_testTextMining_trigrams_ratio          28
39                       online_testMagic_globalCTR           0
Valid Loss, AUC: 0.53404 0.669791                  
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561129969_auc0.669791_loss0.534040_std0.002634.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561129969_auc0.669791_loss0.534040_std0.002634.npy


0.54422200
{                                                  
 "bagging_fraction": 0.9,
 "bagging_freq": 6.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.18,
 "max_bin": 15,
 "min_data_in_leaf": 20.0,
 "num_iterations": 75.0,
 "num_leaves": 25.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.53349               
[40]	valid's binary_logloss: 0.532769              
[60]	valid's binary_logloss: 0.532459              
[20]	valid's binary_logloss: 0.533667              
[40]	valid's binary_logloss: 0.532895              
[60]	valid's binary_logloss: 0.532584              
[20]	valid's binary_logloss: 0.533705              
[40]	valid's binary_logloss: 0.533003              
[60]	valid's binary_logloss: 0.532706              
[20]	valid's binary_logloss: 0.533585              
[40]	valid's binary_logloss: 0.532822              
[60]	valid's binary_logloss: 0.532513              
[20]	valid's binary_logloss: 0.5335                
[40]	valid's binary_logloss: 0.532762              
[60]	valid's binary_logloss: 0.532461              
feature importance:                                
                                               column  importance
45          online_testMagic_unigrams_diffSetSimratio         133
5                online_testTextMining_unigrams_t-len         105
36                         online_testWord2vec_cosine          98
4                online_testTextMining_unigrams_q-len          94
6         online_testTextMining_unigrams_qt-len-radio          68
41                                         query_freq          68
42     online_testMagic_unigrams_diffSetSimdice_ratio          68
1                    online_testTextMining_text_t-len          64
14          online_testTextMining_unigrams_dice_ratio          63
7         online_testTextMining_unigrams_tq-len-radio          62
40                          online_testMagic_localCTR          60
0                    online_testTextMining_text_q-len          58
12           online_testTextMining_text_partial_ratio          48
51           online_testMagic_bigrams_diffSetSimratio          43
46  online_testMagic_unigrams_diffSetSimpartial_ratio          42
16      online_testTextMining_unigrams_edit_set_ratio          42
13        online_testTextMining_text_token_sort_ratio          36
18       online_testTextMining_unigrams_partial_ratio          36
20           online_testTextMining_bigrams_dice_ratio          36
37                      online_testWord2vec_euclidean          31
32                     online_testWord2vec_braycurtis          30
47  online_testMagic_unigrams_diffSetSimtoken_sort...          29
11                   online_testTextMining_text_ratio          28
9           online_testTextMining_text_edit_seq_ratio          27
48      online_testMagic_bigrams_diffSetSimdice_ratio          27
35                      online_testWord2vec_cityblock          25
33                       online_testWord2vec_canberra          25
54     online_testMagic_trigrams_diffSetSimdice_ratio          23
30       online_testTextMining_trigrams_partial_ratio          21
38                    online_testWord2vec_sqeuclidean          20
2             online_testTextMining_text_qt-len-radio          20
22       online_testTextMining_bigrams_edit_set_ratio          19
8               online_testTextMining_text_dice_ratio          18
44  online_testMagic_unigrams_diffSetSimedit_set_r...          18
52   online_testMagic_bigrams_diffSetSimpartial_ratio          17
53  online_testMagic_bigrams_diffSetSimtoken_sort_...          16
21       online_testTextMining_bigrams_edit_seq_ratio          15
43  online_testMagic_unigrams_diffSetSimedit_seq_r...          15
3             online_testTextMining_text_tq-len-radio          14
19    online_testTextMining_unigrams_token_sort_ratio          12
58  online_testMagic_trigrams_diffSetSimpartial_ratio          12
15      online_testTextMining_unigrams_edit_seq_ratio          12
24        online_testTextMining_bigrams_partial_ratio          11
50  online_testMagic_bigrams_diffSetSimedit_set_ratio           9
26          online_testTextMining_trigrams_dice_ratio           8
55  online_testMagic_trigrams_diffSetSimedit_seq_r...           8
10          online_testTextMining_text_edit_set_ratio           7
59  online_testMagic_trigrams_diffSetSimtoken_sort...           7
23                online_testTextMining_bigrams_ratio           7
34                      online_testWord2vec_chebyshev           7
27      online_testTextMining_trigrams_edit_seq_ratio           6
56  online_testMagic_trigrams_diffSetSimedit_set_r...           6
29               online_testTextMining_trigrams_ratio           6
17               online_testTextMining_unigrams_ratio           5
49  online_testMagic_bigrams_diffSetSimedit_seq_ratio           4
57          online_testMagic_trigrams_diffSetSimratio           4
31    online_testTextMining_trigrams_token_sort_ratio           4
25     online_testTextMining_bigrams_token_sort_ratio           3
28      online_testTextMining_trigrams_edit_set_ratio           0
39                         online_testMagic_globalCTR           0
Valid Loss, AUC: 0.534122 0.671618                 
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561211706_auc0.671618_loss0.534122_std0.003873.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561211706_auc0.671618_loss0.534122_std0.003873.npy


- 0.54538400
{                                                                            
 "bagging_fraction": 1.0,
 "bagging_freq": 6.0,
 "feature_fraction": 0.9,
 "learning_rate": 0.14,
 "max_bin": 63,
 "min_data_in_leaf": 30.0,
 "num_iterations": 125.0,
 "num_leaves": 30.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.5337                                          
[40]	valid's binary_logloss: 0.532796                                        
[60]	valid's binary_logloss: 0.532418                                        
[80]	valid's binary_logloss: 0.532245                                        
[100]	valid's binary_logloss: 0.532158                                       
[120]	valid's binary_logloss: 0.532102                                       
[20]	valid's binary_logloss: 0.533862                                        
[40]	valid's binary_logloss: 0.532919                                        
[60]	valid's binary_logloss: 0.532538                                        
[80]	valid's binary_logloss: 0.532348                                        
[100]	valid's binary_logloss: 0.532231                                       
[120]	valid's binary_logloss: 0.53217                                        
[20]	valid's binary_logloss: 0.533895                                        
[40]	valid's binary_logloss: 0.532994                                        
[60]	valid's binary_logloss: 0.532637                                        
[80]	valid's binary_logloss: 0.53246                                         
[100]	valid's binary_logloss: 0.532379                                       
[120]	valid's binary_logloss: 0.532325                                       
[20]	valid's binary_logloss: 0.533775                                        
[60]	valid's binary_logloss: 0.532391                                        
[80]	valid's binary_logloss: 0.532205                                        
[100]	valid's binary_logloss: 0.532109                                       
[120]	valid's binary_logloss: 0.53206                                        
feature importance:                                                          
                                               column  importance            
45          online_testMagic_unigrams_diffSetSimratio         273
36                         online_testWord2vec_cosine         194
1                    online_testTextMining_text_t-len         160
40                          online_testMagic_localCTR         159
5                online_testTextMining_unigrams_t-len         158
0                    online_testTextMining_text_q-len         148
6         online_testTextMining_unigrams_qt-len-radio         147
42     online_testMagic_unigrams_diffSetSimdice_ratio         134
14          online_testTextMining_unigrams_dice_ratio         132
51           online_testMagic_bigrams_diffSetSimratio         113
4                online_testTextMining_unigrams_q-len         107
13        online_testTextMining_text_token_sort_ratio         106
46  online_testMagic_unigrams_diffSetSimpartial_ratio          90
7         online_testTextMining_unigrams_tq-len-radio          89
12           online_testTextMining_text_partial_ratio          86
16      online_testTextMining_unigrams_edit_set_ratio          77
9           online_testTextMining_text_edit_seq_ratio          68
47  online_testMagic_unigrams_diffSetSimtoken_sort...          64
20           online_testTextMining_bigrams_dice_ratio          63
18       online_testTextMining_unigrams_partial_ratio          62
32                     online_testWord2vec_braycurtis          59
35                      online_testWord2vec_cityblock          56
48      online_testMagic_bigrams_diffSetSimdice_ratio          52
30       online_testTextMining_trigrams_partial_ratio          49
15      online_testTextMining_unigrams_edit_seq_ratio          49
53  online_testMagic_bigrams_diffSetSimtoken_sort_...          47
11                   online_testTextMining_text_ratio          46
34                      online_testWord2vec_chebyshev          43
37                      online_testWord2vec_euclidean          42
38                    online_testWord2vec_sqeuclidean          41
3             online_testTextMining_text_tq-len-radio          41
2             online_testTextMining_text_qt-len-radio          40
44  online_testMagic_unigrams_diffSetSimedit_set_r...          40
21       online_testTextMining_bigrams_edit_seq_ratio          39
52   online_testMagic_bigrams_diffSetSimpartial_ratio          38
43  online_testMagic_unigrams_diffSetSimedit_seq_r...          37
58  online_testMagic_trigrams_diffSetSimpartial_ratio          36
54     online_testMagic_trigrams_diffSetSimdice_ratio          35
24        online_testTextMining_bigrams_partial_ratio          34
8               online_testTextMining_text_dice_ratio          30
41                                         query_freq          30
33                       online_testWord2vec_canberra          30
27      online_testTextMining_trigrams_edit_seq_ratio          27
26          online_testTextMining_trigrams_dice_ratio          27
22       online_testTextMining_bigrams_edit_set_ratio          27
57          online_testMagic_trigrams_diffSetSimratio          22
55  online_testMagic_trigrams_diffSetSimedit_seq_r...          20
10          online_testTextMining_text_edit_set_ratio          18
50  online_testMagic_bigrams_diffSetSimedit_set_ratio          18
56  online_testMagic_trigrams_diffSetSimedit_set_r...          17
59  online_testMagic_trigrams_diffSetSimtoken_sort...          17
23                online_testTextMining_bigrams_ratio          16
25     online_testTextMining_bigrams_token_sort_ratio          15
28      online_testTextMining_trigrams_edit_set_ratio          14
17               online_testTextMining_unigrams_ratio          12
29               online_testTextMining_trigrams_ratio          12
49  online_testMagic_bigrams_diffSetSimedit_seq_ratio           8
31    online_testTextMining_trigrams_token_sort_ratio           7
19    online_testTextMining_unigrams_token_sort_ratio           4
39                         online_testMagic_globalCTR           0
Valid Loss, AUC: 0.533564 0.672238 
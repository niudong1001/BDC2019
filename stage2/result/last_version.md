{                                                   
 "bagging_fraction": 0.9,
 "bagging_freq": 2.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.18,
 "max_bin": 255,
 "min_data_in_leaf": 30.0,
 "num_iterations": 300.0,
 "num_leaves": 40.0,
 "num_threads": 8
}
[50]	valid's binary_logloss: 0.528584               
[100]	valid's binary_logloss: 0.527929              
[150]	valid's binary_logloss: 0.527716              
[200]	valid's binary_logloss: 0.527606              
[250]	valid's binary_logloss: 0.527566              
[300]	valid's binary_logloss: 0.52755               
[50]	valid's binary_logloss: 0.528695               
[100]	valid's binary_logloss: 0.528012              
[150]	valid's binary_logloss: 0.527797              
[200]	valid's binary_logloss: 0.527693              
[250]	valid's binary_logloss: 0.527633              
[300]	valid's binary_logloss: 0.527618              
[50]	valid's binary_logloss: 0.528668               
[100]	valid's binary_logloss: 0.528022              
[150]	valid's binary_logloss: 0.527812              
[200]	valid's binary_logloss: 0.527716              
[250]	valid's binary_logloss: 0.527658              
[300]	valid's binary_logloss: 0.527621              
[50]	valid's binary_logloss: 0.52856                
[100]	valid's binary_logloss: 0.5279                
[150]	valid's binary_logloss: 0.52771               
[200]	valid's binary_logloss: 0.527607              
[250]	valid's binary_logloss: 0.527555              
[300]	valid's binary_logloss: 0.527541                
[50]	valid's binary_logloss: 0.52857                  
[100]	valid's binary_logloss: 0.527918                
[150]	valid's binary_logloss: 0.527714                
[200]	valid's binary_logloss: 0.527632                
[250]	valid's binary_logloss: 0.527582                
[300]	valid's binary_logloss: 0.527554                
feature importance:                                   
                                               column  importance
70  online_testVectorSpace_paired_manhattan_distances         564
72                        online_testVectorSpace_TLen         463
44                         online_testWord2vec_cosine         374
68     online_testVectorSpace_paired_cosine_distances         349
40                     online_testWord2vec_braycurtis         338
78                       online_testVectorSpace_QTAvg         297
69  online_testVectorSpace_paired_euclidean_distances         297
75                      online_testVectorSpace_QTDiff         290
23         online_testTextMining_text_token_set_ratio         281
11              online_testTextMining_unichars_qt-avg         252
47                                         query_freq         246
76                       online_testVectorSpace_QTMax         243
43                      online_testWord2vec_cityblock         238
41                       online_testWord2vec_canberra         232
18            online_testTextMining_text_jaro_winkler         223
67               online_testMagic_unigrams_diffqt-avg         214
42                      online_testWord2vec_chebyshev         209
28          online_testTextMining_unigrams_dice_ratio         199
77                       online_testVectorSpace_QTMin         192
17                    online_testTextMining_text_jaro         186
71                        online_testVectorSpace_QLen         182
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio         181
5                online_testTextMining_unigrams_t-len         173
73                  online_testVectorSpace_QTLenRatio         168
59  online_testMagic_trigrams_diffSetSimedit_seq_r...         163
20           online_testTextMining_text_partial_ratio         162
61                online_testMagic_unigrams_difft-len         158
15              online_testTextMining_unigrams_qt-avg         156
52  online_testMagic_unigrams_diffSetSimedit_set_r...         155
30      online_testTextMining_unigrams_edit_seq_ratio         154
..                                                ...         ...
27      online_testTextMining_unichars_edit_set_ratio         109
8              online_testTextMining_unichars_qt-diff         107
10              online_testTextMining_unichars_qt-min         102
60  online_testMagic_trigrams_diffSetSimedit_set_r...          99
35       online_testTextMining_bigrams_edit_set_ratio          97
3             online_testTextMining_text_tq-len-radio          97
9               online_testTextMining_unichars_qt-max          93
32           online_testTextMining_bigrams_dice_ratio          85
6         online_testTextMining_unigrams_qt-len-radio          83
39      online_testTextMining_trigrams_edit_set_ratio          77
53      online_testMagic_bigrams_diffSetSimdice_ratio          76
24          online_testTextMining_unichars_dice_ratio          75
65               online_testMagic_unigrams_diffqt-max          71
48                          online_testMagic_localCTR          70
19                   online_testTextMining_text_ratio          65
64              online_testMagic_unigrams_diffqt-diff          60
12             online_testTextMining_unigrams_qt-diff          53
29       online_testTextMining_unigrams_jaccard_ratio          52
36          online_testTextMining_trigrams_dice_ratio          52
7         online_testTextMining_unigrams_tq-len-radio          49
57     online_testMagic_trigrams_diffSetSimdice_ratio          46
50  online_testMagic_unigrams_diffSetSimjaccard_ratio          33
66               online_testMagic_unigrams_diffqt-min          28
14              online_testTextMining_unigrams_qt-min          26
33        online_testTextMining_bigrams_jaccard_ratio          24
25       online_testTextMining_unichars_jaccard_ratio          17
54   online_testMagic_bigrams_diffSetSimjaccard_ratio          15
4                online_testTextMining_unigrams_q-len          14
37       online_testTextMining_trigrams_jaccard_ratio          10
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           9

[80 rows x 2 columns]
Valid Loss, AUC: 0.528442 0.682904                    
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561831537_auc0.682904_loss0.528442_std0.002730.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561831537_auc0.682904_loss0.528442_std0.002730.npy
{                                                                                   
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 0.0,
 "feature_fraction": 0.9,
 "learning_rate": 0.12,
 "max_bin": 63,
 "min_data_in_leaf": 30.0,
 "num_iterations": 200.0,
 "num_leaves": 40.0,
 "num_threads": 8
}
[50]	valid's binary_logloss: 0.529055                                               
[100]	valid's binary_logloss: 0.528217                                              
[150]	valid's binary_logloss: 0.527861                                              
[200]	valid's binary_logloss: 0.527692                                              
[50]	valid's binary_logloss: 0.529269                                               
[100]	valid's binary_logloss: 0.528367                                              
[150]	valid's binary_logloss: 0.527995                                              
[200]	valid's binary_logloss: 0.527825                                              
[50]	valid's binary_logloss: 0.529173                                               
[100]	valid's binary_logloss: 0.528328                                              
[150]	valid's binary_logloss: 0.527959                                              
[200]	valid's binary_logloss: 0.527796                                              
[50]	valid's binary_logloss: 0.529085                                               
[100]	valid's binary_logloss: 0.528236                                              
[150]	valid's binary_logloss: 0.527865                                              
[200]	valid's binary_logloss: 0.52771                                               
[50]	valid's binary_logloss: 0.529081                                               
[100]	valid's binary_logloss: 0.528221                                              
[150]	valid's binary_logloss: 0.527888                                              
[200]	valid's binary_logloss: 0.527724                                              
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561837214_auc0.682572_loss0.529417_std0.003948.npy
{                                                                                   
 "bagging_fraction": 0.8,
 "bagging_freq": 4.0,
 "feature_fraction": 1.0,
 "learning_rate": 0.14,
 "max_bin": 511,
 "min_data_in_leaf": 20.0,
 "num_iterations": 250.0,
 "num_leaves": 35.0,
 "num_threads": 8
}
[50]	valid's binary_logloss: 0.528911                                               
[100]	valid's binary_logloss: 0.528113                                              
[150]	valid's binary_logloss: 0.527817                                              
[200]	valid's binary_logloss: 0.527679                                              
[250]	valid's binary_logloss: 0.527603                                              
[50]	valid's binary_logloss: 0.529124                                               
[100]	valid's binary_logloss: 0.528282                                              
[150]	valid's binary_logloss: 0.527962                                              
[200]	valid's binary_logloss: 0.527815                                              
[250]	valid's binary_logloss: 0.527715                                              
[50]	valid's binary_logloss: 0.52907                                                
[100]	valid's binary_logloss: 0.528279                                              
[150]	valid's binary_logloss: 0.527964                                              
[200]	valid's binary_logloss: 0.527789                                              
[250]	valid's binary_logloss: 0.527713                                              
[50]	valid's binary_logloss: 0.528955                                               
[100]	valid's binary_logloss: 0.528157                                              
[150]	valid's binary_logloss: 0.527837                                              
[200]	valid's binary_logloss: 0.527695                                              
[250]	valid's binary_logloss: 0.527625                                              
[50]	valid's binary_logloss: 0.528915                                               
[100]	valid's binary_logloss: 0.528121                                              
[150]	valid's binary_logloss: 0.527838                                              
[200]	valid's binary_logloss: 0.527702                                              
[250]	valid's binary_logloss: 0.527611                                              
feature importance:                                                                 
                                               column  importance                   
70  online_testVectorSpace_paired_manhattan_distances         557
72                        online_testVectorSpace_TLen         474
44                         online_testWord2vec_cosine         325
68     online_testVectorSpace_paired_cosine_distances         311
78                       online_testVectorSpace_QTAvg         299
47                                         query_freq         248
40                     online_testWord2vec_braycurtis         247
69  online_testVectorSpace_paired_euclidean_distances         235
75                      online_testVectorSpace_QTDiff         208
23         online_testTextMining_text_token_set_ratio         197
28          online_testTextMining_unigrams_dice_ratio         190
67               online_testMagic_unigrams_diffqt-avg         185
11              online_testTextMining_unichars_qt-avg         180
5                online_testTextMining_unigrams_t-len         172
76                       online_testVectorSpace_QTMax         165
43                      online_testWord2vec_cityblock         155
71                        online_testVectorSpace_QLen         147
18            online_testTextMining_text_jaro_winkler         142
15              online_testTextMining_unigrams_qt-avg         140
73                  online_testVectorSpace_QTLenRatio         137
61                online_testMagic_unigrams_difft-len         135
49     online_testMagic_unigrams_diffSetSimdice_ratio         129
42                      online_testWord2vec_chebyshev         122
59  online_testMagic_trigrams_diffSetSimedit_seq_r...         113
63         online_testMagic_unigrams_difftq-len-radio         112
1                    online_testTextMining_text_t-len         109
17                    online_testTextMining_text_jaro         106
41                       online_testWord2vec_canberra         104
79                     online_testVectorSpace_QTMulti         104
31      online_testTextMining_unigrams_edit_set_ratio         102
..                                                ...         ...
62         online_testMagic_unigrams_diffqt-len-radio          66
65               online_testMagic_unigrams_diffqt-max          66
34       online_testTextMining_bigrams_edit_seq_ratio          65
27      online_testTextMining_unichars_edit_set_ratio          65
46                    online_testWord2vec_sqeuclidean          63
22  online_testTextMining_text_partial_token_sort_...          59
60  online_testMagic_trigrams_diffSetSimedit_set_r...          57
12             online_testTextMining_unigrams_qt-diff          54
3             online_testTextMining_text_tq-len-radio          53
38      online_testTextMining_trigrams_edit_seq_ratio          49
36          online_testTextMining_trigrams_dice_ratio          49
24          online_testTextMining_unichars_dice_ratio          47
57     online_testMagic_trigrams_diffSetSimdice_ratio          45
9               online_testTextMining_unichars_qt-max          42
35       online_testTextMining_bigrams_edit_set_ratio          41
64              online_testMagic_unigrams_diffqt-diff          30
39      online_testTextMining_trigrams_edit_set_ratio          29
19                   online_testTextMining_text_ratio          27
14              online_testTextMining_unigrams_qt-min          23
66               online_testMagic_unigrams_diffqt-min          15
4                online_testTextMining_unigrams_q-len          12
7         online_testTextMining_unigrams_tq-len-radio           9
48                          online_testMagic_localCTR           5
29       online_testTextMining_unigrams_jaccard_ratio           1
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           0
50  online_testMagic_unigrams_diffSetSimjaccard_ratio           0
25       online_testTextMining_unichars_jaccard_ratio           0
37       online_testTextMining_trigrams_jaccard_ratio           0
33        online_testTextMining_bigrams_jaccard_ratio           0
54   online_testMagic_bigrams_diffSetSimjaccard_ratio           0

[80 rows x 2 columns]
Valid Loss, AUC: 0.528919 0.682764                                                  
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561842361_auc0.682764_loss0.528919_std0.003306.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561842361_auc0.682764_loss0.528919_std0.003306.npy
{                                                                                   
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 10.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.13,
 "max_bin": 63,
 "min_data_in_leaf": 40.0,
 "num_iterations": 250.0,
 "num_leaves": 40.0,
 "num_threads": 8
}
[50]	valid's binary_logloss: 0.528972                                               
[100]	valid's binary_logloss: 0.528161                                              
[150]	valid's binary_logloss: 0.527863                                              
[200]	valid's binary_logloss: 0.527719                                              
[250]	valid's binary_logloss: 0.527633                                              
[50]	valid's binary_logloss: 0.529162                                               
[100]	valid's binary_logloss: 0.528294                                              
[150]	valid's binary_logloss: 0.527991                                              
[200]	valid's binary_logloss: 0.527856                                              
[250]	valid's binary_logloss: 0.527768                                              
[50]	valid's binary_logloss: 0.529037                                               
[100]	valid's binary_logloss: 0.528236                                              
[150]	valid's binary_logloss: 0.527932                                              
[200]	valid's binary_logloss: 0.527787                                              
[250]	valid's binary_logloss: 0.527695                                              
[50]	valid's binary_logloss: 0.529006                                               
[100]	valid's binary_logloss: 0.528166                                              
[150]	valid's binary_logloss: 0.527847                                              
[200]	valid's binary_logloss: 0.527718                                              
[250]	valid's binary_logloss: 0.52763                                               
[50]	valid's binary_logloss: 0.52893                                                
[100]	valid's binary_logloss: 0.528136                                              
[150]	valid's binary_logloss: 0.527846                                              
[200]	valid's binary_logloss: 0.527696                                              
[250]	valid's binary_logloss: 0.527603                                              
feature importance:                                                                 
                                               column  importance                   
70  online_testVectorSpace_paired_manhattan_distances         516
72                        online_testVectorSpace_TLen         479
44                         online_testWord2vec_cosine         317
68     online_testVectorSpace_paired_cosine_distances         292
69  online_testVectorSpace_paired_euclidean_distances         283
78                       online_testVectorSpace_QTAvg         268
76                       online_testVectorSpace_QTMax         239
40                     online_testWord2vec_braycurtis         237
47                                         query_freq         234
75                      online_testVectorSpace_QTDiff         233
67               online_testMagic_unigrams_diffqt-avg         232
23         online_testTextMining_text_token_set_ratio         223
15              online_testTextMining_unigrams_qt-avg         204
28          online_testTextMining_unigrams_dice_ratio         198
61                online_testMagic_unigrams_difft-len         189
11              online_testTextMining_unichars_qt-avg         171
5                online_testTextMining_unigrams_t-len         169
43                      online_testWord2vec_cityblock         160
20           online_testTextMining_text_partial_ratio         157
13              online_testTextMining_unigrams_qt-max         154
18            online_testTextMining_text_jaro_winkler         149
49     online_testMagic_unigrams_diffSetSimdice_ratio         147
71                        online_testVectorSpace_QLen         145
17                    online_testTextMining_text_jaro         131
59  online_testMagic_trigrams_diffSetSimedit_seq_r...         130
10              online_testTextMining_unichars_qt-min         130
63         online_testMagic_unigrams_difftq-len-radio         128
41                       online_testWord2vec_canberra         124
73                  online_testVectorSpace_QTLenRatio         120
1                    online_testTextMining_text_t-len         117
..                                                ...         ...
19                   online_testTextMining_text_ratio          81
34       online_testTextMining_bigrams_edit_seq_ratio          79
51  online_testMagic_unigrams_diffSetSimedit_seq_r...          78
53      online_testMagic_bigrams_diffSetSimdice_ratio          78
60  online_testMagic_trigrams_diffSetSimedit_set_r...          77
62         online_testMagic_unigrams_diffqt-len-radio          76
2             online_testTextMining_text_qt-len-radio          76
3             online_testTextMining_text_tq-len-radio          74
9               online_testTextMining_unichars_qt-max          74
24          online_testTextMining_unichars_dice_ratio          58
48                          online_testMagic_localCTR          58
57     online_testMagic_trigrams_diffSetSimdice_ratio          57
64              online_testMagic_unigrams_diffqt-diff          56
38      online_testTextMining_trigrams_edit_seq_ratio          56
6         online_testTextMining_unigrams_qt-len-radio          56
36          online_testTextMining_trigrams_dice_ratio          52
27      online_testTextMining_unichars_edit_set_ratio          49
35       online_testTextMining_bigrams_edit_set_ratio          48
29       online_testTextMining_unigrams_jaccard_ratio          45
39      online_testTextMining_trigrams_edit_set_ratio          44
7         online_testTextMining_unigrams_tq-len-radio          42
4                online_testTextMining_unigrams_q-len          39
50  online_testMagic_unigrams_diffSetSimjaccard_ratio          38
66               online_testMagic_unigrams_diffqt-min          28
14              online_testTextMining_unigrams_qt-min          26
33        online_testTextMining_bigrams_jaccard_ratio          17
54   online_testMagic_bigrams_diffSetSimjaccard_ratio          14
25       online_testTextMining_unichars_jaccard_ratio          12
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           9
37       online_testTextMining_trigrams_jaccard_ratio           7

[80 rows x 2 columns]
Valid Loss, AUC: 0.52902 0.682737                                                   
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561846631_auc0.682737_loss0.529020_std0.003617.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561846631_auc0.682737_loss0.529020_std0.003617.npy
{                                                                                   
 "bagging_fraction": 0.6000000000000001,
 "bagging_freq": 2.0,
 "feature_fraction": 0.6000000000000001,
 "learning_rate": 0.17,
 "max_bin": 511,
 "min_data_in_leaf": 30.0,
 "num_iterations": 250.0,
 "num_leaves": 35.0,
 "num_threads": 8
}
[50]	valid's binary_logloss: 0.528785                                               
[100]	valid's binary_logloss: 0.528084                                              
[150]	valid's binary_logloss: 0.527826                                              
[200]	valid's binary_logloss: 0.527707                                              
[250]	valid's binary_logloss: 0.527655                                              
[50]	valid's binary_logloss: 0.528923                                               
[100]	valid's binary_logloss: 0.528213                                              
[150]	valid's binary_logloss: 0.527964                                              
[200]	valid's binary_logloss: 0.527869                                              
[250]	valid's binary_logloss: 0.527788                                              
[50]	valid's binary_logloss: 0.528876                                               
[100]	valid's binary_logloss: 0.528185                                              
[150]	valid's binary_logloss: 0.527967                                              
[200]	valid's binary_logloss: 0.527851                                              
[250]	valid's binary_logloss: 0.527794                                              
[50]	valid's binary_logloss: 0.52878                                                
[100]	valid's binary_logloss: 0.528067                                              
[150]	valid's binary_logloss: 0.527815                                              
[200]	valid's binary_logloss: 0.527684                                              
[250]	valid's binary_logloss: 0.527616                                              
[50]	valid's binary_logloss: 0.528762                                               
[100]	valid's binary_logloss: 0.52807                                               
[150]	valid's binary_logloss: 0.527858                                              
[200]	valid's binary_logloss: 0.527743                                              
[250]	valid's binary_logloss: 0.527685                                              
feature importance:                                                                 
                                               column  importance                   
70  online_testVectorSpace_paired_manhattan_distances         430
72                        online_testVectorSpace_TLen         379
68     online_testVectorSpace_paired_cosine_distances         301
44                         online_testWord2vec_cosine         253
76                       online_testVectorSpace_QTMax         232
78                       online_testVectorSpace_QTAvg         207
75                      online_testVectorSpace_QTDiff         207
40                     online_testWord2vec_braycurtis         198
69  online_testVectorSpace_paired_euclidean_distances         193
43                      online_testWord2vec_cityblock         174
67               online_testMagic_unigrams_diffqt-avg         170
23         online_testTextMining_text_token_set_ratio         167
47                                         query_freq         151
18            online_testTextMining_text_jaro_winkler         149
11              online_testTextMining_unichars_qt-avg         146
15              online_testTextMining_unigrams_qt-avg         143
41                       online_testWord2vec_canberra         137
17                    online_testTextMining_text_jaro         134
45                      online_testWord2vec_euclidean         133
73                  online_testVectorSpace_QTLenRatio         132
77                       online_testVectorSpace_QTMin         131
71                        online_testVectorSpace_QLen         129
61                online_testMagic_unigrams_difft-len         128
1                    online_testTextMining_text_t-len         128
28          online_testTextMining_unigrams_dice_ratio         127
79                     online_testVectorSpace_QTMulti         125
13              online_testTextMining_unigrams_qt-max         123
74                  online_testVectorSpace_TQLenRatio         121
26      online_testTextMining_unichars_edit_seq_ratio         119
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio         118
..                                                ...         ...
8              online_testTextMining_unichars_qt-diff          76
27      online_testTextMining_unichars_edit_set_ratio          76
35       online_testTextMining_bigrams_edit_set_ratio          70
65               online_testMagic_unigrams_diffqt-max          69
22  online_testTextMining_text_partial_token_sort_...          68
48                          online_testMagic_localCTR          67
3             online_testTextMining_text_tq-len-radio          67
39      online_testTextMining_trigrams_edit_set_ratio          66
32           online_testTextMining_bigrams_dice_ratio          64
16                online_testTextMining_text_distance          61
9               online_testTextMining_unichars_qt-max          59
50  online_testMagic_unigrams_diffSetSimjaccard_ratio          53
62         online_testMagic_unigrams_diffqt-len-radio          53
29       online_testTextMining_unigrams_jaccard_ratio          48
53      online_testMagic_bigrams_diffSetSimdice_ratio          45
24          online_testTextMining_unichars_dice_ratio          42
64              online_testMagic_unigrams_diffqt-diff          41
57     online_testMagic_trigrams_diffSetSimdice_ratio          41
7         online_testTextMining_unigrams_tq-len-radio          38
12             online_testTextMining_unigrams_qt-diff          34
19                   online_testTextMining_text_ratio          32
36          online_testTextMining_trigrams_dice_ratio          25
54   online_testMagic_bigrams_diffSetSimjaccard_ratio          21
33        online_testTextMining_bigrams_jaccard_ratio          20
14              online_testTextMining_unigrams_qt-min          17
37       online_testTextMining_trigrams_jaccard_ratio          17
58  online_testMagic_trigrams_diffSetSimjaccard_ratio          17
66               online_testMagic_unigrams_diffqt-min          16
4                online_testTextMining_unigrams_q-len          13
25       online_testTextMining_unichars_jaccard_ratio          13

[80 rows x 2 columns]
Valid Loss, AUC: 0.528813 0.682662                                                  
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561850051_auc0.682662_loss0.528813_std0.003102.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561850051_auc0.682662_loss0.528813_std0.003102.npy
{                                                                                   
 "bagging_fraction": 0.9,
 "bagging_freq": 8.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.18,
 "max_bin": 1023,
 "min_data_in_leaf": 10.0,
 "num_iterations": 150.0,
 "num_leaves": 40.0,
 "num_threads": 8
}
[50]	valid's binary_logloss: 0.528558                                               
[100]	valid's binary_logloss: 0.527904                                              
[150]	valid's binary_logloss: 0.527733                                              
[50]	valid's binary_logloss: 0.528744                                               
[100]	valid's binary_logloss: 0.528008                                              
[150]	valid's binary_logloss: 0.527851                                              
[50]	valid's binary_logloss: 0.528654                                               
[100]	valid's binary_logloss: 0.52802                                               
[150]	valid's binary_logloss: 0.527798                                              
[50]	valid's binary_logloss: 0.528543                                               
[100]	valid's binary_logloss: 0.527891                                              
[150]	valid's binary_logloss: 0.527688                                              
[50]	valid's binary_logloss: 0.528536                                               
[100]	valid's binary_logloss: 0.527882                                              
[150]	valid's binary_logloss: 0.527698                                              
feature importance:                                                                 
                                               column  importance                   
72                        online_testVectorSpace_TLen         369
70  online_testVectorSpace_paired_manhattan_distances         358
68     online_testVectorSpace_paired_cosine_distances         250
44                         online_testWord2vec_cosine         197
78                       online_testVectorSpace_QTAvg         186
67               online_testMagic_unigrams_diffqt-avg         159
40                     online_testWord2vec_braycurtis         158
75                      online_testVectorSpace_QTDiff         150
47                                         query_freq         145
76                       online_testVectorSpace_QTMax         133
23         online_testTextMining_text_token_set_ratio         120
28          online_testTextMining_unigrams_dice_ratio         120
69  online_testVectorSpace_paired_euclidean_distances         119
43                      online_testWord2vec_cityblock         117
61                online_testMagic_unigrams_difft-len         111
15              online_testTextMining_unigrams_qt-avg         110
11              online_testTextMining_unichars_qt-avg         109
5                online_testTextMining_unigrams_t-len         107
71                        online_testVectorSpace_QLen         105
73                  online_testVectorSpace_QTLenRatio          99
77                       online_testVectorSpace_QTMin          93
79                     online_testVectorSpace_QTMulti          93
18            online_testTextMining_text_jaro_winkler          91
13              online_testTextMining_unigrams_qt-max          85
49     online_testMagic_unigrams_diffSetSimdice_ratio          80
45                      online_testWord2vec_euclidean          76
17                    online_testTextMining_text_jaro          76
2             online_testTextMining_text_qt-len-radio          75
41                       online_testWord2vec_canberra          72
10              online_testTextMining_unichars_qt-min          69
..                                                ...         ...
9               online_testTextMining_unichars_qt-max          41
60  online_testMagic_trigrams_diffSetSimedit_set_r...          41
6         online_testTextMining_unigrams_qt-len-radio          40
30      online_testTextMining_unigrams_edit_seq_ratio          40
3             online_testTextMining_text_tq-len-radio          39
52  online_testMagic_unigrams_diffSetSimedit_set_r...          39
34       online_testTextMining_bigrams_edit_seq_ratio          39
35       online_testTextMining_bigrams_edit_set_ratio          38
22  online_testTextMining_text_partial_token_sort_...          36
12             online_testTextMining_unigrams_qt-diff          36
27      online_testTextMining_unichars_edit_set_ratio          35
32           online_testTextMining_bigrams_dice_ratio          32
62         online_testMagic_unigrams_diffqt-len-radio          30
57     online_testMagic_trigrams_diffSetSimdice_ratio          30
36          online_testTextMining_trigrams_dice_ratio          26
39      online_testTextMining_trigrams_edit_set_ratio          25
64              online_testMagic_unigrams_diffqt-diff          23
14              online_testTextMining_unigrams_qt-min          19
19                   online_testTextMining_text_ratio          17
7         online_testTextMining_unigrams_tq-len-radio          14
50  online_testMagic_unigrams_diffSetSimjaccard_ratio          14
29       online_testTextMining_unigrams_jaccard_ratio          13
24          online_testTextMining_unichars_dice_ratio          13
4                online_testTextMining_unigrams_q-len          12
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           9
66               online_testMagic_unigrams_diffqt-min           9
54   online_testMagic_bigrams_diffSetSimjaccard_ratio           9
33        online_testTextMining_bigrams_jaccard_ratio           8
37       online_testTextMining_trigrams_jaccard_ratio           7
25       online_testTextMining_unichars_jaccard_ratio           4

[80 rows x 2 columns]
Valid Loss, AUC: 0.529241 0.682562                                                  
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561853116_auc0.682562_loss0.529241_std0.003688.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561853116_auc0.682562_loss0.529241_std0.003688.npy

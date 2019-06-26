{                                                   
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 4.0,
 "feature_fraction": 0.9,
 "learning_rate": 0.16,
 "max_bin": 63,
 "min_data_in_leaf": 50.0,
 "num_iterations": 75.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.532137               
[50]	valid's binary_logloss: 0.532236               
[50]	valid's binary_logloss: 0.532264               
[50]	valid's binary_logloss: 0.532123               
[50]	valid's binary_logloss: 0.532099               
feature importance:                                 
                                               column  importance
70  online_testVectorSpace_paired_manhattan_distances         116
47                                         query_freq          68
69  online_testVectorSpace_paired_euclidean_distances          48
67               online_testMagic_unigrams_diffqt-avg          48
44                         online_testWord2vec_cosine          35
68     online_testVectorSpace_paired_cosine_distances          24
61                online_testMagic_unigrams_difft-len          22
28          online_testTextMining_unigrams_dice_ratio          21
65               online_testMagic_unigrams_diffqt-max          19
49     online_testMagic_unigrams_diffSetSimdice_ratio          19
15              online_testTextMining_unigrams_qt-avg          17
23         online_testTextMining_text_token_set_ratio          16
11              online_testTextMining_unichars_qt-avg          13
10              online_testTextMining_unichars_qt-min          12
50  online_testMagic_unigrams_diffSetSimjaccard_ratio          11
48                          online_testMagic_localCTR          11
18            online_testTextMining_text_jaro_winkler          11
53      online_testMagic_bigrams_diffSetSimdice_ratio           9
57     online_testMagic_trigrams_diffSetSimdice_ratio           9
0                    online_testTextMining_text_q-len           9
3             online_testTextMining_text_tq-len-radio           9
66               online_testMagic_unigrams_diffqt-min           8
20           online_testTextMining_text_partial_ratio           7
16                online_testTextMining_text_distance           7
6         online_testTextMining_unigrams_qt-len-radio           7
63         online_testMagic_unigrams_difftq-len-radio           7
4                online_testTextMining_unigrams_q-len           6
32           online_testTextMining_bigrams_dice_ratio           6
5                online_testTextMining_unigrams_t-len           5
17                    online_testTextMining_text_jaro           5
..                                                ...         ...
19                   online_testTextMining_text_ratio           3
9               online_testTextMining_unichars_qt-max           3
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           2
8              online_testTextMining_unichars_qt-diff           2
56  online_testMagic_bigrams_diffSetSimedit_set_ratio           2
59  online_testMagic_trigrams_diffSetSimedit_seq_r...           2
12             online_testTextMining_unigrams_qt-diff           2
35       online_testTextMining_bigrams_edit_set_ratio           2
26      online_testTextMining_unichars_edit_seq_ratio           2
14              online_testTextMining_unigrams_qt-min           1
36          online_testTextMining_trigrams_dice_ratio           1
64              online_testMagic_unigrams_diffqt-diff           1
29       online_testTextMining_unigrams_jaccard_ratio           1
62         online_testMagic_unigrams_diffqt-len-radio           1
60  online_testMagic_trigrams_diffSetSimedit_set_r...           1
51  online_testMagic_unigrams_diffSetSimedit_seq_r...           1
45                      online_testWord2vec_euclidean           1
37       online_testTextMining_trigrams_jaccard_ratio           0
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio           0
34       online_testTextMining_bigrams_edit_seq_ratio           0
33        online_testTextMining_bigrams_jaccard_ratio           0
42                      online_testWord2vec_chebyshev           0
30      online_testTextMining_unigrams_edit_seq_ratio           0
38      online_testTextMining_trigrams_edit_seq_ratio           0
39      online_testTextMining_trigrams_edit_set_ratio           0
41                       online_testWord2vec_canberra           0
27      online_testTextMining_unichars_edit_set_ratio           0
25       online_testTextMining_unichars_jaccard_ratio           0
24          online_testTextMining_unichars_dice_ratio           0
22  online_testTextMining_text_partial_token_sort_...           0

[71 rows x 2 columns]
Valid Loss, AUC: 0.534087 0.673817                  
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561567409_auc0.673817_loss0.534087_std0.004460.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561567409_auc0.673817_loss0.534087_std0.004460.npy
{                                                                               
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 10.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.15,
 "max_bin": 1023,
 "min_data_in_leaf": 20.0,
 "num_iterations": 125.0,
 "num_leaves": 20.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.531572                                           
[100]	valid's binary_logloss: 0.530712                                          
[50]	valid's binary_logloss: 0.53169                                            
[100]	valid's binary_logloss: 0.530774                                          
[50]	valid's binary_logloss: 0.531711                                           
[100]	valid's binary_logloss: 0.530811                                          
[50]	valid's binary_logloss: 0.531518                                           
[100]	valid's binary_logloss: 0.530641                                          
[50]	valid's binary_logloss: 0.531563                                           
[100]	valid's binary_logloss: 0.530678                                          
feature importance:                                                             
                                               column  importance               
70  online_testVectorSpace_paired_manhattan_distances         361
68     online_testVectorSpace_paired_cosine_distances         184
67               online_testMagic_unigrams_diffqt-avg         132
15              online_testTextMining_unigrams_qt-avg          96
11              online_testTextMining_unichars_qt-avg          93
44                         online_testWord2vec_cosine          93
47                                         query_freq          88
69  online_testVectorSpace_paired_euclidean_distances          86
61                online_testMagic_unigrams_difft-len          70
49     online_testMagic_unigrams_diffSetSimdice_ratio          56
23         online_testTextMining_text_token_set_ratio          56
28          online_testTextMining_unigrams_dice_ratio          52
48                          online_testMagic_localCTR          44
1                    online_testTextMining_text_t-len          42
2             online_testTextMining_text_qt-len-radio          39
31      online_testTextMining_unigrams_edit_set_ratio          38
65               online_testMagic_unigrams_diffqt-max          34
32           online_testTextMining_bigrams_dice_ratio          34
10              online_testTextMining_unichars_qt-min          34
17                    online_testTextMining_text_jaro          33
45                      online_testWord2vec_euclidean          30
0                    online_testTextMining_text_q-len          30
20           online_testTextMining_text_partial_ratio          29
63         online_testMagic_unigrams_difftq-len-radio          28
5                online_testTextMining_unigrams_t-len          28
40                     online_testWord2vec_braycurtis          28
18            online_testTextMining_text_jaro_winkler          27
6         online_testTextMining_unigrams_qt-len-radio          26
16                online_testTextMining_text_distance          26
50  online_testMagic_unigrams_diffSetSimjaccard_ratio          24
..                                                ...         ...
46                    online_testWord2vec_sqeuclidean          14
19                   online_testTextMining_text_ratio          13
53      online_testMagic_bigrams_diffSetSimdice_ratio          13
41                       online_testWord2vec_canberra          13
35       online_testTextMining_bigrams_edit_set_ratio          12
29       online_testTextMining_unigrams_jaccard_ratio          12
42                      online_testWord2vec_chebyshev          11
51  online_testMagic_unigrams_diffSetSimedit_seq_r...          11
34       online_testTextMining_bigrams_edit_seq_ratio          11
56  online_testMagic_bigrams_diffSetSimedit_set_ratio          10
8              online_testTextMining_unichars_qt-diff          10
52  online_testMagic_unigrams_diffSetSimedit_set_r...          10
12             online_testTextMining_unigrams_qt-diff          10
14              online_testTextMining_unigrams_qt-min           9
7         online_testTextMining_unigrams_tq-len-radio           9
27      online_testTextMining_unichars_edit_set_ratio           8
64              online_testMagic_unigrams_diffqt-diff           8
4                online_testTextMining_unigrams_q-len           8
62         online_testMagic_unigrams_diffqt-len-radio           8
24          online_testTextMining_unichars_dice_ratio           7
36          online_testTextMining_trigrams_dice_ratio           5
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio           4
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           3
54   online_testMagic_bigrams_diffSetSimjaccard_ratio           3
22  online_testTextMining_text_partial_token_sort_...           3
38      online_testTextMining_trigrams_edit_seq_ratio           2
33        online_testTextMining_bigrams_jaccard_ratio           1
37       online_testTextMining_trigrams_jaccard_ratio           1
25       online_testTextMining_unichars_jaccard_ratio           0
39      online_testTextMining_trigrams_edit_set_ratio           0

[71 rows x 2 columns]
Valid Loss, AUC: 0.532626 0.676248                                              
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561568501_auc0.676248_loss0.532626_std0.004361.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561568501_auc0.676248_loss0.532626_std0.004361.npy
{                                                                               
 "bagging_fraction": 0.9,
 "bagging_freq": 8.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.1,
 "max_bin": 63,
 "min_data_in_leaf": 20.0,
 "num_iterations": 175.0,
 "num_leaves": 15.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.532408                                           
[100]	valid's binary_logloss: 0.531383                                          
[150]	valid's binary_logloss: 0.530879                                          
[50]	valid's binary_logloss: 0.532619                                           
[100]	valid's binary_logloss: 0.53152                                           
[150]	valid's binary_logloss: 0.530978                                          
[50]	valid's binary_logloss: 0.532617                                           
[100]	valid's binary_logloss: 0.531524                                          
[150]	valid's binary_logloss: 0.531015                                          
[50]	valid's binary_logloss: 0.532514                                           
[100]	valid's binary_logloss: 0.531422                                          
[150]	valid's binary_logloss: 0.530893                                          
[50]	valid's binary_logloss: 0.532427                                           
[100]	valid's binary_logloss: 0.531361                                          
[150]	valid's binary_logloss: 0.530857                                          
feature importance:                                                             
                                               column  importance               
70  online_testVectorSpace_paired_manhattan_distances         407
69  online_testVectorSpace_paired_euclidean_distances         153
67               online_testMagic_unigrams_diffqt-avg         148
68     online_testVectorSpace_paired_cosine_distances         136
47                                         query_freq         135
44                         online_testWord2vec_cosine         112
15              online_testTextMining_unigrams_qt-avg         102
11              online_testTextMining_unichars_qt-avg          87
28          online_testTextMining_unigrams_dice_ratio          68
61                online_testMagic_unigrams_difft-len          64
49     online_testMagic_unigrams_diffSetSimdice_ratio          61
23         online_testTextMining_text_token_set_ratio          61
10              online_testTextMining_unichars_qt-min          56
48                          online_testMagic_localCTR          37
3             online_testTextMining_text_tq-len-radio          37
65               online_testMagic_unigrams_diffqt-max          36
18            online_testTextMining_text_jaro_winkler          32
53      online_testMagic_bigrams_diffSetSimdice_ratio          29
4                online_testTextMining_unigrams_q-len          29
16                online_testTextMining_text_distance          27
32           online_testTextMining_bigrams_dice_ratio          27
20           online_testTextMining_text_partial_ratio          26
63         online_testMagic_unigrams_difftq-len-radio          25
7         online_testTextMining_unigrams_tq-len-radio          25
31      online_testTextMining_unigrams_edit_set_ratio          25
0                    online_testTextMining_text_q-len          24
1                    online_testTextMining_text_t-len          23
21        online_testTextMining_text_token_sort_ratio          21
66               online_testMagic_unigrams_diffqt-min          21
17                    online_testTextMining_text_jaro          20
..                                                ...         ...
43                      online_testWord2vec_cityblock          14
19                   online_testTextMining_text_ratio          13
14              online_testTextMining_unigrams_qt-min          13
8              online_testTextMining_unichars_qt-diff          12
12             online_testTextMining_unigrams_qt-diff          12
26      online_testTextMining_unichars_edit_seq_ratio          12
46                    online_testWord2vec_sqeuclidean          12
64              online_testMagic_unigrams_diffqt-diff          11
51  online_testMagic_unigrams_diffSetSimedit_seq_r...          10
35       online_testTextMining_bigrams_edit_set_ratio          10
30      online_testTextMining_unigrams_edit_seq_ratio           9
60  online_testMagic_trigrams_diffSetSimedit_set_r...           8
54   online_testMagic_bigrams_diffSetSimjaccard_ratio           7
34       online_testTextMining_bigrams_edit_seq_ratio           7
41                       online_testWord2vec_canberra           6
33        online_testTextMining_bigrams_jaccard_ratio           5
36          online_testTextMining_trigrams_dice_ratio           5
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           4
62         online_testMagic_unigrams_diffqt-len-radio           4
56  online_testMagic_bigrams_diffSetSimedit_set_ratio           4
42                      online_testWord2vec_chebyshev           4
27      online_testTextMining_unichars_edit_set_ratio           3
52  online_testMagic_unigrams_diffSetSimedit_set_r...           3
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio           3
22  online_testTextMining_text_partial_token_sort_...           3
24          online_testTextMining_unichars_dice_ratio           3
39      online_testTextMining_trigrams_edit_set_ratio           2
25       online_testTextMining_unichars_jaccard_ratio           1
38      online_testTextMining_trigrams_edit_seq_ratio           0
37       online_testTextMining_trigrams_jaccard_ratio           0

[71 rows x 2 columns]
Valid Loss, AUC: 0.532921 0.675754                                              
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561570061_auc0.675754_loss0.532921_std0.004227.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561570061_auc0.675754_loss0.532921_std0.004227.npy
{                                                                                
 "bagging_fraction": 0.9,
 "bagging_freq": 2.0,
 "feature_fraction": 0.9,
 "learning_rate": 0.15,
 "max_bin": 63,
 "min_data_in_leaf": 50.0,
 "num_iterations": 50.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.532199                                            
[50]	valid's binary_logloss: 0.532361                                              
[50]	valid's binary_logloss: 0.532371                                              
[50]	valid's binary_logloss: 0.532215                                              
[50]	valid's binary_logloss: 0.532153                                              
feature importance:                                                                
                                               column  importance                  
70  online_testVectorSpace_paired_manhattan_distances          72
47                                         query_freq          67
67               online_testMagic_unigrams_diffqt-avg          37
44                         online_testWord2vec_cosine          30
69  online_testVectorSpace_paired_euclidean_distances          22
49     online_testMagic_unigrams_diffSetSimdice_ratio          19
68     online_testVectorSpace_paired_cosine_distances          16
23         online_testTextMining_text_token_set_ratio          16
61                online_testMagic_unigrams_difft-len          13
15              online_testTextMining_unigrams_qt-avg          12
65               online_testMagic_unigrams_diffqt-max          12
63         online_testMagic_unigrams_difftq-len-radio          11
48                          online_testMagic_localCTR           9
10              online_testTextMining_unichars_qt-min           8
18            online_testTextMining_text_jaro_winkler           8
28          online_testTextMining_unigrams_dice_ratio           8
20           online_testTextMining_text_partial_ratio           7
57     online_testMagic_trigrams_diffSetSimdice_ratio           7
53      online_testMagic_bigrams_diffSetSimdice_ratio           6
11              online_testTextMining_unichars_qt-avg           6
50  online_testMagic_unigrams_diffSetSimjaccard_ratio           5
40                     online_testWord2vec_braycurtis           5
17                    online_testTextMining_text_jaro           4
31      online_testTextMining_unigrams_edit_set_ratio           4
3             online_testTextMining_text_tq-len-radio           4
2             online_testTextMining_text_qt-len-radio           4
1                    online_testTextMining_text_t-len           4
32           online_testTextMining_bigrams_dice_ratio           4
64              online_testMagic_unigrams_diffqt-diff           3
54   online_testMagic_bigrams_diffSetSimjaccard_ratio           3
..                                                ...         ...
19                   online_testTextMining_text_ratio           1
12             online_testTextMining_unigrams_qt-diff           1
21        online_testTextMining_text_token_sort_ratio           1
45                      online_testWord2vec_euclidean           1
13              online_testTextMining_unigrams_qt-max           1
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio           0
30      online_testTextMining_unigrams_edit_seq_ratio           0
59  online_testMagic_trigrams_diffSetSimedit_seq_r...           0
60  online_testMagic_trigrams_diffSetSimedit_set_r...           0
14              online_testTextMining_unigrams_qt-min           0
9               online_testTextMining_unichars_qt-max           0
8              online_testTextMining_unichars_qt-diff           0
62         online_testMagic_unigrams_diffqt-len-radio           0
51  online_testMagic_unigrams_diffSetSimedit_seq_r...           0
52  online_testMagic_unigrams_diffSetSimedit_set_r...           0
29       online_testTextMining_unigrams_jaccard_ratio           0
22  online_testTextMining_text_partial_token_sort_...           0
24          online_testTextMining_unichars_dice_ratio           0
46                    online_testWord2vec_sqeuclidean           0
25       online_testTextMining_unichars_jaccard_ratio           0
43                      online_testWord2vec_cityblock           0
42                      online_testWord2vec_chebyshev           0
41                       online_testWord2vec_canberra           0
39      online_testTextMining_trigrams_edit_set_ratio           0
38      online_testTextMining_trigrams_edit_seq_ratio           0
37       online_testTextMining_trigrams_jaccard_ratio           0
27      online_testTextMining_unichars_edit_set_ratio           0
34       online_testTextMining_bigrams_edit_seq_ratio           0
33        online_testTextMining_bigrams_jaccard_ratio           0
35       online_testTextMining_bigrams_edit_set_ratio           0

[71 rows x 2 columns]
Valid Loss, AUC: 0.535434 0.672348                                                 
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561570866_auc0.672348_loss0.535434_std0.005284.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561570866_auc0.672348_loss0.535434_std0.005284.npy
{                                                                                  
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 4.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.15,
 "max_bin": 15,
 "min_data_in_leaf": 30.0,
 "num_iterations": 200.0,
 "num_leaves": 5.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.533065                                             
[100]	valid's binary_logloss: 0.532218                                            
[150]	valid's binary_logloss: 0.531768                                            
[200]	valid's binary_logloss: 0.531482                                            
[50]	valid's binary_logloss: 0.533274                                             
[100]	valid's binary_logloss: 0.532401                                            
[150]	valid's binary_logloss: 0.531929                                            
[200]	valid's binary_logloss: 0.531622                                            
[50]	valid's binary_logloss: 0.533251                                             
[100]	valid's binary_logloss: 0.53243                                             
[150]	valid's binary_logloss: 0.531976                                            
[200]	valid's binary_logloss: 0.531683                                            
[50]	valid's binary_logloss: 0.533128                                             
[100]	valid's binary_logloss: 0.532235                                            
[150]	valid's binary_logloss: 0.531786                                            
[200]	valid's binary_logloss: 0.531498                                            
[50]	valid's binary_logloss: 0.533105                                             
[100]	valid's binary_logloss: 0.532238                                            
[150]	valid's binary_logloss: 0.531779                                            
[200]	valid's binary_logloss: 0.531484                                            
feature importance:                                                               
                                               column  importance                 
70  online_testVectorSpace_paired_manhattan_distances         129
47                                         query_freq          59
67               online_testMagic_unigrams_diffqt-avg          52
68     online_testVectorSpace_paired_cosine_distances          47
69  online_testVectorSpace_paired_euclidean_distances          44
44                         online_testWord2vec_cosine          27
61                online_testMagic_unigrams_difft-len          26
48                          online_testMagic_localCTR          24
28          online_testTextMining_unigrams_dice_ratio          23
15              online_testTextMining_unigrams_qt-avg          21
49     online_testMagic_unigrams_diffSetSimdice_ratio          20
16                online_testTextMining_text_distance          19
23         online_testTextMining_text_token_set_ratio          19
11              online_testTextMining_unichars_qt-avg          17
4                online_testTextMining_unigrams_q-len          16
10              online_testTextMining_unichars_qt-min          13
65               online_testMagic_unigrams_diffqt-max          13
50  online_testMagic_unigrams_diffSetSimjaccard_ratio          13
3             online_testTextMining_text_tq-len-radio          12
66               online_testMagic_unigrams_diffqt-min          12
40                     online_testWord2vec_braycurtis          11
63         online_testMagic_unigrams_difftq-len-radio          11
18            online_testTextMining_text_jaro_winkler          10
57     online_testMagic_trigrams_diffSetSimdice_ratio          10
6         online_testTextMining_unigrams_qt-len-radio           9
21        online_testTextMining_text_token_sort_ratio           8
17                    online_testTextMining_text_jaro           8
20           online_testTextMining_text_partial_ratio           8
53      online_testMagic_bigrams_diffSetSimdice_ratio           7
31      online_testTextMining_unigrams_edit_set_ratio           7
..                                                ...         ...
64              online_testMagic_unigrams_diffqt-diff           4
32           online_testTextMining_bigrams_dice_ratio           4
56  online_testMagic_bigrams_diffSetSimedit_set_ratio           4
51  online_testMagic_unigrams_diffSetSimedit_seq_r...           3
54   online_testMagic_bigrams_diffSetSimjaccard_ratio           3
19                   online_testTextMining_text_ratio           3
59  online_testMagic_trigrams_diffSetSimedit_seq_r...           3
13              online_testTextMining_unigrams_qt-max           3
39      online_testTextMining_trigrams_edit_set_ratio           3
62         online_testMagic_unigrams_diffqt-len-radio           2
0                    online_testTextMining_text_q-len           2
24          online_testTextMining_unichars_dice_ratio           2
1                    online_testTextMining_text_t-len           2
43                      online_testWord2vec_cityblock           2
52  online_testMagic_unigrams_diffSetSimedit_set_r...           1
46                    online_testWord2vec_sqeuclidean           1
27      online_testTextMining_unichars_edit_set_ratio           1
22  online_testTextMining_text_partial_token_sort_...           1
9               online_testTextMining_unichars_qt-max           1
37       online_testTextMining_trigrams_jaccard_ratio           0
33        online_testTextMining_bigrams_jaccard_ratio           0
34       online_testTextMining_bigrams_edit_seq_ratio           0
36          online_testTextMining_trigrams_dice_ratio           0
42                      online_testWord2vec_chebyshev           0
38      online_testTextMining_trigrams_edit_seq_ratio           0
41                       online_testWord2vec_canberra           0
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           0
25       online_testTextMining_unichars_jaccard_ratio           0
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio           0
30      online_testTextMining_unigrams_edit_seq_ratio           0

[71 rows x 2 columns]
Valid Loss, AUC: 0.533178 0.673985                                                
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561571903_auc0.673985_loss0.533178_std0.003186.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561571903_auc0.673985_loss0.533178_std0.003186.npy
{                                                                                 
 "bagging_fraction": 0.6000000000000001,
 "bagging_freq": 0.0,
 "feature_fraction": 0.9,
 "learning_rate": 0.17,
 "max_bin": 15,
 "min_data_in_leaf": 30.0,
 "num_iterations": 125.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.532164                                             
[100]	valid's binary_logloss: 0.531333                                            
[50]	valid's binary_logloss: 0.532278                                             
[100]	valid's binary_logloss: 0.531444                                            
[50]	valid's binary_logloss: 0.532289                                             
[100]	valid's binary_logloss: 0.531472                                            
[50]	valid's binary_logloss: 0.532131                                             
[100]	valid's binary_logloss: 0.531309                                            
[50]	valid's binary_logloss: 0.532054                                             
[100]	valid's binary_logloss: 0.53128                                             
feature importance:                                                               
                                               column  importance                 
70  online_testVectorSpace_paired_manhattan_distances         176
68     online_testVectorSpace_paired_cosine_distances          75
47                                         query_freq          73
67               online_testMagic_unigrams_diffqt-avg          66
69  online_testVectorSpace_paired_euclidean_distances          63
44                         online_testWord2vec_cosine          50
15              online_testTextMining_unigrams_qt-avg          38
28          online_testTextMining_unigrams_dice_ratio          38
49     online_testMagic_unigrams_diffSetSimdice_ratio          36
11              online_testTextMining_unichars_qt-avg          33
61                online_testMagic_unigrams_difft-len          33
23         online_testTextMining_text_token_set_ratio          24
48                          online_testMagic_localCTR          24
65               online_testMagic_unigrams_diffqt-max          23
16                online_testTextMining_text_distance          23
10              online_testTextMining_unichars_qt-min          22
6         online_testTextMining_unigrams_qt-len-radio          17
12             online_testTextMining_unigrams_qt-diff          15
4                online_testTextMining_unigrams_q-len          14
17                    online_testTextMining_text_jaro          14
57     online_testMagic_trigrams_diffSetSimdice_ratio          14
53      online_testMagic_bigrams_diffSetSimdice_ratio          13
3             online_testTextMining_text_tq-len-radio          13
7         online_testTextMining_unigrams_tq-len-radio          12
66               online_testMagic_unigrams_diffqt-min          12
18            online_testTextMining_text_jaro_winkler          11
21        online_testTextMining_text_token_sort_ratio          11
20           online_testTextMining_text_partial_ratio          11
32           online_testTextMining_bigrams_dice_ratio          10
40                     online_testWord2vec_braycurtis          10
..                                                ...         ...
60  online_testMagic_trigrams_diffSetSimedit_set_r...           5
34       online_testTextMining_bigrams_edit_seq_ratio           5
26      online_testTextMining_unichars_edit_seq_ratio           5
64              online_testMagic_unigrams_diffqt-diff           4
35       online_testTextMining_bigrams_edit_set_ratio           4
1                    online_testTextMining_text_t-len           4
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           3
36          online_testTextMining_trigrams_dice_ratio           3
56  online_testMagic_bigrams_diffSetSimedit_set_ratio           3
54   online_testMagic_bigrams_diffSetSimjaccard_ratio           3
0                    online_testTextMining_text_q-len           3
39      online_testTextMining_trigrams_edit_set_ratio           3
52  online_testMagic_unigrams_diffSetSimedit_set_r...           2
24          online_testTextMining_unichars_dice_ratio           2
19                   online_testTextMining_text_ratio           2
22  online_testTextMining_text_partial_token_sort_...           2
29       online_testTextMining_unigrams_jaccard_ratio           2
43                      online_testWord2vec_cityblock           2
33        online_testTextMining_bigrams_jaccard_ratio           1
30      online_testTextMining_unigrams_edit_seq_ratio           1
27      online_testTextMining_unichars_edit_set_ratio           1
41                       online_testWord2vec_canberra           1
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio           1
13              online_testTextMining_unigrams_qt-max           1
8              online_testTextMining_unichars_qt-diff           1
42                      online_testWord2vec_chebyshev           0
37       online_testTextMining_trigrams_jaccard_ratio           0
62         online_testMagic_unigrams_diffqt-len-radio           0
25       online_testTextMining_unichars_jaccard_ratio           0
38      online_testTextMining_trigrams_edit_seq_ratio           0

[71 rows x 2 columns]
Valid Loss, AUC: 0.532943 0.674821                                                
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561572978_auc0.674821_loss0.532943_std0.003554.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561572978_auc0.674821_loss0.532943_std0.003554.npy
{                                                                                  
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 4.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.16,
 "max_bin": 63,
 "min_data_in_leaf": 20.0,
 "num_iterations": 100.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.532115                                              
[100]	valid's binary_logloss: 0.531232                                             
[50]	valid's binary_logloss: 0.532295                                              
[100]	valid's binary_logloss: 0.531347                                             
[50]	valid's binary_logloss: 0.532302                                              
[100]	valid's binary_logloss: 0.531432                                             
[50]	valid's binary_logloss: 0.532192                                              
[100]	valid's binary_logloss: 0.531289                                             
[50]	valid's binary_logloss: 0.53211                                               
[100]	valid's binary_logloss: 0.531208                                             
feature importance:                                                                
                                               column  importance                  
70  online_testVectorSpace_paired_manhattan_distances         138
67               online_testMagic_unigrams_diffqt-avg          66
47                                         query_freq          62
69  online_testVectorSpace_paired_euclidean_distances          47
68     online_testVectorSpace_paired_cosine_distances          44
44                         online_testWord2vec_cosine          38
61                online_testMagic_unigrams_difft-len          32
11              online_testTextMining_unichars_qt-avg          31
48                          online_testMagic_localCTR          31
28          online_testTextMining_unigrams_dice_ratio          27
23         online_testTextMining_text_token_set_ratio          25
15              online_testTextMining_unigrams_qt-avg          23
49     online_testMagic_unigrams_diffSetSimdice_ratio          21
10              online_testTextMining_unichars_qt-min          19
65               online_testMagic_unigrams_diffqt-max          16
16                online_testTextMining_text_distance          14
3             online_testTextMining_text_tq-len-radio          14
20           online_testTextMining_text_partial_ratio          13
50  online_testMagic_unigrams_diffSetSimjaccard_ratio          13
18            online_testTextMining_text_jaro_winkler          13
1                    online_testTextMining_text_t-len          12
4                online_testTextMining_unigrams_q-len           9
66               online_testMagic_unigrams_diffqt-min           9
7         online_testTextMining_unigrams_tq-len-radio           9
63         online_testMagic_unigrams_difftq-len-radio           8
40                     online_testWord2vec_braycurtis           8
0                    online_testTextMining_text_q-len           8
17                    online_testTextMining_text_jaro           8
2             online_testTextMining_text_qt-len-radio           8
46                    online_testWord2vec_sqeuclidean           7
..                                                ...         ...
36          online_testTextMining_trigrams_dice_ratio           4
51  online_testMagic_unigrams_diffSetSimedit_seq_r...           4
8              online_testTextMining_unichars_qt-diff           4
45                      online_testWord2vec_euclidean           4
29       online_testTextMining_unigrams_jaccard_ratio           4
9               online_testTextMining_unichars_qt-max           3
64              online_testMagic_unigrams_diffqt-diff           3
60  online_testMagic_trigrams_diffSetSimedit_set_r...           3
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           3
12             online_testTextMining_unigrams_qt-diff           3
27      online_testTextMining_unichars_edit_set_ratio           3
35       online_testTextMining_bigrams_edit_set_ratio           3
14              online_testTextMining_unigrams_qt-min           3
41                       online_testWord2vec_canberra           3
43                      online_testWord2vec_cityblock           2
24          online_testTextMining_unichars_dice_ratio           2
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio           2
19                   online_testTextMining_text_ratio           2
22  online_testTextMining_text_partial_token_sort_...           1
56  online_testMagic_bigrams_diffSetSimedit_set_ratio           1
42                      online_testWord2vec_chebyshev           1
38      online_testTextMining_trigrams_edit_seq_ratio           1
34       online_testTextMining_bigrams_edit_seq_ratio           1
30      online_testTextMining_unigrams_edit_seq_ratio           1
62         online_testMagic_unigrams_diffqt-len-radio           0
39      online_testTextMining_trigrams_edit_set_ratio           0
37       online_testTextMining_trigrams_jaccard_ratio           0
25       online_testTextMining_unichars_jaccard_ratio           0
33        online_testTextMining_bigrams_jaccard_ratio           0
52  online_testMagic_unigrams_diffSetSimedit_set_r...           0

[71 rows x 2 columns]
Valid Loss, AUC: 0.533625 0.674521                                                 
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561573794_auc0.674521_loss0.533625_std0.004539.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561573794_auc0.674521_loss0.533625_std0.004539.npy
{                                                                                  
 "bagging_fraction": 0.6000000000000001,
 "bagging_freq": 8.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.15,
 "max_bin": 1023,
 "min_data_in_leaf": 10.0,
 "num_iterations": 125.0,
 "num_leaves": 20.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.531575                                           
[100]	valid's binary_logloss: 0.530694                                          
[50]	valid's binary_logloss: 0.531674                                           
[100]	valid's binary_logloss: 0.530768                                          
[50]	valid's binary_logloss: 0.531712                                           
[100]	valid's binary_logloss: 0.530828                                          
[50]	valid's binary_logloss: 0.531565                                           
[100]	valid's binary_logloss: 0.530664                                          
[50]	valid's binary_logloss: 0.531552                                           
[100]	valid's binary_logloss: 0.530671                                          
feature importance:                                                             
                                               column  importance               
70  online_testVectorSpace_paired_manhattan_distances         354
68     online_testVectorSpace_paired_cosine_distances         163
67               online_testMagic_unigrams_diffqt-avg         130
69  online_testVectorSpace_paired_euclidean_distances         108
44                         online_testWord2vec_cosine          93
11              online_testTextMining_unichars_qt-avg          91
15              online_testTextMining_unigrams_qt-avg          89
47                                         query_freq          83
28          online_testTextMining_unigrams_dice_ratio          61
23         online_testTextMining_text_token_set_ratio          58
61                online_testMagic_unigrams_difft-len          53
49     online_testMagic_unigrams_diffSetSimdice_ratio          52
1                    online_testTextMining_text_t-len          42
48                          online_testMagic_localCTR          40
16                online_testTextMining_text_distance          37
31      online_testTextMining_unigrams_edit_set_ratio          37
63         online_testMagic_unigrams_difftq-len-radio          36
18            online_testTextMining_text_jaro_winkler          36
10              online_testTextMining_unichars_qt-min          36
40                     online_testWord2vec_braycurtis          34
0                    online_testTextMining_text_q-len          30
20           online_testTextMining_text_partial_ratio          29
65               online_testMagic_unigrams_diffqt-max          29
2             online_testTextMining_text_qt-len-radio          26
17                    online_testTextMining_text_jaro          26
5                online_testTextMining_unigrams_t-len          25
6         online_testTextMining_unigrams_qt-len-radio          25
32           online_testTextMining_bigrams_dice_ratio          24
43                      online_testWord2vec_cityblock          23
3             online_testTextMining_text_tq-len-radio          23
..                                                ...         ...
4                online_testTextMining_unigrams_q-len          16
13              online_testTextMining_unigrams_qt-max          16
30      online_testTextMining_unigrams_edit_seq_ratio          16
34       online_testTextMining_bigrams_edit_seq_ratio          15
41                       online_testWord2vec_canberra          14
12             online_testTextMining_unigrams_qt-diff          14
51  online_testMagic_unigrams_diffSetSimedit_seq_r...          13
60  online_testMagic_trigrams_diffSetSimedit_set_r...          13
27      online_testTextMining_unichars_edit_set_ratio          12
53      online_testMagic_bigrams_diffSetSimdice_ratio          11
42                      online_testWord2vec_chebyshev          10
8              online_testTextMining_unichars_qt-diff          10
64              online_testMagic_unigrams_diffqt-diff           9
62         online_testMagic_unigrams_diffqt-len-radio           9
33        online_testTextMining_bigrams_jaccard_ratio           8
52  online_testMagic_unigrams_diffSetSimedit_set_r...           8
24          online_testTextMining_unichars_dice_ratio           8
38      online_testTextMining_trigrams_edit_seq_ratio           7
19                   online_testTextMining_text_ratio           7
29       online_testTextMining_unigrams_jaccard_ratio           7
22  online_testTextMining_text_partial_token_sort_...           6
7         online_testTextMining_unigrams_tq-len-radio           6
54   online_testMagic_bigrams_diffSetSimjaccard_ratio           6
56  online_testMagic_bigrams_diffSetSimedit_set_ratio           4
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio           4
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           3
36          online_testTextMining_trigrams_dice_ratio           3
39      online_testTextMining_trigrams_edit_set_ratio           2
37       online_testTextMining_trigrams_jaccard_ratio           1
25       online_testTextMining_unichars_jaccard_ratio           0

[71 rows x 2 columns]
Valid Loss, AUC: 0.532629 0.676243                                              
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561574808_auc0.676243_loss0.532629_std0.004358.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561574808_auc0.676243_loss0.532629_std0.004358.npy
{                                                                               
 "bagging_fraction": 0.9,
 "bagging_freq": 2.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.18,
 "max_bin": 63,
 "min_data_in_leaf": 30.0,
 "num_iterations": 75.0,
 "num_leaves": 20.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.531307                                           
[50]	valid's binary_logloss: 0.531427                                           
[50]	valid's binary_logloss: 0.531446                                           
[50]	valid's binary_logloss: 0.531329                                           
[50]	valid's binary_logloss: 0.531272                                           
feature importance:                                                             
                                               column  importance               
70  online_testVectorSpace_paired_manhattan_distances         227
69  online_testVectorSpace_paired_euclidean_distances          88
67               online_testMagic_unigrams_diffqt-avg          87
68     online_testVectorSpace_paired_cosine_distances          71
47                                         query_freq          70
44                         online_testWord2vec_cosine          62
15              online_testTextMining_unigrams_qt-avg          60
11              online_testTextMining_unichars_qt-avg          55
61                online_testMagic_unigrams_difft-len          41
49     online_testMagic_unigrams_diffSetSimdice_ratio          40
28          online_testTextMining_unigrams_dice_ratio          39
10              online_testTextMining_unichars_qt-min          35
23         online_testTextMining_text_token_set_ratio          34
48                          online_testMagic_localCTR          27
3             online_testTextMining_text_tq-len-radio          27
65               online_testMagic_unigrams_diffqt-max          25
16                online_testTextMining_text_distance          22
63         online_testMagic_unigrams_difftq-len-radio          18
1                    online_testTextMining_text_t-len          18
31      online_testTextMining_unigrams_edit_set_ratio          17
50  online_testMagic_unigrams_diffSetSimjaccard_ratio          16
18            online_testTextMining_text_jaro_winkler          16
40                     online_testWord2vec_braycurtis          16
32           online_testTextMining_bigrams_dice_ratio          16
0                    online_testTextMining_text_q-len          15
53      online_testMagic_bigrams_diffSetSimdice_ratio          14
5                online_testTextMining_unigrams_t-len          14
66               online_testMagic_unigrams_diffqt-min          14
57     online_testMagic_trigrams_diffSetSimdice_ratio          14
46                    online_testWord2vec_sqeuclidean          13
..                                                ...         ...
9               online_testTextMining_unichars_qt-max           7
59  online_testMagic_trigrams_diffSetSimedit_seq_r...           7
51  online_testMagic_unigrams_diffSetSimedit_seq_r...           6
2             online_testTextMining_text_qt-len-radio           6
54   online_testMagic_bigrams_diffSetSimjaccard_ratio           5
56  online_testMagic_bigrams_diffSetSimedit_set_ratio           5
60  online_testMagic_trigrams_diffSetSimedit_set_r...           5
35       online_testTextMining_bigrams_edit_set_ratio           5
14              online_testTextMining_unigrams_qt-min           5
34       online_testTextMining_bigrams_edit_seq_ratio           5
19                   online_testTextMining_text_ratio           4
29       online_testTextMining_unigrams_jaccard_ratio           4
43                      online_testWord2vec_cityblock           4
36          online_testTextMining_trigrams_dice_ratio           4
41                       online_testWord2vec_canberra           4
52  online_testMagic_unigrams_diffSetSimedit_set_r...           3
62         online_testMagic_unigrams_diffqt-len-radio           3
64              online_testMagic_unigrams_diffqt-diff           3
30      online_testTextMining_unigrams_edit_seq_ratio           3
24          online_testTextMining_unichars_dice_ratio           3
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           2
33        online_testTextMining_bigrams_jaccard_ratio           2
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio           1
38      online_testTextMining_trigrams_edit_seq_ratio           1
42                      online_testWord2vec_chebyshev           1
27      online_testTextMining_unichars_edit_set_ratio           1
39      online_testTextMining_trigrams_edit_set_ratio           0
37       online_testTextMining_trigrams_jaccard_ratio           0
22  online_testTextMining_text_partial_token_sort_...           0
25       online_testTextMining_unichars_jaccard_ratio           0

[71 rows x 2 columns]
Valid Loss, AUC: 0.533131 0.675502                                              
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561575770_auc0.675502_loss0.533131_std0.004211.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561575770_auc0.675502_loss0.533131_std0.004211.npy
{                                                                               
 "bagging_fraction": 0.8,
 "bagging_freq": 2.0,
 "feature_fraction": 1.0,
 "learning_rate": 0.14,
 "max_bin": 63,
 "min_data_in_leaf": 30.0,
 "num_iterations": 125.0,
 "num_leaves": 5.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.533153                                           
[100]	valid's binary_logloss: 0.532246                                          
[50]	valid's binary_logloss: 0.533311                                           
[100]	valid's binary_logloss: 0.532387                                          
[50]	valid's binary_logloss: 0.533284                                           
[100]	valid's binary_logloss: 0.53241                                           
[50]	valid's binary_logloss: 0.533188                                           
[100]	valid's binary_logloss: 0.532253                                          
[50]	valid's binary_logloss: 0.53311                                            
[100]	valid's binary_logloss: 0.532199                                          
feature importance:                                                             
                                               column  importance               
70  online_testVectorSpace_paired_manhattan_distances          84
47                                         query_freq          77
67               online_testMagic_unigrams_diffqt-avg          44
69  online_testVectorSpace_paired_euclidean_distances          33
44                         online_testWord2vec_cosine          25
49     online_testMagic_unigrams_diffSetSimdice_ratio          23
68     online_testVectorSpace_paired_cosine_distances          17
28          online_testTextMining_unigrams_dice_ratio          15
23         online_testTextMining_text_token_set_ratio          14
61                online_testMagic_unigrams_difft-len          14
15              online_testTextMining_unigrams_qt-avg          11
57     online_testMagic_trigrams_diffSetSimdice_ratio          10
53      online_testMagic_bigrams_diffSetSimdice_ratio           9
10              online_testTextMining_unichars_qt-min           9
65               online_testMagic_unigrams_diffqt-max           9
63         online_testMagic_unigrams_difftq-len-radio           9
18            online_testTextMining_text_jaro_winkler           8
2             online_testTextMining_text_qt-len-radio           6
31      online_testTextMining_unigrams_edit_set_ratio           6
11              online_testTextMining_unichars_qt-avg           6
7         online_testTextMining_unigrams_tq-len-radio           5
20           online_testTextMining_text_partial_ratio           5
17                    online_testTextMining_text_jaro           4
3             online_testTextMining_text_tq-len-radio           4
6         online_testTextMining_unigrams_qt-len-radio           4
26      online_testTextMining_unichars_edit_seq_ratio           4
66               online_testMagic_unigrams_diffqt-min           4
16                online_testTextMining_text_distance           4
21        online_testTextMining_text_token_sort_ratio           3
32           online_testTextMining_bigrams_dice_ratio           3
..                                                ...         ...
45                      online_testWord2vec_euclidean           1
59  online_testMagic_trigrams_diffSetSimedit_seq_r...           1
13              online_testTextMining_unigrams_qt-max           1
64              online_testMagic_unigrams_diffqt-diff           1
46                    online_testWord2vec_sqeuclidean           1
12             online_testTextMining_unigrams_qt-diff           1
5                online_testTextMining_unigrams_t-len           1
34       online_testTextMining_bigrams_edit_seq_ratio           1
4                online_testTextMining_unigrams_q-len           1
24          online_testTextMining_unichars_dice_ratio           0
62         online_testMagic_unigrams_diffqt-len-radio           0
14              online_testTextMining_unigrams_qt-min           0
58  online_testMagic_trigrams_diffSetSimjaccard_ratio           0
22  online_testTextMining_text_partial_token_sort_...           0
37       online_testTextMining_trigrams_jaccard_ratio           0
55  online_testMagic_bigrams_diffSetSimedit_seq_ratio           0
38      online_testTextMining_trigrams_edit_seq_ratio           0
25       online_testTextMining_unichars_jaccard_ratio           0
52  online_testMagic_unigrams_diffSetSimedit_set_r...           0
51  online_testMagic_unigrams_diffSetSimedit_seq_r...           0
27      online_testTextMining_unichars_edit_set_ratio           0
29       online_testTextMining_unigrams_jaccard_ratio           0
48                          online_testMagic_localCTR           0
30      online_testTextMining_unigrams_edit_seq_ratio           0
33        online_testTextMining_bigrams_jaccard_ratio           0
43                      online_testWord2vec_cityblock           0
42                      online_testWord2vec_chebyshev           0
41                       online_testWord2vec_canberra           0
39      online_testTextMining_trigrams_edit_set_ratio           0
54   online_testMagic_bigrams_diffSetSimjaccard_ratio           0

[71 rows x 2 columns]
Valid Loss, AUC: 0.534116 0.672921                                              
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561576722_auc0.672921_loss0.534116_std0.003944.npy
Saved test results to /home/kesci/work/stage2/output/test/lgb_gbdt_1561576722_auc0.672921_loss0.534116_std0.003944.npy
100%|██████████| 10/10 [2:47:04<00:00, 961.84s/it, best loss: 0.5326264305315684]

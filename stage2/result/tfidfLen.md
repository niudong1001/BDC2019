{                                                   
 "bagging_fraction": 0.9,
 "bagging_freq": 6.0,
 "feature_fraction": 1.0,
 "learning_rate": 0.17,
 "max_bin": 63,
 "min_data_in_leaf": 30.0,
 "num_iterations": 200.0,
 "num_leaves": 15.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.530942               
[100]	valid's binary_logloss: 0.530918              
[150]	valid's binary_logloss: 0.530973              
[200]	valid's binary_logloss: 0.531127              
[50]	valid's binary_logloss: 0.530946               
[100]	valid's binary_logloss: 0.530921              
[150]	valid's binary_logloss: 0.531132              
[200]	valid's binary_logloss: 0.53123               
[50]	valid's binary_logloss: 0.529489               
[100]	valid's binary_logloss: 0.529306              
[150]	valid's binary_logloss: 0.52943               
[200]	valid's binary_logloss: 0.529641              
[50]	valid's binary_logloss: 0.529198               
[100]	valid's binary_logloss: 0.529079              
[150]	valid's binary_logloss: 0.529162              
[200]	valid's binary_logloss: 0.529344              
[50]	valid's binary_logloss: 0.530677               
[100]	valid's binary_logloss: 0.530389              
[150]	valid's binary_logloss: 0.530402              
[200]	valid's binary_logloss: 0.530572              
feature importance:                                 
                                               column  importance
47                                         query_freq         104
72                   debug_trainVectorSpace_tfidfTLen          97
40                debug_trainWord2vec_cosine_distance          90
78                  debug_trainVectorSpace_tfidfQTAvg          76
75                 debug_trainVectorSpace_tfidfQTDiff          74
22  debug_trainTextMining_text_partial_token_sort_...          73
20           debug_trainTextMining_text_partial_ratio          70
67               debug_trainMagic_unigrams_diffqt-avg          64
52  debug_trainMagic_unigrams_diffSetSimedit_set_r...          64
17                    debug_trainTextMining_text_jaro          63
28          debug_trainTextMining_unigrams_dice_ratio          62
18            debug_trainTextMining_text_jaro_winkler          62
43              debug_trainWord2vec_canberra_distance          61
70  debug_trainVectorSpace_paired_manhattan_distances          60
51  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          57
59  debug_trainMagic_trigrams_diffSetSimedit_seq_r...          55
55  debug_trainMagic_bigrams_diffSetSimedit_seq_ratio          50
61                debug_trainMagic_unigrams_difft-len          50
45             debug_trainWord2vec_euclidean_distance          49
49     debug_trainMagic_unigrams_diffSetSimdice_ratio          47
23         debug_trainTextMining_text_token_set_ratio          47
42            debug_trainWord2vec_braycurtis_distance          46
21        debug_trainTextMining_text_token_sort_ratio          46
24          debug_trainTextMining_unichars_dice_ratio          46
63         debug_trainMagic_unigrams_difftq-len-radio          45
30      debug_trainTextMining_unigrams_edit_seq_ratio          44
44             debug_trainWord2vec_cityblock_distance          42
68     debug_trainVectorSpace_paired_cosine_distances          40
46             debug_trainWord2vec_minkowski_distance          40
16                debug_trainTextMining_text_distance          39
..                                                ...         ...
69  debug_trainVectorSpace_paired_euclidean_distances          29
15              debug_trainTextMining_unigrams_qt-avg          29
53      debug_trainMagic_bigrams_diffSetSimdice_ratio          26
0                    debug_trainTextMining_text_q-len          26
2             debug_trainTextMining_text_qt-len-radio          26
35       debug_trainTextMining_bigrams_edit_set_ratio          25
32           debug_trainTextMining_bigrams_dice_ratio          25
64              debug_trainMagic_unigrams_diffqt-diff          25
12             debug_trainTextMining_unigrams_qt-diff          24
36          debug_trainTextMining_trigrams_dice_ratio          23
77                  debug_trainVectorSpace_tfidfQTMin          21
9               debug_trainTextMining_unichars_qt-max          21
6         debug_trainTextMining_unigrams_qt-len-radio          20
39      debug_trainTextMining_trigrams_edit_set_ratio          19
57     debug_trainMagic_trigrams_diffSetSimdice_ratio          18
10              debug_trainTextMining_unichars_qt-min          18
65               debug_trainMagic_unigrams_diffqt-max          14
7         debug_trainTextMining_unigrams_tq-len-radio           8
66               debug_trainMagic_unigrams_diffqt-min           8
48                          debug_trainMagic_localCTR           6
4                debug_trainTextMining_unigrams_q-len           2
14              debug_trainTextMining_unigrams_qt-min           1
25       debug_trainTextMining_unichars_jaccard_ratio           0
29       debug_trainTextMining_unigrams_jaccard_ratio           0
54   debug_trainMagic_bigrams_diffSetSimjaccard_ratio           0
33        debug_trainTextMining_bigrams_jaccard_ratio           0
37       debug_trainTextMining_trigrams_jaccard_ratio           0
58  debug_trainMagic_trigrams_diffSetSimjaccard_ratio           0
41               debug_trainWord2vec_jaccard_distance           0
50  debug_trainMagic_unigrams_diffSetSimjaccard_ratio           0

[79 rows x 2 columns]
Valid Loss, AUC: 0.530882 0.675023                  
----->Started 'cal q auc' block...                  
Valid Q AUC: 0.5547275073798665                     
----->Finished 'cal q auc' block, time used:112.85s.
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561645858_auc0.675023_loss0.530882_std0.002946.npy
{                                                                             
 "bagging_fraction": 0.9,
 "bagging_freq": 10.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.17,
 "max_bin": 255,
 "min_data_in_leaf": 40.0,
 "num_iterations": 150.0,
 "num_leaves": 15.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.530959                                         
[100]	valid's binary_logloss: 0.530876                                        
[150]	valid's binary_logloss: 0.531035                                        
[50]	valid's binary_logloss: 0.531037                                         
[100]	valid's binary_logloss: 0.530887                                        
[150]	valid's binary_logloss: 0.531074                                        
[50]	valid's binary_logloss: 0.529445                                         
[100]	valid's binary_logloss: 0.529287                                        
[150]	valid's binary_logloss: 0.529393                                        
[50]	valid's binary_logloss: 0.529152                                         
[100]	valid's binary_logloss: 0.528893                                        
[150]	valid's binary_logloss: 0.528947                                        
[50]	valid's binary_logloss: 0.530717                                         
[100]	valid's binary_logloss: 0.530573                                        
[150]	valid's binary_logloss: 0.53067                                         
feature importance:                                                           
                                               column  importance             
72                   debug_trainVectorSpace_tfidfTLen         105
47                                         query_freq          87
75                 debug_trainVectorSpace_tfidfQTDiff          65
40                debug_trainWord2vec_cosine_distance          58
18            debug_trainTextMining_text_jaro_winkler          53
70  debug_trainVectorSpace_paired_manhattan_distances          52
46             debug_trainWord2vec_minkowski_distance          51
17                    debug_trainTextMining_text_jaro          49
78                  debug_trainVectorSpace_tfidfQTAvg          49
51  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          49
42            debug_trainWord2vec_braycurtis_distance          45
20           debug_trainTextMining_text_partial_ratio          43
45             debug_trainWord2vec_euclidean_distance          41
52  debug_trainMagic_unigrams_diffSetSimedit_set_r...          40
44             debug_trainWord2vec_cityblock_distance          39
68     debug_trainVectorSpace_paired_cosine_distances          39
59  debug_trainMagic_trigrams_diffSetSimedit_seq_r...          39
49     debug_trainMagic_unigrams_diffSetSimdice_ratio          38
69  debug_trainVectorSpace_paired_euclidean_distances          36
43              debug_trainWord2vec_canberra_distance          36
61                debug_trainMagic_unigrams_difft-len          35
73             debug_trainVectorSpace_tfidfQTLenRadio          34
55  debug_trainMagic_bigrams_diffSetSimedit_seq_ratio          34
21        debug_trainTextMining_text_token_sort_ratio          34
28          debug_trainTextMining_unigrams_dice_ratio          32
67               debug_trainMagic_unigrams_diffqt-avg          31
56  debug_trainMagic_bigrams_diffSetSimedit_set_ratio          30
8              debug_trainTextMining_unichars_qt-diff          30
11              debug_trainTextMining_unichars_qt-avg          30
1                    debug_trainTextMining_text_t-len          29
..                                                ...         ...
74             debug_trainVectorSpace_tfidfTQLenRadio          20
71                   debug_trainVectorSpace_tfidfQLen          20
53      debug_trainMagic_bigrams_diffSetSimdice_ratio          19
35       debug_trainTextMining_bigrams_edit_set_ratio          18
9               debug_trainTextMining_unichars_qt-max          18
48                          debug_trainMagic_localCTR          16
13              debug_trainTextMining_unigrams_qt-max          16
64              debug_trainMagic_unigrams_diffqt-diff          14
0                    debug_trainTextMining_text_q-len          14
12             debug_trainTextMining_unigrams_qt-diff          12
36          debug_trainTextMining_trigrams_dice_ratio          12
77                  debug_trainVectorSpace_tfidfQTMin          11
6         debug_trainTextMining_unigrams_qt-len-radio          10
57     debug_trainMagic_trigrams_diffSetSimdice_ratio          10
10              debug_trainTextMining_unichars_qt-min          10
19                   debug_trainTextMining_text_ratio           9
32           debug_trainTextMining_bigrams_dice_ratio           8
7         debug_trainTextMining_unigrams_tq-len-radio           8
39      debug_trainTextMining_trigrams_edit_set_ratio           6
50  debug_trainMagic_unigrams_diffSetSimjaccard_ratio           6
54   debug_trainMagic_bigrams_diffSetSimjaccard_ratio           5
37       debug_trainTextMining_trigrams_jaccard_ratio           5
66               debug_trainMagic_unigrams_diffqt-min           5
29       debug_trainTextMining_unigrams_jaccard_ratio           4
33        debug_trainTextMining_bigrams_jaccard_ratio           3
25       debug_trainTextMining_unichars_jaccard_ratio           2
4                debug_trainTextMining_unigrams_q-len           2
58  debug_trainMagic_trigrams_diffSetSimjaccard_ratio           1
14              debug_trainTextMining_unigrams_qt-min           0
41               debug_trainWord2vec_jaccard_distance           0

[79 rows x 2 columns]
Valid Loss, AUC: 0.531073 0.675349                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5551336999953277                                               
----->Finished 'cal q auc' block, time used:113.12s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561646051_auc0.675349_loss0.531073_std0.003361.npy
{                                                                             
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 10.0,
 "feature_fraction": 1.0,
 "learning_rate": 0.17,
 "max_bin": 63,
 "min_data_in_leaf": 20.0,
 "num_iterations": 100.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.53129                                          
[100]	valid's binary_logloss: 0.531166                                        
[50]	valid's binary_logloss: 0.531152                                         
[100]	valid's binary_logloss: 0.530756                                        
[50]	valid's binary_logloss: 0.529659                                         
[100]	valid's binary_logloss: 0.529416                                        
[50]	valid's binary_logloss: 0.529405                                         
[100]	valid's binary_logloss: 0.529201                                        
[50]	valid's binary_logloss: 0.530797                                         
[100]	valid's binary_logloss: 0.530537                                        
feature importance:                                                           
                                               column  importance             
47                                         query_freq          62
72                   debug_trainVectorSpace_tfidfTLen          62
75                 debug_trainVectorSpace_tfidfQTDiff          35
40                debug_trainWord2vec_cosine_distance          31
78                  debug_trainVectorSpace_tfidfQTAvg          29
61                debug_trainMagic_unigrams_difft-len          29
20           debug_trainTextMining_text_partial_ratio          25
63         debug_trainMagic_unigrams_difftq-len-radio          22
49     debug_trainMagic_unigrams_diffSetSimdice_ratio          22
70  debug_trainVectorSpace_paired_manhattan_distances          22
28          debug_trainTextMining_unigrams_dice_ratio          21
18            debug_trainTextMining_text_jaro_winkler          21
67               debug_trainMagic_unigrams_diffqt-avg          21
17                    debug_trainTextMining_text_jaro          18
59  debug_trainMagic_trigrams_diffSetSimedit_seq_r...          18
53      debug_trainMagic_bigrams_diffSetSimdice_ratio          17
42            debug_trainWord2vec_braycurtis_distance          16
16                debug_trainTextMining_text_distance          15
76                  debug_trainVectorSpace_tfidfQTMax          15
62         debug_trainMagic_unigrams_diffqt-len-radio          15
23         debug_trainTextMining_text_token_set_ratio          14
13              debug_trainTextMining_unigrams_qt-max          14
51  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          14
22  debug_trainTextMining_text_partial_token_sort_...          14
68     debug_trainVectorSpace_paired_cosine_distances          13
5                debug_trainTextMining_unigrams_t-len          13
1                    debug_trainTextMining_text_t-len          12
21        debug_trainTextMining_text_token_sort_ratio          11
73             debug_trainVectorSpace_tfidfQTLenRadio          11
3             debug_trainTextMining_text_tq-len-radio          11
..                                                ...         ...
30      debug_trainTextMining_unigrams_edit_seq_ratio           7
2             debug_trainTextMining_text_qt-len-radio           7
31      debug_trainTextMining_unigrams_edit_set_ratio           6
12             debug_trainTextMining_unigrams_qt-diff           6
60  debug_trainMagic_trigrams_diffSetSimedit_set_r...           6
77                  debug_trainVectorSpace_tfidfQTMin           6
46             debug_trainWord2vec_minkowski_distance           6
6         debug_trainTextMining_unigrams_qt-len-radio           6
56  debug_trainMagic_bigrams_diffSetSimedit_set_ratio           5
35       debug_trainTextMining_bigrams_edit_set_ratio           5
74             debug_trainVectorSpace_tfidfTQLenRadio           5
71                   debug_trainVectorSpace_tfidfQLen           5
44             debug_trainWord2vec_cityblock_distance           5
32           debug_trainTextMining_bigrams_dice_ratio           4
10              debug_trainTextMining_unichars_qt-min           4
7         debug_trainTextMining_unigrams_tq-len-radio           3
34       debug_trainTextMining_bigrams_edit_seq_ratio           3
39      debug_trainTextMining_trigrams_edit_set_ratio           2
4                debug_trainTextMining_unigrams_q-len           2
66               debug_trainMagic_unigrams_diffqt-min           1
48                          debug_trainMagic_localCTR           1
37       debug_trainTextMining_trigrams_jaccard_ratio           0
14              debug_trainTextMining_unigrams_qt-min           0
54   debug_trainMagic_bigrams_diffSetSimjaccard_ratio           0
25       debug_trainTextMining_unichars_jaccard_ratio           0
50  debug_trainMagic_unigrams_diffSetSimjaccard_ratio           0
29       debug_trainTextMining_unigrams_jaccard_ratio           0
41               debug_trainWord2vec_jaccard_distance           0
33        debug_trainTextMining_bigrams_jaccard_ratio           0
58  debug_trainMagic_trigrams_diffSetSimjaccard_ratio           0

[79 rows x 2 columns]
Valid Loss, AUC: 0.53179 0.675369                                             
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5555486150287626                                               
----->Finished 'cal q auc' block, time used:112.52s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561646221_auc0.675369_loss0.531790_std0.004016.npy
{                                                                             
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 6.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.11,
 "max_bin": 255,
 "min_data_in_leaf": 10.0,
 "num_iterations": 100.0,
 "num_leaves": 20.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.531183                                         
[100]	valid's binary_logloss: 0.530942                                        
[50]	valid's binary_logloss: 0.53102                                          
[100]	valid's binary_logloss: 0.53081                                         
[50]	valid's binary_logloss: 0.529634                                         
[100]	valid's binary_logloss: 0.529356                                        
[50]	valid's binary_logloss: 0.529237                                         
[100]	valid's binary_logloss: 0.528898                                        
[50]	valid's binary_logloss: 0.530984                                         
[100]	valid's binary_logloss: 0.530531                                        
feature importance:                                                           
                                               column  importance             
72                   debug_trainVectorSpace_tfidfTLen         128
47                                         query_freq         110
75                 debug_trainVectorSpace_tfidfQTDiff          75
40                debug_trainWord2vec_cosine_distance          59
78                  debug_trainVectorSpace_tfidfQTAvg          50
17                    debug_trainTextMining_text_jaro          49
76                  debug_trainVectorSpace_tfidfQTMax          46
70  debug_trainVectorSpace_paired_manhattan_distances          46
61                debug_trainMagic_unigrams_difft-len          45
67               debug_trainMagic_unigrams_diffqt-avg          44
18            debug_trainTextMining_text_jaro_winkler          44
20           debug_trainTextMining_text_partial_ratio          40
49     debug_trainMagic_unigrams_diffSetSimdice_ratio          35
51  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          35
42            debug_trainWord2vec_braycurtis_distance          35
44             debug_trainWord2vec_cityblock_distance          34
5                debug_trainTextMining_unigrams_t-len          32
1                    debug_trainTextMining_text_t-len          30
63         debug_trainMagic_unigrams_difftq-len-radio          29
68     debug_trainVectorSpace_paired_cosine_distances          28
46             debug_trainWord2vec_minkowski_distance          27
52  debug_trainMagic_unigrams_diffSetSimedit_set_r...          27
73             debug_trainVectorSpace_tfidfQTLenRadio          27
59  debug_trainMagic_trigrams_diffSetSimedit_seq_r...          26
30      debug_trainTextMining_unigrams_edit_seq_ratio          26
55  debug_trainMagic_bigrams_diffSetSimedit_seq_ratio          26
26      debug_trainTextMining_unichars_edit_seq_ratio          25
65               debug_trainMagic_unigrams_diffqt-max          25
21        debug_trainTextMining_text_token_sort_ratio          25
8              debug_trainTextMining_unichars_qt-diff          24
..                                                ...         ...
24          debug_trainTextMining_unichars_dice_ratio          17
27      debug_trainTextMining_unichars_edit_set_ratio          17
35       debug_trainTextMining_bigrams_edit_set_ratio          16
9               debug_trainTextMining_unichars_qt-max          14
56  debug_trainMagic_bigrams_diffSetSimedit_set_ratio          13
69  debug_trainVectorSpace_paired_euclidean_distances          13
48                          debug_trainMagic_localCTR          13
34       debug_trainTextMining_bigrams_edit_seq_ratio          12
39      debug_trainTextMining_trigrams_edit_set_ratio          11
57     debug_trainMagic_trigrams_diffSetSimdice_ratio          11
50  debug_trainMagic_unigrams_diffSetSimjaccard_ratio          10
6         debug_trainTextMining_unigrams_qt-len-radio          10
77                  debug_trainVectorSpace_tfidfQTMin          10
19                   debug_trainTextMining_text_ratio          10
36          debug_trainTextMining_trigrams_dice_ratio           9
12             debug_trainTextMining_unigrams_qt-diff           9
64              debug_trainMagic_unigrams_diffqt-diff           8
10              debug_trainTextMining_unichars_qt-min           7
29       debug_trainTextMining_unigrams_jaccard_ratio           6
33        debug_trainTextMining_bigrams_jaccard_ratio           6
66               debug_trainMagic_unigrams_diffqt-min           5
7         debug_trainTextMining_unigrams_tq-len-radio           5
32           debug_trainTextMining_bigrams_dice_ratio           4
37       debug_trainTextMining_trigrams_jaccard_ratio           3
58  debug_trainMagic_trigrams_diffSetSimjaccard_ratio           2
54   debug_trainMagic_bigrams_diffSetSimjaccard_ratio           2
14              debug_trainTextMining_unigrams_qt-min           1
4                debug_trainTextMining_unigrams_q-len           1
41               debug_trainWord2vec_jaccard_distance           0
25       debug_trainTextMining_unichars_jaccard_ratio           0

[79 rows x 2 columns]
Valid Loss, AUC: 0.532277 0.675579                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5574170249041074                                               
----->Finished 'cal q auc' block, time used:112.27s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561646397_auc0.675579_loss0.532277_std0.005080.npy
{                                                                             
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 6.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.16,
 "max_bin": 63,
 "min_data_in_leaf": 10.0,
 "num_iterations": 175.0,
 "num_leaves": 15.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.530961                                         
[100]	valid's binary_logloss: 0.530907                                        
[150]	valid's binary_logloss: 0.531127                                        
[50]	valid's binary_logloss: 0.531148                                         
[100]	valid's binary_logloss: 0.531037                                        
[150]	valid's binary_logloss: 0.531257                                        
[50]	valid's binary_logloss: 0.529665                                         
[100]	valid's binary_logloss: 0.529545                                        
[150]	valid's binary_logloss: 0.529728                                        
[50]	valid's binary_logloss: 0.529464                                         
[100]	valid's binary_logloss: 0.529241                                        
[150]	valid's binary_logloss: 0.529284                                        
[50]	valid's binary_logloss: 0.530671                                         
[100]	valid's binary_logloss: 0.530615                                        
[150]	valid's binary_logloss: 0.530607                                        
feature importance:                                                           
                                               column  importance             
72                   debug_trainVectorSpace_tfidfTLen         103
47                                         query_freq          88
40                debug_trainWord2vec_cosine_distance          63
20           debug_trainTextMining_text_partial_ratio          61
70  debug_trainVectorSpace_paired_manhattan_distances          59
18            debug_trainTextMining_text_jaro_winkler          57
42            debug_trainWord2vec_braycurtis_distance          54
17                    debug_trainTextMining_text_jaro          54
75                 debug_trainVectorSpace_tfidfQTDiff          51
67               debug_trainMagic_unigrams_diffqt-avg          48
78                  debug_trainVectorSpace_tfidfQTAvg          48
43              debug_trainWord2vec_canberra_distance          47
51  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          47
28          debug_trainTextMining_unigrams_dice_ratio          45
76                  debug_trainVectorSpace_tfidfQTMax          45
52  debug_trainMagic_unigrams_diffSetSimedit_set_r...          43
22  debug_trainTextMining_text_partial_token_sort_...          43
46             debug_trainWord2vec_minkowski_distance          41
49     debug_trainMagic_unigrams_diffSetSimdice_ratio          40
61                debug_trainMagic_unigrams_difft-len          39
59  debug_trainMagic_trigrams_diffSetSimedit_seq_r...          38
13              debug_trainTextMining_unigrams_qt-max          37
1                    debug_trainTextMining_text_t-len          37
55  debug_trainMagic_bigrams_diffSetSimedit_seq_ratio          37
71                   debug_trainVectorSpace_tfidfQLen          36
62         debug_trainMagic_unigrams_diffqt-len-radio          35
63         debug_trainMagic_unigrams_difftq-len-radio          35
30      debug_trainTextMining_unigrams_edit_seq_ratio          35
24          debug_trainTextMining_unichars_dice_ratio          35
23         debug_trainTextMining_text_token_set_ratio          35
..                                                ...         ...
56  debug_trainMagic_bigrams_diffSetSimedit_set_ratio          23
35       debug_trainTextMining_bigrams_edit_set_ratio          23
34       debug_trainTextMining_bigrams_edit_seq_ratio          23
26      debug_trainTextMining_unichars_edit_seq_ratio          23
15              debug_trainTextMining_unigrams_qt-avg          23
32           debug_trainTextMining_bigrams_dice_ratio          22
3             debug_trainTextMining_text_tq-len-radio          21
60  debug_trainMagic_trigrams_diffSetSimedit_set_r...          21
53      debug_trainMagic_bigrams_diffSetSimdice_ratio          20
64              debug_trainMagic_unigrams_diffqt-diff          19
0                    debug_trainTextMining_text_q-len          19
38      debug_trainTextMining_trigrams_edit_seq_ratio          19
57     debug_trainMagic_trigrams_diffSetSimdice_ratio          19
9               debug_trainTextMining_unichars_qt-max          19
39      debug_trainTextMining_trigrams_edit_set_ratio          18
36          debug_trainTextMining_trigrams_dice_ratio          15
29       debug_trainTextMining_unigrams_jaccard_ratio          15
6         debug_trainTextMining_unigrams_qt-len-radio          13
7         debug_trainTextMining_unigrams_tq-len-radio          11
50  debug_trainMagic_unigrams_diffSetSimjaccard_ratio          11
66               debug_trainMagic_unigrams_diffqt-min          11
12             debug_trainTextMining_unigrams_qt-diff          11
25       debug_trainTextMining_unichars_jaccard_ratio           9
4                debug_trainTextMining_unigrams_q-len           5
54   debug_trainMagic_bigrams_diffSetSimjaccard_ratio           4
37       debug_trainTextMining_trigrams_jaccard_ratio           4
33        debug_trainTextMining_bigrams_jaccard_ratio           3
14              debug_trainTextMining_unigrams_qt-min           3
58  debug_trainMagic_trigrams_diffSetSimjaccard_ratio           1
41               debug_trainWord2vec_jaccard_distance           0

[79 rows x 2 columns]
Valid Loss, AUC: 0.531164 0.674653                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5541632953421521                                               
----->Finished 'cal q auc' block, time used:112.33s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561646586_auc0.674653_loss0.531164_std0.003218.npy
{                                                                             
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 4.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.16,
 "max_bin": 255,
 "min_data_in_leaf": 30.0,
 "num_iterations": 125.0,
 "num_leaves": 15.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.531243                                         
[100]	valid's binary_logloss: 0.531234                                        
[50]	valid's binary_logloss: 0.530808                                         
[100]	valid's binary_logloss: 0.530771                                        
[50]	valid's binary_logloss: 0.529468                                         
[100]	valid's binary_logloss: 0.529298                                        
[50]	valid's binary_logloss: 0.529189                                         
[100]	valid's binary_logloss: 0.529069                                        
[50]	valid's binary_logloss: 0.530901                                         
[100]	valid's binary_logloss: 0.53069                                         
feature importance:                                                           
                                               column  importance             
72                   debug_trainVectorSpace_tfidfTLen          82
47                                         query_freq          67
75                 debug_trainVectorSpace_tfidfQTDiff          56
40                debug_trainWord2vec_cosine_distance          54
76                  debug_trainVectorSpace_tfidfQTMax          52
70  debug_trainVectorSpace_paired_manhattan_distances          42
17                    debug_trainTextMining_text_jaro          40
46             debug_trainWord2vec_minkowski_distance          39
51  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          39
78                  debug_trainVectorSpace_tfidfQTAvg          38
43              debug_trainWord2vec_canberra_distance          37
68     debug_trainVectorSpace_paired_cosine_distances          36
18            debug_trainTextMining_text_jaro_winkler          35
67               debug_trainMagic_unigrams_diffqt-avg          35
20           debug_trainTextMining_text_partial_ratio          34
5                debug_trainTextMining_unigrams_t-len          33
59  debug_trainMagic_trigrams_diffSetSimedit_seq_r...          31
24          debug_trainTextMining_unichars_dice_ratio          30
42            debug_trainWord2vec_braycurtis_distance          30
61                debug_trainMagic_unigrams_difft-len          30
63         debug_trainMagic_unigrams_difftq-len-radio          29
22  debug_trainTextMining_text_partial_token_sort_...          29
30      debug_trainTextMining_unigrams_edit_seq_ratio          29
49     debug_trainMagic_unigrams_diffSetSimdice_ratio          25
38      debug_trainTextMining_trigrams_edit_seq_ratio          25
2             debug_trainTextMining_text_qt-len-radio          24
26      debug_trainTextMining_unichars_edit_seq_ratio          24
16                debug_trainTextMining_text_distance          24
8              debug_trainTextMining_unichars_qt-diff          24
55  debug_trainMagic_bigrams_diffSetSimedit_seq_ratio          24
..                                                ...         ...
74             debug_trainVectorSpace_tfidfTQLenRadio          17
27      debug_trainTextMining_unichars_edit_set_ratio          16
3             debug_trainTextMining_text_tq-len-radio          16
23         debug_trainTextMining_text_token_set_ratio          15
53      debug_trainMagic_bigrams_diffSetSimdice_ratio          15
77                  debug_trainVectorSpace_tfidfQTMin          14
64              debug_trainMagic_unigrams_diffqt-diff          13
50  debug_trainMagic_unigrams_diffSetSimjaccard_ratio          13
12             debug_trainTextMining_unigrams_qt-diff          13
57     debug_trainMagic_trigrams_diffSetSimdice_ratio          13
39      debug_trainTextMining_trigrams_edit_set_ratio          12
10              debug_trainTextMining_unichars_qt-min          12
6         debug_trainTextMining_unigrams_qt-len-radio          11
9               debug_trainTextMining_unichars_qt-max          11
35       debug_trainTextMining_bigrams_edit_set_ratio          10
19                   debug_trainTextMining_text_ratio           9
36          debug_trainTextMining_trigrams_dice_ratio           9
29       debug_trainTextMining_unigrams_jaccard_ratio           8
66               debug_trainMagic_unigrams_diffqt-min           8
0                    debug_trainTextMining_text_q-len           7
32           debug_trainTextMining_bigrams_dice_ratio           6
7         debug_trainTextMining_unigrams_tq-len-radio           6
54   debug_trainMagic_bigrams_diffSetSimjaccard_ratio           3
25       debug_trainTextMining_unichars_jaccard_ratio           3
33        debug_trainTextMining_bigrams_jaccard_ratio           3
58  debug_trainMagic_trigrams_diffSetSimjaccard_ratio           3
37       debug_trainTextMining_trigrams_jaccard_ratio           2
14              debug_trainTextMining_unigrams_qt-min           0
41               debug_trainWord2vec_jaccard_distance           0
4                debug_trainTextMining_unigrams_q-len           0

[79 rows x 2 columns]
Valid Loss, AUC: 0.531415 0.675294                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5552582092787288                                               
----->Finished 'cal q auc' block, time used:110.3s.                           
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561646763_auc0.675294_loss0.531415_std0.003768.npy
{                                                                             
 "bagging_fraction": 1.0,
 "bagging_freq": 4.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.16,
 "max_bin": 63,
 "min_data_in_leaf": 50.0,
 "num_iterations": 125.0,
 "num_leaves": 15.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.530965                                         
[100]	valid's binary_logloss: 0.530849                                        
[50]	valid's binary_logloss: 0.530965                                         
[100]	valid's binary_logloss: 0.530778                                        
[50]	valid's binary_logloss: 0.529319                                         
[100]	valid's binary_logloss: 0.529024                                        
[50]	valid's binary_logloss: 0.529104                                         
[100]	valid's binary_logloss: 0.528942                                        
[50]	valid's binary_logloss: 0.530698                                         
[100]	valid's binary_logloss: 0.530634                                        
feature importance:                                                           
                                               column  importance             
72                   debug_trainVectorSpace_tfidfTLen          99
47                                         query_freq          84
40                debug_trainWord2vec_cosine_distance          54
75                 debug_trainVectorSpace_tfidfQTDiff          51
61                debug_trainMagic_unigrams_difft-len          45
18            debug_trainTextMining_text_jaro_winkler          43
67               debug_trainMagic_unigrams_diffqt-avg          40
28          debug_trainTextMining_unigrams_dice_ratio          40
20           debug_trainTextMining_text_partial_ratio          40
51  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          39
78                  debug_trainVectorSpace_tfidfQTAvg          38
68     debug_trainVectorSpace_paired_cosine_distances          36
17                    debug_trainTextMining_text_jaro          35
43              debug_trainWord2vec_canberra_distance          34
76                  debug_trainVectorSpace_tfidfQTMax          33
70  debug_trainVectorSpace_paired_manhattan_distances          33
74             debug_trainVectorSpace_tfidfTQLenRadio          31
5                debug_trainTextMining_unigrams_t-len          30
46             debug_trainWord2vec_minkowski_distance          29
21        debug_trainTextMining_text_token_sort_ratio          29
49     debug_trainMagic_unigrams_diffSetSimdice_ratio          28
52  debug_trainMagic_unigrams_diffSetSimedit_set_r...          27
73             debug_trainVectorSpace_tfidfQTLenRadio          27
44             debug_trainWord2vec_cityblock_distance          27
23         debug_trainTextMining_text_token_set_ratio          27
59  debug_trainMagic_trigrams_diffSetSimedit_seq_r...          26
22  debug_trainTextMining_text_partial_token_sort_...          26
69  debug_trainVectorSpace_paired_euclidean_distances          25
42            debug_trainWord2vec_braycurtis_distance          25
63         debug_trainMagic_unigrams_difftq-len-radio          25
..                                                ...         ...
24          debug_trainTextMining_unichars_dice_ratio          16
38      debug_trainTextMining_trigrams_edit_seq_ratio          16
64              debug_trainMagic_unigrams_diffqt-diff          15
48                          debug_trainMagic_localCTR          15
62         debug_trainMagic_unigrams_diffqt-len-radio          15
60  debug_trainMagic_trigrams_diffSetSimedit_set_r...          14
9               debug_trainTextMining_unichars_qt-max          14
12             debug_trainTextMining_unigrams_qt-diff          14
36          debug_trainTextMining_trigrams_dice_ratio          14
77                  debug_trainVectorSpace_tfidfQTMin          14
6         debug_trainTextMining_unigrams_qt-len-radio          11
32           debug_trainTextMining_bigrams_dice_ratio          11
19                   debug_trainTextMining_text_ratio          11
57     debug_trainMagic_trigrams_diffSetSimdice_ratio          10
71                   debug_trainVectorSpace_tfidfQLen          10
35       debug_trainTextMining_bigrams_edit_set_ratio          10
50  debug_trainMagic_unigrams_diffSetSimjaccard_ratio           9
2             debug_trainTextMining_text_qt-len-radio           8
29       debug_trainTextMining_unigrams_jaccard_ratio           7
39      debug_trainTextMining_trigrams_edit_set_ratio           6
33        debug_trainTextMining_bigrams_jaccard_ratio           6
7         debug_trainTextMining_unigrams_tq-len-radio           5
66               debug_trainMagic_unigrams_diffqt-min           3
25       debug_trainTextMining_unichars_jaccard_ratio           3
37       debug_trainTextMining_trigrams_jaccard_ratio           2
14              debug_trainTextMining_unigrams_qt-min           1
4                debug_trainTextMining_unigrams_q-len           1
54   debug_trainMagic_bigrams_diffSetSimjaccard_ratio           1
58  debug_trainMagic_trigrams_diffSetSimjaccard_ratio           0
41               debug_trainWord2vec_jaccard_distance           0

[79 rows x 2 columns]
Valid Loss, AUC: 0.531294 0.675648                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5560401871021969                                               
----->Finished 'cal q auc' block, time used:113.57s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561646940_auc0.675648_loss0.531294_std0.003796.npy
{                                                                             
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 10.0,
 "feature_fraction": 1.0,
 "learning_rate": 0.15,
 "max_bin": 15,
 "min_data_in_leaf": 30.0,
 "num_iterations": 200.0,
 "num_leaves": 15.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.531332                                         
[100]	valid's binary_logloss: 0.531293                                        
[150]	valid's binary_logloss: 0.531442                                        
[200]	valid's binary_logloss: 0.531501                                        
[50]	valid's binary_logloss: 0.531277                                         
[100]	valid's binary_logloss: 0.531003                                        
[150]	valid's binary_logloss: 0.53098                                         
[200]	valid's binary_logloss: 0.531021                                        
[50]	valid's binary_logloss: 0.529743                                         
[100]	valid's binary_logloss: 0.529453                                        
[150]	valid's binary_logloss: 0.529571                                        
[200]	valid's binary_logloss: 0.529709                                        
[50]	valid's binary_logloss: 0.529488                                         
[100]	valid's binary_logloss: 0.529419                                        
[150]	valid's binary_logloss: 0.529284                                        
[200]	valid's binary_logloss: 0.529443                                        
[50]	valid's binary_logloss: 0.530859                                         
[100]	valid's binary_logloss: 0.530627                                        
[150]	valid's binary_logloss: 0.530628                                        
[200]	valid's binary_logloss: 0.530673                                        
feature importance:                                                           
                                               column  importance             
47                                         query_freq         123
40                debug_trainWord2vec_cosine_distance          85
20           debug_trainTextMining_text_partial_ratio          84
72                   debug_trainVectorSpace_tfidfTLen          82
75                 debug_trainVectorSpace_tfidfQTDiff          79
22  debug_trainTextMining_text_partial_token_sort_...          72
61                debug_trainMagic_unigrams_difft-len          70
28          debug_trainTextMining_unigrams_dice_ratio          68
52  debug_trainMagic_unigrams_diffSetSimedit_set_r...          68
78                  debug_trainVectorSpace_tfidfQTAvg          66
49     debug_trainMagic_unigrams_diffSetSimdice_ratio          66
23         debug_trainTextMining_text_token_set_ratio          65
17                    debug_trainTextMining_text_jaro          64
18            debug_trainTextMining_text_jaro_winkler          61
76                  debug_trainVectorSpace_tfidfQTMax          52
24          debug_trainTextMining_unichars_dice_ratio          50
42            debug_trainWord2vec_braycurtis_distance          49
51  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          48
64              debug_trainMagic_unigrams_diffqt-diff          47
70  debug_trainVectorSpace_paired_manhattan_distances          47
67               debug_trainMagic_unigrams_diffqt-avg          46
30      debug_trainTextMining_unigrams_edit_seq_ratio          44
46             debug_trainWord2vec_minkowski_distance          44
12             debug_trainTextMining_unigrams_qt-diff          43
55  debug_trainMagic_bigrams_diffSetSimedit_seq_ratio          43
15              debug_trainTextMining_unigrams_qt-avg          41
11              debug_trainTextMining_unichars_qt-avg          40
8              debug_trainTextMining_unichars_qt-diff          40
43              debug_trainWord2vec_canberra_distance          40
21        debug_trainTextMining_text_token_sort_ratio          39
..                                                ...         ...
36          debug_trainTextMining_trigrams_dice_ratio          26
1                    debug_trainTextMining_text_t-len          26
62         debug_trainMagic_unigrams_diffqt-len-radio          25
60  debug_trainMagic_trigrams_diffSetSimedit_set_r...          24
74             debug_trainVectorSpace_tfidfTQLenRadio          24
10              debug_trainTextMining_unichars_qt-min          23
57     debug_trainMagic_trigrams_diffSetSimdice_ratio          22
66               debug_trainMagic_unigrams_diffqt-min          21
2             debug_trainTextMining_text_qt-len-radio          21
38      debug_trainTextMining_trigrams_edit_seq_ratio          21
31      debug_trainTextMining_unigrams_edit_set_ratio          21
27      debug_trainTextMining_unichars_edit_set_ratio          21
34       debug_trainTextMining_bigrams_edit_seq_ratio          20
71                   debug_trainVectorSpace_tfidfQLen          18
35       debug_trainTextMining_bigrams_edit_set_ratio          18
9               debug_trainTextMining_unichars_qt-max          16
39      debug_trainTextMining_trigrams_edit_set_ratio          16
7         debug_trainTextMining_unigrams_tq-len-radio          13
6         debug_trainTextMining_unigrams_qt-len-radio          12
3             debug_trainTextMining_text_tq-len-radio          11
4                debug_trainTextMining_unigrams_q-len           8
14              debug_trainTextMining_unigrams_qt-min           3
41               debug_trainWord2vec_jaccard_distance           1
37       debug_trainTextMining_trigrams_jaccard_ratio           0
54   debug_trainMagic_bigrams_diffSetSimjaccard_ratio           0
25       debug_trainTextMining_unichars_jaccard_ratio           0
50  debug_trainMagic_unigrams_diffSetSimjaccard_ratio           0
29       debug_trainTextMining_unigrams_jaccard_ratio           0
33        debug_trainTextMining_bigrams_jaccard_ratio           0
58  debug_trainMagic_trigrams_diffSetSimjaccard_ratio           0

[79 rows x 2 columns]
Valid Loss, AUC: 0.531165 0.674861                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.553143852321894                                                
----->Finished 'cal q auc' block, time used:111.75s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561647155_auc0.674861_loss0.531165_std0.003140.npy
{                                                                             
 "bagging_fraction": 0.9,
 "bagging_freq": 0.0,
 "feature_fraction": 0.6000000000000001,
 "learning_rate": 0.11,
 "max_bin": 15,
 "min_data_in_leaf": 20.0,
 "num_iterations": 75.0,
 "num_leaves": 15.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.531336                                         
[50]	valid's binary_logloss: 0.531276                                         
[50]	valid's binary_logloss: 0.530005                                         
[50]	valid's binary_logloss: 0.529552                                         
[50]	valid's binary_logloss: 0.531182                                         
feature importance:                                                           
                                               column  importance             
47                                         query_freq          86
72                   debug_trainVectorSpace_tfidfTLen          80
76                  debug_trainVectorSpace_tfidfQTMax          57
61                debug_trainMagic_unigrams_difft-len          47
40                debug_trainWord2vec_cosine_distance          44
75                 debug_trainVectorSpace_tfidfQTDiff          44
67               debug_trainMagic_unigrams_diffqt-avg          33
48                          debug_trainMagic_localCTR          32
65               debug_trainMagic_unigrams_diffqt-max          31
5                debug_trainTextMining_unigrams_t-len          27
49     debug_trainMagic_unigrams_diffSetSimdice_ratio          27
18            debug_trainTextMining_text_jaro_winkler          27
13              debug_trainTextMining_unigrams_qt-max          24
78                  debug_trainVectorSpace_tfidfQTAvg          23
74             debug_trainVectorSpace_tfidfTQLenRadio          18
53      debug_trainMagic_bigrams_diffSetSimdice_ratio          18
20           debug_trainTextMining_text_partial_ratio          18
70  debug_trainVectorSpace_paired_manhattan_distances          16
64              debug_trainMagic_unigrams_diffqt-diff          15
50  debug_trainMagic_unigrams_diffSetSimjaccard_ratio          14
21        debug_trainTextMining_text_token_sort_ratio          14
63         debug_trainMagic_unigrams_difftq-len-radio          14
15              debug_trainTextMining_unigrams_qt-avg          14
57     debug_trainMagic_trigrams_diffSetSimdice_ratio          13
69  debug_trainVectorSpace_paired_euclidean_distances          13
19                   debug_trainTextMining_text_ratio          13
28          debug_trainTextMining_unigrams_dice_ratio          12
12             debug_trainTextMining_unigrams_qt-diff          11
17                    debug_trainTextMining_text_jaro          11
42            debug_trainWord2vec_braycurtis_distance          11
..                                                ...         ...
45             debug_trainWord2vec_euclidean_distance           5
56  debug_trainMagic_bigrams_diffSetSimedit_set_ratio           5
24          debug_trainTextMining_unichars_dice_ratio           5
29       debug_trainTextMining_unigrams_jaccard_ratio           5
32           debug_trainTextMining_bigrams_dice_ratio           5
62         debug_trainMagic_unigrams_diffqt-len-radio           5
1                    debug_trainTextMining_text_t-len           5
43              debug_trainWord2vec_canberra_distance           5
59  debug_trainMagic_trigrams_diffSetSimedit_seq_r...           4
60  debug_trainMagic_trigrams_diffSetSimedit_set_r...           4
6         debug_trainTextMining_unigrams_qt-len-radio           4
44             debug_trainWord2vec_cityblock_distance           4
8              debug_trainTextMining_unichars_qt-diff           4
71                   debug_trainVectorSpace_tfidfQLen           4
55  debug_trainMagic_bigrams_diffSetSimedit_seq_ratio           3
4                debug_trainTextMining_unigrams_q-len           3
7         debug_trainTextMining_unigrams_tq-len-radio           3
25       debug_trainTextMining_unichars_jaccard_ratio           3
35       debug_trainTextMining_bigrams_edit_set_ratio           3
30      debug_trainTextMining_unigrams_edit_seq_ratio           3
58  debug_trainMagic_trigrams_diffSetSimjaccard_ratio           3
27      debug_trainTextMining_unichars_edit_set_ratio           2
31      debug_trainTextMining_unigrams_edit_set_ratio           2
39      debug_trainTextMining_trigrams_edit_set_ratio           2
33        debug_trainTextMining_bigrams_jaccard_ratio           1
14              debug_trainTextMining_unigrams_qt-min           1
37       debug_trainTextMining_trigrams_jaccard_ratio           1
38      debug_trainTextMining_trigrams_edit_seq_ratio           0
41               debug_trainWord2vec_jaccard_distance           0
34       debug_trainTextMining_bigrams_edit_seq_ratio           0

[79 rows x 2 columns]
Valid Loss, AUC: 0.53363 0.675129                                             
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5549170908097932                                               
----->Finished 'cal q auc' block, time used:111.8s.                           
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561647318_auc0.675129_loss0.533630_std0.006289.npy
{                                                                             
 "bagging_fraction": 0.8,
 "bagging_freq": 6.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.14,
 "max_bin": 1023,
 "min_data_in_leaf": 40.0,
 "num_iterations": 125.0,
 "num_leaves": 15.0,
 "num_threads": 4
}
[50]	valid's binary_logloss: 0.530993                                         
[100]	valid's binary_logloss: 0.530871                                        
[50]	valid's binary_logloss: 0.530956                                         
[100]	valid's binary_logloss: 0.530841                                        
[50]	valid's binary_logloss: 0.529574                                         
[100]	valid's binary_logloss: 0.529228                                        
[50]	valid's binary_logloss: 0.529193                                         
[100]	valid's binary_logloss: 0.528869                                        
 90%|█████████ | 9/10 [28:13<03:01, 181.56s/it, best loss: 0.5308817577018151]
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-17-d5124e5922a7> in <module>
----> 1 run_lgb_gbdt("len_editSim_ngramSim_word2vecTfidfSim_diffSetSim_queryFreq_globalCTR_tfidfVecSim_tfidfLen", eval_num=10)

~/work/stage2/code/run_hyperopt.py in run_lgb_gbdt(comment, eval_num)
    161                         algo=tpe.suggest,
    162                         max_evals=eval_num,
--> 163                         trials=trials)
    164 
    165     info = trials.best_trial

/opt/conda/lib/python3.6/site-packages/hyperopt/fmin.py in fmin(fn, space, algo, max_evals, trials, rstate, allow_trials_fmin, pass_expr_memo_ctrl, catch_eval_exceptions, verbose, return_argmin, points_to_evaluate, max_queue_len, show_progressbar)
    386             catch_eval_exceptions=catch_eval_exceptions,
    387             return_argmin=return_argmin,
--> 388             show_progressbar=show_progressbar,
    389         )
    390 

/opt/conda/lib/python3.6/site-packages/hyperopt/base.py in fmin(self, fn, space, algo, max_evals, rstate, verbose, pass_expr_memo_ctrl, catch_eval_exceptions, return_argmin, show_progressbar)
    637             catch_eval_exceptions=catch_eval_exceptions,
    638             return_argmin=return_argmin,
--> 639             show_progressbar=show_progressbar)
    640 
    641 

/opt/conda/lib/python3.6/site-packages/hyperopt/fmin.py in fmin(fn, space, algo, max_evals, trials, rstate, allow_trials_fmin, pass_expr_memo_ctrl, catch_eval_exceptions, verbose, return_argmin, points_to_evaluate, max_queue_len, show_progressbar)
    405                     show_progressbar=show_progressbar)
    406     rval.catch_eval_exceptions = catch_eval_exceptions
--> 407     rval.exhaust()
    408     if return_argmin:
    409         return trials.argmin

/opt/conda/lib/python3.6/site-packages/hyperopt/fmin.py in exhaust(self)
    260     def exhaust(self):
    261         n_done = len(self.trials)
--> 262         self.run(self.max_evals - n_done, block_until_done=self.asynchronous)
    263         self.trials.refresh()
    264         return self

/opt/conda/lib/python3.6/site-packages/hyperopt/fmin.py in run(self, N, block_until_done)
    225                     else:
    226                         # -- loop over trials and do the jobs directly
--> 227                         self.serial_evaluate()
    228 
    229                     try:

/opt/conda/lib/python3.6/site-packages/hyperopt/fmin.py in serial_evaluate(self, N)
    139                 ctrl = base.Ctrl(self.trials, current_trial=trial)
    140                 try:
--> 141                     result = self.domain.evaluate(spec, ctrl)
    142                 except Exception as e:
    143                     logger.info('job exception: %s' % str(e))

/opt/conda/lib/python3.6/site-packages/hyperopt/base.py in evaluate(self, config, ctrl, attach_attachments)
    842                 memo=memo,
    843                 print_node_on_error=self.rec_eval_print_node_on_error)
--> 844             rval = self.fn(pyll_rval)
    845 
    846         if isinstance(rval, (float, int, np.number)):

~/work/stage2/code/run_hyperopt.py in fn(params)
     94         train_X, train_y = X[train_index], y[train_index]
     95         valid_X, valid_y = X[valid_index], y[valid_index]
---> 96         loss = model.fit(train_X, train_y, valid_X, valid_y)
     97         losses.extend(loss)
     98         train_predicts[valid_index] = model.predict(valid_X)

~/work/stage2/code/models.py in fit(self, X, y, valid_X, valid_y)
     51                             valid_names=['valid'],
     52                             valid_sets=[valid_set],
---> 53                             num_boost_round=self.num_boost_round)
     54             self.valid_loss = evals_result['valid']['binary_logloss']
     55             return self.valid_loss

/opt/conda/lib/python3.6/site-packages/lightgbm/engine.py in train(params, train_set, num_boost_round, valid_sets, valid_names, fobj, feval, init_model, feature_name, categorical_feature, early_stopping_rounds, evals_result, verbose_eval, learning_rates, keep_training_booster, callbacks)
    216                                     evaluation_result_list=None))
    217 
--> 218         booster.update(fobj=fobj)
    219 
    220         evaluation_result_list = []

/opt/conda/lib/python3.6/site-packages/lightgbm/basic.py in update(self, train_set, fobj)
   1800             _safe_call(_LIB.LGBM_BoosterUpdateOneIter(
   1801                 self.handle,
-> 1802                 ctypes.byref(is_finished)))
   1803             self.__is_predicted_cur_iter = [False for _ in range_(self.__num_dataset)]
   1804             return is_finished.value == 1

KeyboardInterrupt: 

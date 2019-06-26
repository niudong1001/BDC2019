{                                                   
 "bagging_fraction": 0.8,
 "bagging_freq": 0.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.2,
 "max_bin": 63,
 "min_data_in_leaf": 20.0,
 "num_iterations": 150.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533323               
[40]	valid's binary_logloss: 0.53273                
[60]	valid's binary_logloss: 0.53259                
[80]	valid's binary_logloss: 0.532631               
[100]	valid's binary_logloss: 0.532623              
[120]	valid's binary_logloss: 0.532642              
[140]	valid's binary_logloss: 0.53267               
[20]	valid's binary_logloss: 0.533842               
[40]	valid's binary_logloss: 0.533476               
[60]	valid's binary_logloss: 0.533426               
[80]	valid's binary_logloss: 0.533435               
[100]	valid's binary_logloss: 0.533485              
[120]	valid's binary_logloss: 0.533542              
[140]	valid's binary_logloss: 0.533583              
[20]	valid's binary_logloss: 0.53257                
[40]	valid's binary_logloss: 0.531957               
[60]	valid's binary_logloss: 0.531845               
[80]	valid's binary_logloss: 0.531789               
[100]	valid's binary_logloss: 0.531767              
[120]	valid's binary_logloss: 0.531733              
[140]	valid's binary_logloss: 0.531723              
[20]	valid's binary_logloss: 0.532151               
[40]	valid's binary_logloss: 0.531605               
[60]	valid's binary_logloss: 0.531472               
[80]	valid's binary_logloss: 0.531493               
[100]	valid's binary_logloss: 0.531441              
[120]	valid's binary_logloss: 0.531426              
[140]	valid's binary_logloss: 0.531498              
[20]	valid's binary_logloss: 0.533813               
[40]	valid's binary_logloss: 0.533289               
[60]	valid's binary_logloss: 0.533178               
[80]	valid's binary_logloss: 0.533118               
[100]	valid's binary_logloss: 0.533135              
[120]	valid's binary_logloss: 0.533149              
[140]	valid's binary_logloss: 0.533211              
feature importance:                                 
                                               column  importance
33          debug_trainMagic_unigrams_diffSetSimratio          63
29                                         query_freq          62
4                debug_trainTextMining_unigrams_t-len          55
26                         debug_trainWord2vec_cosine          54
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          47
10        debug_trainTextMining_text_token_sort_ratio          46
40                      debug_trainWord2vec_tKurtosis          44
9            debug_trainTextMining_text_partial_ratio          44
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          39
21       debug_trainTextMining_trigrams_partial_ratio          39
0                    debug_trainTextMining_text_q-len          39
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          38
39                      debug_trainWord2vec_qKurtosis          36
5         debug_trainTextMining_unigrams_qt-len-radio          36
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          36
38                          debug_trainWord2vec_tSkew          35
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...          35
13      debug_trainTextMining_unigrams_edit_set_ratio          34
1                    debug_trainTextMining_text_t-len          34
24                      debug_trainWord2vec_chebyshev          34
7           debug_trainTextMining_text_edit_seq_ratio          31
18     debug_trainTextMining_bigrams_token_sort_ratio          31
22                     debug_trainWord2vec_braycurtis          31
14       debug_trainTextMining_unigrams_partial_ratio          30
6               debug_trainTextMining_text_dice_ratio          29
27                      debug_trainWord2vec_euclidean          28
11          debug_trainTextMining_unigrams_dice_ratio          28
23                       debug_trainWord2vec_canberra          28
12      debug_trainTextMining_unigrams_edit_seq_ratio          26
37                          debug_trainWord2vec_qSkew          25
15       debug_trainTextMining_bigrams_edit_seq_ratio          25
19      debug_trainTextMining_trigrams_edit_seq_ratio          23
17        debug_trainTextMining_bigrams_partial_ratio          23
3             debug_trainTextMining_text_tq-len-radio          23
8           debug_trainTextMining_text_edit_set_ratio          20
28                    debug_trainWord2vec_sqeuclidean          19
25                      debug_trainWord2vec_cityblock          19
16       debug_trainTextMining_bigrams_edit_set_ratio          18
2             debug_trainTextMining_text_qt-len-radio          15
36                          debug_trainMagic_localCTR          14
20      debug_trainTextMining_trigrams_edit_set_ratio          14
Valid Loss, AUC: 0.533157 0.669853                  
----->Started 'cal q auc' block...                  
Valid Q AUC: 0.5377058630577555                     
----->Finished 'cal q auc' block, time used:114.92s.
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561365174_auc0.669853_loss0.533157_std0.002711.npy
{                                                                            
 "bagging_fraction": 1.0,
 "bagging_freq": 6.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.15,
 "max_bin": 1023,
 "min_data_in_leaf": 50.0,
 "num_iterations": 150.0,
 "num_leaves": 20.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533397                                        
[40]	valid's binary_logloss: 0.532892                                        
[60]	valid's binary_logloss: 0.532767                                        
[80]	valid's binary_logloss: 0.532792                                        
[100]	valid's binary_logloss: 0.532772                                       
[120]	valid's binary_logloss: 0.532863                                       
[140]	valid's binary_logloss: 0.532963                                       
[20]	valid's binary_logloss: 0.533859                                        
[40]	valid's binary_logloss: 0.533508                                        
[60]	valid's binary_logloss: 0.533398                                        
[80]	valid's binary_logloss: 0.533422                                        
[100]	valid's binary_logloss: 0.533482                                       
[120]	valid's binary_logloss: 0.533553                                       
[140]	valid's binary_logloss: 0.533638                                       
[20]	valid's binary_logloss: 0.532617                                        
[40]	valid's binary_logloss: 0.531999                                        
[60]	valid's binary_logloss: 0.531908                                        
[80]	valid's binary_logloss: 0.531911                                        
[100]	valid's binary_logloss: 0.531878                                       
[120]	valid's binary_logloss: 0.531998                                       
[140]	valid's binary_logloss: 0.531974                                       
[20]	valid's binary_logloss: 0.532116                                        
[40]	valid's binary_logloss: 0.531506                                        
[60]	valid's binary_logloss: 0.531492                                        
[80]	valid's binary_logloss: 0.531508                                        
[100]	valid's binary_logloss: 0.531554                                       
[120]	valid's binary_logloss: 0.531582                                       
[140]	valid's binary_logloss: 0.531645                                       
[20]	valid's binary_logloss: 0.533828                                        
[40]	valid's binary_logloss: 0.533238                                        
[60]	valid's binary_logloss: 0.533059                                        
[80]	valid's binary_logloss: 0.533016                                        
[100]	valid's binary_logloss: 0.533139                                       
[120]	valid's binary_logloss: 0.53315                                        
[140]	valid's binary_logloss: 0.533229                                       
feature importance:                                                          
                                               column  importance            
26                         debug_trainWord2vec_cosine         138
40                      debug_trainWord2vec_tKurtosis         124
38                          debug_trainWord2vec_tSkew         121
29                                         query_freq         112
24                      debug_trainWord2vec_chebyshev         103
1                    debug_trainTextMining_text_t-len          99
39                      debug_trainWord2vec_qKurtosis          92
33          debug_trainMagic_unigrams_diffSetSimratio          91
22                     debug_trainWord2vec_braycurtis          87
7           debug_trainTextMining_text_edit_seq_ratio          83
9            debug_trainTextMining_text_partial_ratio          77
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          75
37                          debug_trainWord2vec_qSkew          72
19      debug_trainTextMining_trigrams_edit_seq_ratio          71
2             debug_trainTextMining_text_qt-len-radio          70
23                       debug_trainWord2vec_canberra          70
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          69
0                    debug_trainTextMining_text_q-len          68
15       debug_trainTextMining_bigrams_edit_seq_ratio          66
13      debug_trainTextMining_unigrams_edit_set_ratio          65
25                      debug_trainWord2vec_cityblock          65
27                      debug_trainWord2vec_euclidean          64
4                debug_trainTextMining_unigrams_t-len          63
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          63
5         debug_trainTextMining_unigrams_qt-len-radio          62
12      debug_trainTextMining_unigrams_edit_seq_ratio          61
16       debug_trainTextMining_bigrams_edit_set_ratio          60
21       debug_trainTextMining_trigrams_partial_ratio          60
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...          59
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          57
17        debug_trainTextMining_bigrams_partial_ratio          56
8           debug_trainTextMining_text_edit_set_ratio          56
10        debug_trainTextMining_text_token_sort_ratio          55
20      debug_trainTextMining_trigrams_edit_set_ratio          52
18     debug_trainTextMining_bigrams_token_sort_ratio          50
11          debug_trainTextMining_unigrams_dice_ratio          49
14       debug_trainTextMining_unigrams_partial_ratio          47
28                    debug_trainWord2vec_sqeuclidean          40
6               debug_trainTextMining_text_dice_ratio          33
3             debug_trainTextMining_text_tq-len-radio          31
36                          debug_trainMagic_localCTR          14
Valid Loss, AUC: 0.53335 0.669255                                            
----->Started 'cal q auc' block...                                           
Valid Q AUC: 0.5370514171706358                                              
----->Finished 'cal q auc' block, time used:115.46s.                         
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561365347_auc0.669255_loss0.533350_std0.003152.npy
{                                                                            
 "bagging_fraction": 0.6000000000000001,
 "bagging_freq": 2.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.2,
 "max_bin": 63,
 "min_data_in_leaf": 10.0,
 "num_iterations": 75.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533308                                        
[40]	valid's binary_logloss: 0.532922                                        
[60]	valid's binary_logloss: 0.532814                                        
[20]	valid's binary_logloss: 0.533799                                        
[40]	valid's binary_logloss: 0.533485                                        
[60]	valid's binary_logloss: 0.533399                                        
[20]	valid's binary_logloss: 0.5326                                          
[40]	valid's binary_logloss: 0.531999                                        
[60]	valid's binary_logloss: 0.531952                                        
[20]	valid's binary_logloss: 0.532078                                        
[40]	valid's binary_logloss: 0.531504                                        
[60]	valid's binary_logloss: 0.531417                                        
[20]	valid's binary_logloss: 0.53392                                         
[40]	valid's binary_logloss: 0.533421                                        
[60]	valid's binary_logloss: 0.533362                                        
feature importance:                                                          
                                               column  importance            
29                                         query_freq          61
33          debug_trainMagic_unigrams_diffSetSimratio          43
4                debug_trainTextMining_unigrams_t-len          37
26                         debug_trainWord2vec_cosine          35
0                    debug_trainTextMining_text_q-len          31
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          26
10        debug_trainTextMining_text_token_sort_ratio          23
9            debug_trainTextMining_text_partial_ratio          22
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          22
27                      debug_trainWord2vec_euclidean          19
24                      debug_trainWord2vec_chebyshev          19
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          18
38                          debug_trainWord2vec_tSkew          18
7           debug_trainTextMining_text_edit_seq_ratio          17
1                    debug_trainTextMining_text_t-len          17
19      debug_trainTextMining_trigrams_edit_seq_ratio          16
13      debug_trainTextMining_unigrams_edit_set_ratio          16
2             debug_trainTextMining_text_qt-len-radio          16
21       debug_trainTextMining_trigrams_partial_ratio          16
40                      debug_trainWord2vec_tKurtosis          15
14       debug_trainTextMining_unigrams_partial_ratio          15
22                     debug_trainWord2vec_braycurtis          14
37                          debug_trainWord2vec_qSkew          14
23                       debug_trainWord2vec_canberra          13
5         debug_trainTextMining_unigrams_qt-len-radio          12
6               debug_trainTextMining_text_dice_ratio          12
12      debug_trainTextMining_unigrams_edit_seq_ratio          12
11          debug_trainTextMining_unigrams_dice_ratio          11
39                      debug_trainWord2vec_qKurtosis          11
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          10
18     debug_trainTextMining_bigrams_token_sort_ratio          10
17        debug_trainTextMining_bigrams_partial_ratio           9
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...           9
15       debug_trainTextMining_bigrams_edit_seq_ratio           8
8           debug_trainTextMining_text_edit_set_ratio           7
36                          debug_trainMagic_localCTR           6
25                      debug_trainWord2vec_cityblock           5
3             debug_trainTextMining_text_tq-len-radio           4
16       debug_trainTextMining_bigrams_edit_set_ratio           3
28                    debug_trainWord2vec_sqeuclidean           2
20      debug_trainTextMining_trigrams_edit_set_ratio           1
Valid Loss, AUC: 0.533799 0.669808                                           
----->Started 'cal q auc' block...                                           
Valid Q AUC: 0.5373164181988987                                              
----->Finished 'cal q auc' block, time used:112.8s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561365491_auc0.669808_loss0.533799_std0.003568.npy
{                                                                            
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 6.0,
 "feature_fraction": 1.0,
 "learning_rate": 0.16,
 "max_bin": 1023,
 "min_data_in_leaf": 10.0,
 "num_iterations": 150.0,
 "num_leaves": 25.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.53333                                         
[40]	valid's binary_logloss: 0.533089                                        
[60]	valid's binary_logloss: 0.533165                                        
[80]	valid's binary_logloss: 0.5333                                          
[100]	valid's binary_logloss: 0.533485                                       
[120]	valid's binary_logloss: 0.533566                                       
[140]	valid's binary_logloss: 0.533627                                       
[20]	valid's binary_logloss: 0.533754                                        
[40]	valid's binary_logloss: 0.533512                                        
[60]	valid's binary_logloss: 0.533482                                        
[80]	valid's binary_logloss: 0.533694                                        
[100]	valid's binary_logloss: 0.533778                                       
[120]	valid's binary_logloss: 0.534059                                       
[140]	valid's binary_logloss: 0.534257                                       
[20]	valid's binary_logloss: 0.532508                                        
[40]	valid's binary_logloss: 0.532027                                        
[60]	valid's binary_logloss: 0.532019                                        
[80]	valid's binary_logloss: 0.532013                                        
[100]	valid's binary_logloss: 0.531986                                       
[120]	valid's binary_logloss: 0.532236                                       
[140]	valid's binary_logloss: 0.53246                                        
[20]	valid's binary_logloss: 0.532121                                        
[40]	valid's binary_logloss: 0.531885                                        
[60]	valid's binary_logloss: 0.531766                                        
[80]	valid's binary_logloss: 0.531828                                        
[100]	valid's binary_logloss: 0.532054                                       
[120]	valid's binary_logloss: 0.532251                                       
[140]	valid's binary_logloss: 0.532429                                       
[20]	valid's binary_logloss: 0.533895                                        
[40]	valid's binary_logloss: 0.533408                                        
[60]	valid's binary_logloss: 0.533451                                        
[80]	valid's binary_logloss: 0.533635                                        
[100]	valid's binary_logloss: 0.533806                                       
[120]	valid's binary_logloss: 0.533864                                       
[140]	valid's binary_logloss: 0.53406                                        
feature importance:                                                          
                                               column  importance            
26                         debug_trainWord2vec_cosine         178
40                      debug_trainWord2vec_tKurtosis         157
38                          debug_trainWord2vec_tSkew         156
1                    debug_trainTextMining_text_t-len         138
39                      debug_trainWord2vec_qKurtosis         127
24                      debug_trainWord2vec_chebyshev         122
29                                         query_freq         118
33          debug_trainMagic_unigrams_diffSetSimratio         118
23                       debug_trainWord2vec_canberra         116
37                          debug_trainWord2vec_qSkew         114
7           debug_trainTextMining_text_edit_seq_ratio         109
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...         107
22                     debug_trainWord2vec_braycurtis         106
19      debug_trainTextMining_trigrams_edit_seq_ratio         103
13      debug_trainTextMining_unigrams_edit_set_ratio          93
12      debug_trainTextMining_unigrams_edit_seq_ratio          92
25                      debug_trainWord2vec_cityblock          92
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...          91
27                      debug_trainWord2vec_euclidean          90
11          debug_trainTextMining_unigrams_dice_ratio          88
15       debug_trainTextMining_bigrams_edit_seq_ratio          87
4                debug_trainTextMining_unigrams_t-len          86
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          82
9            debug_trainTextMining_text_partial_ratio          79
16       debug_trainTextMining_bigrams_edit_set_ratio          77
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          76
21       debug_trainTextMining_trigrams_partial_ratio          74
8           debug_trainTextMining_text_edit_set_ratio          72
2             debug_trainTextMining_text_qt-len-radio          67
14       debug_trainTextMining_unigrams_partial_ratio          66
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          65
0                    debug_trainTextMining_text_q-len          64
17        debug_trainTextMining_bigrams_partial_ratio          58
5         debug_trainTextMining_unigrams_qt-len-radio          58
18     debug_trainTextMining_bigrams_token_sort_ratio          55
6               debug_trainTextMining_text_dice_ratio          50
10        debug_trainTextMining_text_token_sort_ratio          48
3             debug_trainTextMining_text_tq-len-radio          36
20      debug_trainTextMining_trigrams_edit_set_ratio          35
36                          debug_trainMagic_localCTR          27
28                    debug_trainWord2vec_sqeuclidean          23
Valid Loss, AUC: 0.533616 0.66801                                            
----->Started 'cal q auc' block...                                           
Valid Q AUC: 0.5356580483447275                                              
----->Finished 'cal q auc' block, time used:114.7s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561365666_auc0.668010_loss0.533616_std0.002926.npy
{                                                                            
 "bagging_fraction": 0.9,
 "bagging_freq": 2.0,
 "feature_fraction": 1.0,
 "learning_rate": 0.14,
 "max_bin": 255,
 "min_data_in_leaf": 10.0,
 "num_iterations": 175.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533857                                        
[40]	valid's binary_logloss: 0.533043                                        
[60]	valid's binary_logloss: 0.532786                                        
[80]	valid's binary_logloss: 0.532736                                        
[100]	valid's binary_logloss: 0.532688                                       
[120]	valid's binary_logloss: 0.532694                                       
[140]	valid's binary_logloss: 0.532672                                       
[160]	valid's binary_logloss: 0.532688                                       
[20]	valid's binary_logloss: 0.534244                                        
[40]	valid's binary_logloss: 0.533534                                        
[60]	valid's binary_logloss: 0.533371                                        
[80]	valid's binary_logloss: 0.533408                                        
[100]	valid's binary_logloss: 0.533339                                       
[120]	valid's binary_logloss: 0.533315                                       
[140]	valid's binary_logloss: 0.533326                                       
[160]	valid's binary_logloss: 0.53334                                        
[20]	valid's binary_logloss: 0.533108                                        
[40]	valid's binary_logloss: 0.532101                                        
[60]	valid's binary_logloss: 0.531806                                        
[80]	valid's binary_logloss: 0.5317                                          
[100]	valid's binary_logloss: 0.531673                                       
[120]	valid's binary_logloss: 0.53161                                        
[140]	valid's binary_logloss: 0.531606                                       
[160]	valid's binary_logloss: 0.531692                                       
[20]	valid's binary_logloss: 0.532711                                        
[40]	valid's binary_logloss: 0.531746                                        
[60]	valid's binary_logloss: 0.531518                                        
[80]	valid's binary_logloss: 0.53144                                         
[100]	valid's binary_logloss: 0.531478                                       
[120]	valid's binary_logloss: 0.53146                                        
[140]	valid's binary_logloss: 0.531418                                       
[160]	valid's binary_logloss: 0.531456                                       
[20]	valid's binary_logloss: 0.534344                                        
[40]	valid's binary_logloss: 0.533572                                        
[60]	valid's binary_logloss: 0.533361                                        
[80]	valid's binary_logloss: 0.533183                                        
[100]	valid's binary_logloss: 0.533146                                       
[120]	valid's binary_logloss: 0.533129                                       
[140]	valid's binary_logloss: 0.533063                                       
[160]	valid's binary_logloss: 0.533075                                       
feature importance:                                                          
                                               column  importance            
29                                         query_freq          95
33          debug_trainMagic_unigrams_diffSetSimratio          75
26                         debug_trainWord2vec_cosine          74
1                    debug_trainTextMining_text_t-len          73
40                      debug_trainWord2vec_tKurtosis          70
24                      debug_trainWord2vec_chebyshev          65
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          53
4                debug_trainTextMining_unigrams_t-len          50
37                          debug_trainWord2vec_qSkew          47
9            debug_trainTextMining_text_partial_ratio          46
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          44
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          42
0                    debug_trainTextMining_text_q-len          42
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          41
39                      debug_trainWord2vec_qKurtosis          41
13      debug_trainTextMining_unigrams_edit_set_ratio          40
21       debug_trainTextMining_trigrams_partial_ratio          40
5         debug_trainTextMining_unigrams_qt-len-radio          40
7           debug_trainTextMining_text_edit_seq_ratio          39
10        debug_trainTextMining_text_token_sort_ratio          37
38                          debug_trainWord2vec_tSkew          36
18     debug_trainTextMining_bigrams_token_sort_ratio          35
25                      debug_trainWord2vec_cityblock          34
22                     debug_trainWord2vec_braycurtis          32
11          debug_trainTextMining_unigrams_dice_ratio          32
15       debug_trainTextMining_bigrams_edit_seq_ratio          30
8           debug_trainTextMining_text_edit_set_ratio          30
14       debug_trainTextMining_unigrams_partial_ratio          27
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...          27
12      debug_trainTextMining_unigrams_edit_seq_ratio          26
17        debug_trainTextMining_bigrams_partial_ratio          26
2             debug_trainTextMining_text_qt-len-radio          26
23                       debug_trainWord2vec_canberra          25
19      debug_trainTextMining_trigrams_edit_seq_ratio          24
27                      debug_trainWord2vec_euclidean          22
16       debug_trainTextMining_bigrams_edit_set_ratio          22
6               debug_trainTextMining_text_dice_ratio          19
3             debug_trainTextMining_text_tq-len-radio          18
20      debug_trainTextMining_trigrams_edit_set_ratio          15
28                    debug_trainWord2vec_sqeuclidean           9
36                          debug_trainMagic_localCTR           6
Valid Loss, AUC: 0.533299 0.669955                                           
----->Started 'cal q auc' block...                                           
Valid Q AUC: 0.5371946753156652                                              
----->Finished 'cal q auc' block, time used:116.73s.                         
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561365850_auc0.669955_loss0.533299_std0.003179.npy
{                                                                            
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 8.0,
 "feature_fraction": 1.0,
 "learning_rate": 0.16,
 "max_bin": 255,
 "min_data_in_leaf": 50.0,
 "num_iterations": 50.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533674                                        
[40]	valid's binary_logloss: 0.53296                                         
[20]	valid's binary_logloss: 0.534034                                        
[40]	valid's binary_logloss: 0.533497                                        
[20]	valid's binary_logloss: 0.532825                                        
[40]	valid's binary_logloss: 0.532141                                        
[20]	valid's binary_logloss: 0.532353                                        
[40]	valid's binary_logloss: 0.531652                                        
[20]	valid's binary_logloss: 0.534137                                        
[40]	valid's binary_logloss: 0.533559                                        
feature importance:                                                          
                                               column  importance            
29                                         query_freq          73
26                         debug_trainWord2vec_cosine          38
4                debug_trainTextMining_unigrams_t-len          30
33          debug_trainMagic_unigrams_diffSetSimratio          29
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          27
0                    debug_trainTextMining_text_q-len          19
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          18
9            debug_trainTextMining_text_partial_ratio          17
1                    debug_trainTextMining_text_t-len          15
24                      debug_trainWord2vec_chebyshev          11
10        debug_trainTextMining_text_token_sort_ratio          10
11          debug_trainTextMining_unigrams_dice_ratio          10
5         debug_trainTextMining_unigrams_qt-len-radio           9
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...           9
37                          debug_trainWord2vec_qSkew           9
22                     debug_trainWord2vec_braycurtis           8
21       debug_trainTextMining_trigrams_partial_ratio           8
40                      debug_trainWord2vec_tKurtosis           8
12      debug_trainTextMining_unigrams_edit_seq_ratio           8
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...           7
2             debug_trainTextMining_text_qt-len-radio           7
3             debug_trainTextMining_text_tq-len-radio           7
6               debug_trainTextMining_text_dice_ratio           7
23                       debug_trainWord2vec_canberra           7
13      debug_trainTextMining_unigrams_edit_set_ratio           7
27                      debug_trainWord2vec_euclidean           6
7           debug_trainTextMining_text_edit_seq_ratio           5
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...           5
20      debug_trainTextMining_trigrams_edit_set_ratio           5
14       debug_trainTextMining_unigrams_partial_ratio           5
15       debug_trainTextMining_bigrams_edit_seq_ratio           5
25                      debug_trainWord2vec_cityblock           4
17        debug_trainTextMining_bigrams_partial_ratio           4
39                      debug_trainWord2vec_qKurtosis           4
19      debug_trainTextMining_trigrams_edit_seq_ratio           3
16       debug_trainTextMining_bigrams_edit_set_ratio           3
18     debug_trainTextMining_bigrams_token_sort_ratio           2
36                          debug_trainMagic_localCTR           1
8           debug_trainTextMining_text_edit_set_ratio           0
28                    debug_trainWord2vec_sqeuclidean           0
38                          debug_trainWord2vec_tSkew           0
Valid Loss, AUC: 0.53496 0.6695                                              
----->Started 'cal q auc' block...                                           
Valid Q AUC: 0.5371533060180445                                              
----->Finished 'cal q auc' block, time used:115.84s.                         
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561365994_auc0.669500_loss0.534960_std0.004858.npy
{                                                                            
 "bagging_fraction": 1.0,
 "bagging_freq": 8.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.17,
 "max_bin": 1023,
 "min_data_in_leaf": 40.0,
 "num_iterations": 175.0,
 "num_leaves": 30.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533226                                        
[40]	valid's binary_logloss: 0.533049                                        
[60]	valid's binary_logloss: 0.533143                                        
[80]	valid's binary_logloss: 0.533268                                        
[100]	valid's binary_logloss: 0.533393                                       
[120]	valid's binary_logloss: 0.533514                                       
[140]	valid's binary_logloss: 0.533654                                       
[160]	valid's binary_logloss: 0.533701                                       
[20]	valid's binary_logloss: 0.53378                                         
[40]	valid's binary_logloss: 0.533606                                        
[60]	valid's binary_logloss: 0.533517                                        
[80]	valid's binary_logloss: 0.533575                                        
[100]	valid's binary_logloss: 0.533775                                       
[120]	valid's binary_logloss: 0.533966                                       
[140]	valid's binary_logloss: 0.534112                                       
[160]	valid's binary_logloss: 0.534296                                       
[20]	valid's binary_logloss: 0.532326                                        
[40]	valid's binary_logloss: 0.531949                                        
[60]	valid's binary_logloss: 0.531989                                        
[80]	valid's binary_logloss: 0.532066                                        
[100]	valid's binary_logloss: 0.532198                                       
[120]	valid's binary_logloss: 0.532402                                       
[140]	valid's binary_logloss: 0.532635                                       
[160]	valid's binary_logloss: 0.532755                                       
[20]	valid's binary_logloss: 0.531938                                        
[40]	valid's binary_logloss: 0.531625                                        
[60]	valid's binary_logloss: 0.531633                                        
[80]	valid's binary_logloss: 0.531662                                        
[100]	valid's binary_logloss: 0.531825                                       
[120]	valid's binary_logloss: 0.532004                                       
[140]	valid's binary_logloss: 0.532101                                       
[160]	valid's binary_logloss: 0.532244                                       
[20]	valid's binary_logloss: 0.533662                                        
[40]	valid's binary_logloss: 0.533284                                        
[60]	valid's binary_logloss: 0.533343                                        
[80]	valid's binary_logloss: 0.533443                                        
[100]	valid's binary_logloss: 0.533654                                       
[120]	valid's binary_logloss: 0.533768                                       
[140]	valid's binary_logloss: 0.533922                                       
[160]	valid's binary_logloss: 0.53421                                        
feature importance:                                                          
                                               column  importance            
38                          debug_trainWord2vec_tSkew         248
40                      debug_trainWord2vec_tKurtosis         215
26                         debug_trainWord2vec_cosine         210
24                      debug_trainWord2vec_chebyshev         203
39                      debug_trainWord2vec_qKurtosis         197
37                          debug_trainWord2vec_qSkew         182
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...         175
7           debug_trainTextMining_text_edit_seq_ratio         165
33          debug_trainMagic_unigrams_diffSetSimratio         157
1                    debug_trainTextMining_text_t-len         156
22                     debug_trainWord2vec_braycurtis         154
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...         154
23                       debug_trainWord2vec_canberra         153
29                                         query_freq         146
8           debug_trainTextMining_text_edit_set_ratio         135
12      debug_trainTextMining_unigrams_edit_seq_ratio         123
19      debug_trainTextMining_trigrams_edit_seq_ratio         118
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...         116
2             debug_trainTextMining_text_qt-len-radio         114
21       debug_trainTextMining_trigrams_partial_ratio         113
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio         113
9            debug_trainTextMining_text_partial_ratio         111
4                debug_trainTextMining_unigrams_t-len         111
13      debug_trainTextMining_unigrams_edit_set_ratio         110
27                      debug_trainWord2vec_euclidean         107
25                      debug_trainWord2vec_cityblock         103
16       debug_trainTextMining_bigrams_edit_set_ratio         102
15       debug_trainTextMining_bigrams_edit_seq_ratio         101
11          debug_trainTextMining_unigrams_dice_ratio          96
0                    debug_trainTextMining_text_q-len          95
17        debug_trainTextMining_bigrams_partial_ratio          85
5         debug_trainTextMining_unigrams_qt-len-radio          84
10        debug_trainTextMining_text_token_sort_ratio          82
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          78
18     debug_trainTextMining_bigrams_token_sort_ratio          78
28                    debug_trainWord2vec_sqeuclidean          77
20      debug_trainTextMining_trigrams_edit_set_ratio          72
14       debug_trainTextMining_unigrams_partial_ratio          68
3             debug_trainTextMining_text_tq-len-radio          67
6               debug_trainTextMining_text_dice_ratio          65
36                          debug_trainMagic_localCTR          36
Valid Loss, AUC: 0.53349 0.667534                                            
----->Started 'cal q auc' block...                                           
Valid Q AUC: 0.5314326516983683                                              
----->Finished 'cal q auc' block, time used:117.77s.                         
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561366180_auc0.667534_loss0.533490_std0.002640.npy
{                                                                            
 "bagging_fraction": 1.0,
 "bagging_freq": 10.0,
 "feature_fraction": 0.6000000000000001,
 "learning_rate": 0.11,
 "max_bin": 1023,
 "min_data_in_leaf": 30.0,
 "num_iterations": 150.0,
 "num_leaves": 25.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.534074                                        
[40]	valid's binary_logloss: 0.533057                                        
[60]	valid's binary_logloss: 0.532816                                        
[80]	valid's binary_logloss: 0.532793                                        
[100]	valid's binary_logloss: 0.532809                                       
[120]	valid's binary_logloss: 0.532882                                       
[140]	valid's binary_logloss: 0.532913                                       
[20]	valid's binary_logloss: 0.534489                                        
[40]	valid's binary_logloss: 0.533586                                        
[60]	valid's binary_logloss: 0.53339                                         
[80]	valid's binary_logloss: 0.533413                                        
[100]	valid's binary_logloss: 0.533429                                       
[120]	valid's binary_logloss: 0.5335                                         
[140]	valid's binary_logloss: 0.533536                                       
[20]	valid's binary_logloss: 0.533439                                        
[40]	valid's binary_logloss: 0.532261                                        
[60]	valid's binary_logloss: 0.531924                                        
[80]	valid's binary_logloss: 0.531825                                        
[100]	valid's binary_logloss: 0.531863                                       
[120]	valid's binary_logloss: 0.531814                                       
[140]	valid's binary_logloss: 0.531827                                       
[20]	valid's binary_logloss: 0.532969                                        
[40]	valid's binary_logloss: 0.531632                                        
[60]	valid's binary_logloss: 0.531412                                        
[80]	valid's binary_logloss: 0.531371                                        
[100]	valid's binary_logloss: 0.531368                                       
[120]	valid's binary_logloss: 0.531364                                       
[140]	valid's binary_logloss: 0.531347                                       
[20]	valid's binary_logloss: 0.534475                                        
[40]	valid's binary_logloss: 0.533439                                        
[60]	valid's binary_logloss: 0.533146                                        
[80]	valid's binary_logloss: 0.533109                                        
[100]	valid's binary_logloss: 0.53308                                        
[120]	valid's binary_logloss: 0.533095                                       
[140]	valid's binary_logloss: 0.533138                                       
feature importance:                                                          
                                               column  importance            
26                         debug_trainWord2vec_cosine         167
38                          debug_trainWord2vec_tSkew         142
29                                         query_freq         140
1                    debug_trainTextMining_text_t-len         132
33          debug_trainMagic_unigrams_diffSetSimratio         123
24                      debug_trainWord2vec_chebyshev         117
22                     debug_trainWord2vec_braycurtis         112
4                debug_trainTextMining_unigrams_t-len         110
7           debug_trainTextMining_text_edit_seq_ratio         108
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...         103
9            debug_trainTextMining_text_partial_ratio         103
2             debug_trainTextMining_text_qt-len-radio         103
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...         101
39                      debug_trainWord2vec_qKurtosis         101
40                      debug_trainWord2vec_tKurtosis         101
19      debug_trainTextMining_trigrams_edit_seq_ratio          93
23                       debug_trainWord2vec_canberra          93
0                    debug_trainTextMining_text_q-len          93
37                          debug_trainWord2vec_qSkew          91
27                      debug_trainWord2vec_euclidean          84
25                      debug_trainWord2vec_cityblock          83
8           debug_trainTextMining_text_edit_set_ratio          83
13      debug_trainTextMining_unigrams_edit_set_ratio          80
15       debug_trainTextMining_bigrams_edit_seq_ratio          79
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          77
21       debug_trainTextMining_trigrams_partial_ratio          74
12      debug_trainTextMining_unigrams_edit_seq_ratio          73
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          73
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          72
16       debug_trainTextMining_bigrams_edit_set_ratio          71
10        debug_trainTextMining_text_token_sort_ratio          70
20      debug_trainTextMining_trigrams_edit_set_ratio          69
17        debug_trainTextMining_bigrams_partial_ratio          69
5         debug_trainTextMining_unigrams_qt-len-radio          68
11          debug_trainTextMining_unigrams_dice_ratio          56
28                    debug_trainWord2vec_sqeuclidean          51
18     debug_trainTextMining_bigrams_token_sort_ratio          51
3             debug_trainTextMining_text_tq-len-radio          50
36                          debug_trainMagic_localCTR          47
14       debug_trainTextMining_unigrams_partial_ratio          46
6               debug_trainTextMining_text_dice_ratio          41
Valid Loss, AUC: 0.533708 0.669653                                           
----->Started 'cal q auc' block...                                           
Valid Q AUC: 0.5361814184972822                                              
----->Finished 'cal q auc' block, time used:114.4s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561366353_auc0.669653_loss0.533708_std0.003936.npy
{                                                                            
 "bagging_fraction": 1.0,
 "bagging_freq": 8.0,
 "feature_fraction": 0.6000000000000001,
 "learning_rate": 0.13,
 "max_bin": 1023,
 "min_data_in_leaf": 50.0,
 "num_iterations": 175.0,
 "num_leaves": 25.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.53362                                         
[40]	valid's binary_logloss: 0.532913                                        
[60]	valid's binary_logloss: 0.532766                                        
[80]	valid's binary_logloss: 0.532811                                        
[100]	valid's binary_logloss: 0.532864                                       
[120]	valid's binary_logloss: 0.532906                                       
[140]	valid's binary_logloss: 0.532905                                       
[160]	valid's binary_logloss: 0.532917                                       
[20]	valid's binary_logloss: 0.534092                                        
[40]	valid's binary_logloss: 0.533429                                        
[60]	valid's binary_logloss: 0.533367                                        
[80]	valid's binary_logloss: 0.533364                                        
[100]	valid's binary_logloss: 0.533378                                       
[120]	valid's binary_logloss: 0.533409                                       
[140]	valid's binary_logloss: 0.533435                                       
[160]	valid's binary_logloss: 0.533475                                       
[20]	valid's binary_logloss: 0.533004                                        
[40]	valid's binary_logloss: 0.53197                                         
[60]	valid's binary_logloss: 0.531857                                        
[80]	valid's binary_logloss: 0.531785                                        
[100]	valid's binary_logloss: 0.531826                                       
[120]	valid's binary_logloss: 0.531846                                       
[140]	valid's binary_logloss: 0.531909                                       
[160]	valid's binary_logloss: 0.531995                                       
[20]	valid's binary_logloss: 0.532468                                        
[40]	valid's binary_logloss: 0.531554                                        
[60]	valid's binary_logloss: 0.531403                                        
[80]	valid's binary_logloss: 0.531444                                        
[100]	valid's binary_logloss: 0.531447                                       
[120]	valid's binary_logloss: 0.531426                                       
[140]	valid's binary_logloss: 0.531535                                       
[160]	valid's binary_logloss: 0.531606                                       
[20]	valid's binary_logloss: 0.534158                                        
[40]	valid's binary_logloss: 0.533355                                        
[60]	valid's binary_logloss: 0.533171                                        
[80]	valid's binary_logloss: 0.533094                                        
[100]	valid's binary_logloss: 0.53311                                        
[120]	valid's binary_logloss: 0.53317                                        
[140]	valid's binary_logloss: 0.533223                                       
[160]	valid's binary_logloss: 0.533266                                       
feature importance:                                                          
                                               column  importance            
26                         debug_trainWord2vec_cosine         189
38                          debug_trainWord2vec_tSkew         168
24                      debug_trainWord2vec_chebyshev         150
33          debug_trainMagic_unigrams_diffSetSimratio         142
1                    debug_trainTextMining_text_t-len         138
40                      debug_trainWord2vec_tKurtosis         136
29                                         query_freq         136
37                          debug_trainWord2vec_qSkew         128
19      debug_trainTextMining_trigrams_edit_seq_ratio         126
39                      debug_trainWord2vec_qKurtosis         125
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...         124
27                      debug_trainWord2vec_euclidean         120
22                     debug_trainWord2vec_braycurtis         120
7           debug_trainTextMining_text_edit_seq_ratio         119
2             debug_trainTextMining_text_qt-len-radio         111
23                       debug_trainWord2vec_canberra         109
13      debug_trainTextMining_unigrams_edit_set_ratio         109
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...         108
8           debug_trainTextMining_text_edit_set_ratio         107
9            debug_trainTextMining_text_partial_ratio         106
16       debug_trainTextMining_bigrams_edit_set_ratio         104
15       debug_trainTextMining_bigrams_edit_seq_ratio         100
12      debug_trainTextMining_unigrams_edit_seq_ratio          99
25                      debug_trainWord2vec_cityblock          93
20      debug_trainTextMining_trigrams_edit_set_ratio          91
4                debug_trainTextMining_unigrams_t-len          91
21       debug_trainTextMining_trigrams_partial_ratio          88
0                    debug_trainTextMining_text_q-len          88
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          83
28                    debug_trainWord2vec_sqeuclidean          82
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          81
5         debug_trainTextMining_unigrams_qt-len-radio          81
14       debug_trainTextMining_unigrams_partial_ratio          74
18     debug_trainTextMining_bigrams_token_sort_ratio          72
10        debug_trainTextMining_text_token_sort_ratio          71
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          68
17        debug_trainTextMining_bigrams_partial_ratio          64
6               debug_trainTextMining_text_dice_ratio          56
11          debug_trainTextMining_unigrams_dice_ratio          49
36                          debug_trainMagic_localCTR          49
3             debug_trainTextMining_text_tq-len-radio          45
Valid Loss, AUC: 0.533384 0.669322                                           
----->Started 'cal q auc' block...                                           
Valid Q AUC: 0.5353029670392189                                              
----->Finished 'cal q auc' block, time used:112.32s.                         
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561366528_auc0.669322_loss0.533384_std0.003300.npy
{                                                                            
 "bagging_fraction": 1.0,
 "bagging_freq": 8.0,
 "feature_fraction": 0.9,
 "learning_rate": 0.15,
 "max_bin": 15,
 "min_data_in_leaf": 20.0,
 "num_iterations": 75.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533721                                        
[40]	valid's binary_logloss: 0.532956                                        
[60]	valid's binary_logloss: 0.532862                                        
[20]	valid's binary_logloss: 0.53419                                         
[40]	valid's binary_logloss: 0.533579                                        
[60]	valid's binary_logloss: 0.533525                                        
[20]	valid's binary_logloss: 0.533115                                        
[40]	valid's binary_logloss: 0.532312                                        
[60]	valid's binary_logloss: 0.532071                                        
[20]	valid's binary_logloss: 0.532637                                        
[40]	valid's binary_logloss: 0.531808                                        
[60]	valid's binary_logloss: 0.531632                                        
[20]	valid's binary_logloss: 0.53419                                         
[40]	valid's binary_logloss: 0.533535                                        
[60]	valid's binary_logloss: 0.533305                                        
feature importance:                                                          
                                               column  importance            
29                                         query_freq          66
4                debug_trainTextMining_unigrams_t-len          47
33          debug_trainMagic_unigrams_diffSetSimratio          47
26                         debug_trainWord2vec_cosine          45
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          42
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          30
5         debug_trainTextMining_unigrams_qt-len-radio          25
9            debug_trainTextMining_text_partial_ratio          25
0                    debug_trainTextMining_text_q-len          23
36                          debug_trainMagic_localCTR          22
21       debug_trainTextMining_trigrams_partial_ratio          20
6               debug_trainTextMining_text_dice_ratio          16
10        debug_trainTextMining_text_token_sort_ratio          16
1                    debug_trainTextMining_text_t-len          15
40                      debug_trainWord2vec_tKurtosis          14
11          debug_trainTextMining_unigrams_dice_ratio          14
13      debug_trainTextMining_unigrams_edit_set_ratio          13
22                     debug_trainWord2vec_braycurtis          13
14       debug_trainTextMining_unigrams_partial_ratio          13
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          12
7           debug_trainTextMining_text_edit_seq_ratio          12
23                       debug_trainWord2vec_canberra          11
25                      debug_trainWord2vec_cityblock          10
24                      debug_trainWord2vec_chebyshev           9
12      debug_trainTextMining_unigrams_edit_seq_ratio           9
39                      debug_trainWord2vec_qKurtosis           9
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...           9
17        debug_trainTextMining_bigrams_partial_ratio           9
2             debug_trainTextMining_text_qt-len-radio           8
27                      debug_trainWord2vec_euclidean           8
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...           7
37                          debug_trainWord2vec_qSkew           7
20      debug_trainTextMining_trigrams_edit_set_ratio           7
16       debug_trainTextMining_bigrams_edit_set_ratio           7
19      debug_trainTextMining_trigrams_edit_seq_ratio           7
18     debug_trainTextMining_bigrams_token_sort_ratio           6
38                          debug_trainWord2vec_tSkew           6
8           debug_trainTextMining_text_edit_set_ratio           5
3             debug_trainTextMining_text_tq-len-radio           5
15       debug_trainTextMining_bigrams_edit_seq_ratio           4
28                    debug_trainWord2vec_sqeuclidean           2
Valid Loss, AUC: 0.53436 0.66975                                             
----->Started 'cal q auc' block...                                           
Valid Q AUC: 0.5377127752439859                                              
----->Finished 'cal q auc' block, time used:113.05s.                         
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561366676_auc0.669750_loss0.534360_std0.004321.npy
{                                                                             
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 4.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.2,
 "max_bin": 255,
 "min_data_in_leaf": 10.0,
 "num_iterations": 200.0,
 "num_leaves": 20.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.53332                                          
[40]	valid's binary_logloss: 0.533259                                         
[60]	valid's binary_logloss: 0.53337                                          
[80]	valid's binary_logloss: 0.533507                                         
[100]	valid's binary_logloss: 0.533745                                        
[120]	valid's binary_logloss: 0.533883                                        
[140]	valid's binary_logloss: 0.534119                                        
[160]	valid's binary_logloss: 0.534331                                        
[180]	valid's binary_logloss: 0.534493                                        
[200]	valid's binary_logloss: 0.534612                                        
[20]	valid's binary_logloss: 0.533727                                         
[40]	valid's binary_logloss: 0.533576                                         
[60]	valid's binary_logloss: 0.533814                                         
[80]	valid's binary_logloss: 0.533872                                         
[100]	valid's binary_logloss: 0.53398                                         
[120]	valid's binary_logloss: 0.53408                                         
[140]	valid's binary_logloss: 0.534233                                        
[160]	valid's binary_logloss: 0.534482                                        
[180]	valid's binary_logloss: 0.534827                                        
[200]	valid's binary_logloss: 0.535155                                        
[20]	valid's binary_logloss: 0.532372                                         
[40]	valid's binary_logloss: 0.531923                                         
[60]	valid's binary_logloss: 0.532156                                         
[80]	valid's binary_logloss: 0.532229                                         
[100]	valid's binary_logloss: 0.532347                                        
[120]	valid's binary_logloss: 0.532533                                        
[140]	valid's binary_logloss: 0.53277                                         
[160]	valid's binary_logloss: 0.532958                                        
[180]	valid's binary_logloss: 0.533255                                        
[200]	valid's binary_logloss: 0.533463                                        
[20]	valid's binary_logloss: 0.531931                                         
[40]	valid's binary_logloss: 0.531842                                         
[60]	valid's binary_logloss: 0.531933                                         
[80]	valid's binary_logloss: 0.532172                                         
[100]	valid's binary_logloss: 0.532359                                        
[120]	valid's binary_logloss: 0.532603                                        
[140]	valid's binary_logloss: 0.532792                                        
[160]	valid's binary_logloss: 0.533031                                        
[180]	valid's binary_logloss: 0.533331                                        
[200]	valid's binary_logloss: 0.533503                                        
[20]	valid's binary_logloss: 0.533778                                         
[40]	valid's binary_logloss: 0.5335                                           
[60]	valid's binary_logloss: 0.533535                                         
[80]	valid's binary_logloss: 0.533734                                         
[100]	valid's binary_logloss: 0.533934                                        
[120]	valid's binary_logloss: 0.534128                                        
[140]	valid's binary_logloss: 0.534476                                        
[160]	valid's binary_logloss: 0.534729                                        
[180]	valid's binary_logloss: 0.534814                                        
[200]	valid's binary_logloss: 0.53509                                         
feature importance:                                                           
                                               column  importance             
26                         debug_trainWord2vec_cosine         158
38                          debug_trainWord2vec_tSkew         153
39                      debug_trainWord2vec_qKurtosis         137
40                      debug_trainWord2vec_tKurtosis         134
1                    debug_trainTextMining_text_t-len         134
37                          debug_trainWord2vec_qSkew         123
33          debug_trainMagic_unigrams_diffSetSimratio         122
24                      debug_trainWord2vec_chebyshev         120
9            debug_trainTextMining_text_partial_ratio         112
23                       debug_trainWord2vec_canberra         111
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...         107
27                      debug_trainWord2vec_euclidean         105
12      debug_trainTextMining_unigrams_edit_seq_ratio         105
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...         104
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...         104
22                     debug_trainWord2vec_braycurtis         104
29                                         query_freq         103
7           debug_trainTextMining_text_edit_seq_ratio         101
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio         101
13      debug_trainTextMining_unigrams_edit_set_ratio         100
0                    debug_trainTextMining_text_q-len          92
19      debug_trainTextMining_trigrams_edit_seq_ratio          91
4                debug_trainTextMining_unigrams_t-len          89
21       debug_trainTextMining_trigrams_partial_ratio          87
25                      debug_trainWord2vec_cityblock          87
15       debug_trainTextMining_bigrams_edit_seq_ratio          84
14       debug_trainTextMining_unigrams_partial_ratio          82
5         debug_trainTextMining_unigrams_qt-len-radio          80
10        debug_trainTextMining_text_token_sort_ratio          77
8           debug_trainTextMining_text_edit_set_ratio          75
17        debug_trainTextMining_bigrams_partial_ratio          75
16       debug_trainTextMining_bigrams_edit_set_ratio          75
2             debug_trainTextMining_text_qt-len-radio          70
11          debug_trainTextMining_unigrams_dice_ratio          66
20      debug_trainTextMining_trigrams_edit_set_ratio          62
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          59
18     debug_trainTextMining_bigrams_token_sort_ratio          58
3             debug_trainTextMining_text_tq-len-radio          44
28                    debug_trainWord2vec_sqeuclidean          39
6               debug_trainTextMining_text_dice_ratio          35
36                          debug_trainMagic_localCTR          35
Valid Loss, AUC: 0.533769 0.666527                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5310105955303894                                               
----->Finished 'cal q auc' block, time used:114.12s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561366847_auc0.666527_loss0.533769_std0.002227.npy
{                                                                             
 "bagging_fraction": 0.9,
 "bagging_freq": 8.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.19,
 "max_bin": 255,
 "min_data_in_leaf": 30.0,
 "num_iterations": 175.0,
 "num_leaves": 5.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533766                                         
[40]	valid's binary_logloss: 0.533041                                         
[60]	valid's binary_logloss: 0.532791                                         
[80]	valid's binary_logloss: 0.532656                                         
[100]	valid's binary_logloss: 0.5326                                          
[120]	valid's binary_logloss: 0.532526                                        
[140]	valid's binary_logloss: 0.532452                                        
[160]	valid's binary_logloss: 0.532457                                        
[20]	valid's binary_logloss: 0.534339                                         
[40]	valid's binary_logloss: 0.533749                                         
[60]	valid's binary_logloss: 0.533535                                         
[80]	valid's binary_logloss: 0.533444                                         
[100]	valid's binary_logloss: 0.533476                                        
[120]	valid's binary_logloss: 0.533396                                        
[140]	valid's binary_logloss: 0.533374                                        
[160]	valid's binary_logloss: 0.533393                                        
[20]	valid's binary_logloss: 0.533221                                         
[40]	valid's binary_logloss: 0.532479                                         
[60]	valid's binary_logloss: 0.532154                                         
[80]	valid's binary_logloss: 0.532016                                         
[100]	valid's binary_logloss: 0.531977                                        
[120]	valid's binary_logloss: 0.531843                                        
[140]	valid's binary_logloss: 0.531768                                        
[160]	valid's binary_logloss: 0.53177                                         
[20]	valid's binary_logloss: 0.532714                                         
[40]	valid's binary_logloss: 0.531952                                         
[60]	valid's binary_logloss: 0.531625                                         
[80]	valid's binary_logloss: 0.531503                                         
[100]	valid's binary_logloss: 0.531459                                        
[120]	valid's binary_logloss: 0.531368                                        
[140]	valid's binary_logloss: 0.531378                                        
[160]	valid's binary_logloss: 0.531369                                        
[20]	valid's binary_logloss: 0.534441                                         
[40]	valid's binary_logloss: 0.533821                                         
[60]	valid's binary_logloss: 0.533507                                         
[80]	valid's binary_logloss: 0.533347                                         
[100]	valid's binary_logloss: 0.533226                                        
[120]	valid's binary_logloss: 0.533168                                        
[140]	valid's binary_logloss: 0.533119                                        
[160]	valid's binary_logloss: 0.533078                                        
feature importance:                                                           
                                               column  importance             
29                                         query_freq          48
33          debug_trainMagic_unigrams_diffSetSimratio          41
1                    debug_trainTextMining_text_t-len          34
4                debug_trainTextMining_unigrams_t-len          28
26                         debug_trainWord2vec_cosine          26
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          25
7           debug_trainTextMining_text_edit_seq_ratio          23
9            debug_trainTextMining_text_partial_ratio          22
13      debug_trainTextMining_unigrams_edit_set_ratio          21
0                    debug_trainTextMining_text_q-len          21
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          20
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          19
5         debug_trainTextMining_unigrams_qt-len-radio          19
38                          debug_trainWord2vec_tSkew          18
15       debug_trainTextMining_bigrams_edit_seq_ratio          17
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...          16
39                      debug_trainWord2vec_qKurtosis          16
21       debug_trainTextMining_trigrams_partial_ratio          16
40                      debug_trainWord2vec_tKurtosis          16
10        debug_trainTextMining_text_token_sort_ratio          16
12      debug_trainTextMining_unigrams_edit_seq_ratio          15
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          14
14       debug_trainTextMining_unigrams_partial_ratio          14
27                      debug_trainWord2vec_euclidean          13
2             debug_trainTextMining_text_qt-len-radio          13
37                          debug_trainWord2vec_qSkew          13
18     debug_trainTextMining_bigrams_token_sort_ratio          13
20      debug_trainTextMining_trigrams_edit_set_ratio          13
24                      debug_trainWord2vec_chebyshev          13
11          debug_trainTextMining_unigrams_dice_ratio          12
23                       debug_trainWord2vec_canberra          12
19      debug_trainTextMining_trigrams_edit_seq_ratio          12
3             debug_trainTextMining_text_tq-len-radio          11
16       debug_trainTextMining_bigrams_edit_set_ratio          10
8           debug_trainTextMining_text_edit_set_ratio          10
6               debug_trainTextMining_text_dice_ratio          10
22                     debug_trainWord2vec_braycurtis          10
25                      debug_trainWord2vec_cityblock           8
36                          debug_trainMagic_localCTR           8
28                    debug_trainWord2vec_sqeuclidean           7
17        debug_trainTextMining_bigrams_partial_ratio           7
Valid Loss, AUC: 0.533254 0.670147                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5381179987687874                                               
----->Finished 'cal q auc' block, time used:112.58s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561367010_auc0.670147_loss0.533254_std0.002736.npy
{                                                                             
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 6.0,
 "feature_fraction": 0.8,
 "learning_rate": 0.14,
 "max_bin": 1023,
 "min_data_in_leaf": 40.0,
 "num_iterations": 175.0,
 "num_leaves": 25.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533534                                         
[40]	valid's binary_logloss: 0.53298                                          
[60]	valid's binary_logloss: 0.532993                                         
[80]	valid's binary_logloss: 0.533074                                         
[100]	valid's binary_logloss: 0.533224                                        
[120]	valid's binary_logloss: 0.533301                                        
[140]	valid's binary_logloss: 0.533497                                        
[160]	valid's binary_logloss: 0.533598                                        
[20]	valid's binary_logloss: 0.533843                                         
[40]	valid's binary_logloss: 0.5336                                           
[60]	valid's binary_logloss: 0.533633                                         
[80]	valid's binary_logloss: 0.533651                                         
[100]	valid's binary_logloss: 0.533654                                        
[120]	valid's binary_logloss: 0.533816                                        
[140]	valid's binary_logloss: 0.533839                                        
[160]	valid's binary_logloss: 0.533901                                        
[20]	valid's binary_logloss: 0.532834                                         
[40]	valid's binary_logloss: 0.532163                                         
[60]	valid's binary_logloss: 0.532131                                         
[80]	valid's binary_logloss: 0.532126                                         
[100]	valid's binary_logloss: 0.532279                                        
[120]	valid's binary_logloss: 0.532417                                        
[140]	valid's binary_logloss: 0.532593                                        
[160]	valid's binary_logloss: 0.532642                                        
[20]	valid's binary_logloss: 0.532366                                         
[40]	valid's binary_logloss: 0.531716                                         
[60]	valid's binary_logloss: 0.531691                                         
[80]	valid's binary_logloss: 0.53174                                          
[100]	valid's binary_logloss: 0.531779                                        
[120]	valid's binary_logloss: 0.531859                                        
[140]	valid's binary_logloss: 0.531957                                        
[160]	valid's binary_logloss: 0.53202                                         
[20]	valid's binary_logloss: 0.533948                                         
[40]	valid's binary_logloss: 0.533403                                         
[60]	valid's binary_logloss: 0.533264                                         
[80]	valid's binary_logloss: 0.533219                                         
[100]	valid's binary_logloss: 0.533303                                        
[120]	valid's binary_logloss: 0.533394                                        
[140]	valid's binary_logloss: 0.533511                                        
[160]	valid's binary_logloss: 0.533676                                        
feature importance:                                                           
                                               column  importance             
26                         debug_trainWord2vec_cosine         192
40                      debug_trainWord2vec_tKurtosis         177
37                          debug_trainWord2vec_qSkew         172
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...         161
24                      debug_trainWord2vec_chebyshev         157
38                          debug_trainWord2vec_tSkew         156
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...         148
39                      debug_trainWord2vec_qKurtosis         143
23                       debug_trainWord2vec_canberra         140
22                     debug_trainWord2vec_braycurtis         134
29                                         query_freq         129
1                    debug_trainTextMining_text_t-len         128
33          debug_trainMagic_unigrams_diffSetSimratio         124
7           debug_trainTextMining_text_edit_seq_ratio         124
25                      debug_trainWord2vec_cityblock         112
27                      debug_trainWord2vec_euclidean         104
12      debug_trainTextMining_unigrams_edit_seq_ratio         104
9            debug_trainTextMining_text_partial_ratio         103
8           debug_trainTextMining_text_edit_set_ratio         101
19      debug_trainTextMining_trigrams_edit_seq_ratio         100
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          99
15       debug_trainTextMining_bigrams_edit_seq_ratio          99
4                debug_trainTextMining_unigrams_t-len          97
13      debug_trainTextMining_unigrams_edit_set_ratio          88
16       debug_trainTextMining_bigrams_edit_set_ratio          88
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          88
2             debug_trainTextMining_text_qt-len-radio          86
0                    debug_trainTextMining_text_q-len          81
21       debug_trainTextMining_trigrams_partial_ratio          74
5         debug_trainTextMining_unigrams_qt-len-radio          70
14       debug_trainTextMining_unigrams_partial_ratio          69
11          debug_trainTextMining_unigrams_dice_ratio          68
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          66
20      debug_trainTextMining_trigrams_edit_set_ratio          65
10        debug_trainTextMining_text_token_sort_ratio          64
28                    debug_trainWord2vec_sqeuclidean          57
17        debug_trainTextMining_bigrams_partial_ratio          55
6               debug_trainTextMining_text_dice_ratio          51
3             debug_trainTextMining_text_tq-len-radio          49
18     debug_trainTextMining_bigrams_token_sort_ratio          47
36                          debug_trainMagic_localCTR          30
Valid Loss, AUC: 0.533559 0.668069                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5335858199854641                                               
----->Finished 'cal q auc' block, time used:112.58s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561367190_auc0.668069_loss0.533559_std0.002992.npy
{                                                                             
 "bagging_fraction": 0.6000000000000001,
 "bagging_freq": 4.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.16,
 "max_bin": 63,
 "min_data_in_leaf": 30.0,
 "num_iterations": 75.0,
 "num_leaves": 25.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533347                                         
[40]	valid's binary_logloss: 0.533089                                         
[60]	valid's binary_logloss: 0.533028                                         
[20]	valid's binary_logloss: 0.533829                                         
[40]	valid's binary_logloss: 0.533449                                         
[60]	valid's binary_logloss: 0.533605                                         
[20]	valid's binary_logloss: 0.532581                                         
[40]	valid's binary_logloss: 0.532154                                         
[60]	valid's binary_logloss: 0.532206                                         
[20]	valid's binary_logloss: 0.532159                                         
[40]	valid's binary_logloss: 0.531746                                         
[60]	valid's binary_logloss: 0.531793                                         
[20]	valid's binary_logloss: 0.533944                                         
[40]	valid's binary_logloss: 0.533537                                         
[60]	valid's binary_logloss: 0.533462                                         
feature importance:                                                           
                                               column  importance             
29                                         query_freq         105
4                debug_trainTextMining_unigrams_t-len          81
26                         debug_trainWord2vec_cosine          73
33          debug_trainMagic_unigrams_diffSetSimratio          68
1                    debug_trainTextMining_text_t-len          66
9            debug_trainTextMining_text_partial_ratio          58
40                      debug_trainWord2vec_tKurtosis          56
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          54
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          54
0                    debug_trainTextMining_text_q-len          54
22                     debug_trainWord2vec_braycurtis          53
38                          debug_trainWord2vec_tSkew          52
27                      debug_trainWord2vec_euclidean          50
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          49
23                       debug_trainWord2vec_canberra          49
37                          debug_trainWord2vec_qSkew          48
21       debug_trainTextMining_trigrams_partial_ratio          47
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...          46
7           debug_trainTextMining_text_edit_seq_ratio          44
14       debug_trainTextMining_unigrams_partial_ratio          40
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          40
17        debug_trainTextMining_bigrams_partial_ratio          39
24                      debug_trainWord2vec_chebyshev          39
12      debug_trainTextMining_unigrams_edit_seq_ratio          38
19      debug_trainTextMining_trigrams_edit_seq_ratio          38
11          debug_trainTextMining_unigrams_dice_ratio          38
10        debug_trainTextMining_text_token_sort_ratio          36
39                      debug_trainWord2vec_qKurtosis          36
13      debug_trainTextMining_unigrams_edit_set_ratio          35
5         debug_trainTextMining_unigrams_qt-len-radio          33
25                      debug_trainWord2vec_cityblock          31
6               debug_trainTextMining_text_dice_ratio          31
18     debug_trainTextMining_bigrams_token_sort_ratio          31
8           debug_trainTextMining_text_edit_set_ratio          27
36                          debug_trainMagic_localCTR          27
3             debug_trainTextMining_text_tq-len-radio          26
15       debug_trainTextMining_bigrams_edit_seq_ratio          26
16       debug_trainTextMining_bigrams_edit_set_ratio          24
20      debug_trainTextMining_trigrams_edit_set_ratio          24
2             debug_trainTextMining_text_qt-len-radio          20
28                    debug_trainWord2vec_sqeuclidean          14
Valid Loss, AUC: 0.534204 0.66898                                             
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5352847427464731                                               
----->Finished 'cal q auc' block, time used:118.18s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561367332_auc0.668980_loss0.534204_std0.004063.npy
{                                                                             
 "bagging_fraction": 0.8,
 "bagging_freq": 4.0,
 "feature_fraction": 1.0,
 "learning_rate": 0.12,
 "max_bin": 255,
 "min_data_in_leaf": 50.0,
 "num_iterations": 75.0,
 "num_leaves": 30.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533611                                         
[40]	valid's binary_logloss: 0.53294                                          
[60]	valid's binary_logloss: 0.532844                                         
[20]	valid's binary_logloss: 0.534021                                         
[40]	valid's binary_logloss: 0.533385                                         
[60]	valid's binary_logloss: 0.533252                                         
[20]	valid's binary_logloss: 0.532848                                         
[40]	valid's binary_logloss: 0.531902                                         
[60]	valid's binary_logloss: 0.53179                                          
[20]	valid's binary_logloss: 0.532425                                         
[40]	valid's binary_logloss: 0.5316                                           
[60]	valid's binary_logloss: 0.531433                                         
[20]	valid's binary_logloss: 0.534127                                         
[40]	valid's binary_logloss: 0.533374                                         
[60]	valid's binary_logloss: 0.533316                                         
feature importance:                                                           
                                               column  importance             
29                                         query_freq         150
26                         debug_trainWord2vec_cosine         115
33          debug_trainMagic_unigrams_diffSetSimratio         112
1                    debug_trainTextMining_text_t-len          98
4                debug_trainTextMining_unigrams_t-len          93
40                      debug_trainWord2vec_tKurtosis          83
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          80
0                    debug_trainTextMining_text_q-len          70
9            debug_trainTextMining_text_partial_ratio          65
39                      debug_trainWord2vec_qKurtosis          61
24                      debug_trainWord2vec_chebyshev          60
38                          debug_trainWord2vec_tSkew          59
22                     debug_trainWord2vec_braycurtis          59
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...          56
12      debug_trainTextMining_unigrams_edit_seq_ratio          55
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          54
7           debug_trainTextMining_text_edit_seq_ratio          53
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          52
37                          debug_trainWord2vec_qSkew          49
13      debug_trainTextMining_unigrams_edit_set_ratio          47
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          45
5         debug_trainTextMining_unigrams_qt-len-radio          44
10        debug_trainTextMining_text_token_sort_ratio          43
21       debug_trainTextMining_trigrams_partial_ratio          43
14       debug_trainTextMining_unigrams_partial_ratio          42
19      debug_trainTextMining_trigrams_edit_seq_ratio          42
23                       debug_trainWord2vec_canberra          41
25                      debug_trainWord2vec_cityblock          40
15       debug_trainTextMining_bigrams_edit_seq_ratio          40
27                      debug_trainWord2vec_euclidean          37
17        debug_trainTextMining_bigrams_partial_ratio          35
8           debug_trainTextMining_text_edit_set_ratio          34
3             debug_trainTextMining_text_tq-len-radio          31
11          debug_trainTextMining_unigrams_dice_ratio          30
2             debug_trainTextMining_text_qt-len-radio          29
6               debug_trainTextMining_text_dice_ratio          28
18     debug_trainTextMining_bigrams_token_sort_ratio          27
20      debug_trainTextMining_trigrams_edit_set_ratio          25
16       debug_trainTextMining_bigrams_edit_set_ratio          24
28                    debug_trainWord2vec_sqeuclidean          22
36                          debug_trainMagic_localCTR           2
Valid Loss, AUC: 0.534459 0.669772                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5380019413589965                                               
----->Finished 'cal q auc' block, time used:112.6s.                           
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561367492_auc0.669772_loss0.534459_std0.004849.npy
{                                                                             
 "bagging_fraction": 0.8,
 "bagging_freq": 0.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.15,
 "max_bin": 1023,
 "min_data_in_leaf": 50.0,
 "num_iterations": 75.0,
 "num_leaves": 5.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.534293                                         
[40]	valid's binary_logloss: 0.533302                                         
[60]	valid's binary_logloss: 0.532982                                         
[20]	valid's binary_logloss: 0.534739                                         
[40]	valid's binary_logloss: 0.533908                                         
[60]	valid's binary_logloss: 0.533655                                         
[20]	valid's binary_logloss: 0.533618                                         
[40]	valid's binary_logloss: 0.532582                                         
[60]	valid's binary_logloss: 0.532205                                         
[20]	valid's binary_logloss: 0.533227                                         
[40]	valid's binary_logloss: 0.532166                                         
[60]	valid's binary_logloss: 0.531865                                         
[20]	valid's binary_logloss: 0.534794                                         
[40]	valid's binary_logloss: 0.534022                                         
[60]	valid's binary_logloss: 0.533639                                         
feature importance:                                                           
                                               column  importance             
29                                         query_freq          54
4                debug_trainTextMining_unigrams_t-len          24
26                         debug_trainWord2vec_cosine          23
33          debug_trainMagic_unigrams_diffSetSimratio          19
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          18
1                    debug_trainTextMining_text_t-len          15
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          13
0                    debug_trainTextMining_text_q-len          11
9            debug_trainTextMining_text_partial_ratio          10
36                          debug_trainMagic_localCTR           8
2             debug_trainTextMining_text_qt-len-radio           8
5         debug_trainTextMining_unigrams_qt-len-radio           7
21       debug_trainTextMining_trigrams_partial_ratio           7
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...           6
13      debug_trainTextMining_unigrams_edit_set_ratio           6
22                     debug_trainWord2vec_braycurtis           6
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...           5
40                      debug_trainWord2vec_tKurtosis           5
11          debug_trainTextMining_unigrams_dice_ratio           5
7           debug_trainTextMining_text_edit_seq_ratio           5
6               debug_trainTextMining_text_dice_ratio           4
15       debug_trainTextMining_bigrams_edit_seq_ratio           4
10        debug_trainTextMining_text_token_sort_ratio           4
3             debug_trainTextMining_text_tq-len-radio           3
23                       debug_trainWord2vec_canberra           3
8           debug_trainTextMining_text_edit_set_ratio           3
14       debug_trainTextMining_unigrams_partial_ratio           3
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...           3
18     debug_trainTextMining_bigrams_token_sort_ratio           2
12      debug_trainTextMining_unigrams_edit_seq_ratio           2
19      debug_trainTextMining_trigrams_edit_seq_ratio           2
28                    debug_trainWord2vec_sqeuclidean           2
27                      debug_trainWord2vec_euclidean           2
25                      debug_trainWord2vec_cityblock           2
24                      debug_trainWord2vec_chebyshev           2
17        debug_trainTextMining_bigrams_partial_ratio           1
38                          debug_trainWord2vec_tSkew           1
39                      debug_trainWord2vec_qKurtosis           1
20      debug_trainTextMining_trigrams_edit_set_ratio           1
16       debug_trainTextMining_bigrams_edit_set_ratio           0
37                          debug_trainWord2vec_qSkew           0
Valid Loss, AUC: 0.534837 0.669423                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5374218645573783                                               
----->Finished 'cal q auc' block, time used:113.4s.                           
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561367640_auc0.669423_loss0.534837_std0.004471.npy
{                                                                             
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 8.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.11,
 "max_bin": 1023,
 "min_data_in_leaf": 40.0,
 "num_iterations": 175.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.534414                                         
[40]	valid's binary_logloss: 0.533211                                         
[60]	valid's binary_logloss: 0.532895                                         
[80]	valid's binary_logloss: 0.532783                                         
[100]	valid's binary_logloss: 0.532729                                        
[120]	valid's binary_logloss: 0.532625                                        
[140]	valid's binary_logloss: 0.532627                                        
[160]	valid's binary_logloss: 0.532602                                        
[20]	valid's binary_logloss: 0.534795                                         
[40]	valid's binary_logloss: 0.533732                                         
[60]	valid's binary_logloss: 0.533508                                         
[80]	valid's binary_logloss: 0.533398                                         
[100]	valid's binary_logloss: 0.533377                                        
[120]	valid's binary_logloss: 0.53328                                         
[140]	valid's binary_logloss: 0.533244                                        
[160]	valid's binary_logloss: 0.533206                                        
[20]	valid's binary_logloss: 0.533848                                         
[40]	valid's binary_logloss: 0.532404                                         
[60]	valid's binary_logloss: 0.532113                                         
[80]	valid's binary_logloss: 0.532023                                         
[100]	valid's binary_logloss: 0.531905                                        
[120]	valid's binary_logloss: 0.531874                                        
[140]	valid's binary_logloss: 0.531828                                        
[160]	valid's binary_logloss: 0.531809                                        
[20]	valid's binary_logloss: 0.533397                                         
[40]	valid's binary_logloss: 0.532013                                         
[60]	valid's binary_logloss: 0.531718                                         
[80]	valid's binary_logloss: 0.531518                                         
[100]	valid's binary_logloss: 0.531476                                        
[120]	valid's binary_logloss: 0.531413                                        
[140]	valid's binary_logloss: 0.531329                                        
[160]	valid's binary_logloss: 0.531314                                        
[20]	valid's binary_logloss: 0.534948                                         
[40]	valid's binary_logloss: 0.533868                                         
[60]	valid's binary_logloss: 0.53359                                          
[80]	valid's binary_logloss: 0.533455                                         
[100]	valid's binary_logloss: 0.53334                                         
[120]	valid's binary_logloss: 0.533277                                        
[140]	valid's binary_logloss: 0.53316                                         
[160]	valid's binary_logloss: 0.533185                                        
feature importance:                                                           
                                               column  importance             
29                                         query_freq         101
26                         debug_trainWord2vec_cosine          86
33          debug_trainMagic_unigrams_diffSetSimratio          73
1                    debug_trainTextMining_text_t-len          57
24                      debug_trainWord2vec_chebyshev          55
4                debug_trainTextMining_unigrams_t-len          54
7           debug_trainTextMining_text_edit_seq_ratio          53
40                      debug_trainWord2vec_tKurtosis          50
9            debug_trainTextMining_text_partial_ratio          50
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          46
38                          debug_trainWord2vec_tSkew          44
0                    debug_trainTextMining_text_q-len          44
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          40
22                     debug_trainWord2vec_braycurtis          40
12      debug_trainTextMining_unigrams_edit_seq_ratio          39
21       debug_trainTextMining_trigrams_partial_ratio          39
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          38
27                      debug_trainWord2vec_euclidean          37
20      debug_trainTextMining_trigrams_edit_set_ratio          36
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...          34
23                       debug_trainWord2vec_canberra          34
10        debug_trainTextMining_text_token_sort_ratio          33
15       debug_trainTextMining_bigrams_edit_seq_ratio          32
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          31
13      debug_trainTextMining_unigrams_edit_set_ratio          31
37                          debug_trainWord2vec_qSkew          29
16       debug_trainTextMining_bigrams_edit_set_ratio          29
39                      debug_trainWord2vec_qKurtosis          28
19      debug_trainTextMining_trigrams_edit_seq_ratio          27
25                      debug_trainWord2vec_cityblock          27
11          debug_trainTextMining_unigrams_dice_ratio          26
5         debug_trainTextMining_unigrams_qt-len-radio          26
14       debug_trainTextMining_unigrams_partial_ratio          26
36                          debug_trainMagic_localCTR          26
17        debug_trainTextMining_bigrams_partial_ratio          26
2             debug_trainTextMining_text_qt-len-radio          26
8           debug_trainTextMining_text_edit_set_ratio          26
3             debug_trainTextMining_text_tq-len-radio          20
28                    debug_trainWord2vec_sqeuclidean          19
18     debug_trainTextMining_bigrams_token_sort_ratio          19
6               debug_trainTextMining_text_dice_ratio          18
Valid Loss, AUC: 0.533654 0.670025                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5368288216248154                                               
----->Finished 'cal q auc' block, time used:113.23s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561367811_auc0.670025_loss0.533654_std0.003743.npy
{                                                                             
 "bagging_fraction": 1.0,
 "bagging_freq": 0.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.11,
 "max_bin": 15,
 "min_data_in_leaf": 20.0,
 "num_iterations": 200.0,
 "num_leaves": 30.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.534066                                         
[40]	valid's binary_logloss: 0.533146                                         
[60]	valid's binary_logloss: 0.532926                                         
[80]	valid's binary_logloss: 0.532922                                         
[100]	valid's binary_logloss: 0.532901                                        
[120]	valid's binary_logloss: 0.532988                                        
[140]	valid's binary_logloss: 0.533034                                        
[160]	valid's binary_logloss: 0.533098                                        
[180]	valid's binary_logloss: 0.533122                                        
[200]	valid's binary_logloss: 0.533156                                        
[20]	valid's binary_logloss: 0.534432                                         
[40]	valid's binary_logloss: 0.533662                                         
[60]	valid's binary_logloss: 0.53357                                          
[80]	valid's binary_logloss: 0.533579                                         
[100]	valid's binary_logloss: 0.533617                                        
[120]	valid's binary_logloss: 0.533604                                        
[140]	valid's binary_logloss: 0.533697                                        
[160]	valid's binary_logloss: 0.533682                                        
[180]	valid's binary_logloss: 0.533701                                        
[200]	valid's binary_logloss: 0.533793                                        
[20]	valid's binary_logloss: 0.533346                                         
[40]	valid's binary_logloss: 0.532269                                         
[60]	valid's binary_logloss: 0.532032                                         
[80]	valid's binary_logloss: 0.531985                                         
[100]	valid's binary_logloss: 0.531966                                        
[120]	valid's binary_logloss: 0.532                                           
[140]	valid's binary_logloss: 0.531985                                        
[160]	valid's binary_logloss: 0.532057                                        
[180]	valid's binary_logloss: 0.532067                                        
[200]	valid's binary_logloss: 0.532095                                        
[20]	valid's binary_logloss: 0.5328                                           
[40]	valid's binary_logloss: 0.531664                                         
[60]	valid's binary_logloss: 0.531502                                         
[80]	valid's binary_logloss: 0.531486                                         
[100]	valid's binary_logloss: 0.531539                                        
[120]	valid's binary_logloss: 0.531503                                        
[140]	valid's binary_logloss: 0.531496                                        
[160]	valid's binary_logloss: 0.531524                                        
[180]	valid's binary_logloss: 0.531507                                        
[200]	valid's binary_logloss: 0.531523                                        
[20]	valid's binary_logloss: 0.534436                                         
[40]	valid's binary_logloss: 0.533446                                         
[60]	valid's binary_logloss: 0.533246                                         
[80]	valid's binary_logloss: 0.533242                                         
[100]	valid's binary_logloss: 0.533234                                        
[120]	valid's binary_logloss: 0.53323                                         
[140]	valid's binary_logloss: 0.533291                                        
[160]	valid's binary_logloss: 0.533302                                        
[180]	valid's binary_logloss: 0.533254                                        
[200]	valid's binary_logloss: 0.53328                                         
feature importance:                                                           
                                               column  importance             
33          debug_trainMagic_unigrams_diffSetSimratio         251
26                         debug_trainWord2vec_cosine         225
29                                         query_freq         214
4                debug_trainTextMining_unigrams_t-len         211
38                          debug_trainWord2vec_tSkew         197
9            debug_trainTextMining_text_partial_ratio         196
40                      debug_trainWord2vec_tKurtosis         192
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio         186
39                      debug_trainWord2vec_qKurtosis         176
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...         173
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...         171
0                    debug_trainTextMining_text_q-len         171
37                          debug_trainWord2vec_qSkew         167
1                    debug_trainTextMining_text_t-len         166
24                      debug_trainWord2vec_chebyshev         162
14       debug_trainTextMining_unigrams_partial_ratio         159
21       debug_trainTextMining_trigrams_partial_ratio         156
6               debug_trainTextMining_text_dice_ratio         156
30     debug_trainMagic_unigrams_diffSetSimdice_ratio         143
17        debug_trainTextMining_bigrams_partial_ratio         142
23                       debug_trainWord2vec_canberra         140
22                     debug_trainWord2vec_braycurtis         136
11          debug_trainTextMining_unigrams_dice_ratio         133
5         debug_trainTextMining_unigrams_qt-len-radio         131
10        debug_trainTextMining_text_token_sort_ratio         130
27                      debug_trainWord2vec_euclidean         128
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...         125
13      debug_trainTextMining_unigrams_edit_set_ratio         122
36                          debug_trainMagic_localCTR         120
7           debug_trainTextMining_text_edit_seq_ratio         120
12      debug_trainTextMining_unigrams_edit_seq_ratio         110
25                      debug_trainWord2vec_cityblock         104
19      debug_trainTextMining_trigrams_edit_seq_ratio          96
18     debug_trainTextMining_bigrams_token_sort_ratio          91
15       debug_trainTextMining_bigrams_edit_seq_ratio          88
8           debug_trainTextMining_text_edit_set_ratio          78
16       debug_trainTextMining_bigrams_edit_set_ratio          73
2             debug_trainTextMining_text_qt-len-radio          73
20      debug_trainTextMining_trigrams_edit_set_ratio          72
28                    debug_trainWord2vec_sqeuclidean          62
3             debug_trainTextMining_text_tq-len-radio          54
Valid Loss, AUC: 0.533537 0.669214                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5359384522741578                                               
----->Finished 'cal q auc' block, time used:114.92s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561367995_auc0.669214_loss0.533537_std0.003439.npy
{                                                                             
 "bagging_fraction": 0.8,
 "bagging_freq": 0.0,
 "feature_fraction": 1.0,
 "learning_rate": 0.13,
 "max_bin": 63,
 "min_data_in_leaf": 10.0,
 "num_iterations": 150.0,
 "num_leaves": 10.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533984                                         
[40]	valid's binary_logloss: 0.53301                                          
[60]	valid's binary_logloss: 0.532789                                         
[80]	valid's binary_logloss: 0.532671                                         
[100]	valid's binary_logloss: 0.532594                                        
[120]	valid's binary_logloss: 0.532563                                        
[140]	valid's binary_logloss: 0.532536                                        
[20]	valid's binary_logloss: 0.534363                                         
[40]	valid's binary_logloss: 0.533563                                         
[60]	valid's binary_logloss: 0.533383                                         
[80]	valid's binary_logloss: 0.533366                                         
[100]	valid's binary_logloss: 0.533335                                        
[120]	valid's binary_logloss: 0.533361                                        
[140]	valid's binary_logloss: 0.533377                                        
[20]	valid's binary_logloss: 0.533327                                         
[40]	valid's binary_logloss: 0.532319                                         
[60]	valid's binary_logloss: 0.532044                                         
[80]	valid's binary_logloss: 0.531935                                         
[100]	valid's binary_logloss: 0.53181                                         
[120]	valid's binary_logloss: 0.53175                                         
[140]	valid's binary_logloss: 0.531716                                        
[20]	valid's binary_logloss: 0.532866                                         
[40]	valid's binary_logloss: 0.531804                                         
[60]	valid's binary_logloss: 0.531542                                         
[80]	valid's binary_logloss: 0.531384                                         
[100]	valid's binary_logloss: 0.531379                                        
[120]	valid's binary_logloss: 0.531327                                        
[140]	valid's binary_logloss: 0.53131                                         
[20]	valid's binary_logloss: 0.534407                                         
[40]	valid's binary_logloss: 0.533572                                         
[60]	valid's binary_logloss: 0.533309                                         
[80]	valid's binary_logloss: 0.533232                                         
[100]	valid's binary_logloss: 0.533157                                        
[120]	valid's binary_logloss: 0.533113                                        
[140]	valid's binary_logloss: 0.533033                                        
feature importance:                                                           
                                               column  importance             
29                                         query_freq         106
33          debug_trainMagic_unigrams_diffSetSimratio          78
4                debug_trainTextMining_unigrams_t-len          72
26                         debug_trainWord2vec_cosine          62
40                      debug_trainWord2vec_tKurtosis          57
1                    debug_trainTextMining_text_t-len          54
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          54
0                    debug_trainTextMining_text_q-len          53
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          49
9            debug_trainTextMining_text_partial_ratio          45
10        debug_trainTextMining_text_token_sort_ratio          42
24                      debug_trainWord2vec_chebyshev          35
21       debug_trainTextMining_trigrams_partial_ratio          35
5         debug_trainTextMining_unigrams_qt-len-radio          34
37                          debug_trainWord2vec_qSkew          31
6               debug_trainTextMining_text_dice_ratio          31
14       debug_trainTextMining_unigrams_partial_ratio          30
38                          debug_trainWord2vec_tSkew          29
19      debug_trainTextMining_trigrams_edit_seq_ratio          29
22                     debug_trainWord2vec_braycurtis          28
11          debug_trainTextMining_unigrams_dice_ratio          28
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          27
39                      debug_trainWord2vec_qKurtosis          26
18     debug_trainTextMining_bigrams_token_sort_ratio          26
7           debug_trainTextMining_text_edit_seq_ratio          26
13      debug_trainTextMining_unigrams_edit_set_ratio          25
23                       debug_trainWord2vec_canberra          24
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          23
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...          23
12      debug_trainTextMining_unigrams_edit_seq_ratio          22
8           debug_trainTextMining_text_edit_set_ratio          21
17        debug_trainTextMining_bigrams_partial_ratio          21
15       debug_trainTextMining_bigrams_edit_seq_ratio          18
20      debug_trainTextMining_trigrams_edit_set_ratio          16
3             debug_trainTextMining_text_tq-len-radio          15
27                      debug_trainWord2vec_euclidean          13
28                    debug_trainWord2vec_sqeuclidean          10
25                      debug_trainWord2vec_cityblock          10
2             debug_trainTextMining_text_qt-len-radio           9
16       debug_trainTextMining_bigrams_edit_set_ratio           9
36                          debug_trainMagic_localCTR           4
Valid Loss, AUC: 0.533523 0.670159                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5397299352702282                                               
----->Finished 'cal q auc' block, time used:115.43s.                          
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561368175_auc0.670159_loss0.533523_std0.003552.npy
{                                                                             
 "bagging_fraction": 0.8,
 "bagging_freq": 0.0,
 "feature_fraction": 0.7000000000000001,
 "learning_rate": 0.12,
 "max_bin": 1023,
 "min_data_in_leaf": 30.0,
 "num_iterations": 150.0,
 "num_leaves": 15.0,
 "num_threads": 4
}
[20]	valid's binary_logloss: 0.533926                                         
[40]	valid's binary_logloss: 0.532971                                         
[60]	valid's binary_logloss: 0.532792                                         
[80]	valid's binary_logloss: 0.532706                                         
[100]	valid's binary_logloss: 0.532752                                        
[120]	valid's binary_logloss: 0.532746                                        
[140]	valid's binary_logloss: 0.532814                                        
[20]	valid's binary_logloss: 0.534289                                         
[40]	valid's binary_logloss: 0.533531                                         
[60]	valid's binary_logloss: 0.533357                                         
[80]	valid's binary_logloss: 0.533318                                         
[100]	valid's binary_logloss: 0.533321                                        
[120]	valid's binary_logloss: 0.533335                                        
[140]	valid's binary_logloss: 0.533367                                        
[20]	valid's binary_logloss: 0.53326                                          
[40]	valid's binary_logloss: 0.532133                                         
[60]	valid's binary_logloss: 0.531897                                         
[80]	valid's binary_logloss: 0.531857                                         
[100]	valid's binary_logloss: 0.53178                                         
[120]	valid's binary_logloss: 0.531759                                        
[140]	valid's binary_logloss: 0.53175                                         
[20]	valid's binary_logloss: 0.532776                                         
[40]	valid's binary_logloss: 0.531639                                         
[60]	valid's binary_logloss: 0.531407                                         
[80]	valid's binary_logloss: 0.531342                                         
[100]	valid's binary_logloss: 0.531252                                        
[120]	valid's binary_logloss: 0.531223                                        
[140]	valid's binary_logloss: 0.531257                                        
[20]	valid's binary_logloss: 0.534358                                         
[40]	valid's binary_logloss: 0.533537                                         
[60]	valid's binary_logloss: 0.533252                                         
[80]	valid's binary_logloss: 0.533185                                         
[100]	valid's binary_logloss: 0.533139                                        
[120]	valid's binary_logloss: 0.533192                                        
[140]	valid's binary_logloss: 0.533151                                        
feature importance:                                                           
                                               column  importance             
26                         debug_trainWord2vec_cosine         114
29                                         query_freq         108
1                    debug_trainTextMining_text_t-len          93
40                      debug_trainWord2vec_tKurtosis          75
33          debug_trainMagic_unigrams_diffSetSimratio          74
9            debug_trainTextMining_text_partial_ratio          71
4                debug_trainTextMining_unigrams_t-len          67
24                      debug_trainWord2vec_chebyshev          65
38                          debug_trainWord2vec_tSkew          64
27                      debug_trainWord2vec_euclidean          63
32  debug_trainMagic_unigrams_diffSetSimedit_set_r...          61
7           debug_trainTextMining_text_edit_seq_ratio          59
31  debug_trainMagic_unigrams_diffSetSimedit_seq_r...          57
34  debug_trainMagic_unigrams_diffSetSimpartial_ratio          56
13      debug_trainTextMining_unigrams_edit_set_ratio          56
30     debug_trainMagic_unigrams_diffSetSimdice_ratio          55
22                     debug_trainWord2vec_braycurtis          50
21       debug_trainTextMining_trigrams_partial_ratio          50
0                    debug_trainTextMining_text_q-len          49
2             debug_trainTextMining_text_qt-len-radio          49
23                       debug_trainWord2vec_canberra          47
15       debug_trainTextMining_bigrams_edit_seq_ratio          47
5         debug_trainTextMining_unigrams_qt-len-radio          46
8           debug_trainTextMining_text_edit_set_ratio          45
39                      debug_trainWord2vec_qKurtosis          44
19      debug_trainTextMining_trigrams_edit_seq_ratio          43
25                      debug_trainWord2vec_cityblock          43
37                          debug_trainWord2vec_qSkew          43
12      debug_trainTextMining_unigrams_edit_seq_ratio          42
35  debug_trainMagic_unigrams_diffSetSimtoken_sort...          42
18     debug_trainTextMining_bigrams_token_sort_ratio          40
10        debug_trainTextMining_text_token_sort_ratio          37
17        debug_trainTextMining_bigrams_partial_ratio          34
16       debug_trainTextMining_bigrams_edit_set_ratio          33
14       debug_trainTextMining_unigrams_partial_ratio          32
11          debug_trainTextMining_unigrams_dice_ratio          31
36                          debug_trainMagic_localCTR          30
3             debug_trainTextMining_text_tq-len-radio          26
6               debug_trainTextMining_text_dice_ratio          21
20      debug_trainTextMining_trigrams_edit_set_ratio          21
28                    debug_trainWord2vec_sqeuclidean          17
Valid Loss, AUC: 0.533602 0.669834                                            
----->Started 'cal q auc' block...                                            
Valid Q AUC: 0.5365839757408165                                               
----->Finished 'cal q auc' block, time used:116.9s.                           
Saved train results to /home/kesci/work/stage2/output/train/lgb_gbdt_1561368346_auc0.669834_loss0.533602_std0.003784.npy
100%|██████████| 20/20 [55:30<00:00, 172.14s/it, best loss: 0.533156546741731]

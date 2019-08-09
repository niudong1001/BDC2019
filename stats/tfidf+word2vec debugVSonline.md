- online:

{                                                  
 "bagging_fraction": 0.9,
 "bagging_freq": 2.0,
 "feature_fraction": 0.6000000000000001,
 "lambda_l1": 0.4,
 "lambda_l2": 6.0,
 "learning_rate": 0.13,
 "max_bin": 255,
 "min_data_in_leaf": 40.0,
 "min_gain_to_split": 0.6000000000000001,
 "num_iterations": 120.0,
 "num_leaves": 40.0,
 "num_threads": 10
}
[50]	valid's binary_logloss: 0.46146               
[100]	valid's binary_logloss: 0.461027             
混淆矩阵：                                              
[[12292641     1829]                               
 [ 2700755     4775]]
feature importance:                                
                                               column  importance
3           online_trainVectorSpace_tfidfVecFeat_QSum         647
8           online_trainVectorSpace_tfidfVecFeat_TLen         573
10  online_trainVectorSpace_tfidfVecFeat_paired_eu...         559
7           online_trainVectorSpace_tfidfVecFeat_QLen         542
9   online_trainVectorSpace_tfidfVecFeat_paired_co...         510
11  online_trainVectorSpace_tfidfVecFeat_paired_ma...         492
0                online_trainWord2vec_cosine_distance         422
4           online_trainVectorSpace_tfidfVecFeat_TSum         415
1             online_trainWord2vec_euclidean_distance         222
2             online_trainWord2vec_cityblock_distance         187
6          online_trainVectorSpace_tfidfVecFeat_TMean          75
5          online_trainVectorSpace_tfidfVecFeat_QMean          36
Valid Loss and AUC: 0.461848 0.605735              
Saved test results to /home/kesci/work/outputs/test/lgb_gbdt_nd_auc0.605735_loss0.461848_std0.001491_0802121101.npy
{                                                                  
 "bagging_fraction": 0.7000000000000001,
 "bagging_freq": 6.0,
 "feature_fraction": 0.8,
 "lambda_l1": 0.2,
 "lambda_l2": 8.0,
 "learning_rate": 0.19,
 "max_bin": 255,
 "min_data_in_leaf": 30.0,
 "min_gain_to_split": 0.9,
 "num_iterations": 160.0,
 "num_leaves": 40.0,
 "num_threads": 10
}
[50]	valid's binary_logloss: 0.461207                              
[100]	valid's binary_logloss: 0.460742                             
[150]	valid's binary_logloss: 0.460497                             
混淆矩阵：                                                              
[[12292464     2006]                                               
 [ 2700568     4962]]
feature importance:                                                
                                               column  importance  
3           online_trainVectorSpace_tfidfVecFeat_QSum         910
11  online_trainVectorSpace_tfidfVecFeat_paired_ma...         737
9   online_trainVectorSpace_tfidfVecFeat_paired_co...         722
8           online_trainVectorSpace_tfidfVecFeat_TLen         715
4           online_trainVectorSpace_tfidfVecFeat_TSum         711
10  online_trainVectorSpace_tfidfVecFeat_paired_eu...         666
7           online_trainVectorSpace_tfidfVecFeat_QLen         625
0                online_trainWord2vec_cosine_distance         513
1             online_trainWord2vec_euclidean_distance         337
2             online_trainWord2vec_cityblock_distance         239
6          online_trainVectorSpace_tfidfVecFeat_TMean          44
5          online_trainVectorSpace_tfidfVecFeat_QMean          21
Valid Loss and AUC: 0.461229 0.607952                              
Saved test results to /home/kesci/work/outputs/test/lgb_gbdt_nd_auc0.607952_loss0.461229_std0.001162_0802121959.npy
{                                                                  
 "bagging_fraction": 0.9,
 "bagging_freq": 4.0,
 "feature_fraction": 0.6000000000000001,
 "lambda_l1": 0.2,
 "lambda_l2": 4.0,
 "learning_rate": 0.17,
 "max_bin": 63,
 "min_data_in_leaf": 50.0,
 "min_gain_to_split": 0.9,
 "num_iterations": 160.0,
 "num_leaves": 45.0,
 "num_threads": 10
}
 40%|████      | 2/5 [17:36<26:30, 530.30s/it, best loss: 0.461229]

- debug:
 {                                                  
 "bagging_fraction": 1.0,
 "bagging_freq": 2.0,
 "feature_fraction": 0.8,
 "lambda_l1": 0.5,
 "lambda_l2": 8.0,
 "learning_rate": 0.16,
 "max_bin": 63,
 "min_data_in_leaf": 50.0,
 "min_gain_to_split": 1.0,
 "num_iterations": 120.0,
 "num_leaves": 45.0,
 "num_threads": 10
}
[50]	valid's binary_logloss: 0.463768              
[100]	valid's binary_logloss: 0.463774             
混淆矩阵：                                              
[[245422     45]                                   
 [ 54452     81]]
feature importance:                                
                                               column  importance
8            debug_trainVectorSpace_tfidfVecFeat_TLen         316
0                 debug_trainWord2vec_cosine_distance         300
9   debug_trainVectorSpace_tfidfVecFeat_paired_cos...         294
1              debug_trainWord2vec_euclidean_distance         279
7            debug_trainVectorSpace_tfidfVecFeat_QLen         279
11  debug_trainVectorSpace_tfidfVecFeat_paired_man...         256
3            debug_trainVectorSpace_tfidfVecFeat_QSum         229
10  debug_trainVectorSpace_tfidfVecFeat_paired_euc...         218
2              debug_trainWord2vec_cityblock_distance         217
4            debug_trainVectorSpace_tfidfVecFeat_TSum         140
6           debug_trainVectorSpace_tfidfVecFeat_TMean           6
5           debug_trainVectorSpace_tfidfVecFeat_QMean           2
Valid Loss and AUC: 0.464139 0.602184              
----->started 'cal valid qauc' block...            
Valid QAUC: 0.574343                               
----->finished 'cal valid qauc' block, time used:33.55s.
----->started 'cal test qauc' block...             
Test QAUC: 0.56871                                 
----->finished 'cal test qauc' block, time used:44.98s.
{                                                                 
 "bagging_fraction": 0.9,
 "bagging_freq": 16.0,
 "feature_fraction": 0.8,
 "lambda_l1": 0.2,
 "lambda_l2": 6.0,
 "learning_rate": 0.14,
 "max_bin": 255,
 "min_data_in_leaf": 10.0,
 "min_gain_to_split": 0.4,
 "num_iterations": 180.0,
 "num_leaves": 40.0,
 "num_threads": 10
}
[50]	valid's binary_logloss: 0.463794                             
[100]	valid's binary_logloss: 0.463769                            
[150]	valid's binary_logloss: 0.463844                            
混淆矩阵：                                                             
[[245418     49]                                                  
 [ 54441     92]]
feature importance:                                               
                                               column  importance 
0                 debug_trainWord2vec_cosine_distance         957
3            debug_trainVectorSpace_tfidfVecFeat_QSum         894
1              debug_trainWord2vec_euclidean_distance         772
11  debug_trainVectorSpace_tfidfVecFeat_paired_man...         756
2              debug_trainWord2vec_cityblock_distance         732
4            debug_trainVectorSpace_tfidfVecFeat_TSum         717
9   debug_trainVectorSpace_tfidfVecFeat_paired_cos...         711
10  debug_trainVectorSpace_tfidfVecFeat_paired_euc...         602
8            debug_trainVectorSpace_tfidfVecFeat_TLen         525
7            debug_trainVectorSpace_tfidfVecFeat_QLen         346
6           debug_trainVectorSpace_tfidfVecFeat_TMean           5
5           debug_trainVectorSpace_tfidfVecFeat_QMean           3
Valid Loss and AUC: 0.464091 0.601572                             
----->started 'cal valid qauc' block...                           
Valid QAUC: 0.572526                                              
----->finished 'cal valid qauc' block, time used:33.71s.          
----->started 'cal test qauc' block...                            
Test QAUC: 0.56864                                                
----->finished 'cal test qauc' block, time used:45.12s.           
{                                                                 
 "bagging_fraction": 0.8,
 "bagging_freq": 8.0,
 "feature_fraction": 0.8,
 "lambda_l1": 0.5,
 "lambda_l2": 6.0,
 "learning_rate": 0.18,
 "max_bin": 255,
 "min_data_in_leaf": 20.0,
 "min_gain_to_split": 0.30000000000000004,
 "num_iterations": 180.0,
 "num_leaves": 25.0,
 "num_threads": 10
}
[50]	valid's binary_logloss: 0.463727                             
[100]	valid's binary_logloss: 0.463709                            
[150]	valid's binary_logloss: 0.463846                            
混淆矩阵：                                                             
[[245401     66]                                                  
 [ 54426    107]]
feature importance:                                               
                                               column  importance 
0                 debug_trainWord2vec_cosine_distance         629
3            debug_trainVectorSpace_tfidfVecFeat_QSum         554
11  debug_trainVectorSpace_tfidfVecFeat_paired_man...         489
9   debug_trainVectorSpace_tfidfVecFeat_paired_cos...         433
4            debug_trainVectorSpace_tfidfVecFeat_TSum         432
1              debug_trainWord2vec_euclidean_distance         428
2              debug_trainWord2vec_cityblock_distance         405
10  debug_trainVectorSpace_tfidfVecFeat_paired_euc...         380
8            debug_trainVectorSpace_tfidfVecFeat_TLen         355
7            debug_trainVectorSpace_tfidfVecFeat_QLen         210
6           debug_trainVectorSpace_tfidfVecFeat_TMean           4
5           debug_trainVectorSpace_tfidfVecFeat_QMean           1
Valid Loss and AUC: 0.464003 0.60151                              
----->started 'cal valid qauc' block...                           
Valid QAUC: 0.570927                                              
----->finished 'cal valid qauc' block, time used:33.54s.          
----->started 'cal test qauc' block...                            
Test QAUC: 0.568875                                               
----->finished 'cal test qauc' block, time used:45.38s.           
{                                                                 
 "bagging_fraction": 0.9,
 "bagging_freq": 6.0,
 "feature_fraction": 0.9,
 "lambda_l1": 0.0,
 "lambda_l2": 2.0,
 "learning_rate": 0.14,
 "max_bin": 255,
 "min_data_in_leaf": 10.0,
 "min_gain_to_split": 0.6000000000000001,
 "num_iterations": 200.0,
 "num_leaves": 25.0,
 "num_threads": 10
}
[50]	valid's binary_logloss: 0.46381                              
[100]	valid's binary_logloss: 0.463772                            
[150]	valid's binary_logloss: 0.463802                            
[200]	valid's binary_logloss: 0.463861                            
混淆矩阵：                                                             
[[245408     59]                                                  
 [ 54431    102]]
feature importance:                                               
                                               column  importance 
0                 debug_trainWord2vec_cosine_distance         686
3            debug_trainVectorSpace_tfidfVecFeat_QSum         656
4            debug_trainVectorSpace_tfidfVecFeat_TSum         518
11  debug_trainVectorSpace_tfidfVecFeat_paired_man...         501
2              debug_trainWord2vec_cityblock_distance         476
1              debug_trainWord2vec_euclidean_distance         466
9   debug_trainVectorSpace_tfidfVecFeat_paired_cos...         452
10  debug_trainVectorSpace_tfidfVecFeat_paired_euc...         451
8            debug_trainVectorSpace_tfidfVecFeat_TLen         330
7            debug_trainVectorSpace_tfidfVecFeat_QLen         258
6           debug_trainVectorSpace_tfidfVecFeat_TMean           6
5           debug_trainVectorSpace_tfidfVecFeat_QMean           0
Valid Loss and AUC: 0.464092 0.601898                             
----->started 'cal valid qauc' block...                           
Valid QAUC: 0.573112                                              
----->finished 'cal valid qauc' block, time used:34.48s.          
----->started 'cal test qauc' block...                            
Test QAUC: 0.5688                                                 
----->finished 'cal test qauc' block, time used:45.98s.           
{                                                                 
 "bagging_fraction": 0.8,
 "bagging_freq": 0.0,
 "feature_fraction": 0.8,
 "lambda_l1": 0.7000000000000001,
 "lambda_l2": 6.0,
 "learning_rate": 0.11,
 "max_bin": 63,
 "min_data_in_leaf": 20.0,
 "min_gain_to_split": 0.30000000000000004,
 "num_iterations": 140.0,
 "num_leaves": 30.0,
 "num_threads": 10
}
[50]	valid's binary_logloss: 0.463806                             
[100]	valid's binary_logloss: 0.463716                            
混淆矩阵：                                                             
[[245421     46]                                                  
 [ 54447     86]]
feature importance:                                               
                                               column  importance 
0                 debug_trainWord2vec_cosine_distance         556
1              debug_trainWord2vec_euclidean_distance         453
8            debug_trainVectorSpace_tfidfVecFeat_TLen         430
3            debug_trainVectorSpace_tfidfVecFeat_QSum         416
9   debug_trainVectorSpace_tfidfVecFeat_paired_cos...         407
11  debug_trainVectorSpace_tfidfVecFeat_paired_man...         390
2              debug_trainWord2vec_cityblock_distance         367
10  debug_trainVectorSpace_tfidfVecFeat_paired_euc...         358
7            debug_trainVectorSpace_tfidfVecFeat_QLen         350
4            debug_trainVectorSpace_tfidfVecFeat_TSum         311
6           debug_trainVectorSpace_tfidfVecFeat_TMean          15
5           debug_trainVectorSpace_tfidfVecFeat_QMean           7
Valid Loss and AUC: 0.464271 0.602401                             
----->started 'cal valid qauc' block...                           
Valid QAUC: 0.574957                                              
----->finished 'cal valid qauc' block, time used:34.13s.          
----->started 'cal test qauc' block...                            
Test QAUC: 0.569886                                               
----->finished 'cal test qauc' block, time used:44.86s.           
100%|██████████| 5/5 [07:26<00:00, 88.68s/it, best loss: 0.464003]
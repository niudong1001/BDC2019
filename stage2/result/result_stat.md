
1. run_lgb_gbdt("len_editSim_ngramSim", eval_num=5)

- Valid Loss, AUC: 0.561971 0.568221
- Valid Q AUC: 0.5286228033320373

2. run_lgb_gbdt("len_editSim_ngramSim_word2vecAvgSim", eval_num=5)

- Valid Loss, AUC: 0.561212 0.573106  
- Valid Q AUC: 0.5326026719783656 

3. run_lgb_gbdt("len_editSim_ngramSim_word2vecAvgSim_word2vecTfidfSim", eval_num=5)

- Valid Loss, AUC: 0.56147 0.572649
- Valid Q AUC: 0.5324699129186086

4. run_lgb_gbdt("len_editSim_ngramSim_word2vecTfidfSim", eval_num=5)

- Valid Loss, AUC: 0.561442 0.572002
- Valid Q AUC: 0.5323624303334058

5. run_lgb_gbdt("len_editSim_ngramSim_word2vecTfidfSim_queryFreq", eval_num=5)

- Valid Loss, AUC: 0.534834 0.668866
- Valid Q AUC: 0.5351311980447957
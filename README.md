===============
*Requirements*
===============
1. Python2.7
2. Numpy
3. Pandas
4. joblib
5. sklearn
6. xgboost

==================
*File description*
==================

1. ensid = ensembl IDs.
2. mirna-list-id = List of mature miRNAs ID, mirbase id and mirTarBase ids.
3. xgb.py = Python script for predicting expression of mature miRNAs.
4. Gene_expression.txt = Example file for user given input[Two column file: First column has ensembl gene ID, second column has expression values for these gene IDs.]

./benchmarking

1. validation.py = Python script for benchmarking
2. validation.csv = Example file for benchmarking [Three column file: First column has miRNAs name, second column has Actual expression or expression came from expreimental data , third column has predicted expression or expression predicted by mirBiom tool.]
 
./xgb_all
[Warning: Following directory contain model files, kindly don't try to touch or modify these files]

==================
*Running script*
==================
To predict the expression of mature miRNAs, In parent directory execute following command:

python xgb.py Gene_expression.txt[User defined input]


To benchmark the output, execute following command in benchmark directory:

python validation.py validation.csv[User defined input]

==================
*Output description*
==================

Mature miRNAs expression prediction module (xgb.py) gives output in following format:

hsa-let-7a-2-3p[mature miRNAs ID] , 41.339638[Predicted expression value] , MI0000061[mirBase ID] , MIRT058253[mirTarBase ID]

Benchmarking script (validation.py) gives output in following format:

Root Mean Square Error (RMSE):  2.474966127090315 [RMS Error value]
Mean Absolute Percentage Error (MAPE):  6.079726698681235 [MAP Error value]
Accuracy(%):  93.92 [Accuracy value]


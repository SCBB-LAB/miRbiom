===============
*Requirements*
===============
1. Python2.7
2. Numpy
3. Pandas
4. joblib
5. sklearn
6. xgboost
7. Models for all 1,204 miRNAs, download it from https://scbb.ihbt.res.in/miRbiom-webserver/SC/Source_code_miRbiom-v-1.0.tar.gz (extract it into the parent folder)

==================
*File description*
==================

1. ensid = ensembl IDs.
2. mirna-list-id = List of mature miRNAs ID, mirbase id and mirTarBase ids.
3. xgb.py = Python script for predicting expression of mature miRNAs.
4. Gene_expression.txt = Example file for user given input[Two column file: First column has ensembl gene ID, second column has expression values for these gene IDs.]
5. example1.txt, example2.txt , example3.txt = Example files for user given input[Two column file: First column has ensembl gene ID, second column has expression values for these gene IDs.]


./benchmarking

1. validation.py = Python script for benchmarking
2. test.csv = Example file for benchmarking [Three column file: First column has miRNAs name, second column has Actual expression or expression came from expreimental data , third column has predicted expression or expression predicted by mirBiom tool.In this file example1.txt predicted and actual expression is used]
3. example1_miRNA_actual_expression.txt , example2_miRNA_actual_expression.txt, example3_miRNA_actual_expression.txt = Actual miRNA expression came from expreimental data for example1.txt , example2.txt , example3.txt respectively.


./xgb_all
[Warning: Following directory contain model files, kindly don't try to touch or modify these files]

==================
*Running script*
==================
To predict the expression of mature miRNAs, In parent directory execute following command:

python xgb.py example1.txt > example1_out.txt


To benchmark the output, execute following command in benchmark directory:
echo "miRNA,Predicted,Actual" >test.csv
awk '{print $1}' example1_out.txt |while read i; do printf "$i,";  grep -P "^$i " example1_out.txt |awk '{printf $3}'; grep -P "^$i\t" example1_miRNA_actual_expression.txt | awk '{printf ","$2}' ; echo "";done  |awk -F"," '{if(NF==3) print $0}' >>test.csv

python validation.py test.csv[User defined input]

==================
*Output description*
==================

Mature miRNAs expression prediction module (xgb.py) gives output in following format [ example1_out.txt]:

hsa-let-7a-2-3p[mature miRNAs ID] , 10.608787[Predicted expression value] , MI0000061[mirBase ID] , MIRT058253[mirTarBase ID]

Benchmarking script (validation.py) gives output in following format:

Root Mean Square Error (RMSE):  1.0670394705731083 [RMS Error value]
Mean Absolute Percentage Error (MAPE): 8.943718334276047 [MAP Error value]
Accuracy(%):  91.06 [Accuracy value]


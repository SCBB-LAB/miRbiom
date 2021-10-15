#!user/bin/python
import pandas as pd
import numpy as np
from joblib import load
#print 'miRNA',',','expression',',','miRBase-id'
expfile=sys.argv[1]
fin=open(expfile)
rows = ( line.rstrip("\n").split('\t') for line in fin )
d = { row[0].split('.')[0]:row[1] for row in rows }
ensem_id=open('ensid')
ensembl_gene_id=[line.rstrip("\n") for line in ensem_id ]
for key in ensembl_gene_id:
	if key not in d:
		d[key]=0	


mirnas=open('mirna-list-id')
mirna_list = [line.rstrip("\n") for line in mirnas ]
for mirna in mirna_list:
	associated_gene='xgb_all/'+mirna.split(",")[0]+'_gene_ense_feature_new'
	flist=open(associated_gene)
	gene_list = [line.rstrip("\n") for line in flist ]
	f=int(len(gene_list)*0.4)
	try:
		expression=[float(d[i]) for i in gene_list]
		expression1=[float(d[i]) for i in gene_list if float(d[i])>0]
		h=int(len(expression1))
		if h>=f:
			loaded_model = load(open('xgb_all/'+mirna.split(",")[0]+'_final_input_new.sav', 'rb'))
			exp=[0]+expression
			df = pd.DataFrame([exp])
			X = df.iloc[:,1:]
			y_load_predit=loaded_model.predict(X)
			c=math.log(float(y_load_predit[0]),2)
			if y_load_predit[0]>0:
				print mirna.split(",")[0],',',y_load_predit[0],',',mirna.split(",")[1],',',mirna.split(",")[2],',',c
		else:
			print("More than 60% genes have no expression")
	except:
		print("Not sufficient genes")


import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
from cmapPy.pandasGEXpress.parse import parse

#file_in
dir_in='/mnt/data1/fancong/fan_data/perturb_gene_expr/LINCS'
fn_query=f'{dir_in}/cp_coeff_mat.gctx'
fn_ref=f'{dir_in}/oe_coeff_mat.gctx'
fn_gene_list='./HCAR1_centered_gene_set.list'
ref_col='OEB006_A375_96H_H01_HCAR1'

#loading files
def read_list(fn1):
    pd1=pd.read_csv(fn1,header=None)
    list1=pd1.iloc[:,0].tolist()
    return(list1)
def read_gctx(fn1,list1): #list of focused genes
    gct1=parse(fn1)
    pd1=gct1.data_df
    list2=[x for x in pd1.index.tolist() if x in list1]
    pd2=pd1.loc[list2]
    return(pd2)

list_gene=read_list(fn_gene_list)
pd_ref=read_gctx(fn_ref,list_gene)
pd_query=read_gctx(fn_query,list_gene)

#calculate similarity
col_ref=pd_ref.loc[:,ref_col]*(-1)
dict_cos = {}
for col in pd_query.columns:
    col_query = pd_query.loc[:,col]
    similarity = 1 - cosine(col_ref, col_query)
    dict_cos[col]=similarity

#output res
fn_out = "./gene_expr_cos_simi.txt"
with open(fn_out, 'w') as fm:
    for key, value in dict_cos.items():
        fm.write(f"{key}\t{value}\n")

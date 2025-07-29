import pandas as pd

dir_tani='/mnt/data1/fancong/HCAR1_compete/compare_ligand'
dir_meta='/mnt/data1/fancong/HCAR1_compete/official_compound/Computational_Compound_Library'

def read_list(fn1):
    pd1=pd.read_csv(fn1,header=None,names=['N'],dtype={'N':str})
    list1=pd1.iloc[:,0]
    return(list1)

def proc_tani(n1): #max tanimoto score
    fn1_tani=f'{dir_tani}/plit_{n1}_res.tani'
    fn1_meta=f'{dir_meta}/split_{n1}.csv'
    pd1_tani=pd.read_csv(fn1_tani,sep='\t',header=None,usecols=[0,2],names=['Name','Score'])
    pd2_tani=pd1_tani.groupby('Name', as_index=False).agg(Score=('Score', 'max'))
    pd2_tani.query('Score>0.8',inplace=True)
    print(f'max tani score is \n{pd2_tani}')
    pd1_meta=pd.read_csv(fn1_meta,header=0)
    pd1_merge=pd.merge(pd2_tani,pd1_meta,left_on='Name',right_on='hit_id',how='inner')
    return(pd1_merge)

lst_N=read_list('./num.list')
pd_res=proc_tani(lst_N[0])
for i in range(1,len(lst_N)):
    n=lst_N[i]
    print(n)
    pd_i=proc_tani(n)
    pd_res=pd.concat([pd_res,pd_i])
pd_res.sort_values('Score',ascending=False,inplace=True)
pd_res=pd_res.iloc[0:100,:]
pd_res.to_csv('fan_results.csv')

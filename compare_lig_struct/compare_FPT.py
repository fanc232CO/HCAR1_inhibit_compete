import sys
import pandas as pd
import numpy as np
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem, MACCSkeys, RDKFingerprint, rdMolDescriptors
from rdkit.VLib.NodeLib.SmilesSupply import SmilesSupplyNode
from rdkit import DataStructs

#types of fingerprints
fpgen_topo=AllChem.GetRDKitFPGenerator()
fpgen_pair=AllChem.GetAtomPairGenerator()
fpgen_tors=AllChem.GetTopologicalTorsionGenerator()
fpgen_morg=AllChem.GetMorganGenerator(radius=2)
#input files
fn_refer='./active_small_molecules.smi'
dir_query='/mnt/data1/fancong/HCAR1_compete/official_compound/Computational_Compound_Library'
fn_query=sys.argv[1]
bn_query=fn_query.strip('.csv')
fn_out=f'{bn_query}_res.tani'
fn_query=f'{dir_query}/{fn_query}'

def file2fpt(fn1,sep_sign1,indx_name1,indx_smi1,indx_title1):
    suppl1 = SmilesSupplyNode(fn1,delim=sep_sign1,smilesColumn=indx_smi1,nameColumn=indx_name1,titleLine=indx_title1) #change this yourself!
    ms1=[x for x in suppl1 if x is not None]
    lst_mol_name=[x.GetProp('_Name') for x in ms1]
    fps_topo1=[fpgen_topo.GetSparseCountFingerprint(x) for x in ms1]
    fps_pair1=[fpgen_pair.GetSparseCountFingerprint(x) for x in ms1]
    fps_tors1=[fpgen_tors.GetSparseCountFingerprint(x) for x in ms1]
    fps_morg1=[fpgen_morg.GetSparseCountFingerprint(x) for x in ms1]
    return(lst_mol_name,fps_topo1,fps_pair1,fps_tors1,fps_morg1)

def compare_lig(indx1,indx2): #index of ligand, MUST be query and refer
    #lig1=query_mol_name[indx1]
    #lig2=refer_mol_name[indx2]
    score1=(DataStructs.TanimotoSimilarity(query_fps_topo[indx1],refer_fps_topo[indx2])+
        DataStructs.TanimotoSimilarity(query_fps_pair[indx1],refer_fps_pair[indx2])+
        DataStructs.TanimotoSimilarity(query_fps_tors[indx1],refer_fps_tors[indx2])+
        DataStructs.TanimotoSimilarity(query_fps_morg[indx1],refer_fps_morg[indx2]))/4
    score1=round(score1,3)
    #return(lig1,lig2,score1)
    return(score1)

#generate fingerprint
refer_mol_name,refer_fps_topo,refer_fps_pair,refer_fps_tors,refer_fps_morg=file2fpt(fn_refer,'\t',0,4,0)
query_mol_name,query_fps_topo,query_fps_pair,query_fps_tors,query_fps_morg=file2fpt(fn_query,',',0,1,0)
#calculate tanimoto
dict_tani={} #for example, dict_tani[0][5]=0.891
for indx_query in range(len(query_mol_name)):
    if indx_query not in dict_tani.keys():
        dict_tani[indx_query]={}
    for indx_refer in range(len(refer_mol_name)):
        tani_score=compare_lig(indx_query,indx_refer)
        dict_tani[indx_query][indx_refer]=tani_score
#output results
with open (fn_out,'w') as fm:
    for indx_query in dict_tani.keys():
        name_query=query_mol_name[indx_query]
        for indx_refer in dict_tani[indx_query].keys():
            name_refer=refer_mol_name[indx_refer]
            fm.write(f'{name_query}\t{name_refer}\t{dict_tani[indx_query][indx_refer]}\n')





    

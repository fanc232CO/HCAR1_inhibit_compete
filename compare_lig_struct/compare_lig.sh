#!/bin/bash
dir_query='/mnt/data1/fancong/HCAR1_compete/official_compound/Computational_Compound_Library'
fn_LINCS_meta='/mnt/data1/fancong/fan_data/perturb_gene_expr/LINCS/meta_info/LINCS_small_molecules.tsv'
#extract the SMILES of active seed molecules
head -n 1 $fn_LINCS_meta > active_small_molecules.smi
for i in $(sort ../compare_gene_expr/active_top100_BRD.list|uniq);do
	grep $i $fn_LINCS_meta >> ./active_small_molecules.smi 
done
#find potential HCAR1 inhibitors by structual similarity with the seed molecules
for i in $(cat ./fn_query.list);do
	{
		python ./compare_FPT.py "$i"
	} &
done
wait

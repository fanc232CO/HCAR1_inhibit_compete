#!/bin/bash
fn_meta='/mnt/work_fan/fan_database/perturb_DB/LINCS/LINCS_small_molecules.tsv'
fn_ID='../compare_gene_expr/active_top100_BRD.list'

awk -F'\t' 'NR==FNR{a[$1]=$1"\t"$5;next}{print a[$1]}' $fn_meta $fn_ID > ./active_small_molecules.smi

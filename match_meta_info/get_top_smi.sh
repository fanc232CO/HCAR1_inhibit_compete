#!/bin/bash
function get_top_smi {
	i1=$1
	bn1=lig${i1}
	fn1_tani=../compare_ligand/plit_${i1}_res.tani
	fn1_smi=../official_compound/Computational_Compound_Library/split_${i1}.csv
	awk '$3>0.8{print $1}' $fn1_tani|sort|uniq > ${bn1}_cut08.list
	for j1 in $(cat ${bn1}_cut08.list);do
		grep -w $j1 $fn1_smi|awk -F',' '{print $1, $2}' >> ./top_smi/${bn1}_cut08.smi
		#awk -F',' '$1==j{print $1, $2}' j=j1 $fn1_smi > ${bn1}_cut08.smi
	done
}

for n in $(cat ./num.list);do
	get_top_smi $n
done

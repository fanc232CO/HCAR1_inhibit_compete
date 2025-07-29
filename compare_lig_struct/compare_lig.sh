#!/bin/bash
dir_query='/mnt/data1/fancong/HCAR1_compete/official_compound/Computational_Compound_Library'
for i in $(cat ./fn_query.list);do
	{
		python ./compare_FPT.py "$i"
	} &
done
wait

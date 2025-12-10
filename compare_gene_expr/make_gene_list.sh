#!/bin/bash
fn_string='/home/fanc232/Downloads/string_interactions_short.tsv'
awk -F'\t' 'FNR>1{print $1}' $fn_string > fantemp
awk -F'\t' 'FNR>1{print $2}' $fn_string >> fantemp
sort fantemp|sort|uniq > gene_set.list

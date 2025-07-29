Below we list out the preparation needed for code running
1. database to download:
	In SigCom LINCS database (https://maayanlab.cloud/sigcom-lincs/#/Download), you need to download two dataset:
	(1) oe_coeff_mat.gctx--Normalized gene differential expression profile, perturbed by certain gene over-expression. This is needed to simulate the normalized gene differential expression profile in the condition of HCAR1 inhibition.
	(2) cp_coeff_mat.gctx--Normalized gene differential expression profile, perturbed by compound. These profile will be compared to the HCAR1 inhibition gene profile, to find out which compound would lead to the HCAR1 inhibition effect.
	(3) LINCS_small_molecules.tsv--Meta infomation of compound. This is used to extract the SMILES of small-molecular compound, for structure comparison with query small-molecules.

2. python module to install:
	(1) RDKit -- version 2025.03.4. used to calculate structual Tanimoto similarity between small-molecules.
	(2) cmapPy -- version 4.0.1. used to read the .gctx format of gene differential expression profile.
	(3) scipy -- used to calculate the cosine similarity between gene differential expression profiles.
	(4) pandas -- used to process meta information of small-molecules.

3. input files to prepare:
	(1) list of gene set, which consititute the gene co-effect network module, inside which HCAR1 perform a center-hub role. These genes are generated from STRING database (https://cn.string-db.org/)

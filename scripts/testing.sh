#!/bin/bash
working_dir=$(read -p "Please enter the full path to where felix_xxxx.pdf is stored, e.g. /Volumes/felix1/wherever/medianas/is/Current\ Issue ")
pdf_end=".pdf"
felix_start="felix_"
# Assert that only 1 file has name felix_xxxx.pdf
# store value of issue_number variable as that xxxx
issue_number=0
# create a new directory to store all issue pdfs
mkdir ../$issue_number
# create the pdfe prefixes.
pdfe_const="PDFE-E01-S2-$(date -v Fri +"%m%d")-0"
# run python to split up felix_xxxx.pdf 

# move all PDFE files
mv ../tests/files/PDFE* ../$issue_number
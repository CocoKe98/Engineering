import pandas as pd
import os
import sys

def excel_to_tsv(dir, excel_file):
    name = excel_file.split(".")[0]
    TSV_file = name + ".tsv"

    path = os.path.abspath(os.path.dirname(__file__)) + "/" + dir
    read_file = pd.read_excel (path + "/" + excel_file)
    read_file.to_csv (path + "/" + TSV_file, sep="\t", index = None, header=True)

if __name__ == '__main__':
    dir = "data"
    excel_file = "metadata.xlsx"
    
    excel_to_tsv(dir, excel_file)
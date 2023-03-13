#Required packages to install

#!pip install openpyxl
#!pip install odfpy
#!pip install xlrd

import pandas as pd 

continuingstudents = pd.read_excel("continuing.xlsx", index_col=0, sheet_name="continuing students")
freshmen = pd.read_excel("freshers.xlsx", index_col=0, sheet_name="freshers")



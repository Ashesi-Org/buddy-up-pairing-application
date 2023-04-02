#Required packages to install

#!pip install openpyxl
#!pip install odfpy
#!pip install xlrd

import pandas as pd 

continuingstudents = pd.read_excel("../controller/continuing.xlsx", index_col=0, sheet_name="continuing students")
freshmen = pd.read_excel("../controller/freshers.xlsx", index_col=0, sheet_name="freshers")

'''sorting dataframe such that continuing students who specified \\Any\\
come last, followed by those who specified \\Not country(s)\\
then at the top those who specified \\country(s)\\
'''
continuingstudents['Please indicate the preferred country/countries of your fresher buddy/buddies.'] = continuingstudents['Please indicate the preferred country/countries of your fresher buddy/buddies.'].replace(to_replace =['Any','Not'], value = ['zz','yy'], regex = True)
continuingstudents = continuingstudents.sort_values(by=['Please indicate the preferred country/countries of your fresher buddy/buddies.'])
continuingstudents['Please indicate the preferred country/countries of your fresher buddy/buddies.'] = continuingstudents['Please indicate the preferred country/countries of your fresher buddy/buddies.'].replace(to_replace =['zz','yy'], value = ['Any','Not'], regex = True)

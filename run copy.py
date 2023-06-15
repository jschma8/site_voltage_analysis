import pandas as pd   
from tqdm import tqdm
import os
import warnings
warnings.simplefilter("ignore")
import clean_final as cf




file_list =  os.listdir('files')

isFile = os.path.isfile('compiled.csv')

if isFile == True:
    out_df = pd.read_csv('compiled.csv')
    out_df.set_index('IP', drop=False, inplace=True)

else: 
    ip_list = pd.read_excel('Mother 2023.xlsx', sheet_name='Ops Scans')
    out_df = pd.DataFrame(ip_list['IP'].values, columns=['IP'], index=ip_list['IP'].values)
    del ip_list

for file in tqdm(file_list):
    filename = './files/' + file
    import_df = pd.read_excel(filename, sheet_name='Sheet0')
    column_name = import_df.at[1, 'Date (UTC+0:00)']

    if column_name not in out_df.columns:         
        df =pd.DataFrame(import_df['24-hour AVG Hashrate (RT)'].values, columns=[column_name], index=import_df['IP'])
        out_df = out_df.join(df)
        del df
    del filename
    del import_df 
    del column_name
    out_df.to_csv('compiled.csv', index=False)


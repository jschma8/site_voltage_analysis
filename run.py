import pandas as pd   
from tqdm import tqdm
import os




file_list =  os.listdir('files')

isFile = os.path.isfile('compiled.csv')

if isFile == True:
    out_df = pd.read_csv('compiled.csv')
else: 
    out_df= pd.DataFrame(columns=['IP', 'x0', 'x1', 'x2', 'x3'])


for file in file_list:

    df = pd.read_excel(file, sheet_name='Sheet0')
    column_name = df.at[1, 'Date (UTC+0:00)']

    if column_name not in out_df.columns:
        out_df[df.at[1, 'Date (UTC+0:00)']] = ''

        for i in tqdm(df.index):

            if df.at[i, 'IP'] not in out_df.values:
                list_data = ['' for column in out_df.columns]
                list_data[0] = df.at[i, 'IP']
                out_df.loc[len(out_df.index)] = list_data

            location = out_df.index[out_df['IP'] == df.at[i, 'IP']].to_list()
            out_df.at[location[0], df.at[1, 'Date (UTC+0:00)']] = df.at[i, '24-hour AVG Hashrate (RT)']
            x_list = df.at[i, 'IP'].split('.')
            out_df.at[location[0], 'x0'] = int(x_list[0])
            out_df.at[location[0], 'x1'] = int(x_list[1])
            out_df.at[location[0], 'x2'] = int(x_list[2])
            out_df.at[location[0], 'x3'] = int(x_list[3])
        del i
        del df
        del column_name
        del x_list
        res = input('next? ')
        out_df.sort_values(by=['x1', 'x2', 'x3'], inplace=True)
        out_df.drop(columns=['x0', 'x1', 'x2', 'x3'], inplace=True)
        out_df.to_csv('compiled.csv', index=False)

    


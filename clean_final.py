import pandas as pd
from tqdm import tqdm

def clean():
        df = pd.read_csv("compiled.csv")
        print(len(df))
        df.dropna(inplace=True)
        print(len(df))
        df.drop_duplicates(subset="IP", inplace=True)
        print(len(df))
        df['x0'] = ''
        df['x1'] = ''
        df['x2'] = ''
        df['x3'] = ''
        for i in tqdm(df.index):
                x_list = df.at[i, 'IP'].split('.')
                df.at[i, 'x0'] = int(x_list[0])
                df.at[i, 'x1'] = int(x_list[1])
                df.at[i, 'x2'] = int(x_list[2])
                df.at[i, 'x3'] = int(x_list[3])

        del x_list
        df.sort_values(by=['x1', 'x2', 'x3'], inplace=True)
        # print(df.head())
        df.to_csv('final.csv', index=False)

if __name__ == "__main__":
        clean()
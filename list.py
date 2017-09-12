import datetime
import glob
import pandas as pd

def get_retrieved_urls():
    alldf = pd.DataFrame()
    csv_files = glob.glob('data/posts/*.csv')
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        alldf = pd.concat([alldf,df], ignore_index=True)


    alldf.set_index('id')
    #print(alldf[['id','url']])
    #print(len(alldf['id'].unique()))
    return alldf

print(get_retrieved_urls())
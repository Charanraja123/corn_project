import os
import pandas as pd
import logging
logging.basicConfig(filename='corn.log',level=logging.DEBUG ,filemode='w+',format='%(levelname)s - %(message)s')


chunksize = 10 ** 4
iterator = 1
df_agg = pd.DataFrame()
for df_chunk in pd.read_csv('2017_cdqt_data.txt', delimiter = "\t", chunksize=chunksize):
    print(iterator)
    df_agg = df_agg.append(df_chunk)
    iterator = iterator + 1
    if iterator > 250 :
        break

for column in df_agg.columns:

    logging.info(f'{column} : {df_agg[column][1]}')
print(df_agg['CENSUS_TABLE'].nunique())

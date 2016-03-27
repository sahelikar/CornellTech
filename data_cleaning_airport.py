# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:28:54 2016

@author: sonatushi
"""

import pandas as pd
import json

datafile="C:\\Users\\sonatushi\\OneDrive for Business\\Cornell Tech\\airports.csv"
out_json_file ="C:\\Users\\sonatushi\\OneDrive for Business\\Cornell Tech\\airport_json.json"
 
airport_df = pd.read_csv(datafile, index_col=0, parse_dates=True)
country=pd.unique(airport_df['iso_country'].values.ravel())
airport_df['iso_region'] = airport_df['iso_region'].str.split('-').str.get(1)
table = pd.pivot_table(airport_df[airport_df['iso_country']=="US"], values='iso_country', index='iso_region', columns='type', aggfunc='count')

table=table.fillna(0)

aggregated_airport_tojson = table.to_json(orient='index')
d = json.loads(aggregated_airport_tojson)

airport_json=[{"AirportType": d[key], "Region": key} for key in d]

with open(out_json_file, 'w') as outfile:
    json.dump(airport_json, outfile)

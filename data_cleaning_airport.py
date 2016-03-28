# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:28:54 2016

@author: sonatushi
"""

import pandas as pd
import json

## initialization of varibles
datafile="airports.csv"
out_json_file ="airport_json.json"
 
## read Data file 
airport_df = pd.read_csv(datafile, index_col=0, parse_dates=True)

## Clean up the region column
airport_df['iso_region'] = airport_df['iso_region'].str.split('-').str.get(1)

## Get the 
table = pd.pivot_table(airport_df[airport_df['iso_country']=="US"], values='iso_country', index='iso_region', columns='type', aggfunc='count')

table=table.fillna(0)

## Convert to json format
aggregated_airport_tojson = table.to_json(orient='index')
d = json.loads(aggregated_airport_tojson)

airport_json=[{"AirportType": d[key], "Region": key} for key in d]


##Dump to a json file
with open(out_json_file, 'w') as outfile:
    json.dump(airport_json, outfile)

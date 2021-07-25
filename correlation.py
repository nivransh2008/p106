import pandas as pd 
import plotly.express as px 
import csv 
import numpy as np 

def  getdatasource(datapath):
    icecreamsales = [] 
    coldrinksales = []
    with open(datapath) as f: 
        df = csv.DictReader(f) 
        for i in df : 
            icecreamsales.append(float(i["Size of TV"]))
            coldrinksales.append(float(i["	Average time spent watching TV in a week (hours)"])) 
    return {"x":icecreamsales, "y":coldrinksales} 

def findcorrelation (datasource) : 
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation[0,1])

def setup():
    datapath = "./data-3.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource) 

setup() 
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:37:44 2022

@author: HIDRAULICA-Dani
"""

import os
import pandas as pd
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

os.chdir("D:/DANI/2021/TEMA4_PRONOSTICOS/DATOS/")
os.listdir()

#lista de estaciones a extraer
est = pd.read_csv("D:/DANI/2021/TEMA4_PRONOSTICOS/GIS/Tables/EstacionesId.csv")
# est = est.drop(['FID'], axis=1)
est = list(est['Name'])
est.sort()

#Extraer datos de estaciones de html a csv
for id in est:
    url = "https://smn.conagua.gob.mx/tools/RESOURCES/Diarios/"+str(id)+".txt"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()
    text = text.replace(',', '')

    f = open("D:/DANI/2021/TEMA4_PRONOSTICOS/DATOS/CNA/"+str(id)+".csv", "w", encoding="latin-1")
    f.write(text)
    f.close()


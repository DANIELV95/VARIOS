# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:35:29 2021

@author: HIDRAULICA-DANI
"""

import os
import glob

#Set cwd
os.chdir("D:/DANI/2021/TEMA4_PRONOSTICOS/DATOS/PERSIANN/ASCII_proj")

#List files
list = glob.glob("*.asc")

# Generate control file
# Set PATH=C:/hecexe/; %PATH%
# asc2DSSGrid INPUT=input.asc DSS=output.dss PATH=/reference_system/location_or_provider/parameter/start_time/end_time/data_version GRIDTYPE=UTM ZONE=14N DUNITS=mm DTYPE=PER-CUM
# e.g. PATH=/UTM14/Mexico/Precip/01MAR2000:0000/01MAR2000:2400/PROJECTED/

#ERA5
f = open('asc2dssGrid.bat','w')
f.write('Set PATH=C:/hecexe/; %PATH%\n')
for file in list:
    f.write('asc2DSSGrid INPUT='+file+' DSS=Persiann.dss PATH=/UTM14/Mexico/Precip/'+file[11:13]+'MAR2000:0000/'+file[11:13]+'MAR2000:2400/PROJECTED/ GRIDTYPE=UTM ZONE=14N DUNITS=mm DTYPE=PER-CUM \n')
f.close()

#PERSIANN
f = open('asc2dssGrid.bat','w')
f.write('Set PATH=C:/hecexe/; %PATH%\n')
for file in list:
    f.write('asc2DSSGrid INPUT='+file+' DSS=Persiann.dss PATH=/UTM14/Mexico/Precip/'+file[11:13]+'MAR2000:0000/'+file[11:13]+'MAR2000:2400/PROJECTED/ GRIDTYPE=UTM ZONE=14N DUNITS=mm DTYPE=PER-CUM \n')
f.close()



# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:32:40 2021

@author: HIDRAULICA-Dani
"""

import os
import datetime as dt
from dateutil.rrule import *
from ecmwfapi import ECMWFDataServer

os.chdir("D:/DANI/2021/TEMA4_PRONOSTICOS/DATOS/ECMWF/")
# os.listdir()

rtf_dates = list(rrule(WEEKLY, byweekday=[MO,TH], dtstart=dt.datetime(2019,12,31), until=dt.datetime(2020,12,31)))
# rtf_dates_MO = list(rrule(WEEKLY, byweekday=[MO], dtstart=dt.datetime(2019,12,29), until=dt.datetime(2020,12,31)))
# rtf_dates_TH = list(rrule(WEEKLY, byweekday=[TH], dtstart=dt.datetime(2019,12,29), until=dt.datetime(2020,12,31)))
# str(rtf_dates[0])[0:4]
# rtf_dates

server = ECMWFDataServer()
f = open('errors_log.txt', 'w')

for rtf_day in rtf_dates:
    date = str(rtf_day)[:10]
    ref_date = list(rrule(YEARLY, dtstart=dt.datetime(rtf_day.year-20,rtf_day.month,rtf_day.day), until=dt.datetime(rtf_day.year-1,rtf_day.month,rtf_day.day)))
#     print(rtf_day, ref_date[-1], ref_date[0], len(ref_date))
    hdates = str([str(i)[:10] for i in ref_date])
    hdates = hdates.replace('[','')
    hdates = hdates.replace(']','')
    hdates = hdates.replace("'","")
    hdates = hdates.replace(', ','/')
    print(rtf_day)
    

#!/usr/bin/env python
    try:
        server.retrieve({
            "class": "s2",
            "dataset": "s2s",
            "date": date,
            "expver": "prod",
            "hdate": hdates,
            "levtype": "sfc",
            "model": "glob",
            "number": "1/2/3/4/5/6/7/8/9/10",
            "origin": "ecmf",
            "param": "228228", #tp
            "step": "0/to/480/by/6",
            "area": "27/-102/24/-99", #N/W/S/E
            "grid": "0.25/0.25",
            "stream": "enfh",
            "time": "00:00:00",
            "type": "pf",
            "target": "param_228228_"+date+".grib",
        })
    except:
        f.write('1 '+date)
        print(1, date)
        pass
    try:
        server.retrieve({
            "class": "s2",
            "dataset": "s2s",
            "date": date,
            "expver": "prod",
            "hdate": hdates,
            "levtype": "sfc",
            "model": "glob",
            "number": "1/2/3/4/5/6/7/8/9/10",
            "origin": "ecmf",
            "param": "165/166", #wu, wv
            "step": "0/to/480/by/24",
            "area": "27/-102/24/-99", #N/W/S/E
            "grid": "0.25/0.25",
            "stream": "enfh",
            "time": "00:00:00",
            "type": "pf",
            "target": "param_165-166_"+date+".grib",
        })
    except:
        f.write('2 '+date)
        print(2, date)
        pass
    try:
        server.retrieve({
            "class": "s2",
            "dataset": "s2s",
            "date": date,
            "expver": "prod",
            "hdate": hdates,
            "levtype": "sfc",
            "model": "glob",
            "number": "1/2/3/4/5/6/7/8/9/10",
            "origin": "ecmf",
            "param": "169/175", #ssrd, strd
            "step": "0/to/480/by/24",
            "area": "27/-102/24/-99",
            "grid": "0.25/0.25",
            "stream": "enfh",
            "time": "00:00:00",
            "type": "pf",
            "target": "param_169-175_"+date+".grib",
        })
    except:
        f.write('3 '+date)
        print(3, date)
        pass
    try:
        server.retrieve({
            "class": "s2",
            "dataset": "s2s",
            "date": date,
            "expver": "prod",
            "hdate": hdates,
            "levelist": "10",
            "levtype": "pl",
            "model": "glob",
            "number": "1/2/3/4/5/6/7/8/9/10",
            "origin": "ecmf",
            "param": "130", #T
            "step": "0/to/480/by/24",
            "area": "27/-102/24/-99",
            "grid": "0.25/0.25",
            "stream": "enfh",
            "time": "00:00:00",
            "type": "pf",
            "target": "param_130_"+date+".grib",
        })
    except:
        f.write('4 '+date)
        print(4, date)
        pass

f.close()
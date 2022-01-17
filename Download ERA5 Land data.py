# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:33:57 2021

@author: HIDRAULICA-DANI
"""

import os
import cdsapi

os.chdir('D:/DANI/2021/TEMA4_PRONOSTICOS/DATOS/ERA5/ERA5_Land/ERA5_Land_All')

start = 1950
end = 2021

for i in range(start, end+1):
    year = str(i)
    print(year)
    
    if not os.path.exists('./precip_era5_land_'+year+'.nc'):

        c = cdsapi.Client()
        
        c.retrieve(
            'reanalysis-era5-land',
            {
                'variable': [
                    '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
                    '2m_temperature', 'potential_evaporation', 'runoff',
                    'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards', 'total_evaporation',
                    'total_precipitation',
                ],
                'year': year,
                'month': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                ],
                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'time': [
                    '00:00', '01:00', '02:00',
                    '03:00', '04:00', '05:00',
                    '06:00', '07:00', '08:00',
                    '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00',
                    '15:00', '16:00', '17:00',
                    '18:00', '19:00', '20:00',
                    '21:00', '22:00', '23:00',
                ],
                'area': [
                    26, -101, 25,
                    -100,
                ],
                'format': 'netcdf',
            },
            './precip_era5_land_'+year+'.nc')


# 'year': [str(i) for i in range(start,end+1)]
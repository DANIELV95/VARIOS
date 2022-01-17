list = os.listdir("D:/DANI/2021/TEMA4_PRONOSTICOS/DATOS/DEM/DTM/MT_Grid/")
for file in list:
    root_name = "D:/DANI/2021/TEMA4_PRONOSTICOS/DATOS/DEM/DTM/MT_Grid/"+file+"/"+file+"/"
    raster_file= root_name+"hdr.adf"
    iface.addRasterLayer(raster_file, file)
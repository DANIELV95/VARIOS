library(raster)
getwd()
setwd('D:/DANI/2021/TEMA4_PRONOSTICOS/')

#open your raster with n bands
r<-stack('./GIS/Raster/t2m.tif')
#Plot it just to see if everything is ok
plot(r)
#Check the number of bands
nlayers(r)
for(i in 1:nlayers(r)){
  band<-r[[i]]
  #save raster in a separate file
  writeRaster(band,paste('./PYR/ERA5_ASC/band',i,'.asc', sep=''))
}
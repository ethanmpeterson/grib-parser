import pygrib, json, numpy

grb = pygrib.open('output.grib2')

print(grb.message(1))
keys = grb.message(1).keys()
for i in keys:
   print(i)
   pass
message = grb.message(1)
#print(message.shortName)
#print(message.name)
#print(message.maximum)
#print(message.numberOfSection)
#print(message.numberOfValues)
#print(message.sectionNumber)
#print(len(message.latitudes))
#print(len(message.longitudes))

data = {}


exit()

import pygrib, json, numpy

grb = pygrib.open('gfs.t18z.pgrb2.0p25.f008.UGRD')

print(grb.message(1))
keys = grb.message(1).keys()
for i in keys:
   #print(i)
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

data = {
    'count' : message.numberOfValues,
    'positions' : [{
        'latitude' : 0,
        'longitude' : 0,
    }],
    'velocities' : [{
        
    }],
}

for i in range(0, message.numberOfValues):
    break

print(data)
exit()

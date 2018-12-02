import pygrib, json, numpy

grb = pygrib.open('gfs.t18z.pgrb2.0p25.f008.VGRD')

print(grb.message(1))
keys = grb.message(1).keys()
for i in keys:
   print(i)
   pass
message = grb.message(1)
print(message.name)
print(message.units)
print(message.codedValues)
#print(message.name)
print(message.minimum)
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
    'velocities' : [],
}



print(data)
exit()

import pygrib, json, numpy

dirFile = pygrib.open('gfs.t18z.pgrb2.0p25.f008.VGRD')
vFile = pygrib.open('gfs.t18z.pgrb2.0p25.f008.UGRD')

vMessage = vFile.message(1)
dirMessage = dirFile.message(1)

data = {
	'count' : dirMessage.numberOfValues,
	'data' : [{
		'latitude' : 0,
		'longitude' : 0,
		'direction' : 0,
		'velocity' : 0,
	}],
	'units' : {
		'velocity' : vMessage.units,
		'direction' : dirMessage.units,
	},
}

lats = dirMessage.latitudes
lons = dirMessage.longitudes

dirn = dirMessage.codedValues

velocities = vMessage.codedValues

for i in range(0, data['count']):
	val = {
		'latitude' : lats[i],
		'longitiude' : lons[i],
		'direction' : dirn[i],
		'velocity' : velocities[i],
	}
	data['data'].append(val.copy())

#json = json.dumps(data)
with open('output.json', 'w') as outfile:  
    json.dump(data, outfile)
exit()

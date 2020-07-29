# Converting coordinates to geographical locations

# pip install geopy

from geopy import Nominatim

lat = float(input('Enter lattitude : '))
lon = float(input('Enter longitude : '))

coord = (lat,lon)
# [Example] coord = (26.8393,80.9231)


try:
	geolocator = Nominatim(user_agent='test/1')
	location = geolocator.reverse(f'{coord[0]},{coord[1]}')
	print('Based on entered coordinates, the location is :',location.address)
except:
	print('looks like you are not connected with internet')
	print('or given coordinates may be wrong')
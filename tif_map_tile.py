import math


def deg2num(lat_deg, lon_deg, zoom):
	lat_rad = math.radians(lat_deg)
	n = 2.0 ** zoom
	xtile = int((lon_deg + 180.0) / 360.0 * n)
	ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
	return xtile, ytile


def num2deg(xtile, ytile, zoom):
	n = 2.0 ** zoom
	lon_deg = xtile / n * 360.0 - 180.0
	lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
	lat_deg = math.degrees(lat_rad)
	return (lat_deg, lon_deg)


origin_x, origin_y = deg2num(29.267232865200878, -95.4547119140625, 16)
# 30.095599, -95.890865
#-29.267232865200878, -95.4547119140625


def printCoords(height, width, style, username, folder):
	params = []

	for row in range(height):
		for col in range(width):
			params.append((origin_x + row, origin_y+col))

	token = 'pk.eyJ1IjoiZGVyZWtsaTIwMTEiLCJhIjoiY2syaTJyYXU5MGcyNzNobnRncW96OGFrYyJ9.94Wh5W0Soz-6NXB6Iz5cjQ'
	template = 'curl "https://api.mapbox.com/styles/v1/{0:}/{1:}/tiles/16/{2:}/{3:}?access_token={4:}" -o {6:}/{5:}.jpg'

	for x, y in params:
		degx,degy = num2deg(x,y,16)
		new_x,new_y = deg2num(-degx,degy,16)
		print(template.format(username, style, x, y, token, str(16) + '_' + str(new_x) + '_' + str(new_y), folder))

# mapbox://styles/derekli2011/ck2i557xm2m2v1cteqwipj0pt
# ck2i4otr92bho1cpegfiufjhc
# pk.eyJ1IjoiZGVyZWtsaTIwMTEiLCJhIjoiY2syaTVidndqMGdrOTNqbnRhamsza2xxcSJ9.JFWGvAcqn60CDOW8Y_mToQ
# pk.eyJ1IjoiZGVyZWtsaTIwMTEiLCJhIjoiY2syaTJyYXU5MGcyNzNobnRncW96OGFrYyJ9.94Wh5W0Soz-6NXB6Iz5cjQ
# printCoords(3,3, "satellite-v9", "mapbox", "satellite")
# 38344-385


def run(sat):
	if sat:
		printCoords(203, 98, "satellite-v9", "mapbox", "satellite")
	else:
		printCoords(203, 98, "ck2i4otr92bho1cpegfiufjhc", "derekli2011", "roads")


run(not True)

# 38344-38380
# 15391-15392

contours = '5,10,15'

addrs = {
    'lincoln_park': "-123.109495,45.527719",
    'talisman_city_park': "-123.126243,45.528791",
    'thatcher_city_park': "-123.134358,45.535558",
    'joseph_gale': "-123.093986,45.516187",
    'bard_park': "-123.095529,45.522748",
    'Rogers_park': "-123.103958,45.516644",
    'Harlemen_park': "-123.062675,45.513251",
    'Tarrybrooke_park': "-123.067173,45.515927",
    'stites_city_park': "-123.117109,45.527630",
    'hazel_sills_park': "-123.119122,45.531580",
    'roth_family_park': "-123.140526,45.527797",
}

with open('fetch.sh', 'w') as f:
    for place, latlng in addrs.items():
        f.write(f"curl 'https://api.mapbox.com/isochrone/v1/mapbox/walking/{latlng}?contours_minutes={contours}&contours_colors=6706ce,04e813,4286f4&polygons=true&access_token=pk.eyJ1Ijoia3Bpc2hkYWRpYW4iLCJhIjoiY2pvMTVzN2lwMDdrbTNrcG9mb2RvcDF5aSJ9.wbFcMArvH5wSmVwvRomNmg' > data/{place}.geojson\n")

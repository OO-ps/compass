import overpass


def get_ways(origin, dest):
    lats = [origin['lat'], dest['lat']]
    lngs = [origin['lng'], dest['lng']]
    bounds = [min(lats), min(lngs), max(lats), max(lngs)]
    query = overpass.MapQuery(*[round(x, 3) for x in bounds])
    res = overpass.API().Get(query)
    ways = []
    for x in res['features']:
        if "highway" in x['properties'] \
                and x['geometry']['type'] == "LineString":
            ways.append(x)
    return ways

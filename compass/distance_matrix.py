import requests

api_url = "https://maps.googleapis.com/maps/api/distancematrix/"
params = "json?origins={origins_param}&destinations={dests_param}&key={key}"
key = "AIzaSyC6rh33flbFuQUaKgU4uOP7u9SkSPO-AKU"


def get_distance_matrix(origins, dests):
    origins = [str(o[0]) + ',' + str(o[1]) for o in origins]
    dests = [str(d[0]) + ',' + str(d[1]) for d in dests]
    origins_param = '|'.join(origins)
    dests_param = '|'.join(dests)
    req_url = api_url + params.format(origins_param=origins_param,
                                      dests_param=dests_param,
                                      key=key)
    req_get = requests.get(req_url).json()
    row_elements = [x['elements'] for x in req_get['rows']]
    dist_mat = []
    for r in row_elements:
        row = []
        for d in r:
            row.append(d['distance']['value'] + d['duration']['value'])
        dist_mat.append(row)
    return dist_mat

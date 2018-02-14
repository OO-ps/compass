import requests

api_url = "https://maps.googleapis.com/maps/api/geocode/"
params = "json?address={address}&key={key}"
key = "AIzaSyC6rh33flbFuQUaKgU4uOP7u9SkSPO-AKU"


def get_latlong(address_list):
    return_list = []
    for address in address_list:
        result = requests.get(api_url + params.format(address=address, key=key))
        return_list.append(result.json()['results'][0]['geometry']['location'])
    return return_list

from geocoder import get_latlong

origin = input("Please enter your current location: ")
dest = input("Please enter destination: ")
address_list = [origin, dest]
print(get_latlong(address_list))

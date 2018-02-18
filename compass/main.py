from geocoder import get_latlong
from ways import get_ways
from a_star import get_waypoints
from plot import plot_on_map
import webbrowser

origin = input("Please enter your current location: ")
dest = input("Please enter destination: ")
address_list = [origin, dest]
coords = get_latlong(address_list)
print(coords)
way_pts = get_waypoints(get_ways(*coords), *coords)
plot_on_map(way_pts)
webbrowser.open("map.html")

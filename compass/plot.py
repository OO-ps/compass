import gmplot


def plot_on_map(way_pts):
    var1 = [x[0] for x in way_pts]
    var2 = [x[1] for x in way_pts]
    gmap = gmplot.GoogleMapPlotter(var1[0], var2[0], 15, '')
    gmap.scatter(var1, var2, 'k')
    gmap.plot(var1, var2, "cornflowerblue", edge_width=5)
    gmap.draw('map.html')

from geopy.distance import great_circle
from distance_matrix import get_distance_matrix


def get_waypoints(ways, orig, dest):
    all_pts, all_ways = get_all_pts_and_ways(ways)
    orig_pt, dest_pt = (orig['lat'], orig['lng']), (dest['lat'], dest['lng'])
    way_pts = [orig_pt, get_closet_pt_on_rd(orig_pt, all_pts)]
    rem_dist = min_dist = float("inf")
    while rem_dist > 100:
        if min_dist > rem_dist:
            min_dist = rem_dist
        knn = get_knn(orig_pt, all_pts.keys())
        knn = [k for k in knn if k != ()]
        if not knn and len(all_pts) > 1:
            way_pts.append(dest_pt)
            return way_pts
        orig_to_knn = get_distance_matrix([orig_pt], knn)[0]
        knn_to_dest_hue = get_heu_for_pts(knn, dest_pt)
        cost = [orig_to_knn[i] + knn_to_dest_hue[i] for i in
                range(len(orig_to_knn))]
        nxt_pt = knn[cost.index(min(cost))]
        print("next_pt= ", nxt_pt)
        if great_circle(nxt_pt, dest_pt).meters > 2 * min_dist:
            if orig_pt in knn:
                knn.remove(orig_pt)
            for k in knn:
                all_pts.pop(k)
            continue
        way_pts.append(nxt_pt)
        all_pts.pop(orig_pt, None)
        orig_pt = nxt_pt
        print("way_pts=", way_pts)
        rem_dist = great_circle(orig_pt, dest_pt).meters
        print("rem_dist= ", rem_dist)
    way_pts.append(dest_pt)
    return way_pts


def get_all_pts_and_ways(ways):
    all_pts = {}
    all_ways = {}
    for way in ways:
        way_id = way['id']
        all_ways[way_id] = []
        for poly_line in [way['geometry']['coordinates']]:
            for point in poly_line:
                p = tuple([point[1], point[0]])
                if p not in all_pts:
                    all_pts[p] = [way_id]
                else:
                    all_pts[p].append(way_id)
                all_ways[way_id].append(p)
    return all_pts, all_ways


def get_closet_pt_on_rd(orig_pt, all_pts):
    knn = get_knn(orig_pt, all_pts.keys())
    knn = [k for k in knn if k != ()]
    if not knn:
        return orig_pt
    cost = get_distance_matrix([orig_pt], knn)[0]
    return knn[cost.index(min(cost))]


def get_knn(pt, all_pts, params=None):
    if params is None:
        params = {'k': 3, "min_dist": 10}
    knn = [(float("inf"), ()) for x in range(0, params['k'])]
    for x in all_pts:
        for i in range(0, params['k']):
            dist = great_circle(pt, x).meters
            if knn[i][0] > dist >= params['min_dist']:
                knn.pop()
                knn.append((dist, x))
                knn = sorted(knn)
                break
    return [x[1] for x in knn]


def get_heu_for_pts(pts, dest_pt):
    heuristics = []
    for pt in pts:
        heuristics.append(great_circle(pt, dest_pt).meters)
    return heuristics

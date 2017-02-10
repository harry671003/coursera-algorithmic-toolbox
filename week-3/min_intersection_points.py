"""Minimum points that touches all segments"""

def min_points(segments):
    """Min Points"""
    # Sort the points by increasing order of end point
    sorted_segments = sorted(segments, key=lambda x: x[1])

    print(sorted_segments)
    return_value = {
        "count": 0,
        "points": []
    }

    last_point = None
    for segment in sorted_segments:
        if last_point is None or segment[0] > last_point:
            last_point = segment[1]
            return_value["count"] += 1
            return_value["points"].append(last_point)

    return return_value

def test():
    """Test function """
    # segments = [
    #     (4, 7),
    #     (1, 3),
    #     (2, 5),
    #     (5, 6)
    # ]

    segments = [
        (-1, 0),
        (-1, 2),
        (-1, 3),
        (-1, 4),
        (-1, 10),
        (-1, 9),
        (-1, 12)
    ]

    print(min_points(segments))


def print_sep():
    """Print Seperator"""
    print("")

if __name__ == "__main__":
    test()

"""Min Groups Module"""

def min_groups(points, max_segment_length):
    """Minimum Groups

    Divides a set of points of segments of MaxSegmentLength
    returns the count of minimum groups
    Uses Greedy Approach
    """
    group_count = 0 # the count of groups
    segments = [] # The map of segments

    cur_segment = False # The starting value of cur_segment

    for point in points:
        # Check if the point 'p' belong to the current segment
        if not cur_segment or point > cur_segment:
            # 'p' doesn't belong to current segment
            # Create a new segment with 'p' in it
            cur_segment = point + max_segment_length
            segments.append([point])
            group_count += 1

        else:
            # 'p' belongs to current segment
            # Add p to the current segment
            segments[group_count - 1].append(point)

    return {
        "segments"      : segments,
        "group_count"   : group_count
    }

def test():
    """Test function """
    test_points = [
        [0.5, 0.6, 0.7, 1, 1.2, 2, 2.8, 3.4, 5, 6, 6.9],
        [0.5],
        []
    ]
    max_segment_length = 1

    print_sep()
    
    groups = min_groups(test_points[0], max_segment_length)
    print(groups)
    print_sep()

    groups = min_groups(test_points[1], max_segment_length)
    print(groups)
    print_sep()

    groups = min_groups(test_points[2], max_segment_length)
    print(groups)
    print_sep()

def print_sep():
    """Print Seperator"""
    print("")

if __name__ == "__main__":
    test()

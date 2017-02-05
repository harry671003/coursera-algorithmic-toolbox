# Min Refills
# 
# Calculates the minimum refills required
# map   - Map of petrol bunks and their distance from O
# L     - fuel tank capacity of the car measured in 
#         amount of distance it can go once full
# Returns minimum refills required or -1 if impossible 
def min_refills(map, L):
    # Few assertions
    assert(L > 0)
    assert(len(map) > 0)

    cur_stop        = 0
    refill_count    = 0
    refills         = []
    last_refill     = 0

    # the max_distance the car can go with
    max_distance = map[cur_stop] + L
    print("max_distance: %d" %(max_distance, ))
    
    while cur_stop < len(map) - 1:
        print ("cur_stop: %d | next: %d | fuel_left: %d" % (map[cur_stop], map[cur_stop + 1], max_distance) )

        # Check if the car can move to the next stop
        if ( map[cur_stop] + max_distance >= map[cur_stop + 1] ):
            # Reduce the max_distance by the amount of movement
            max_distance = max_distance - ( map[cur_stop + 1] - map[cur_stop] )
            cur_stop = cur_stop + 1
        
        elif cur_stop == last_refill:
            # We are not able to progress beyond the current stop
            # This is an impossible map
            return -1
        else:
            # Do a refill
            max_distance = L
            refill_count = refill_count + 1
            last_refill = cur_stop
            refills.append(map[cur_stop])
            

            print ("refilling @ %d " % (cur_stop,) )
            print (refills)


    print(refills)
    return refill_count

if __name__ == "__main__":
    map = [0, 100, 220, 340, 500, 650, 750, 800, 1000]
    L = 250
    refills = min_refills(map, L)
    print ("min_refills: %d" % (refills, ))
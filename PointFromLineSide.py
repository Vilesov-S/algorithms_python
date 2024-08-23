
def point_from_segment_side(segment_coord, point_coord):
    ax = segment_coord[0][0]
    ay = segment_coord[0][1]
    bx = segment_coord[1][0]
    by = segment_coord[1][1]
    px = point_coord[0]
    py = point_coord[1]
    
    sign = round((by - ay)*(px - ax) - (bx - ax)*(py - ay), 5)
    
    if sign > 0:
        return 1
    elif sign < 0:
        return -1
    else:
        return 0


def main():
    print(point_from_segment_side([(5, 5), (5, -5)], (5, 1)))   # 0
    print(point_from_segment_side([(5, 5), (5, -5)], (5, -1)))  # 0
    print(point_from_segment_side([(5, 5), (5, -5)], (-5, -2))) # 1
    print(point_from_segment_side([(5, 5), (5, -5)], (15, -2))) # -1

if __name__ == "__main__":
    main()

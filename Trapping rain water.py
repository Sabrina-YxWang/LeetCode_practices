#Yingxuan Wang
#Trapping rain water

def TRW(elevation):
    #you can trap any water if there's less than 3 pillar
    if len(elevation) < 3 or len(elevation) == 0:
        return 0
    
    res = 0
    height = len(elevation)
    left_max = []
    left_max.append(elevation[0])
    
    for i in range(1, height):
        left_max.append(max(elevation[i], left_max[i-1]))
    
    right = []
    right.append(elevation[height-1])
    for i in range(1, 12):
        right.append(int(0))
    right_max = []
    for i in range(11, -1, -1):
        right_max.append(right[i])
    
    for i in range(height-2, 0, -1):
        right_max[i] = (max(elevation[i], right_max[i+1]))
        
    for i in range(1, len(elevation)):
        res += min(left_max[i], right_max[i]) - elevation[i]
        
    return res
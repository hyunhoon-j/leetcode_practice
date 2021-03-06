def trap(height):
    if not height:
        return 0
    
    volume = 0 # This is the amount of water
    
    left = 0 # Index from left
    right = len(height) - 1 # In here, variable 'right' is an index
    
    left_max = height[left] # This is an actual element in the list
    right_max = height[right] # This is also an actual element in the list

    while left < right: # If two pointers meet, this program would end
        left_max = max(height[left], left_max) # This is to get the max element in the list from left to right
        right_max = max(height[right], right_max) # This is to get the max element in the list from right to left

        if left_max <= right_max:
            volume = volume + left_max - height[left]
            left = left + 1
        else:
            volume = volume + right_max - height[right]
            right = right - 1

    return volume

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

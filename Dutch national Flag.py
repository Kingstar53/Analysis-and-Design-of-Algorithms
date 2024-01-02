def dutch_national_flag(arr):
    low = 0      # Pointer for 0s
    high = len(arr) - 1  # Pointer for 2s
    i = 0        # Current index
    
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            i += 1
        elif arr[i] == 2:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
        else:
            i += 1

# Example usage:
arr = [2, 0, 1, 2, 1, 0]
dutch_national_flag(arr)
print(arr)

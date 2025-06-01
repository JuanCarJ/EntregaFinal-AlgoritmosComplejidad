def quicksort(unsorted):
        if len(unsorted) <= 1:
            return unsorted
        else:
            puntoMedio = unsorted[len(unsorted) // 2]
            menores = [num for num in unsorted if num < puntoMedio]
            iguales = [num for num in unsorted if num == puntoMedio]
            mayores = [num for num in unsorted if num > puntoMedio]
            return quicksort(menores) + iguales + quicksort(mayores)
def removeElement(nums, val):
        nums[:] = quicksort(nums)  
        k = 0  
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  
                k += 1
        return k  
# Example usage:
nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print(k) 

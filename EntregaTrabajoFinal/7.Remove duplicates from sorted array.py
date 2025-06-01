
def removeDuplicates(nums):
        Size = len(nums)  
        if Size == 0:
            return 0
        k = 1  
        i = 1  
        while i < Size:
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
            i += 1 
        LastSize = k  
        RayitasPendientes = Size - LastSize  
        for j in range(RayitasPendientes):
            nums.append("_")
        return LastSize  
nums = [1, 1, 2, 3, 3]
result = removeDuplicates(nums)
print("Len del array antes de remover", result)
print("Len del array antes de remover", nums[:result])  
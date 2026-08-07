class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-2
        curr_max = arr[-1]
        prev_max = arr[-1]
        arr[-1] = -1
        while i >= 0:
            if arr[i] > curr_max:
                prev_max = curr_max 
                curr_max = arr[i]
                arr[i] = prev_max
            else:
                arr[i] = curr_max
            i -= 1
        return arr
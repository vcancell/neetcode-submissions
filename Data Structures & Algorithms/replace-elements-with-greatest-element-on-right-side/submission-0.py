class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.append(-1)
        curr = -1
        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = max(arr[i + 1], curr)
            curr = temp
        arr.pop()
        return arr
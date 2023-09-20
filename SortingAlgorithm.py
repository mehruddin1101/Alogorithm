class SortingAlgorithm:
    # insertion sort
    def insertionSort(self, arr):
        for j in range(1, len(arr)):  # Start from index 1
            key = arr[j]
            i = j - 1
            while i >= 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i -= 1
            arr[i + 1] = key
        return arr

    # merge sort 
    def MergeSort(self, a, left, right):
        if left < right:
            mid = (left + right) // 2
            self.MergeSort(a, left, mid)
            self.MergeSort(a, mid + 1, right)
            self.merge(a, left, mid, right)
            
    # two way merging 
    def merge(self, a, left, mid, right):
        temp1, temp2 = [], []
        ans = []
        for i in range(left, mid + 1):
            temp1.append(a[i])
        for j in range(mid + 1, right + 1):
            temp2.append(a[j])
        p1 = 0
        p2 = 0
        while p1 < len(temp1) and p2 < len(temp2):
            if temp1[p1] < temp2[p2]:
                ans.append(temp1[p1])
                p1 += 1
            else:
                ans.append(temp2[p2])
                p2 += 1
        while p1 < len(temp1):
            ans.append(temp1[p1])
            p1 += 1
        while p2 < len(temp2):
            ans.append(temp2[p2])
            p2 += 1
        for i in range(len(ans)):
            a[left + i] = ans[i]
    
    # quick sort 
    def quickSort(self, A, l, h):
        if l < h:
            j = self.partition(A, l, h)
            self.quickSort(A, l, j)
            self.quickSort(A, j + 1, h)
    def partition(self, A, l, h):
        pivot = A[l]
        i, j = l, h
        while True:
            while A[i] < pivot:
                i += 1
            while A[j] > pivot:
                j -= 1
            if i >= j:
                return j
            A[i], A[j] = A[j], A[i]

sol = SortingAlgorithm()
# insertion sort
arr = [1, 29, 0]
print(sol.insertionSort(arr))

# merge sort
arr = [1, 8, 6, 3, 9, 8]
left = 0
right = len(arr) - 1  
sol.MergeSort(arr, left, right)
print(arr) 

# quick sort
qrr=[1,8,4,2,6,0]
l= 0
r= len(qrr)-1
print(sol.quickSort(qrr,l,r))
print("arr",qrr)

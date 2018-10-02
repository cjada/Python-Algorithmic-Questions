class Solution:
    # @param A : integer
    # @return a list of list of integers
    def fill_line(self, arr, direction, i, j, counter):
        print("------")
        print(direction)
        print(i, j)
        if direction == "n":
            while i >= 0 and arr[i][j] == 0:
                arr[i][j] = counter
                counter += 1
                i -= 1
            i += 1
            j += 1
        elif direction == "w":
            while j >= 0 and arr[i][j] == 0:
                arr[i][j] = counter
                counter += 1
                j -= 1
            j += 1
            i += 1
        elif direction == "e":
            while j < len(arr) and arr[i][j] == 0:
                arr[i][j] = counter
                counter += 1
                j += 1
            j -= 1
            i -= 1
        elif direction == "s":
            while i < len(arr) and arr[i][j] == 0:
                arr[i][j] = counter
                counter += 1
                i += 1
            i -= 1
            j -= 1
        print(direction)
        print(i, j)
        print("----------")
        return (arr, i, j, counter)
    
    def complete(self, arr, i, j):
        if arr[i][j] ==  0:
            return False
        if i > 0:
            if arr[i-1][j] == 0:
                return False
        if i < (len(arr)-1):
            if arr[i+1][j] == 0:
                return False
        if j > 0:
            if arr[i][j-1] == 0:
                return False
        if j < (len(arr)-1):
            if arr[i][j+1] == 0:
                return False
        return True
        
    def generateMatrix(self, A):
        arr = []
        directions = ["e", "s", "w", "n"]
        for i in range(A):
            arr.append([0]*A)
            
        counter = 1
        direction = 0
        i = 0
        j = 0
        while not self.complete(arr, i, j):
            (arr, i, j, counter) = self.fill_line(arr, directions[direction % 4], i, j, counter)
            direction += 1
        return arr
            

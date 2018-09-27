def maxset(A):
        firstIndex = [0]
        index = [0]
        length = [0]
        maxSum = [0]
        i = 0
        for i in range(0, len(A)):
            if A[i] > 0:
                maxSum.append(A[i] + maxSum[i])
                length.append(length[i] + 1)
                if index[i] < 0:
                    firstIndex.append(i)
                    index.append(i)
                else:
                    firstIndex.append(firstIndex[i])
                    index.append(i)
            else:
                maxSum.append(0)
                length.append(0)
                index.append(-1)
                firstIndex.append(-1)
        
        maxSumInfo = []

        for i in range(0, len(maxSum)):
            maxSumInfo.append((maxSum[i], length[i], firstIndex[i], index[i]))

        maxSumInfo = sorted(maxSumInfo, key=lambda x : (x[0], x[1], -x[2]), reverse=True)
from typing import List

def flipAndInvertImage(A:List[List[int]]) -> List[List[int]]:
    
    # 길이 측정
    l = len(A)
    
    # 수평으로 뒤집기
    for i in range(l):
        A[i].reverse()
        
    # 0과 1 바꾸기
    for i in range(l):
        for j in range(l):
            A[i][j] = abs(A[i][j] - 1)
    
    return A


A = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(A))
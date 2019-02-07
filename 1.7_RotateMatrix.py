# 1.7 행렬회전 : 이미지를 표현하는 N * N 행렬이 있다.
# 이미지의 각 픽셀은 4바이트로 표현된다.
# 이때, 이미지를 90도 회전시키는 메서드를 작성하라.
# 행렬을 추가로 사용하지 않고서도 할 수 있겠는가?



def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    print(n)


data = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]


def test(data):
    for i in data:
        print ('>>>> ', i)

test(data)



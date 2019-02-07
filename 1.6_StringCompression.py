# 1.6 문자열 압축 : 반복되는 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라.
# 예를 들어 문자열 aabcccccaaa를 압축하면 a2b1c5a3이 된다.
# 만약 ‘압축된’ 문자열의 길이가 기존 문자열의 길이보다 길다면 기존 문자열을 반환해야 한다.
# 문자열은 대소문자 알파벳(a~z)으로만 이루어져 있다.

a = 'aaaaabbbbbcc' #a5b5c2
b = 'aabbbcccc' #a2b3c4
c = 'abcc' #a1b1c2 ====> abcc(기존 문자열 반환)
d = 'acccccbbbaaaaa' #a1c5b3a5

arr = [a,b,c,d]

def comp(arr):
    for strVar in arr:
        strNum = {}
        length = len(strVar)
        for alph in strVar:
            if alph in strNum:
                strNum[alph] += 1
            else:
                strNum[alph] = 1
        result = ''
        for key in strNum:
            key_num = key + str(strNum[key])
            result += key_num
        if len(result) > length:
            print(strVar)
        else:
            print(result)


comp(arr)

# 복잡도 : O(N^2) ?????

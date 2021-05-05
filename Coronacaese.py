def main(str1, str2):
    m = len(str1)
    n = len(str2)
    i = j = 0 # Index of str1 and str2
    

    while i < m and j < n:
        if str1[i] == str2[j]:
            i = i+1
        j = j + 1


    return i == m

str2 = str(input())
N = int(input())

for j in range(N):
    str1 = str(input())
    if main(str1, str2):
        print("POSITIVE")
    else:
        print( "NEGATIVE")

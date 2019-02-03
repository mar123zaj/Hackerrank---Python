if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    if len(arr)==n:
        arr.sort(reverse=False)
        for i in (range(1,n+1)):
            if arr[n-1]!=arr[n-i]:
                print(arr[n-i])
                break
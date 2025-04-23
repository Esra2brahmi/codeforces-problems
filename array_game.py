import sys
from bisect import bisect_left

def test_case():
    global ptr, input_data
    
    n = int(input_data[ptr])
    ptr += 1
    k = int(input_data[ptr])
    ptr += 1
    
    a = list(map(int, input_data[ptr:ptr + n]))
    ptr += n

    a.sort()
    
    if k >= 3:
        print(0)
        return
    
    min_k1 = a[0]
    for i in range(1, n):
        min_k1 = min(min_k1, a[i] - a[i-1])
    
    if k == 1:
        print(min_k1)
        return
    
    # k == 2
    ans = min_k1
    for i in range(n):
        for j in range(i + 1, n):
            d = abs(a[i] - a[j])
            ans = min(ans, d)
            pos = bisect_left(a, d)
            if pos < n:
                ans = min(ans, a[pos] - d)
            if pos > 0:
                ans = min(ans, d - a[pos - 1])
    print(ans)

def main():
    global ptr, input_data
    input_data = sys.stdin.read().split()
    ptr = 0
    T = int(input_data[ptr])
    ptr += 1
    for _ in range(T):
        test_case()

if __name__ == "__main__":
    main()
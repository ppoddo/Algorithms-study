import sys

def main() -> None:
    input = sys.stdin.readline
    n = int(input().strip())
    towers = list(map(int, input().strip().split()))

    results = [0] * n
    stack = []
    for i in range(n):
        while stack and stack[-1][1] < towers[i]:
            stack.pop()

        if stack:
            results[i] = stack[-1][0] + 1
        
        stack.append((i, towers[i]))

    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()

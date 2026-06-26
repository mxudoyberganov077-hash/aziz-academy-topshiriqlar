n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append((name, int(score)))
print(f"{'Name':<10} | {'Score'}")
print("-"*10 + "+-----")
for name, score in rows:
    print(f"{name:<10} | {score:>5}")
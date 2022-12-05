with open('1.txt') as f:
    max_sum, total_sum = max(sum(int(x) for x in group.split('\n')) for group in f), sum(sorted([sum(int(x) for x in group.split('\n')) for group in f], reverse=True)[:3])
print(max_sum)
print(total_sum)

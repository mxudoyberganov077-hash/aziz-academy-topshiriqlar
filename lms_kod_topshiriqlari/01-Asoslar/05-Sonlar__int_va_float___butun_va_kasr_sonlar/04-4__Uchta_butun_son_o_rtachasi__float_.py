numbers = (input())
num_list = list(map(int, numbers.split()))
average = sum(num_list) / len(num_list)
print(f"Average: {average}")
import sys

input_data = sys.stdin.read().splitlines()

if input_data:
    
    n = int(input_data[0])
    
    words = input_data[1:n+1]
    
    target = input_data[n+1]
    
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    print(word_counts.get(target, 0))
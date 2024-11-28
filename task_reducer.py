from itertools import count
import sys
count_array= {}
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        if word in count_array:
            count_array[word] = count_array[word] + 1
        else:
            count_array[word] = 1
# print({k: v for k, v in sorted(count_array.items(), key=lambda item: item[1])})
sorted_dict = sorted(count_array.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict[0])

print(count_array['Romeo'])

print(count_array['circumference'])
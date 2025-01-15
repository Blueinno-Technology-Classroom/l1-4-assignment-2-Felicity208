# TODO: add your code here!
number = int(input())
count = 1
sequence = []
for i in range (number):
    if len(sequence) <= 1:
        count = 1
    elif len(sequence) > 1:
        count = (sequence[-2]+ sequence[-1])
    sequence.append(count)
print(sequence)
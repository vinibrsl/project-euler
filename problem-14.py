def collatz(n):
    sequence = [n]
    last = n
    while last != 1:
        if last % 2 == 0:
            last = int(last/2)
        else:
            last = (3*last) + 1            
        sequence.append(last)
    return sequence

# starting number, count
longest = [0,0]
for n in range(1,1000000):
    sequence = collatz(n)
    count = len(sequence)
    if count > longest[1]:
        longest = [n,count]

print("Starting number < 1000000 that produces the longest chain: ", longest[0])

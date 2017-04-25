sequence = [1,2]
sequence_only_odds = [2]
last_value = sequence[1]
last_count = 2

while last_value <= 4000000:
    last_value = sequence[last_count - 1] + sequence[last_count - 2]
    last_count += 1
    sequence.append(last_value)

    if last_value % 2 == 0:
        sequence_only_odds.append(last_value)

print(sum(sequence_only_odds))

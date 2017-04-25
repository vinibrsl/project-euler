n = 0
while True:
    n += 1
    divisible_list = []
    for i in range(1,21):
        is_divisible = (n % i == 0)
        if is_divisible:
            divisible_list.append(is_divisible)
        else:
            break
        
    if len(divisible_list) == 20:
        break

print(n)

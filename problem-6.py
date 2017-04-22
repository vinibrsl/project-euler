sum_of_the_squares = 0
square_of_the_sum = 0

for i in range(0,100):
    sum_of_the_squares = sum_of_the_squares + (i+1)**2
    square_of_the_sum = square_of_the_sum + (i+1)
    
print((square_of_the_sum**2) - sum_of_the_squares)

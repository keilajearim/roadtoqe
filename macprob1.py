'''
Machine Problem #1
1. create a function that accepts an array of integers with random numbers. 
2. return the sum of all odd numbers from the array of integers
'''

def odd_nos_sum(numbers = []):
    sum_of_odds = 0
    if len(numbers) > 0:
        for i in range(len(numbers)):
            if numbers[i] % 2 != 0:
                sum_of_odds = sum_of_odds + numbers[i]
    return sum_of_odds

total = odd_nos_sum([1, 2, 3, 4, 5])
print(total)
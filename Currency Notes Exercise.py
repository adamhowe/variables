#Adam Howe
#18/09/2014
#Currency notes

whole_number = int(input("Enter a whole number: "))

twenties = whole_number // 20
remainder_twenties = whole_number % 20
#This will find how many twenties go into the whole number and the remainder.

tens = remainder_twenties //10
remainder_tens = remainder_twenties %10

fives = remainder_tens // 5
remainder_fives = remainder_tens %5

twos = remainder_fives // 2
remainder_twos = remainder_fives % 2

ones = remainder_twos // 1
remainder_ones = remainder_twos % 1

print(twenties)
print(tens)
print(fives)
print(twos)
print(ones)

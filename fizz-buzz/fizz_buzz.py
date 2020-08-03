# Start with some pseudo-code!

# range (1..100)
# numbers divisible by 3 and five -> fizzbuzz
# if number / 3 -> fizz
# if number / 5 --> buzz 


#range(start, stop, step)
for n in range(1, 100 + 1):
    if n % 5 == 0 & n % 3 == 0:
        print('fizzbuzz')
    elif n % 5 == 0:
        print('buzz')
    elif n % 3 == 0:
        print('fizz')
    else: 
        print(n)
# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2  
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

fib_list = [0,0]
calc = 0
while calc < 50:
    if calc <= 2:
        print("term:",calc,"/ number: ",fib_list[len(fib_list) - 1])
        calc += 1
        fib_list.append(1)
    else:
        fib_list.append(fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2])
        print("term:",calc,"/ number: ",fib_list[len(fib_list) - 1])
        calc += 1


# fib_seq = [0, 1]
# while len(fib_seq) <= 50:
#   fib_seq.append(fib_seq[-1] + fib_seq[-2])
# for x in range(0, 51):
#   print(f'term: {x} / number: {fib_seq[x]}')
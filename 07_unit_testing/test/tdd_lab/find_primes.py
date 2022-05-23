def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for n in range(2, int(i/2)+1):
                if i % n == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
 

starting_range = 2
ending_range = 101
prime_numbers = prime(starting_range, ending_range)
if len(prime_numbers) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", prime_numbers)

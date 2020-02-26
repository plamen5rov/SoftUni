first = int(input())
second = int(input())
for number in range(first, second + 1):

    even_sum = 0
    odd_sum = 0
    counter = 1
    number_copy = number

    while number_copy > 0:
        last = number_copy % 10


        if counter % 2 == 0:
            even_sum += last
        else:
            odd_sum += last
        number_copy = number_copy // 10
        counter += 1

    if even_sum == odd_sum:
        print(number, end=" ")

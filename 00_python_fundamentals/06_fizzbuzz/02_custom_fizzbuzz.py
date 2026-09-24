def fizz_buzz_custom(n, divisor1, divisor2, word1, word2):
    result = []

    for i in range(1, n + 1):

        if i % divisor1 == 0 and i % divisor2 == 0:
            result.append(word1 + word2)

        elif i % divisor1 == 0:
            result.append(word1)

        elif i % divisor2 == 0:
            result.append(word2)

        else:
            result.append(i)

    return result


print(
    fizz_buzz_custom(
        15,
        3,
        5,
        "Fizz",
        "Buzz"
    )
)
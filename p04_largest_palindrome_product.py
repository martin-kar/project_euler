"""
Largest palindrome product
Problem 4
Find the largest palindrome made from the product of two 3-digit numbers.
"""
start = 100
stop = 999


def is_palindrome(nbr):
    return nbr == int(str(nbr)[::-1])


def is_product_new_record(product, largest):
    return product > largest and is_palindrome(product)


def get_largest_palindrome():
    largest = 0
    for a in range(start, stop + 1):
        for b in range(start, stop + 1):
            product = a * b
            if is_product_new_record(product, largest):
                largest = product
    return largest


def main():
    largest_palindrome = get_largest_palindrome()
    print(largest_palindrome)


if __name__ == '__main__':
    main()

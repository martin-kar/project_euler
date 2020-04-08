"""
Special Pythagorean triplet
Problem 9

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

REQUIRED_SUM_OF_ABC = 1000


def is_pythagorean_triplet(a, b, c):
    return (a ** 2 + b ** 2 == c ** 2) and (a < b) and (b < c)


def product_of_abc_found(product_of_abc):
    return product_of_abc is not None


def get_product_of_abc():
    product_of_abc = None
    for a in range(1, REQUIRED_SUM_OF_ABC):
        if product_of_abc_found(product_of_abc):
            break
        for b in range(a + 1, REQUIRED_SUM_OF_ABC):
            c = REQUIRED_SUM_OF_ABC - a - b
            if is_pythagorean_triplet(a, b, c):
                product_of_abc = a * b * c
    return product_of_abc


def main():
    product_of_abc = get_product_of_abc()
    print(product_of_abc)


if __name__ == '__main__':
    main()

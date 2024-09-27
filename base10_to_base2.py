def base10_to_base2(n: int) -> str:
    """Calculates an n from base 10 to base 2,
    provided that the integer is non negative.
    
    >>> base10_to_base2(43)
    101011
    >>> base10_to_base2(1)
    1
    """
       
    if n == 0:
        return '0'
    elif n == 1: 
        return '1'
    else:
        return base10_to_base2(n // 2) + str(n % 2)

if __name__ == '__main__':
    while True:
        n = int(input('Plase type a non-negative integer: '))
        print(base10_to_base2(n))

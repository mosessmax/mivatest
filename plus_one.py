def plus_one(digits):
    carry = 1
    
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        
        if digits[i] == 10:
            digits[i] = 0
            carry = 1
        else:
            carry = 0
            break
    
    # if we still have a carry, prepend 1
    if carry == 1:
        digits.insert(0, 1)
    
    return digits


def main():
    # test cases from the problem
    test_cases = [
        [1, 2, 3],
        [4, 3, 2, 1], 
        [9],
        [9, 9, 9]
    ]
    
    for digits in test_cases:
        original = digits.copy()
        result = plus_one(digits)
        print(f"Input: {original} -> Output: {result}")


if __name__ == "__main__":
    main()
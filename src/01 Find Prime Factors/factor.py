# '''A prime number is a natural number greater than 1 that has only two divisors:
# 👉 1 and the number itself.
# Examples:
# Prime numbers: 2, 3, 5, 7, 11, 13
# Not prime:
# 4 → divisible by 1, 2, and 4
# 9 → divisible by 1, 3, and '''

def is_prime_Check(num):
      # Any number less than or equal to 1 is not prime.
      if num <=1 :
        return False
      # verify divisibility by numbers from 2 up to its square root
   
      for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
          return False           
      return True

# '''Objective: Write a Python function to find the prime factorization of a given number, returning a list of its prime factors.
# Approach:
# Start dividing the number by 2 and continue with larger values sequentially.
# Check if the number divides evenly (no remainder). If it does, add the 
# divisor to the list of factors and update the number to the quotient.
# Continue this process until all prime factors are found.'''


def prime_factors(n):
   factors = []

    # Step 1: Handle factor 2 separately
   while n % 2 == 0:
     factors.append(2)
     n //=2             # divide by 2 until it’s no longer divisible
   
    # Step 2: Now check for odd factors from 3 up to sqrt(number)
   i=3
   while i <= int(n**0.5) + 1:
     while n % i == 0:
        factors.append(i)
        n //= i
     i = i + 2   # skipping even number
   # Step 3: If number > 2, it’s a prime factor itself

   if n > 2:
     factors.append(n)
   return factors

def get_prime_factors(number):
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return factors

def get_primeFromRange(startNum, endNum):
  print(f"\nPrime numbers between {startNum} and {endNum} are:")  
  for n in range(startNum, endNum + 1):
    #If number is greater then 1 then  Number can be prime .
      if n > 1 : 
          is_prime = True
      # verify divisibility by numbers from 2 up to its square root
          for i in range(2, int(n**0.5) + 1):
            if n % i == 0 :
              is_prime = False
              break
          if is_prime:
              print(n, end=" ") 

if __name__ == '__main__':
    # print("Is 2 prime number? ", is_prime_Check(2))
    # print("Is 13 prime number? ", is_prime_Check(13))
    # print("Is 130 prime number? ", is_prime_Check(130))
    # print("Is 7 ?", is_prime_Check(7))
    # print("Is 10 ?", is_prime_Check(10))
    # print("Is 14 ?", is_prime_Check(14))
    # print("Is 200 ?",is_prime_Check(200))
    # print("Is 678 ?", is_prime_Check(678))
    # print("Is 51 ?", is_prime_Check(51))

    # print("Prime Factors Of 160 are : " , prime_factors(160))
    # print("Prime Factors Of 13 are : " , prime_factors(13))
    # print("Prime Factors Of 360 are : " , prime_factors(630))

    # print(get_prime_factors(630))  # [2, 3, 3, 5, 7] 
    # print(get_prime_factors(13))  # [13]
    get_primeFromRange(2, 40)
    get_primeFromRange(41, 70)
    get_primeFromRange(50, 100)
    get_primeFromRange(1, 100)
    
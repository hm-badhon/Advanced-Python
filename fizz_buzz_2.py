class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result

if __name__ == "__main__":
    solution = Solution()

    # Take user input for n
    n = int(input("Enter a value for n: "))

    # Call the fizzBuzz method and print the result
    result = solution.fizzBuzz(n)
    print(result)

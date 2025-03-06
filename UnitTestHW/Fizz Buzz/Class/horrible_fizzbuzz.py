from typing import List
class Solution:
    def singleFizzBuzz(self, n: int) -> str:
        if n%3==0:
            return "Fizz"
        if n%5==0:
            return "Buzz"
        if n%15==0:
            return "Fizz" + "Buzz"
        elif n%1==0:
            return f"{str(n)}"
        return "OwO"

    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            ans.append(self.singleFizzBuzz(i))
        return ans
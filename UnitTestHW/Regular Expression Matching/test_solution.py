import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()
    
testcases = [
    # s, p, expected_res
    ["", "", True],
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    ["a", ".*.", True],
    ["aab", "c*a*b", True],
    ["aaa", "ab*a*c*a", True]
]

@pytest.mark.parametrize("s, p, expected_res", testcases)
def test_isMatch(solution, s, p, expected_res):
    assert solution.isMatch(s, p) == expected_res

@pytest.mark.xfail
def test_broken_solution(solution):
    assert solution.isMatch("mississippi", "mis*is*p*.") == True 

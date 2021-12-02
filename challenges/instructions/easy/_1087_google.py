"""
Given two strings A and B, return whether or not A can be shifted some number of times to get B.
For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""

def compute(a: str, b: str) -> bool:
    """ return whether or not A can be shifted some number of times to get B """
    if len(a) != len(b): return False
    a = a.split().sort()
    b = b.split().sort()
    if a == b:
        return True
    else:
        return False

# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 12:12:14 2025

@author: Kaden Sawyer
"""

_author_ = "Kaden Sawyer"
_credits_ = ["none"]
_email_ = "sawyerkd@mail.uc.edu" # Your email address
# CS2023 - Lab 3 Required Questions 
# All functions should be written using recursion.
# RQ1
def doubletime(i,n):
    """Returns the result of repeatedly doubling the number i a total of n times
    >>> doubletime(3, 1)
    6
    >>> doubletime(2, 0)
    2
    >>> doubletime(2, 9)
    1024
    """
    "*** YOUR CODE HERE ***"
    if n == 0: return i
    else: 
        return  2 * doubletime(i, n-1)
    
    


# RQ2
def skip2_add(n):
    """ Takes a number x and returns x + x-3 + x-6 + x-9 + ... + 0.

    >>> skip2_add(5)  # 5 + 2  + 0
    7
    >>> skip2_add(10) # 10 + 7 + 4 + 1 + 0
    22
    """
    "*** YOUR CODE HERE ***"
    if(n-3 < 0):
        return n
    else:
        return n + skip2_add(n-3)
    

# RQ3
def a(n):
    """Return the number in the sequence defined by a(1) = 1;
    a(n) = (3/2)*a(n-1) if a(n-1) is even; a(n) = (3/2)*(a(n-1)+1) if a(n-1) is odd.
    (see, http://oeis.org/A070885)

    >>> a(1)
    1
    >>> a(2) 
    3
    >>> a(3)
    6
    >>> a(10)
    123
    """
    "*** YOUR CODE HERE ***"
    "3 times everything else then divide by two "
    if n == 1:
        return 1
    else:
        if(a(n-1) % 2 == 0):
            return (3* a(n-1)) // 2
        else:
            return (3 * (a(n-1)+1)) //2

#RQ4
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    "number of paths from cell to the right then below"
    if n == 1 or m == 1: return 1
    else:
        return paths(m-1,n) + paths(m, n-1)
        

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
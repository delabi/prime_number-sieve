# prime_number-sieve
Generating prime numbers via the Sieve of Erastothenes.
The method omits calculating for 1 and 2 which are given. 
It also omits all even numbers when calculating from the beginning.
This makes it more efficient very quickly.
The time complexity of this algorithm is O(n log log n), provided the array update is an O(1) operation, as is usually the case.

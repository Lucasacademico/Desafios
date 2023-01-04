'''
Read an integer value, which is the duration in seconds of a certain event in a factory, 
and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds 
ike the following example.
'''

n = int(input())

h = int(n/3600)

aux = (n%3600)
m = int(aux/60)

aux = (aux%60)
s = int(aux/1)

print(f'{h}:{m}:{s}')

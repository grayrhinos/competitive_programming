# Relatively fast way to read line in CodeForces

# Tip #1
'''
- Use alias for the functions that are called too many times.
* 'Local variable lookups are much faster than global or built-in variable lookups: the Python "compiler" optimizes most function bodies so that for local variables, 
no dictionary lookup is necessary, but a simple array indexing operation is sufficient.'

* Local variables are faster than global; if you use global constants in a loop, copy it to a local variable beofre the loop. In Pyhton function names (global or build-in) 
are also global constants

* Try to use map(), filter() or reduce() to replace an explicit for loop, but only if you can use a built-in function: map with a built-in function beats for loop, 
but a for loop with in-line code beats map with a lambda function!
- For example, if we want to convert each string in a list to upper/lower case we can do that efficiently as new_list = map(str.upper, old_list)

- In most of the cases the number of input is huge. That means we have to call input() function many times to read each line. So, every time we call input() function,
Python recognizes that input() is a build in function and looks up for that does input() do. After lookup is when it starts executing it. By using alias 
(assigning a new name to input()) we can save that lookup time. 
'''
import sys

def main():
    input = sys.stdin.readline
    print = sys.stdout.write
    t = int(input())
    for i1 in [0]*t:
        n, x = map(int, input().split())
        nums = list(map(int, input().split()))
        
     print(answer + '\n')
    
if __name__=="__main__":
    main()



        
        
        
        
# Code for testing runtime
import timeit

print(timeit.timeit(
'''

j = 0
for i in [0]*100000:
    j += 1
'''    
, number = 1000))

# Day 10: Elves Look, Elves Say

sequence `211` is read as `one "two" two "ones"` which becomes `1221` 

Given an input `seq` , we need to apply this process `n` times. Probably best to treat the input as a string. 

Approach:
Two pointers can be used to count the number of consecutive characters in a sequence.  

E.G. 

seq = 1211

- `i = 0, j = 0`:
    - Check `seq[0:j+1]` while incrementing `j`. E.G. 
    - `seq[0:1] == seq[0] * (j- i + 1)`, so far we have "1" one. `curr_count` = 1. Increment `j`
    - `seq[0:2] != seq[0] * (j- i + 1)`, so we can stop there. Total count of `1` is `j-i = 1`. Append `f"{(j-i)}{seq[0]}"` to the final string.
- `i=1, j = 1` etc. 
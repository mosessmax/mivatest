# backend engineer miva test 

## plus_one.py

adds 1 to a large number stored as an array of digits. basically simulates how you'd add numbers by hand, start from the right, handle carries when digits hit 10. the tricky part is when you get something like [9,9,9] which becomes [1,0,0,0].

approach:
- loop backwards through the array
- add carry to each digit
- if digit becomes 10, set to 0 and carry forward
- if still have carry at the end, prepend 1

## min_max_rearrange.py

rearranges an array so it goes: smallest, largest, 2nd smallest, 2nd largest, etc.

approach:
- sort the array first
- use two pointers (left for smallest, right for largest)
- alternate picking from each end
- move pointers inward after each pick

both solutions handle the edge cases mentioned in the test cases.

python3 plus_one.py
python3 min_max_rearrange.py
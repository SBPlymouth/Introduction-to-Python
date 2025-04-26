# Copyright STEM Builders inc - All rights reserved

print(0.1+0.1) 
# Output: 
# 0.2 

# However, sometimes you will get an answer with an unexpectly long decimal part:
print(0.1+0.2) 
# Output: 
# 0.30000000000000004 

# This happens because of the way computers represent numbers internally; this has nothing to do with Python itself. Basically, we are used to working in powers of ten, where one tenth plus two tenths is just three tenths. But computers work in powers of two. So your computer has to represent 0.1 in a power of two, and then 0.2 as a power of two, and express their sum as a power of two. There is no exact representation for 0.3 in powers of two, and we see that in the answer to 0.1+0.2.
# Python tries to hide this kind of stuff when possible. Don't worry about it much for now; just don't be surprised by it, and know that we will learn to clean up our results a little later on.
# You can also get the same kind of result with other operations.
print(3*0.1) 
# Output: 
# 0.30000000000000004 

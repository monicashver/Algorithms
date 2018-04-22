import sys

###############################################
#              PRACTICE PROBLEM               #
# 1. Read from a text file or HTTP response   #
# 2. Convert text to upper case               #
# 3. Save modified test to a new file         #
# 4. Display success state to the user        #
###############################################


###############################################
#            Python file APIs 

# f = open('filename.ext', 'w') 
#     - 'r'  : reading (default)
#     - 'a'  : append
#     - 'r+' : read and write 


# f.read()
#    - reads entire contents starting from
#   last read portion
# i.e. if you called readline already -> 
# starts from whatever line is next


# f.close()
#    - closes file object

# f.closed
#    - returns True if file is closed

# f.readline()
#    - reads one line at a time

if __name__ == "__main__":
    print("main fxn")
    
    f = open('sample.txt')
    for line in f:
        print(line)
        
    
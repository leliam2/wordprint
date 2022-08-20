#Import the library
import sys

def print_word(word, num):
    #take word and print num times
    for i in range(num):
        print(word)

if __name__ == '__main__':
    
    n = len(sys.argv)
    print("Total arguments passed:", n)
    
    print(type(sys.argv))
    print(sys.argv)
   
    new_num = int(sys.argv[2])
    print_word(sys.argv[1], new_num)


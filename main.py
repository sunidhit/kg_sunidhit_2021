#The main function reading input and writing output to standard io
import sys
from code.MapCharacter import MapCharacter
def main():
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    canmap = MapCharacter(input1,input2)
    answer=canmap.checkcharactermap()
    print(str(answer).lower())


if __name__ == '__main__':
    main()



#The main function reading input and writing output to standard io
import sys
from code.MapCharacter import MapCharacter
def main():
    input1 = "123"
    input2 = "321"
    canmap = MapCharacter(input1,input2)
    answer=canmap.checkcharactermap()
    print(answer)


if __name__ == '__main__':
    print(str(sys.argv))
    main()



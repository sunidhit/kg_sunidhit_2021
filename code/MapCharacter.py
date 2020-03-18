class MapCharacter:
    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2
        self.can_map =True


    def checkcharactermap(self):

        if len(self.str1) is not len(self.str2):
            return False
        else:
            charmap = {}
            i=0
            for i in range(0,len(self.str1)):
                if self.str1[i] not in charmap:
                    charmap[self.str1[i]]=self.str2[i]
                else:
                    self.can_map = False
                    break
            print(self.can_map)
            return self.can_map










class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap ,tMap= {}, {}
        sFreq = self.countFrequency(s, sMap)
        tFreq = self.countFrequency(t, tMap)
        result =  self.checkAnagram(sMap, tMap) 
        if(result):
            return True
        else:
            return False
    def countFrequency(self,s, map):
        for n in s:
            if n in map:
                map[n]+=1
            else:
                map[n] =1
        return map
    def checkAnagram(self,map1, map2):
        # Check if the dictionaries have the same keys
        if set(map1.keys()) != set(map2.keys()):
            return False
            # Check if the dictionaries have the same values for each key
            # comparing map
        for key in map1:
            if map1[key] != map2[key]:
                return False
        return True

       
            


        
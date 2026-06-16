class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs :
            key = "".join(sorted(i))
            if key not in dic:
                dic[key] = []
            dic[key].append(i) 
        l = list(dic.values())
        return l      
                
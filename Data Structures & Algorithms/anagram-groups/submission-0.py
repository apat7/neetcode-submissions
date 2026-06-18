class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # mapping char count of each string

        for s in strs:
            count = [0] * 26 # a ... z (one for each character)

            for c in s:
                count[ord(c) - ord("a")] += 1 # substracts ascii value of char with a 

            result[tuple(count)].append(s)

        return list(result.values())
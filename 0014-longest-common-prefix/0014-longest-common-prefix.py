class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        common_prefix = ""
        min_length = 200
        shortest_str = ""
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
                shortest_str = s
        ind = 0
        for char in shortest_str:
            for s in strs:
                if s[ind] != char:
                    return common_prefix
            common_prefix += char
            ind += 1
        return common_prefix
            
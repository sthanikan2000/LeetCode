class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {\2\:\abc\, \3\:\def\, \4\:\ghi\, \5\:\jkl\, \6\:\mno\, \7\:\pqrs\, \8\:\tuv\, \9\:\wxyz\}
        res = [\\]
        for digit in digits:
            new_res = []
            x = mapping[digit]
            for c in x:
                for i in res:
                    new_res.append(i+c)
            res = new_res
        if res[0] == \\:
            return []
        return res



        
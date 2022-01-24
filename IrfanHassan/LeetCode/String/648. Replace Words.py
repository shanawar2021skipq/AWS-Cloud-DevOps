class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        lens = list(map(len, dictionary))
        short, long = min(lens), max(lens)
        dictionary = set(dictionary)
        res = ''
        for word in sentence.split():
            n = len(word)
            if n < short:
                res += word + ' '
                continue
            
            cur = ''
            for i in range(min(n, long)):
                cur += word[i]
                if cur in dictionary:
                    res += cur + ' '
                    break
            else:
                res += word + ' '
        
        return res.strip()
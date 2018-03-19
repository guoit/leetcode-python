"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
class Solution:
    dict = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 
    11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Ninteen', 
    20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninty'}
    
    def _convensionWithinThousand(self, num):
        """
        convert to words for number within one thousand
        """
        res = []
        if num//100 != 0:
            res.append(self.dict[num//100])
            res.append('Hundred')
            num %= 100

        if num != 0:
            if num < 21:
                # 1 - 20
                res.append(self.dict[num])
            else:
                # 21 - 99
                res.append(self.dict[(num//10)*10])
                if num % 10 != 0:
                    res.append(self.dict[num%10])

        return res
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        words = []
        if num // 10**9 != 0:
            words.extend(self._convensionWithinThousand(num//10**9))
            words.append('Billion')
            num %= 10**9

        if num // 10**6 != 0:
            words.extend(self._convensionWithinThousand(num//10**6))
            words.append('Million')
            num %= 10**6

        if num // 10**3 != 0:
            words.extend(self._convensionWithinThousand(num//10**3))
            words.append('Thousand')
            num %= 10**3

        words.extend(self._convensionWithinThousand(num))

        return ' '.join(words)

test_cases = [0, 9, 1900, 101, 123, 100001, 12345, 1234567, 2**31-1]
obj = Solution()
for case in test_cases:
    print(case, end = ' -> ')
    print(obj.numberToWords(case))
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        ret = ''
        if numerator / denominator < 0:
            ret += '-'

        numerator = abs(numerator)
        denominator = abs(denominator)

        if numerator % denominator == 0:
            return ret + str(int(numerator / denominator))

        ret += str(int(numerator / denominator)) + '.'
        table = {}
        i = len(ret)
        numerator = numerator % denominator
        while numerator != 0:   
            if numerator not in table.keys():
                table[numerator] = i
            else:
                i = table[numerator]
                ret = ret[:i] + '(' + ret[i:] + ')'
                return ret

            numerator *= 10
            ret += str(int(numerator / denominator))
            numerator %= denominator
            i += 1
        return ret

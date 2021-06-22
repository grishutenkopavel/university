import math


def countDigitInNum(nQ):
    digitSize = 0
    while nQ > 0:
        nQ = math.floor(nQ / 10)
        digitSize += 1
    
    return digitSize


def squareSequenceDigit(n):
    num = 1
    digit = 1
    orderDigit = 1
    while orderDigit <= n:
        num += 1
        numQ = num ** 2
        countDigit = countDigitInNum(numQ)
        if orderDigit + countDigit >= n:
            while orderDigit != n:
                countDigit -= 1
                orderDigit += 1
                digit = math.floor(numQ / (10 ** countDigit))
        
        orderDigit += countDigit
        digit %= 10

    return digit

    
def test():
    assert squareSequenceDigit(1)  == 1
    assert squareSequenceDigit(2) == 4
    assert squareSequenceDigit(3) == 9
    assert squareSequenceDigit(4) == 1
    assert squareSequenceDigit(5) == 6
    assert squareSequenceDigit(6) == 2
    assert squareSequenceDigit(7) == 5
    assert squareSequenceDigit(8) == 3
    assert squareSequenceDigit(9) == 6
    assert squareSequenceDigit(10) == 4
    assert squareSequenceDigit(11) == 9
    assert squareSequenceDigit(12) == 6
    assert squareSequenceDigit(13) == 4
    assert squareSequenceDigit(14) == 8
    assert squareSequenceDigit(15) == 1
    assert squareSequenceDigit(16) == 1
    assert squareSequenceDigit(17) == 0
    assert squareSequenceDigit(18) == 0
    assert squareSequenceDigit(19) == 1
    assert squareSequenceDigit(20) == 2
    assert squareSequenceDigit(21) == 1    

    
if __name__ == "__main__":
    squareSequenceDigit(1)
    squareSequenceDigit(2)
    squareSequenceDigit(7)
    squareSequenceDigit(12)
    squareSequenceDigit(17)
    squareSequenceDigit(27)
    test()

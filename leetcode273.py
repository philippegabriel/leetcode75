'''
273. Integer to English Words
'''
class Solution:
    # pylint: disable-next=invalid-name
    def numberToWords(self, num: int) -> str:
        toword:dict[int,str] = {
            1:'One', 2:'Two', 3: 'Three', 4:'Four', 5:'Five',6:'Six',
            7:'Seven', 8:'Eight', 9:'Nine',
            10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen',
            15:'Fifteen', 16:'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19:'Nineteen',
            20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy',
            80:'Eighty', 90:'Ninety',
            100:'Hundred', 10**3:'Thousand', 10**6:'Million', 10**9:'Billion'
        }
        if not num:
            return 'Zero'
        result:list[int]=[]
        for i in [10**9,10**6,10**3,1]:
            n,num = divmod(num,i)
            if not n:
                continue
            hundreds = n // 100
            tens = n % 100
            onehundreds=0
            ones=0
            if hundreds >20:
                onehundreds = hundreds % 10
                hundreds-= onehundreds
            if tens >20:
                ones = tens % 10
                tens -= ones

            #print(f'{i=},{n=},{num=},{hundreds=},{tens=},{ones=}')
            result.append(hundreds)
            result.append(onehundreds)
            if hundreds or onehundreds:
                result.append(100)
            result.append(tens)
            result.append(ones)
            if i != 1:
                result.append(i)
        return ' '.join(toword[i] for i in result if i)

def test() -> None:
    s=Solution()
    print(s.numberToWords(120313317))
    print(s.numberToWords(123))
    print(s.numberToWords(12345))
    print(s.numberToWords(1234567))
    print(s.numberToWords(16000000))
if __name__ == "__main__":
    test()

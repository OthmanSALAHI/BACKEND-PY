class Solution(object):
    def BinDec(self,bin):
        self.Dec = 0
        for i in range(len(bin)):
            if bin[i] == '1':
                self.Dec += 2 ** i
            elif bin[i] == '0':
                self.Dec += 0
            else:
                return None
        return self.Dec
    def DecBin(self, dec):
        if dec == 0:
            return '0'
        binary_str = ''
        while dec > 0:
            binary_str = str(dec % 2) + binary_str
            dec //= 2
        return binary_str
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a.isdigit() and b.isdigit():
            Dec_a = self.BinDec(a)
            Dec_b = self.BinDec(b)
            if Dec_a != None and Dec_b != None:
                res = Dec_a + Dec_b
            else:
                return "only use 1 or 0";
        else :
            return "dont Use non digit"
        return self.DecBin(res)
    

def main():
    solution = Solution()
    
    a = input("enter first binary number :")
    b = input("enter second binary number :")
    result = solution.addBinary(a, b)
    print("Result:", result)

if __name__ == "__main__":
    main()
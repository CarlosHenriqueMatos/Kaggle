# atributos
#1 . numerador ; 2 denominador

#metodos
#somar; subtrair; multiplicar; dividir; inverter;

class Frac:
    def __init__(self, num:float, den:float):

        self.num = num
        if den == 0:
            self.den = 1
        else:
            self.den = den

    def sum(self, outra:float)-> float:
        if self.den == outra.den:
            num = self.num + outra.den
            den = self.den
            return Frac(num, den)
        num = self.num * outra.den + outra.den*self.den
        den = self.den+outra.den
        return Frac(num,den)
    
    
    def deduct(self, outra:float)-> float:
        return self.sum(outra.reverse())

    def multiply(self, outra:float) -> float:
        numerator = self.num * outra.num
        denominator = self.den * outra.den
        return Frac(numerator, denominator)
    
    def divide(self, outra:float) -> float:
        return self.multiply(outra.invert())

    def invert(self) -> float:
        return Frac(self.den, self.num)
    
    def reverse(self) -> float:
        return Frac(-self.num, self.den)
    
    def simplify(self):
        pass

    def __str__(self) -> str:
        representation = "{}/{}".format(self.num, self.den)
        return representation
if __name__ == '__main__':
    primeira = Frac(4, 5)
    print(primeira)
    print(primeira.num, primeira.den)
class Calculator:
    def addition (self,num1,num2):
        sum = num1+num2
        return sum
    def deduct (self,num1,num2):
        sub = num1 - num2
        return sub
    def divison (self,num1,num2):
        div = num1//num2
        return div
    def multiplication (self,num1,num2):
        mul = num1*num2
        return mul
my_calculatior = Calculator()

result_of_sum = my_calculatior.addition(20,10)
print(result_of_sum)

result_of_sub = my_calculatior.deduct(20,10)
print(result_of_sub)

result_of_div = my_calculatior.divison(20,2)
print(result_of_div)

result_of_mul = my_calculatior.multiplication(10,2)
print(result_of_mul)

    
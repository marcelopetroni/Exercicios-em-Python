i = 0
lista = []
lista2 = []
num = float(input())
num2 = float(input())
string = str(input())
while True:
    num3 = input()
    string2 = input()
    
    lista.append(float(num3))
    lista2.append(string2)
    if string2 == '&':
        break

if string == "+":
    a = (num + num2)
    total = a
    print(format(a, ".3f"))
elif string == "-":
    a = (num - num2)
    total = a
    print(format(a, ".3f"))
elif string == "*":
    a = (num * num2)
    total = a
    print(format(a, ".3f"))
elif string == "/":
    if num2 == 0:
         print("operacao não pode ser realizada")
    else:
         a = (num / num2)
         total = a
         print(format(a, ".3f"))
         
while lista2[i] != "&":
     if lista2[i] == "+":
          total = total + lista[i] 
          print(format(total, ".3f"))
     elif lista2[i] == "-":
          total = total - lista[i]
          print(format(total, ".3f"))
     elif lista2[i] == "*":
          total = total * lista[i]
          print(format(total, ".3f"))
     elif lista2[i] == "/":
          if lista[i] == 0:
               print("operacao não pode ser realizada")
          else:
               total = total / lista[i]
               print(format(total, ".3f"))
     i += 1
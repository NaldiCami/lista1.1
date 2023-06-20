n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
me=float(input("Digite a média dos exercícios realizados anteriormente: "))
ma = (n1 + n2*2 + n3*3 + me)/7.
mr = round(ma,2)
if ma >= 9:
    print("Parabéns, sua média foi",mr,". Fez um ótimo trabalho!")
elif ma >= 4 and ma < 9:
    print("Sua média foi {}".format(mr))
else:
    print("Sua média foi {}, você está de recuperação!".format(mr))
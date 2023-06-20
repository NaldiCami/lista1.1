l = int(input("Digite a quantidade de lados de um polígono: "))
while l < 3:
    l =int(input("Isso não é um poligono, digite outro valor: \n"))
while l > 8:
    l = int(input("Não posso calcular esse valor, insira um valor menor do que 8: \n"))
if l == 3:
    print("TRIANGULO")
elif l == 4:
    print("QUADRADO")
elif l == 5:
    print("PENTÁGONO")
elif l == 6:
    print("HEXÁGONO")
elif l == 7:
    print("HEPTÁGONO")
else:
    print("OCTÓGONO")
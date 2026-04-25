print("Veja se você pode parcelar seu pedido 💸!")
qtd = int(input("quantas unidades de melancia você vai querer? "))
total = int(input("informe quantidade de parcelas desejadas? "))
valor = qtd*20
print(f"o valor de cada parcela é: R$ {valor/total}")
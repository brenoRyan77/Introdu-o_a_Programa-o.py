from collections import defaultdict
duplicar = defaultdict(list)

vet = []
for conte in range(0, 50):
    vet.append(int(input('Digite um valor: ')))


    for adicionar, numero in enumerate(vet):
        duplicar[numero].append(adicionar + 1)

result = {faca: valor for faca, valor in duplicar.items() if len(valor) > 1}
print(result)
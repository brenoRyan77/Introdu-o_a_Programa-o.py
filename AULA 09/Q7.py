convidados = ["Tim Maia", "Faustão", "Messi", "LeBron James", "Luva de Pedreiro"]

for mensagem in convidados:
    print("Olá {}, estamos convidando você e sua família para o nosso evento na uniesp".format(mensagem))

print("")
print("")

nao_comparece = ["Messi"]
del(convidados[2])

for quem_nao_comparece in nao_comparece:
    print("{} não vai comparecer ao evento!".format(quem_nao_comparece))

print("")

for mensagemAtualizada in convidados:
    print("Olá {}, estamos convidando você e sua família para o nosso evento na uniesp".format(mensagemAtualizada))
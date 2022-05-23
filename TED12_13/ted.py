import os
#Funções
def cadastrar():
    nome = input('Digite seu nome: ')
    sobrenome = input('Digite seu sobrenome: ')
    idade = int(input('Idade: '))
    email = input('Digite seu email: ')
    agenda = open('%s_%s.txt' %(nome, sobrenome),'a')
    agenda.write('%s %s, %d, %s\n'%(nome, sobrenome, idade, email))
    agenda.close()

def buscar():
    n = input('Digite o nome do contato a ser pesquisado: ')
    s = input('Digite o sobrenome do contato a ser pesquisado: ')
    agenda = open('%s_%s.txt'%(n,s),'r')

    for x in agenda.readlines():
        print(x)
    agenda.close()

def deletar():
    n = input('Digite o nome que deseja apagar: ')
    s = input('Digite o sobrenome que deseja apagar: ')
    os.remove('%s_%s.txt'%(n,s))

#Função principal

def main():
    print('              MENU')
    print('1. Novo contato\n2. Buscar contato pelo nome')
    print('3. Atualizar contato\n4. Apagar contato\n0. Sair')
    opcao = 1
    while opcao!=0:
        op = int(input('\nDigite a opção: '))
        if opcao ==1:            
            cadastrar()            
        elif opcao ==2:
            buscar()
        elif opcao ==3:
            deletar()    
        elif opcao ==4:
            deletar()            
        elif opcao ==0:
            print('Programa finalizado.')
            break
        else:
            print('Opção incorreta, tente novamente. ')
main()
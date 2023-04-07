from operacoesbd import *
import os

def menu():
    print('╔========================================╗')
    print('║      UNIVERSIDADE ABELLA SYSTEMS       ║')
    print('╠========================================╣')
    print('║             MENU OUVIDORIA             ║')
    print('╠========================================╣')
    print('║1) Listar as reclamações.               ║')
    print('║2) Adicionar nova reclamação.           ║')
    print('║3) Remover uma reclamação.              ║')
    print('║4) Pesquisar uma reclamação por código. ║')
    print('║5) Sair do Sistema Ouvidoria.           ║')
    print('╚=═======================================╝')
    opcao = input('Selecione uma opção: ')
    return opcao

def listarReclamacoes(conexao):
    os.system('cls')
    consultaListagem = 'select * from manifestacoes'
    listaReclamacoes = listarBancoDados(conexao, consultaListagem)

    if len(listaReclamacoes) == 0:
        print('Nenhuma reclamação cadastrada no sistema.')
        print()
        input('Aperte "Enter" para voltar nas opções. ')
        os.system('cls')
    else:
        print('==========================================')
        print('           LISTA DAS RECLAMAÇÕES          ')
        print('==========================================')

        for manifestacao in listaReclamacoes:
            print('Código:', manifestacao[0], '- Reclamação:', manifestacao[1])

        print()
        input('Aperte "Enter" para voltar nas opções. ')
        os.system('cls')

def inserirReclamacoes(conexao):
    os.system('cls')
    novaReclamacao = input('Por favor, digite sua reclamação, em seguida, aperte "Enter": ')
    print()

    if novaReclamacao == ' ' or len(novaReclamacao) < 5 or novaReclamacao == ' '*len(novaReclamacao) \
    or novaReclamacao == novaReclamacao[0]*len(novaReclamacao):
        print('Descrição inválida. Por favor, digite algum texto sobre a sua reclamação.')
        print()
        input('Para Voltar ao Menu Principal Aperte "Enter". ')
        os.system('cls')

    else:
        consultaNovaReclamacao = 'insert into manifestacoes(sugestoes) values(%s)'
        dados = (novaReclamacao,)
        insertNoBancoDados(conexao, consultaNovaReclamacao, dados)

        consultaCodigo = 'select MAX(codigo) from manifestacoes'
        codigoAdicionado = listarBancoDados(conexao, consultaCodigo)

        for manifestacao in codigoAdicionado:
            print(f'Reclamação cadastrada com sucesso. O código da reclamação é {manifestacao[0]}.')
            print("")
            input('Para Voltar ao Menu Principal Aperte "Enter".  ')
            os.system('cls')

def removerReclamacoes(conexao):
    os.system('cls')
    consultaListagem = 'select * from manifestacoes'
    listaReclamacoes = listarBancoDados(conexao, consultaListagem)

    if len(listaReclamacoes) == 0:
        print('Nenhuma reclamação cadastrada no sistema para remover.')
        print()
        input('Aperte "Enter" para voltar nas opções. ')
        os.system('cls')

    else:
        print('==========================================')
        print('           LISTA DAS RECLAMAÇÕES          ')
        print('==========================================')

        for manifestacoes in listaReclamacoes:
            print('Código:', manifestacoes[0], '- Reclamação:', manifestacoes[1])

        print()
        codigoRemover = input('Por favor, qual o código da reclamação que deseja remover? ')

        try:
            codigoRemoverInt = int(codigoRemover)

        except:
            print()
            print('Código inválido. Por favor, digite apenas número de acordo com a listagem!')
            print()
            input('Aperte "Enter" para voltar nas opções. ')
            os.system('cls')

        else:
            consultaRemoverReclamacao = 'delete from manifestacoes where codigo = %s'
            dados = (codigoRemoverInt,)

            reclamacaoRemovida = excluirBancoDados(conexao, consultaRemoverReclamacao, dados)

            if reclamacaoRemovida == 0:
                print()
                print('Código inválido. Por favor, digite apenas número de acordo com a listagem!')
                print()
                input('Aperte "Enter" para voltar nas opções. ')
                os.system('cls')
            else:
                print()
                print('Reclamação removida com sucesso!')
                print()
                input('Aperte "Enter" para voltar nas opções. ')
                os.system('cls')

def pesquisarReclamacoes(conexao):
    os.system('cls')
    consultaListagem = 'select * from manifestacoes'
    listaReclamacoes = listarBancoDados(conexao, consultaListagem)

    if len(listaReclamacoes) == 0:
        print('Nenhuma reclamação cadastrada no sistema para pesquisar.')
        print()
        input('Aperte "Enter" para voltar nas opções. ')
        os.system('cls')
    else:
        print('==========================================')
        print('            LISTA DE CÓDIGOS              ')
        print('==========================================')

        for manifestacoes in listaReclamacoes:
            print('Código:', manifestacoes[0])

        print()
        codigoPesquisa = input('Por favor, informe o código da reclamação a ser pesquisada: ')

        try:
            codigoPesquisaInt = int(codigoPesquisa)
        except:
            print()
            print('Código inválido. Por favor, digite apenas número de acordo com a listagem!!')
            print()
            input('Aperte "Enter" para voltar nas opções. ')
            os.system('cls')
        else:
            consultaListagem = 'select * from manifestacoes where codigo = ' + codigoPesquisa
            listaReclamacoes = listarBancoDados(conexao, consultaListagem)

            if len(listaReclamacoes) == 0:
                print()
                print('Código inválido. Por favor, digite apenas número de acordo com a listagem!')
                print()
                input('Aperte "Enter" para voltar nas opções. ')
                os.system('cls')
            else:
                print()
                print('Resposta da pesquisa:')
                for manifestacoes in listaReclamacoes:
                    print('Código:', manifestacoes[0], '- Reclamação:', manifestacoes[1])
                print()
                input('Aperte "Enter" para voltar nas opções. ')
                os.system('cls')

def agradecimento():
    os.system('cls')
    print("")
    print('Muito obrigado por usar o Sistema Ouvidoria. Até logo!')
    print("")

def opcaoInvalida():
    os.system('cls')
    print('Opção inválida. Por favor, escolha uma das opções sugeridas.')
    print("")
    input('Aperte "Enter"" para voltar nas opções. ')
    os.system('cls')
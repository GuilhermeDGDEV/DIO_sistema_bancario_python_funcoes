from os import system
import funcoes_bancarias as fb


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = fb.menu()

        if opcao == 'd':
            valor = input('Informe o valor do depósito: ')
            saldo, extrato = fb.depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = input('Informe o valor do saque: ')
            saldo, extrato = fb.sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            fb.exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            fb.criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = fb.criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            fb.listar_contas(contas)

        elif opcao == 'l':
            system('cls')

        elif opcao == 'q':
            break

        else:
            print('Operação inválida, por favor selecione novamente a operação desejada.')


main()

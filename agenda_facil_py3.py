# ==========================================
# PROJETO INTEGRADOR - AGENDA FACIL
# Sistema de cadastro de clientes e agendamentos
# ==========================================

clientes = []
agendamentos = []

while True:

    print("\n========== AGENDA FACIL ==========")
    print("1 - Cadastrar cliente")
    print("2 - Pesquisar cliente")
    print("3 - Listar clientes")
    print("4 - Cadastrar agendamento")
    print("5 - Listar agendamentos")
    print("6 - Sair")
    print("=================================")

    opcao = input("Escolha uma opcao: ")

    # OPCAO 1 - CADASTRAR CLIENTE
    if opcao == "1":

        nome = input("Nome do cliente: ").strip()

        if nome == "":
            print("Nome nao pode ficar vazio.")

        elif nome.lower() in [c.lower() for c in clientes]:
            print("Cliente ja cadastrado!")

        else:
            clientes.append(nome)
            print("Cliente cadastrado com sucesso!")

    # OPCAO 2 - PESQUISAR CLIENTE
    elif opcao == "2":

        nome = input("Digite o nome do cliente: ").strip()

        cliente_encontrado = None

        for cliente in clientes:
            if cliente.lower() == nome.lower():
                cliente_encontrado = cliente
                break

        if cliente_encontrado is not None:
            print("Cliente encontrado:", cliente_encontrado)
        else:
            print("Cliente nao encontrado.")

    # OPCAO 3 - LISTAR CLIENTES
    elif opcao == "3":

        print("\n========== LISTA DE CLIENTES ==========")

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")

        else:
            for cliente in clientes:
                print("-", cliente)

    # OPCAO 4 - CADASTRAR AGENDAMENTO
    elif opcao == "4":

        nome = input("Nome do cliente: ").strip()

        cliente_encontrado = None

        for cliente in clientes:
            if cliente.lower() == nome.lower():
                cliente_encontrado = cliente
                break

        if cliente_encontrado is None:
            print("Cadastre o cliente antes do agendamento.")

        else:
            servico = input("Servico: ").strip()
            data = input("Data (DD/MM/AAAA): ").strip()
            horario = input("Horario (HH:MM): ").strip()

            conflito = False

            for agendamento in agendamentos:

                if (agendamento["data"] == data and
                    agendamento["horario"] == horario):

                    conflito = True
                    break

            if conflito:
                print("Horario ja ocupado! Escolha outro.")

            else:
                agendamentos.append({
                    "cliente": cliente_encontrado,
                    "servico": servico,
                    "data": data,
                    "horario": horario
                })

                print("Agendamento realizado com sucesso!")

    # OPCAO 5 - LISTAR AGENDAMENTOS
    elif opcao == "5":

        print("\n========== LISTA DE AGENDAMENTOS ==========")

        if len(agendamentos) == 0:
            print("Nenhum agendamento cadastrado.")

        else:
            for agendamento in agendamentos:

                print("--------------------------------")
                print("Cliente:", agendamento["cliente"])
                print("Servico:", agendamento["servico"])
                print("Data:", agendamento["data"])
                print("Horario:", agendamento["horario"])

    # OPCAO 6 - SAIR
    elif opcao == "6":

        print("Encerrando o Agenda Facil!")
        break

    # OPCAO INVALIDA
    else:
        print("Opcao invalida! Tente novamente.")
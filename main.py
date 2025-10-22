from estoque import ModuloEstoque, menu_estoque
from servico import ModuloServicos, menu_servicos
from cliente import ModuloClientes, menu_clientes, Cliente
from relatorio import menu_relatorio

def menu():
    modulo_clientes = ModuloClientes()
    modulo_estoque = ModuloEstoque()
    modulo_servicos = ModuloServicos()

    modulo_clientes.cadastrar_cliente("João", "99999-9999", "joao@email.com")
    modulo_clientes.cadastrar_cliente("Maria", "98888-8888", "maria@email.com")

    while True:
        print("""
===== MENU - PRINCIPAL =====
1. Módulo Cliente
2. Módulo Serviço
3. Módulo Estoque
4. Módulo Relatório
0. Sair
====================================
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes(modulo_clientes)

        elif opcao == "2":
            menu_servicos(modulo_servicos, modulo_clientes.clientes)  

        elif opcao == "3":
            menu_estoque(modulo_estoque)

        elif opcao == "4":
            menu_relatorio(modulo_clientes.clientes, modulo_servicos.servicos)

        elif opcao == "0":
            print("Encerrando o sistema... 👋")
            break

        else:
            print("❌ Opção inválida ou módulo ainda não implementado.")

if __name__ == "__main__":
    menu()

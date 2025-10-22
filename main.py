from estoque import ModuloEstoque, menu_estoque
from servico import ModuloServicos, menu_servicos


def menu():
    modulo_estoque = ModuloEstoque()
    modulo_servicos = ModuloServicos()

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
        if opcao == "2":
            menu_servicos(modulo_servicos)
        elif opcao == "3":
            menu_estoque(modulo_estoque)
        elif opcao == "0":
            print("Encerrando o sistema... 👋")
            break
        else:
            print("❌ Opção inválida ou módulo ainda não implementado.")


if __name__ == "__main__":
    menu()

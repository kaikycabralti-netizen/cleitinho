class Relatorio:
    def __init__(self, clientes, servicos):
        """
        Inicializa o módulo de relatório
        :param clientes: lista de objetos Cliente
        :param servicos: lista de objetos Servico
        """
        self.clientes = clientes
        self.servicos = servicos

    def listar_clientes(self):
        """Exibe todos os clientes cadastrados"""
        if not self.clientes:
            print("\n⚠️ Nenhum cliente cadastrado.\n")
            return
        print("\n📋 Relatório de Clientes:\n")
        for c in self.clientes:
            print(f"[{c.id_cliente}] {c.nome} | {c.telefone} | {c.email}")
        print()

    def listar_servicos(self):
        """Exibe todos os serviços cadastrados"""
        if not self.servicos:
            print("\n⚠️ Nenhum serviço cadastrado.\n")
            return
        print("\n📋 Relatório de Serviços:\n")
        for s in self.servicos:
            print(f"[{s.id_servico}] Cliente: {s.cliente.nome} | Problema: {s.descricao} | Status: {s.status} | Valor: R${s.valor}")
        print()

def menu_relatorio(clientes, servicos):
    relatorio = Relatorio(clientes, servicos)

    while True:
        print("""
===== MENU - RELATÓRIO =====
1. Listar todos os clientes
2. Listar todos os serviços
0. Voltar ao menu principal
====================================
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorio.listar_clientes()

        elif opcao == "2":
            relatorio.listar_servicos()

        elif opcao == "0":
            print("Voltando ao menu principal...\n")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

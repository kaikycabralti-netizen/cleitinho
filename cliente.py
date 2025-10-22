class Cliente:
    def __init__(self, id_cliente, nome, telefone, email):
        self.id_cliente = id_cliente
        self.nome = nome.strip().title()
        self.telefone = telefone.strip()
        self.email = email.strip()

    def atualizar_dados(self, nome=None, telefone=None, email=None):
        if nome:
            self.nome = nome.strip().title()
        if telefone:
            self.telefone = telefone.strip()
        if email:
            self.email = email.strip()
        print(f"✅ Dados do cliente '{self.nome}' atualizados com sucesso!")


class ModuloClientes:
    def __init__(self):
        self.clientes = []
        self.proximo_id = 1

    def cadastrar_cliente(self, nome, telefone, email):
        cliente = Cliente(self.proximo_id, nome, telefone, email)
        self.clientes.append(cliente)
        self.proximo_id += 1
        print(f"\n✅ Cliente cadastrado com sucesso! ID: {cliente.id_cliente}\n")

    def listar_clientes(self):
        if not self.clientes:
            print("\n⚠️ Nenhum cliente cadastrado.\n")
            return
        print("\n📋 Lista de Clientes:\n")
        for c in self.clientes:
            print(f"[{c.id_cliente}] Nome: {c.nome} | Telefone: {c.telefone} | Email: {c.email}")
        print()

    def buscar_cliente(self, nome):
        resultado = [c for c in self.clientes if nome.lower() in c.nome.lower()]
        if not resultado:
            print(f"\n⚠️ Nenhum cliente encontrado com o nome '{nome}'.\n")
            return []
        return resultado

    def remover_cliente(self, id_cliente):
        for c in self.clientes:
            if c.id_cliente == id_cliente:
                self.clientes.remove(c)
                print(f"\n❌ Cliente '{c.nome}' removido com sucesso!\n")
                return
        print("❌ Cliente não encontrado.")


def menu_clientes(modulo_clientes):
    while True:
        print("""
===== MENU - MÓDULO DE CLIENTES =====
1. Cadastrar novo cliente
2. Listar clientes
3. Buscar cliente por nome
4. Atualizar dados de um cliente
5. Remover cliente
0. Voltar ao menu principal
====================================
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            modulo_clientes.cadastrar_cliente(nome, telefone, email)

        elif opcao == "2":
            modulo_clientes.listar_clientes()

        elif opcao == "3":
            nome = input("Nome para busca: ")
            encontrados = modulo_clientes.buscar_cliente(nome)
            for c in encontrados:
                print(f"[{c.id_cliente}] {c.nome} | {c.telefone} | {c.email}")

        elif opcao == "4":
            try:
                id_cliente = int(input("Digite o ID do cliente: "))
                nome = input("Novo nome (ou deixe em branco): ")
                telefone = input("Novo telefone (ou deixe em branco): ")
                email = input("Novo email (ou deixe em branco): ")
                for c in modulo_clientes.clientes:
                    if c.id_cliente == id_cliente:
                        c.atualizar_dados(nome, telefone, email)
                        break
                else:
                    print("❌ Cliente não encontrado.")
            except ValueError:
                print("❌ ID inválido. Digite um número inteiro.")

        elif opcao == "5":
            try:
                id_cliente = int(input("Digite o ID do cliente a remover: "))
                modulo_clientes.remover_cliente(id_cliente)
            except ValueError:
                print("❌ ID inválido. Digite um número inteiro.")

        elif opcao == "0":
            print("Voltando ao menu principal...\n")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

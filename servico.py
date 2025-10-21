class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Servico:
    def __init__(self, id_servico, cliente, descricao, valor, status="Na bancada"):
        self.id_servico = id_servico
        self.cliente = cliente  # objeto Cliente
        self.descricao = descricao
        self.valor = valor
        self.status = status

    def atualizar_status(self, novo_status):
        status_validos = ["Na bancada", "Aguardando peça", "Pronto para retirada", "Entregue"]
        if novo_status in status_validos:
            self.status = novo_status
            print(f"✅ Status atualizado para: {novo_status}")
        else:
            print("❌ Status inválido! Use um dos seguintes:")
            for s in status_validos:
                print(" -", s)


class ModuloServicos:
    def __init__(self):
        self.servicos = []
        self.proximo_id = 1

    def registrar_servico(self, cliente, descricao, valor):
        servico = Servico(self.proximo_id, cliente, descricao, valor)
        self.servicos.append(servico)
        self.proximo_id += 1
        print(f"\n✅ Serviço registrado com sucesso! ID: {servico.id_servico}\n")

    def listar_servicos(self):
        if not self.servicos:
            print("\n⚠️ Nenhum serviço cadastrado.\n")
            return
        print("\n📋 Lista de Serviços:\n")
        for s in self.servicos:
            print(f"[{s.id_servico}] Cliente: {s.cliente.nome} | Problema: {s.descricao} | Status: {s.status} | Valor: R${s.valor}")
        print()

    def atualizar_status(self, id_servico, novo_status):
        for s in self.servicos:
            if s.id_servico == id_servico:
                s.atualizar_status(novo_status)
                return
        print("❌ Serviço não encontrado.")

def menu_servicos(modulo_servicos, clientes):
    while True:
        print("""
===== MENU - MÓDULO DE SERVIÇOS =====
1. Registrar novo serviço
2. Listar serviços
3. Atualizar status de um serviço
0. Voltar ao menu principal
=====================================
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Registrar novo serviço ---")
            nome_cliente = input("Nome do cliente: ").strip()

            # Buscar cliente
            cliente_encontrado = None
            for c in clientes:
                if c.nome.lower() == nome_cliente.lower():
                    cliente_encontrado = c
                    break

            if not cliente_encontrado:
                print("❌ Cliente não encontrado! Cadastre o cliente primeiro.")
                continue

            descricao = input("Descrição do problema: ").strip()
            try:
                valor = float(input("Valor do serviço (R$): "))
                modulo_servicos.registrar_servico(cliente_encontrado, descricao, valor)
            except ValueError:
                print("❌ Valor inválido. Digite apenas números.")
            
        elif opcao == "2":
            modulo_servicos.listar_servicos()

        elif opcao == "3":
            try:
                id_servico = int(input("Digite o ID do serviço: "))
                novo_status = input("Novo status: ")
                modulo_servicos.atualizar_status(id_servico, novo_status)
            except ValueError:
                print("❌ ID inválido. Digite um número inteiro.")
            
        elif opcao == "0":
            print("Voltando ao menu principal...\n")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


# ===============================
# EXEMPLO DE USO / TESTE LOCAL
# ===============================
if __name__ == "__main__":
    # Clientes fictícios (no projeto real vêm do módulo 1)
    clientes = [
        Cliente("João", "99999-9999", "joao@email.com"),
        Cliente("Maria", "98888-8888", "maria@email.com")
    ]

    modulo_servicos = ModuloServicos()
    menu_servicos(modulo_servicos, clientes)

class Peca:
    def __init__(self, id_peca, nome, quantidade, preco_custo):
        self.id_peca = id_peca
        self.nome = nome
        self.quantidade = quantidade
        self.preco_custo = preco_custo

    def dar_baixa(self, quantidade_usada):
        if quantidade_usada <= self.quantidade:
            self.quantidade -= quantidade_usada
            print(f"✅ Baixa realizada. Novo estoque: {self.quantidade} unidades.")
        else:
            print("❌ Quantidade insuficiente em estoque!")


class ModuloEstoque:
    def __init__(self):
        self.pecas = []
        self.proximo_id = 1

    def cadastrar_peca(self, nome, quantidade, preco_custo):
        peca = Peca(self.proximo_id, nome, quantidade, preco_custo)
        self.pecas.append(peca)
        self.proximo_id += 1
        print(f"\n✅ Peça '{nome}' cadastrada com sucesso! ID: {peca.id_peca}\n")

    def listar_pecas(self):
        if not self.pecas:
            print("\n⚠️ Nenhuma peça cadastrada.\n")
            return
        print("\n📦 Lista de Peças:\n")
        for p in self.pecas:
            alerta = "⚠️ Estoque baixo!" if p.quantidade < 5 else ""
            print(f"[{p.id_peca}] {p.nome} | Quantidade: {p.quantidade} | Custo: R${p.preco_custo:.2f} {alerta}")
        print()

    def dar_baixa(self, id_peca, quantidade_usada):
        for p in self.pecas:
            if p.id_peca == id_peca:
                p.dar_baixa(quantidade_usada)
                return
        print("❌ Peça não encontrada.")


def menu_estoque(modulo_estoque):
    while True:
        print("""
===== MENU - MÓDULO DE ESTOQUE =====
1. Cadastrar nova peça
2. Listar peças
3. Dar baixa em peça
0. Voltar ao menu principal
====================================
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Cadastrar nova peça ---")
            nome = input("Nome da peça: ").strip()
            try:
                quantidade = int(input("Quantidade inicial: "))
                preco_custo = float(input("Preço de custo (R$): "))
                modulo_estoque.cadastrar_peca(nome, quantidade, preco_custo)
            except ValueError:
                print("❌ Valor inválido. Digite números válidos para quantidade e preço.")

        elif opcao == "2":
            modulo_estoque.listar_pecas()

        elif opcao == "3":
            try:
                id_peca = int(input("ID da peça: "))
                quantidade_usada = int(input("Quantidade usada: "))
                modulo_estoque.dar_baixa(id_peca, quantidade_usada)
            except ValueError:
                print("❌ Digite valores numéricos válidos.")
            
        elif opcao == "0":
            print("Voltando ao menu principal...\n")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

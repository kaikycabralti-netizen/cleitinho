class Peca:
    def __init__(self, id_peca, nome, quantidade, preco_custo):
        self.id_peca = id_peca
        self.nome = nome.strip().title()
        self._quantidade = 0
        self._preco_custo = 0.0

    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade_new):
        if not isinstance(quantidade_new, int) or quantidade_new < 0:
            raise ValueError("A quantidade deve ser um número inteiro e positivo :().")
        self._quantidade = quantidade_new
    
    @property
    def preco_custo(self):
        return self._preco_custo
    
    @preco_custo.setter
    def preco_custo(self, preco_new):
        if not isinstance (preco_new, (int,float) or preco_new < 0):
            raise ValueError ("❌ Valor abaixo de zero ou não é número")
        self._preco_custo = float(preco_new)

    
    def dar_baixa(self, quantidade_usada):
        
        #usando variável local para segurança maior de código e mais flexibilidade
        quantidade_nova = self.quantidade - quantidade_usada
        
        if quantidade_nova >= 0:
            #colocando a nova quantidade para ser a real
            self.quantidade = quantidade_nova
            print(f"✅ Baixa realizada. Novo estoque: {self.quantidade} unidades.")
        else:
            print("❌ Quantidade insuficiente em estoque!")


class ModuloEstoque:
    def __init__(self):
        self.pecas = []
        self.proximo_id = 1

    def cadastrar_peca(self, nome, quantidade, preco_custo):
        try:
            peca = Peca(self.proximo_id, nome, quantidade, preco_custo)
            self.pecas.append(peca)
            self.proximo_id += 1
            print(f"\n✅ Peça '{nome}' cadastrada com sucesso! ID: {peca.id_peca}\n")
        except ValueError as e:
            print(f"\n❌ Erro ao cadastrar peça: {e}\n")
            
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

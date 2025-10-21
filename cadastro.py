class Banco:
    def __init__(self):
        self._contas = []
    
    def cadastro_user(self):
        cliente = input("Digite o nome do cliente: ")
        num = input("Insira o número do cliente: ")
        email = float(input("Digite o e-mail: "))

        if  == "1":
            limite_cc = float(input("Digite o limite da conta corrente: "))
            nova_conta = ContaCorrente(titular, saldo_inicial, limite_cc)
            self._contas.append(nova_conta)
            print(f"Conta para {titular} criada com sucesso!")
            return nova_conta
        elif conta_type_input == "2":
            nova_conta = ContaPoupanca(titular, saldo_inicial)
            self._contas.append(nova_conta)
            print(f"Conta para {titular} criada com sucesso!")
            return nova_conta
        else:
            print("Tipo de conta inválido. Nenhuma conta foi criada.")
            return None

    def listar_contas(self):
        print("\n--- Listagem de Contas ---")
        if not self._contas:
            print("Nenhuma conta cadastrada.")
        else:
            for i, conta in enumerate(self._contas):
                print(f"{i + 1}. Titular: {conta.titular}, Saldo: R$ {conta.pegar_saldo():.2f}")
        print("--------------------------\n")
        
    def transferir(self, conta_origem, conta_destino, valor):
        try:
            print(f"\nTentando transferir R$ {valor:.2f} de {conta_origem.titular} para {conta_destino.titular}...")
            conta_origem.sacar(valor)
            conta_destino.depositar(valor)
            print("Transferência realizada com sucesso!")
        except (ValueError, RuntimeError) as e:
            print(f"Erro na transferência: {e}")

meu_banco = Banco()

while True:
    print("\n--- Menu Principal ---")
    print("1. Abrir nova conta")
    print("2. Listar contas")
    print("3. Realizar operações (ex: depósito, saque, transferência)")
    print("4. Sair")
    
    escolha = input("Digite o número da sua escolha: ")
    
    if escolha == "1":
        meu_banco.abrir_conta_user()
    elif escolha == "2":
        meu_banco.listar_contas()
    elif escolha == "3":
        if len(meu_banco._contas) < 2:
            print("É necessário ter pelo menos duas contas para realizar transferências ou outras operações.")
            continue
            
        print("\n--- Operações ---")
        meu_banco.listar_contas()
        
        try:
            idx_origem = int(input("Escolha o número da conta de origem: ")) - 1
            idx_destino = int(input("Escolha o número da conta de destino: ")) - 1
            valor_transferencia = float(input("Digite o valor a ser transferido: "))
            
            conta_origem = meu_banco._contas[idx_origem]
            conta_destino = meu_banco._contas[idx_destino]
            
            meu_banco.transferir(conta_origem, conta_destino, valor_transferencia)
            
        except (ValueError, IndexError):
            print("Entrada inválida. Por favor, digite um número válido de conta e valor.")
            
    elif escolha == "4":
        print("Saindo do sistema. Obrigado por usar o WydenBank!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
        
import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()       

clientes = []

def cad_cliente (ID,nome,tel,email):
    novo_cliente = {
        "nome": nome.strip().title(),
        "tel": tel.strip(),
        "email": email.strip(),
        "ID": id.strip()
    }
    
    clientes.append [(novo_cliente): 
        print (f"\nSeu cliente foi CADASTRADO com sucesso, Cleitinho!" )
                     ]

def list_cliente ():
    
    if not clientes:
        print (f"\nTem nenhum cliente, Cleitinho, fique de boa")
        return False
    else:
        print (f"\n------- LISTA DE CLIENTES -------")
        for id, clientes in enumerate(clientes):
            print (f"ID: {ID}")
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

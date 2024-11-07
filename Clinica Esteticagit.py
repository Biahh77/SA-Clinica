#Grupo: Bianca - Julia - Matheus Yuri - Susana

class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.historico = []

   def adicionar_servico(self, servico):
        self.historico.append(servico)

    def mostrar_historico(self):
        if self.historico:
            print(f"Histórico de serviços de {self.nome}:")
            for servico in self.historico:
                print(f"- {servico.nome}: R${servico.preco:.2f}")
        else:
             print(f"{self.nome} não tem serviços registrados ainda.")


class Servico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
  

class ClinicaEstetica:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite o email do cliente: ")
        cliente = Cliente(nome, telefone, email)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!\n")

    def buscar_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome.lower() == nome.lower():
                return cliente
        return None

    def agendar_servico(self):
        nome_cliente = input("Digite o nome do cliente para agendar o serviço: ")
        cliente = self.buscar_cliente(nome_cliente)
        if cliente:
            print("\nServiços disponíveis:")
           print("1. Limpeza de Pele - R$ 120,00")
            print("2. Massagem Relaxante - R$ 150,00")
            print("3. Depilação - R$ 90,00")
            opcao = input("Escolha o número do serviço desejado: ")
            
            if opcao == '1':
                servico = Servico("Limpeza de Pele", 120.0)
            elif opcao == '2':
                servico = Servico("Massagem Relaxante", 150.0)
            elif opcao == '3':
                servico = Servico("Depilação", 90.0)
            else:
                print("Opção inválida!")
                return

            


if __name__ == "__main__":
    main()

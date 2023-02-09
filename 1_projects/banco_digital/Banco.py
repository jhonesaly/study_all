#Conta

class Conta:
    def __init__(self, agência, numero, saldo):
        self.agencia = agência
        self.numero = numero
        self.saldo = saldo
    
    #Métodos

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        raise NotImplementedError

    def __repr__(self):
        return f"Tipo={self.__class__.__name__}, agência={self.agencia}, numero={self.numero}, saldo={self.saldo}"

class ContaCorrente(Conta):
    def __init__(self, agência, numero, saldo=0, limite=1000):
        super().__init__(agência, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor        

class ContaPoupanca(Conta):
    def __init__(self, agência, numero, saldo=0):
        super().__init__(agência, numero, saldo)
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor


#Pessoa

#Atributos

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, novo_idade):
        self._idade = novo_idade
    

class Cliente(Pessoa):
    def __init__(self, nome, idade, *args):
        super().__init__(nome, idade)
        self.contas = list(args)
    
    def __repr__(self):
        return f"Cliente(nome={self.nome}, idade={self.idade}, conta={self.contas})"


#Banco

#Atributos

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
    
    def __repr__(self):
        return f"Banco: {self.nome} \nclientes: {self.clientes} \ncontas: {self.contas}"

#Métodos

    #Adicionar

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    #Remover

    def remover_cliente(self, cliente):
        self.clientes.remove(cliente)

    def remover_conta(self, conta):
        self.contas.remove(conta)

    #Autenticação

    def autenticar_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def autenticar_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def autenticar_agencia(self, agencia):
        for conta in self.contas:
            if conta.agencia == agencia:
                return True
        return False

conta1 = (ContaCorrente(1000, 1111))
#print(conta1)

conta2 = (ContaPoupanca(1000, 1112))
#print(conta2)

conta3 = (ContaCorrente(1000, 1113))

cliente1 = (Cliente('Alyson', 29, conta1, conta2))
#print(cliente1)
cliente2 = (Cliente('Thaís', 30, conta3))
#print(cliente2)


banco1 = Banco('Banco do Brasil')
print(banco1)

#Adicionando contas e clientes

banco1.adicionar_cliente(cliente1)
banco1.adicionar_cliente(cliente2)
banco1.adicionar_conta(conta1)
banco1.adicionar_conta(conta2)
banco1.adicionar_conta(conta3)

print(banco1)

#Operar contas dos clientes



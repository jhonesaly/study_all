import time

class Meditacao:
    def __init__(self, nome):
        self.nome = nome

    def mindfulness(self):
        print("Iniciando meditação de mindfulness...")
        time.sleep(5)
        print("Meditação de mindfulness concluída.")

    def respiracao_consciente(self):
        print("Iniciando meditação de respiração consciente...")
        time.sleep(5)
        print("Meditação de respiração consciente concluída.")
    
    def visualizacao(self):
        print("Iniciando meditação de visualização...")
        time.sleep(5)
        print("Meditação de visualização concluída.")

    def escolher_trilha(self):
        print("Escolha uma trilha sonora:")
        print("1. Sons da natureza")
        print("2. Música clássica")
        print("3. Música ambiente")
        opcao = input("Digite o número da trilha escolhida: ")
        if opcao == "1":
            print("Você escolheu sons da natureza.")
        elif opcao == "2":
            print("Você escolheu música clássica.")
        elif opcao == "3":
            print("Você escolheu música ambiente.")
        else:
            print("Opção inválida.")

    def escolher_meditacao(self):
        print("Escolha uma meditação:")
        print("1. Mindfulness")
        print("2. Respiração consciente")
        print("3. Visualização")
        opcao = input("Digite o número da meditação escolhida: ")
        if opcao == "1":
            self.mindfulness()
        elif opcao == "2":
            self.respiracao_consciente()
        elif opcao == "3":
            self.visualizacao()
        else:
            print("Opção inválida.")
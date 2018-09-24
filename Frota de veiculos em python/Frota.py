'''
1) Deve existir uma classe base para o veículo, que defina os dados comuns entre os veículos: cor, placa, modelo, marca,
  ano de fabricação, tipo de veículo, nome do condutor atual.

1.a) Os tipos possíveis de veículos são: moto e carro.
1.b) Entre os atributos, o que deve ser publico, privado ou protegido?
1.c) Deve existir uma função virtual pura que retorne a quantidade de rodas do veículo.

2) Para cada tipo de veículo, deve ser criada uma classe filha que herda a classe base do veículo.
  Em cada uma destas classes, deve ser definido uma função que retorne o número de rodas: uma moto tem duas rodas,
  um carro tem quatro.

3) Uma classe frota deve agrupar os veículos de forma que seja possível encontrar um veículo pela placa em
  um tempo constante. Use um container STL para isso.

4) Crie operações na classe frota: vender, comprar, atribuirMotorista.

'''

# import Veiculo as V

# ########## CLASSE VEICULO ########################

import os # apenas para usar o clear

class Veiculo(object):

    def __init__(self, cor, placa, modelo, marca, anoFabricacao, condutor):
        self.cor = cor
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.anoFabricacao = anoFabricacao
        self.condutor = condutor

    def mostraAttPai(self):
        print('Cor = ', self.cor)
        print('Placa = ', self.placa)
        print('Modelo = ', self.modelo)
        print('Marca = ', self.marca)
        print('anoFabricacao = ', self.anoFabricacao)
        print('Condutor = {} \n'.format(self.condutor))

# ########## CLASSE CARRO ########################

class Carro(Veiculo):
    def qtdRodas(self):
        # print('Carro possui 4 rodas')
        return 4

    def __init__(self, cor, placa, modelo, marca, anoFabricacao, condutor):
        self.tipo = 'Carro'
        super(Carro, self).__init__(cor, placa, modelo, marca, anoFabricacao, condutor)

    def mostraAtt(self):
        print('Tipo = ', self.tipo)
        super(Carro, self).mostraAttPai()


# ########## CLASSE MOTO ########################

class Moto(Veiculo):

    def qtdRodas(self):
        # print('Moto possui 2 rodas')
        return 2

    def __init__(self, cor, placa, modelo, marca, anoFabricacao, condutor):
        self.tipo = 'Moto'
        super(Moto, self).__init__(cor, placa, modelo, marca, anoFabricacao, condutor)

    def mostraAtt(self):
        print('Tipo = ', self.tipo)
        super(Moto, self).mostraAttPai()

    def alteraCondutorVar(self, condutor):
        self.condutor = condutor

# ########## CLASSE FROTA ########################

class Frota(object):

    frota = dict()

    def criaVeiculo(self, tipo, cor, placa, modelo, marca, anoFabricacao, condutor):

        if tipo == "Moto": newVeiculo = Moto(cor, placa, modelo, marca, anoFabricacao, condutor)
        if tipo == "Carro": newVeiculo = Carro(cor, placa, modelo, marca, anoFabricacao, condutor)
        return newVeiculo

    def valorHash(self, placa):
        count = 0
        total = 1
        for i in placa:
            if count < 3:
                if(type(i)!=str):
                    print("ERRO: Formato de placa invalido : ", count)
                    return 0
                a = ord(i)
                total *= a
                pass
            else:
                if(count>6 or ord(i)<48 or ord(i)>57):
                    print("ERRO: Formato de placa invalido : ", count, ord(i))
                    return 0
                total += int(i)
            count += 1
        if(count<7):
            return 0
        return total

    def addFrota(self, tipo, cor, placa, modelo, marca, ano, condutor):
        veiculo = self.criaVeiculo(tipo, cor, placa, modelo, marca, ano, condutor)
        valorHash = self.valorHash(placa)
        if(valorHash==0):
            return
        if(valorHash in self.frota):
            print('ERRO: Placa já consta no banco de dados.')
            return
        temp = {valorHash: veiculo}
        self.frota.update(temp)

    def encontrar(self):
        a = len(self.frota)
        if(a==0):
            print('Sem Registros: Frota vazia.')
            return
        self.imprime()
        print("Digite a placa do carro a ser encontrado")
        placa = input()
        valorHash = self.valorHash(placa)
        if(valorHash==0):
            return 0
        if(valorHash not in self.frota):
            print('ERRO: Placa não consta no banco de dados.')
            return 0
        print("\nVeiculo encontrado.\n")
        return valorHash

    def procura(self):
        valorHash = self.encontrar()
        if(valorHash == 0):
            return
        self.frota[valorHash].mostraAtt()
        print(" ")

    def alteraCondutor(self):
        valorHash = self.encontrar()
        if(valorHash == 0):
            return
        self.frota[valorHash].mostraAtt()
        print('Digite o novo condutor:')
        novoCondutor = input()
        self.frota[valorHash].alteraCondutorVar(novoCondutor)
        self.frota[valorHash].mostraAtt()

    def comprarVeiculo(self):
        print("Digite os dados para adicionar um veiculo.")
        tipo = 'a'
        while tipo != 'Carro' and tipo != 'Moto':
            print("Tipo(Carro/Moto):")
            tipo = input()
            pass
        print("Cor:")
        cor = input()
        print("Placa:")
        placa = input()
        while(self.valorHash(placa)==0):
            print('Valor invalido, digite novamente.')
            placa = input()
        print("Modelo:")
        modelo = input()
        print("Marca:")
        marca = input()
        print("Ano:")
        a = input()
        condicao = True
        while(condicao):
            count = 0
            for i in a:
                if(ord(i)<48 or ord(i)>57):
                    print('Valor invalido, digite novamente.')
                    break
                else:
                    count += 1
            if(count==len(a)):
                condicao = False
            else:
                a = input()
        ano = int(a)
        print("Condutor:")
        condutor = input()
        self.addFrota(tipo, cor, placa, modelo, marca, ano, condutor)

    def venderVeiculo(self):
        a = len(self.frota)
        if(a==0):
            print('Sem Registros: Frota vazia.')
            return
        self.imprime()
        print("Digite a placa do carro que foi vendido")
        placa = input()
        valorHash = self.valorHash(placa)
        if(valorHash==0):
            return
        if (valorHash not in self.frota):
            print("ERRO: Placa não consta no banco de dados.")
            return
        tamanhoantigo = len(self.frota)
        del self.frota[self.valorHash(placa)]
        tamanhonovo = len(self.frota)
        if(tamanhonovo<tamanhoantigo):
            print("Veiculo Excluido.")



    def inicializacao(self):
        self.addFrota('Moto', 'Azul', 'tpo0912', 'biz', 'honda', 2014, 'Maria')
        self.addFrota('Carro', 'amarelo', 'rep1234', 'civic', 'honda', 2010, 'Joao')
        self.addFrota('Carro', 'verde', 'pao4698', 'opala', 'chevlolet', 1995, 'Andre')
        self.addFrota('Carro', 'branco', 'tom3264', 'A6', 'bmw', 2019, 'Pedro')
        self.addFrota('Moto', 'bege', 'sjm6458', 'kavasaki', 'shuzuki', 2011, 'Antonio')
        self.addFrota('Moto', 'preto', 'aum6123', 'fazer', 'yamaha', 2005, 'Paula')

    def imprime(self):
        for i in self.frota:
            self.frota[i].mostraAtt()


f = Frota()
f.inicializacao()
while(True):
    print("Sistema de Frota\n")
    print("Comandos:\n")
    print("1 : Comprar\n")
    print("2 : Vender\n")
    print("3 : Consultar\n")
    print("4 : Alterar Condutor\n")
    print("5 : Sair\n")

    escolha = input()
    os.system('clear')
    if(escolha=='1'):
        f.comprarVeiculo()
    if(escolha=='2'):
        f.venderVeiculo()
    if(escolha=='3'):
        f.procura()
    if(escolha=='4'):
        f.alteraCondutor()
    if(escolha=='5'):
        exit()
    escolha = 0

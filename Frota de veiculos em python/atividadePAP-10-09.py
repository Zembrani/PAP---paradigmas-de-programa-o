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


# ########## CLASSE VEICULO ########################

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

# ########## CLASSE FROTA ########################

class Frota(object):
    def newVeiculo( tipo, cor, placa, modelo, marca, anoFabricacao, condutor):

        if tipo == "Moto": newVeiculo = Moto(cor, placa, modelo, marca, anoFabricacao, condutor)
        if tipo == "Carro": newVeiculo = Carro(cor, placa, modelo, marca, anoFabricacao, condutor)
        return newVeiculo

    def valorHash(placa):
        count = 0
        total = 1
        for i in placa:
            if count < 3:
                a = ord(i)
                total *= a
                pass
            else:
                total += int(i)
            count += 1

        return total

    def addFrota(tipo, cor, placa, modelo, marca, anoFabricacao, condutor):
        veiculo = Frota.newVeiculo(tipo, cor, placa, modelo, marca, anoFabricacao, condutor)
        valorHash = Frota.valorHash(placa)

        temp = {valorHash: veiculo}
        
        return temp

    def encontrar(frota, placa):
        print('procurando ..')
        return frota[Frota.valorHash(placa)]

# ########## INICIALIZACAO DA FROTA ####################################

frota = dict(Frota.addFrota('Moto', 'Azul', 'tpo0912', 'biz', 'honda', 2014, 'Maria'))
frota.update(Frota.addFrota('Carro', 'amarelo', 'rep1234', 'civic', 'honda', 2010, 'Joao'))
frota.update(Frota.addFrota('Carro', 'verde', 'pao4698', 'opala', 'chevlolet', 1995, 'Andre'))
frota.update(Frota.addFrota('Carro', 'branco', 'tom3264', 'A6', 'bmw', 2019, 'Pedro'))
frota.update(Frota.addFrota('Moto', 'bege', 'sjm6458', 'kavasaki', 'shuzuki', 2011, 'Antonio'))
frota.update(Frota.addFrota('Moto', 'preto', 'aum6123', 'fazer', 'yamaha', 2005, 'Paula'))

for i in frota:
    frota[i].mostraAtt()

temp = dict()
temp = Frota.encontrar(frota, 'rep1234')
temp.mostraAtt()

# # frota = []
# # frota.append(Frota.newVeiculo('Carro', 'amarelo', 'rep1234', 'civic', 'honda', 2010, 'Joao'))
# # frota[0].mostraAtt()

# # frota.append(Frota.newVeiculo('Moto', 'Azul', 'tpo0912', 'biz', 'honda', 2014, 'Maria'))
# frota[1].mostraAtt()



#
# teste = Carro('amarelo', 'rep1234', 'civic', 'honda', 2010, 'Joao')
# teste.mostraAtt()
#
# teste2 = Moto('Azul', 'tpo0912', 'biz', 'honda', 2014, 'Maria')
# teste2.mostraAtt()

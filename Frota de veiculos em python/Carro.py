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
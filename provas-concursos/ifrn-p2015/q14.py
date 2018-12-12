class Equipamento:
    def __init__(self, cod):
        self.codigo = cod


class Impressora(Equipamento):
    def __init__(self, cod, marca, sala):
        super().__init__(cod)
        self.marca = marca
        self.sala = sala


equip_01 = Equipamento(1)
print(equip_01)
print(equip_01.codigo)

impress_01 = Impressora(2, 'HP', 'lab.01')
print(impress_01)
print('Dados impressora: {} [Códifo] - {} [Marca] - {} [Sala]'.format(impress_01.codigo,
                                                                      impress_01.marca, impress_01.sala))

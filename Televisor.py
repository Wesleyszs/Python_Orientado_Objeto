class televisor:
    def __init__(self, fab, modelo):
        self.fabricante = fab
        self.modelo = modelo  # Corrigido aqui
        self.canal_Atual = None
        self.lista_de_Canais = []
        self.volume = 20

    def aumentar_volume(self, valor):
        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100

    def diminuir_volume(self, valor):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def trocar_canal(self, canal):
        if canal in self.lista_de_Canais:
            self.canal_Atual = canal

    def sintonizar_canal(self, canal):
        if canal not in self.lista_de_Canais:
            self.lista_de_Canais.append(canal)


class controleRemoto:
    def __init__(self, tv):
        self.tv = tv

    def aumentar_volume(self, valor):
        self.tv.aumentar_volume(valor)

    def diminuir_volume(self, valor):
        self.tv.diminuir_volume(valor)

    def trocar_canal(self, canal):
        self.tv.trocar_canal(canal)  # Passando o canal como argumento

    def sintonizar_canal(self, canal):
        self.tv.sintonizar_canal(canal)

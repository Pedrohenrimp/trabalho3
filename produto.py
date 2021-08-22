class Produto():
    def __init__(self, nome, val, qtd):
        self.__nome = nome
        self.__valor = val
        self.__quantidade = qtd
    def atualizaQuantidade(self, qtd):
        self.__quantidade = qtd
        print("nova quantidade:", qtd)
    def setQuantidade(self, qtd):
        self.__quantidade = qtd
    def getQuantidade(self):
        return self.__quantidade
    def getNome(self):
        return self.__nome
    def getValor(self):
        return self.__valor
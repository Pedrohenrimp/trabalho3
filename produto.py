class Produto():
    def __init__(self, nome, val, qtd):
        self.nome = nome
        self.valor = val
        self.quantidade = qtd
    def atualizaQuantidade(self, qtd):
        self.quantidade = qtd
        print("nova quantidade:", qtd)
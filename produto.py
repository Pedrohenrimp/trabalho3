class Produto():
    def __init__(self, nome, val, qtd):
        self.nome = nome
        self.valor = val
        self.quantidade = qtd
    def atualizaProduto(self, val, qtd):
        self.valor = val
        self.quantidade = qtd
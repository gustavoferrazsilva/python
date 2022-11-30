class Recibo:

    def __init__(self,nome):
        self.nome = nome

    def descricao(self,valor): #não é possível ter atributos com nome de função
        self._descricao = valor

    @property
    def valor(self):
        return(self._valor)
    
    @valor.setter 
    def valor(self,_valor):
        self._valor = _valor

    def __str__(self):
        texto = f' Recebemos de {self.nome} a quantia de R$ {self._valor}'
        descricao = f'\nReferente {self._descricao}'
        titulo = 'Recibo'.center(len(texto), '*')
        dados = f'{titulo}\n{texto}{descricao}'
        return (dados)
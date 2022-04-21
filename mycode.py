# Filtro de Faturas
# Você deverá implementar um filtro para uma coleção de faturas. Uma fatura contém um código, um valor, uma data,
# e pertence a um cliente. Um cliente tem um nome, data de inclusão e um estado do país.
#
# O filtro deverá então, dado uma lista de faturas, remover as que se encaixam em algum dos critérios abaixo:
# Se o valor da fatura for menor que 2000;
# Se o valor da fatura estiver entre 2000 e 2500 e a data for menor ou igual a de um mês atrás;
# Se o valor da fatura estiver entre 2500 e 3000 e a data de inclusão do cliente for menor ou igual a 2 meses atrás;
# Se o valor da fatura for maior que 4000 e pertencer a algum estado da região sudeste do Brasil.
# Você deve criar todo o código responsável pelo filtro de faturas.
# Uma classe com o método "main()" deverá ser entregue ao final, com exemplo de uso das unidades criadas.

class cliente:
    def __init__(self, nome, data, estado):
        self.nome = nome
        self.data = data
        self.estado = estado

class fatura(cliente):
    def __init__(self, codigo, valor, data, nome, estado):
        super().__init__(nome, data, estado)
        self.codigo = codigo
        self.valor = valor
        self.data = data


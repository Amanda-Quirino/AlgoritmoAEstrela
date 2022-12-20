class algoritmo_estrela:
	def __init__(self, matrix_direta, matrix_distancia, lista_fronteira, lista_h, lista_relacionamentos):
		self.matrix_direct = matrix_direta
		self.matrix_dist = matrix_distancia
		self.border_list = lista_fronteira
		self.h_list = lista_h
        self.links_list = lista_relacionamentos
		self.node = 0
    def select(self):
	    self.node = lista_h.index(min(lista_h))
    def test(self, destino):
	    return self.border_list[self.node] == destino
    def verify(self):
    def add_border(self):


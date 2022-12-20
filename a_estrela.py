from matriz import *

class algoritmo_estrela:
	def __init__(self, matrix_direta, matrix_distancia, lista_vizinhos, lista_h, lista_relacionamentos, no_partida, no_destino):
		
		#Não sei para q serve
		self.h_list = lista_h
		self.links_list = lista_relacionamentos

		#Setando as matrizes de distância real, direta e a lista de vizinhos
		self.matrix_direct = matrix_direta
		self.matrix_real = matrix_real
		self.vizinhos_lista = lista_vizinhos

		#Variável para armazenar no o nó atual, inical e final
		self.no_inicial = no_partida - 1
		self.no_final = no_destino - 1
		self.no_atual = self.no_inicial
		#Variável que irá armazenar o custo atual do caminho e a fronteira
		self.g = 0 
		self.border_list = [self.no_inicial]

	def select(self):
		self.node = self.lista_h.index(min(self.lista_h))
	def test(self, destino):
		return self.border_list[self.node] == destino

	def execution(self):
		#Condição de parada -> Quando o primeiro valor da lista for o nó final
		while(self.no_final != self.border_list[0]):

			self.add_border()


		

	#Função Heurística
	def func_h(self):
		pass
	
	#função Gulosa
	def func_g(self):
		pass

	def verify(self):
		pass

	#Temos que realizar essa conversão sempre, melhor trabalhar com tempo em minutos
	def converte_tempo(val):
		return (val / 30) * 60

	def verificar_troca_estacao(self, no):
		presente = False

		for lista in ESTACOES.values():
			if no in lista and self.no_atual in lista:
				return 0

			else:
				return 4


	def ordenar_borda(self, no):
		add = true
		"""
		Aqui eu to fazendo uma inserção ordenada na lista, para isso eu comparo o valor da heuristica com o g(Custo real até agora) com a 
		distância do nó atual para esse próximo nó que está sendo inserido na lista, para saber qual será sua posição na fronteira

		!!Esborço, temos que converter para tempo
		!!Acredito que vamos desmembrar essa função em g e h

		"""
		for x in range(len(self.border_list)):
			if matrix_direct[self.no][self.no_fina] + matrix_real[self.no][self.no_atual] + self.g < matrix_direct[self.border_list[x]][self.no_final] + matrix_real[self.no][self.no_atual] + self.g:
				self.border_list.insert(x, self.no)
				add = false

		if add:
			self.border_list.append(self.no)
			

	def adicionar_borda(self):

		#Percorre a lista de vizinhos e os adiciona em uma lista
		#Toda vez que ele insere um novo valor na borda, ele já entra ordenado
		for nos in VIZINHOS_NO[self.no_atual]:
			self.ordenar_borda(nos)




		


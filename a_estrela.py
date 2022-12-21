from matriz import *

"""
Classe nó para evitar a gambiarra de várias listas e possiblitar chegar no nó final e ir voltando apontando para o pai

no -> Número nó
g -> Valor g
f -> Valor de f = g + h
pai -> Pai desse nó
"""

class no:
	def __init__(self, no, g, f, pai):
		self.no = no
		self.g = g
		self.f = f
		self.pai = pai

class algoritmo_estrela:
	def __init__(self, matrix_direta, matrix_distancia, lista_vizinhos, no_partida, no_destino):
		
		#Setando as matrizes de distância real, direta e a lista de vizinhos
		self.matrix_direct = matrix_direta
		self.matrix_real = matrix_distancia
		self.vizinhos_lista = lista_vizinhos

		#Variável para armazenar no o nó atual, inical e final
		self.no_inicial = no_partida - 1
		self.no_final = no_destino - 1
		self.no_atual = self.no_inicial
		
		#Variável que irá armazenar o custo atual do caminho e a fronteira
		self.g = 0 
		self.border_list = [self.no_inicial]
		self.border_list_f = [self.matrix_direct[self.no_inicial][self.no_final]]
		self.border_list_g = [0]
		self.caminho_final = []

	def execution(self):
		#Condição de parada -> Quando o primeiro valor da lista for o nó final
		while(self.no_final != self.border_list[0]):
			caminho = self.adicionar_borda()
			if not caminho:
				self.caminho_final.append(self.border_list.pop(0))
			else:
				self.border_list.pop(0)

			self.border_list_f.pop(0)
			self.border_list_g.pop(0)
			self.no_atual = self.border_list[0]

		self.caminho_final.append(self.no_final)
		self.print_caminho()

	def print_caminho(self):
		for x in self.caminho_final:
			print(f"{x + 1} -> ", end='')

	#Temos que realizar essa conversão sempre, melhor trabalhar com tempo em minutos
	def converte_tempo(self, val):
		return (val / 30) * 60

	#Função Heurística -> Distancia até o nó final
	def func_h(self, no):
		return self.matrix_direct[no][self.no_final]

	#função Gulosa
	def func_g(self, no):
		#Soma o valor do g até agora com a distância entre as duas estações
		return self.matrix_real[no][self.no_atual] + self.border_list_g[self.border_list.index(self.no_atual)]

	#Função que serve para testar se o no_atual e o nó para ser o próximo estão na mesma estaçãou ou em estações diferentes
	#Retorna o valor em minutos caso haja uma troca de estação
	def verificar_troca_estacao(self, no):
		
		for lista in ESTACOES.values():
			if no in lista and self.no_atual in lista:
				return 0

		return 4


	def ordenar_borda(self, no):
		#Inicialmente calculo o valor do g, h e f do nó atual, após isso faço a inserção na fronteira na posição correta

		add = True
		g = self.func_g(no)
		h = self.func_h(no)
		f = g + h
		f = self.converte_tempo(f) + self.verificar_troca_estacao(no)

		#Inserção ordenada
		for x in range(len(self.border_list)):
			if  f < self.border_list_f[x] and x == 0: # caso em que ele é o menor valor da fronteira
				self.border_list.insert(x, no)
				self.border_list_f.insert(x, f)
				self.border_list_g.insert(x, g)
				add = False

			elif self.border_list_f[x - 1] < f < self.border_list_f[x]: # valor no meio da fronteira
				self.border_list.insert(x, no)
				self.border_list_f.insert(x, f)
				self.border_list_g.insert(x, g)
				add = False

		if add: #Maior valor da fronteira
			self.border_list.append(no)
			self.border_list_g.append(g)
			self.border_list_f.append(f)
			

	def adicionar_borda(self):
		#Percorre a lista de vizinhos e os adiciona em uma lista
		#Toda vez que ele insere um novo valor na borda, ele já entra ordenado
		for nos in VIZINHOS_NO[self.no_atual]:
			self.ordenar_borda(nos)

if __name__ == '__main__':
	no_inicial = int(input("Digite o Nó inicial: E"))
	no_final = int(input("Digite o Nó Final: E"))

	A = algoritmo_estrela(DIST_DIRET, DIST_REAL, VIZINHOS_NO, no_inicial, no_final)
	A.execution()

from matriz import *

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

		#Declaração de Arrays
		self.border_list = [self.no_inicial] #Armazenar a fronteira
		self.border_list_f = [self.converte_tempo(self.matrix_direct[self.no_inicial][self.no_final])] # Armazena o F do nó inicial
		self.border_list_g = [0] #Armazena o G do nó inicial
		self.pais = [-1] * 14 #Array que indica o pai daquele nó
		self.lista_visitados = [] #Array de controle que armazena os nós já visitados para evitar que um nó seja sobrescrito
		self.pais.insert(self.no_atual, 'HEAD') # Inserindo na lista de pais dos nós o HEAD
		self.lista_visitados.append(self.no_inicial) #Adcionando o nó inicial a lista de nós iniciais

	def execution(self):

		#Condição de parada -> Quando o primeiro valor da lista for o nó final
		#Adiciona os vizinhos a borda e depois tira esse Elemento
		while(self.no_final != self.border_list[0]):
			self.adicionar_borda()
			self.border_list.pop(0)
			self.border_list_f.pop(0)
			self.border_list_g.pop(0)
			self.no_atual = self.border_list[0] #Atualiza a variável de nó atual, é a partir dela que adicionamos os vizinhos a borda

		self.print_caminho_alternativo()

	#Função que realiza o print final
	def print_caminho_alternativo(self):
		#Print do nó final
		no_atual = self.pais[self.no_final]
		print(f"{self.no_final + 1} -> ", end='')

		#Print do caminho
		while no_atual != 'HEAD':
			print(f"{no_atual + 1} -> ", end='')

			no_atual = self.pais[no_atual]

	#Conversção de km/h -> horas -> minutos
	"""
	Input: Distância entre nós
	Output: Minutos
	"""
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


	#Função responsável por inserir na borda, na lista de F e na lista de valores G
	#Modularização, evitar ficar repetindo código
	def inserir_borda(self, pos, no, f, g):
		self.border_list.insert(pos, no)
		self.border_list_f.insert(pos, f)
		self.border_list_g.insert(pos, g)


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
				self.inserir_borda(x, no, f, g)
				add = False
				break
				

			elif self.border_list_f[x - 1] <= f < self.border_list_f[x]: # valor no meio da fronteira
				self.inserir_borda(x, no, f, g)
				add = False
				break
				
		if add: #Maior valor da fronteira
			self.inserir_borda(len(self.border_list), no, f, g)
			

	def adicionar_borda(self):
		#Percorre a lista de vizinhos e os adiciona em uma lista
		#Toda vez que ele insere um novo valor na borda, ele já entra ordenado
		for nos in VIZINHOS_NO[self.no_atual]:
			if nos not in self.lista_visitados:
				self.lista_visitados.append(nos)
				self.pais[nos] = self.no_atual
			self.ordenar_borda(nos)

if __name__ == '__main__':
	#Recebendo dados das Estações
	no_inicial = int(input("Digite o Nó inicial: E"))
	no_final = int(input("Digite o Nó Final: E"))
	
	#Declarando Classe e Executando o Algoritmo
	A = algoritmo_estrela(DIST_DIRET, DIST_REAL, VIZINHOS_NO, no_inicial, no_final)
	A.execution()
from matriz import *

class vertice:
	def __init__(self, vertice,f, g, pai, cor, trocas) -> None:
		self.vertice = vertice
		self.f = f
		self.g = g
		self.pai = pai
		self.estacao = cor
		self.n_trocas = trocas

class algoritmo_estrela:
	def __init__(self, matrix_direta, matrix_distancia, lista_vizinhos, no_partida, no_destino):
		
		#Setando as matrizes de distância real, direta e a lista de vizinhos
		self.matrix_direct = matrix_direta
		self.matrix_real = matrix_distancia
		self.vizinhos_lista = lista_vizinhos

		self.no_final = no_destino - 1
		#Variável para armazenar no o nó atual, inical e final
		self.no_inicial = vertice(no_partida - 1, self.converte_tempo(self.matrix_direct[no_partida - 1][self.no_final]), 0, 'HEAD', 'NULL', 0)
		self.no_atual = self.no_inicial

		#Declaração de Arrays
		self.border_list = [self.no_inicial] #Armazenar a fronteira

	def execution(self):
		iteracao = 1
		#Condição de parada -> Quando o primeiro valor da lista for o nó final
		#Adiciona os vizinhos a borda e depois tira esse Elemento
		while(self.no_final != self.border_list[0].vertice):

			self.adicionar_borda()
			self.print_fronteira(iteracao)
			self.border_list.pop(0)
			self.no_atual = self.border_list[0] #Atualiza a variável de nó atual, é a partir dela que adicionamos os vizinhos a borda
			iteracao += 1

		self.print_caminho_alternativo()

	def print_fronteira(self, interacao):
		print("\n\nFRONTEIRA")
		print(f"Fronteira Iteração {interacao}:")
		for x in self.border_list:
			print(f'E{x.vertice + 1} - Tempo até agora = {self.converte_tempo(x.g)}')
		print("")

	#Função que realiza o print final
	def print_caminho_alternativo(self):

		lista_final = []

		while self.no_atual.pai != 'HEAD':

			lista_final.append(self.no_atual.vertice + 1)
			self.no_atual = self.no_atual.pai

		lista_final.append(self.no_atual.vertice + 1)

		for x in range(len(lista_final) -1 , -1, -1):
			if x != 0:
				print(f'{lista_final[x]} -> ', end='')

			else:
				print(lista_final[x])


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
		return self.matrix_real[no][self.no_atual.vertice] + self.no_atual.g
	#self.border_list_g[self.border_list.index(self.no_atual)]

	#Função que serve para testar se o no_atual e o nó para ser o próximo estão na mesma estaçãou ou em estações diferentes
	#Retorna o valor em minutos caso haja uma troca de estação
	def verificar_troca_estacao(self, no):

		estacao_ligacao = ""

		if no in ESTACOES['azul'] and self.no_atual.vertice in ESTACOES['azul']:
			estacao_ligacao = 'azul'

		elif no in ESTACOES['amarelo'] and self.no_atual.vertice in ESTACOES['amarelo']:
			estacao_ligacao = 'amarelo'

		elif no in ESTACOES['vermelho'] and self.no_atual.vertice in ESTACOES['vermelho']:
			estacao_ligacao = 'vermelho'

		elif no in ESTACOES['verde'] and self.no_atual.vertice in ESTACOES['verde']:
			estacao_ligacao = 'verde'

		return estacao_ligacao
	
	def adicao_troca_estacao(self, cor, no):
		if self.no_atual.estacao == 'NULL' or cor == self.no_atual.estacao:
			return 0
		elif cor != self.no_atual.estacao:
			print(f"Passei aqui - {self.no_atual.vertice + 1} -> {no + 1}")
			return 1

	#Função responsável por inserir na borda, na lista de F e na lista de valores G
	#Modularização, evitar ficar repetindo código
	def inserir_borda(self, pos, no, f, g, cor, trocas):
		node = vertice(no, f, g, self.no_atual, cor, trocas)
		self.border_list.insert(pos, node)

	def ordenar_borda(self, no):
		#Inicialmente calculo o valor do g, h e f do nó atual, após isso faço a inserção na fronteira na posição correta

		add = True
		g = self.func_g(no)
		h = self.func_h(no)
		f = g + h

		cor_estacao = self.verificar_troca_estacao(no)
		trocas = self.no_atual.n_trocas + self.adicao_troca_estacao(cor_estacao, no)

		f = self.converte_tempo(f) + 4 * trocas

		#Inserção ordenada
		for x in range(len(self.border_list)):
			if  f < self.border_list[x].f and x == 0: # caso em que ele é o menor valor da fronteira 0
				self.inserir_borda(x, no, f, g, cor_estacao, trocas)
				add = False
				break
				

			elif self.border_list[x - 1].f <= f < self.border_list[x].f: # valor no meio da fronteira
				self.inserir_borda(x, no, f, g, cor_estacao, trocas)
				add = False
				break
				
		if add: #Maior valor da fronteira
			self.inserir_borda(len(self.border_list), no, f, g, cor_estacao, trocas)
			

	def adicionar_borda(self):
		#Percorre a lista de vizinhos e os adiciona em uma lista
		#Toda vez que ele insere um novo valor na borda, ele já entra ordenado
		for nos in VIZINHOS_NO[self.no_atual.vertice]:
				self.ordenar_borda(nos)

if __name__ == '__main__':
	#Recebendo dados das Estações
	no_inicial = int(input("Digite o Nó inicial: E"))
	no_final = int(input("Digite o Nó Final: E"))
	
	#Declarando Classe e Executando o Algoritmo
	A = algoritmo_estrela(DIST_DIRET, DIST_REAL, VIZINHOS_NO, no_inicial, no_final)
	A.execution()
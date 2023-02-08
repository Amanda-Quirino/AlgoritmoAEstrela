# Busca_Heuristica

### Algoritmo A* - Problema do metrô de Paris 

#### Problema abordado: 
Suponha que queremos construir um sistema para auxiliar um usuário do metrô de Paris a saber o trajeto mais rápido entre a estação onde ele se encontra e a estação de destino. O usuário tem um painel com o mapa, podendo selecionar a sua estação de destino. O sistema então acende as luzes sobre o mapa mostrando o melhor trajeto a seguir (em termos de quais estações ele vai atravessar e quais as conexões mais rápidas a fazer – se for o caso). Para 	facilitar a vida, consideramos apenas 4 linhas do metrô.
Considere que:
* a distância em linha reta entre duas estações quaisquer é dada pela tabela 1 e a distância real é dada pela tabela 2.
* a velocidade média de um trem é de 30km/h;
* o tempo gasto para trocar de linha dentro de mesma estação (fazer baldeação) é de 4 minutos.


#### Mapa de Paris:

![image](https://user-images.githubusercontent.com/94120629/217413936-858e5d99-b955-4f20-ba34-5ad97abd1b20.png)


#### Inputs:
* 1º: indicar número da estação inicial
> ![no_inicial](https://user-images.githubusercontent.com/94120629/217416604-2337f803-cba8-41e5-8a7c-5556d73a50f9.png)
* 2º: inidicar número da estação final
> ![no_final](https://user-images.githubusercontent.com/94120629/217416625-b719ea12-b112-4617-8ef0-291bd13b86ff.png)

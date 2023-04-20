"""4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca,
a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia,
qual estará mais próximo a cidade de Ribeirão Preto?



IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.
"""
carro = 110
caminhao = 80
distancia = 100

tempo_carro = carro / distancia
print(tempo_carro)

tempo_caminhao = (caminhao / distancia) + (2 * 0.05)
print(tempo_caminhao)
'''
Quando os veículos se cruzarem na rodovia, estará mais próximo de Ribeirão Preto aquele que ainda tiver menos distância a percorrer até chegar a essa cidade. 
Como o carro percorreu 49,5 km até o ponto de cruzamento, ele ainda precisa percorrer mais 50,5 km até Ribeirão Preto (os outros 50 km até Franca já foram percorridos). 
Já o caminhão percorreu 63,2 km até o ponto de cruzamento, o que significa que ele ainda precisa percorrer 36,8 km até Ribeirão Preto.

Portanto, o carro estará mais próximo de Ribeirão Preto quando eles se cruzarem na rodovia.
'''
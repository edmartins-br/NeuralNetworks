#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:42:36 2019
@author: eduardo
"""
import numpy as np
from sklearn import datasets
# DEFINE A FUNÇÃO SIGMOID PARA SER USADA PELA CAMADA OCULTA COMO FUNÇÃO DE ATIVAÇÃO

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))
np.exp(1) #resultado = numero de Euler 2.718281828459045

def sigmoidDerivada(sig):
    return sig * (1-sig) # Implementação da derivada da função sigmoide

base = datasets.load_breast_cancer()
entradas = base.data
valoresSaida = base.target
saidas = np.empty([569, 1], dtype = int)

for i in range(569):
    saidas[i] = valoresSaida[i]

#DEFINIR OS CONJUTNOS DE PESOS
    
#Pesos que saem das entradas e apontam para as camadas ocultas (neuronios)
#pesos0 = np.array([[-0.424, -0.740, -0.961],
#                   [0.358, -0.577, -0.469]])
    
#Pesos para cada um dos neuronios ocultos que estão apontando para a camada de saida
#pesos1 = np.array([[-0.017], [-0.893], [0.148]])

# O CORRTO É INICIAR OS PESOS ALEATORIAMENTE - 3 é o numero de neuronios na camada oculta
pesos0 = 2 * np.random.random((30,5)) - 1 #mesclar valores positivos e negativos
pesos1 = 2 * np.random.random((5,1)) - 1

#Quantidade de vezes que os erros serão atualizados, para isso usa-se a variavel EPOCAS
epocas = 10000
taxaAprendizagem = 0.2
momento = 1

#loop para aplicação da função Sigmoidal
cont = 0

for j in range(epocas):
    camadaEntrada = entradas    
    cont += 1
    # Multiplicacao e soma entre a camada de entrada e a camada oculta
    somaSinapse0 = np.dot(camadaEntrada, pesos0) 
    
    # Gerar os valores para a camada oculta aplicando a função sigmoidal *(função de ativação)
    camadaOculta = sigmoid(somaSinapse0) # VALORES DAS ATIVAÇÕES FINAIS
    
    # REALIZAR A SOMA E APLICAÇÃO DA FUNÇÃO DE ATIVAÇÃO
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)    
    print('Calculando {}%'.format(cont))
    
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print("Percentual de Erro" + str(mediaAbsoluta))
    
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida
    
    pesos1Transposta = pesos1.T
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)
    
    #É preciso fazer a transposta da matriz para que se possa realizar o DOT PRODUCT deixando a camada oculta com 4 colunas
    # ao invés de 4 linhas, pois a matriz do deltaSaida possui 4 linhas
    camadaOcultaTransposta = camadaOculta.T #matriz transposta
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
    
    #IMPLEMENTANDO O BACK PROPAGATION para atualização dos pesos - ajuste dos pesos
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)
    
    # alterar os pesos que vão da camada de entrada até a camada oculta
    camadaEntradaTransposta = camadaEntrada.T # trocando as linahs por colunas
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (pesosNovo0 * taxaAprendizagem)
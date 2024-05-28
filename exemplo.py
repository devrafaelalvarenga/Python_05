# * nao define a quantidade de argumentos que a função vai receber
from time import sleep


def contador(* numeros):
    contagem = len(numeros)
    print(f'Recebi os numeros {numeros}. Ao todo são {contagem} numeros.')


contador(2, 3, 4, 6, 7, 8)

#

valores = [2, 4, 6, 8, 10]


def dobra_valores(lista):
    posicao = 0
    while posicao < len(valores):
        lista[posicao] *= 2
        posicao += 1


dobra_valores(valores)
print(valores)

#


def somar(* vlr):
    soma = 0
    for num in vlr:
        soma += num
    print(f'Somando os valores {vlr} temos {soma} ')


somar(2, 3, 4)
somar(50, 40)

#

largura = float(input('Informe a largura do terreno: '))
comprimento = float(input('Informe o comprimento do terreno: '))


def calcular_area(largura, comprimento):
    area = largura*comprimento
    print(f'A area de um terreno {largura}x{comprimento} é {area} m²')


calcular_area(largura=largura, comprimento=comprimento)

#

texto: str = input('Texto: ')


def escreva(texto):
    tamanho = len(texto)
    intro = '~' * tamanho
    print(intro)
    print(texto)
    print(intro)


escreva(texto=texto)

#


def contador(inicio: int, fim: int, passo: int):
    if passo < 0:
        passo *= -1  # transforma negativo em positivo
    if passo == 0:
        print('Valor para o passo invalido')
        exit()
    print(f'Contagem de {inicio} a {fim} de {passo} em {passo}: ')
    sleep(2)

    if inicio < fim:
        inicio_contagem: int = inicio
        while inicio_contagem <= fim:
            # flush=True elimina o buffer e executa o sleep na contagem
            print(f'{inicio_contagem}', end=' ', flush=True)
            sleep(0.2)
            inicio_contagem += passo
        print('Fim!')
    else:
        inicio_contagem: int = inicio
        while inicio_contagem >= fim:
            # flush=True elimina o buffer e executa o sleep na contagem
            print(f'{inicio_contagem}', end=' ', flush=True)
            sleep(0.2)
            inicio_contagem -= passo
        print('Fim!')
    print('-' * 40)


contador(1, 10, 1)
contador(10, 0, 2)
print('Informe a sua contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio=inicio, fim=fim, passo=passo)

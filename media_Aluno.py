
print("Bem vindo ao Cálculo de Média!")
nome = input('Escreva seu nome: ')
nota1 = int(input('Escreva sua Primeira nota: '))
nota2 = int(input('Escreva sua Segunda nota: '))
nota3 = int(input('Escreva sua terceira nota '))

media = (nota1 + nota2 + nota3)/3

if(media >=7):
    print(f'Parabéns {nome} você foi aprovado com a média final de: {media}')
elif (media >=6):
    print(f'{nome}, você está de recuperação precisa de {7 - media} para passar!')
else:
    print(f'{nome} você foi reprovado. :(')
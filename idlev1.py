from time import sleep
print('#' * 18)
print('INCREMENTAL MATRIX ')
print('#' * 18)
for c in range(1, 4):
	sleep(0.5)
	print('.')
print('[Carregando dados de consciência] ')
for c in range(1, 4):
	sleep(0.3)
	print('.')
print('Dados carregados com sucesso! ')
sleep(1)
print('Bem-vindo à matrix! ')
sleep(1)
print('Antes de começar, realize uma decisão crucial... ')
escolha = str(input('Em uma situação hipotética em que duas pílulas de cores diferentes estão dispostas lado a lado em uma mesa diretamente na sua frente, você escolhe (AZUL) ou (VERMELHO): ')).upper().strip()
azul = 0
vermelho = 0
if escolha == 'AZUL':
	azul += 1
elif escolha == 'VERMELHO':
	vermelho += 1
while vermelho != 0 and vermelho < 10:
	print('!!!FALHA NA MATRIX!!!')
	vermelho += 1
	
	
	
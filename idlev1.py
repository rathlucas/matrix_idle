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
escolha = str(input('\nEm uma situação hipotética em que duas pílulas de cores diferentes estão dispostas lado a lado em uma mesa diretamente na sua frente, você escolhe \033[34m(AZUL)\033[m ou \033[31m(VERMELHO):\033[m ')).upper().strip()
azul = 0
vermelho = 0
retry = ' '
if escolha == 'AZUL':
	azul += 1
while escolha != 'VERMELHO' != 'AZUL':
	retry = str(input('Opção inválida! Digite vermelho ou azul: '))
if escolha == 'VERMELHO':
	vermelho += 1
while vermelho != 0 and vermelho < 10:
	print('\n!!!FALHA NA MATRIX!!!')
	vermelho += 1
if vermelho > 1:
	print('\n\033[31mSábia escolha, jovem guerreiro...\033[m')


	
	
	
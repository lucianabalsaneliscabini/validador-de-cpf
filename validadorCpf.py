cpf = input('Digite seu cpf: ')

while len(cpf) != 11:
    print('\033[32mPor favor, digite um valor válido !\033[m')
    cpf = input('Digite seu cpf: ')

validateNumbers = cpf[:9]

multiplicador_1 = 10
somador_1= 0


for number in validateNumbers:
    result = int(number) * multiplicador_1
    multiplicador_1 -= 1
    somador_1 += result
  
DigitlCalculation = 11 - (somador_1 % 11)
primeiroDigito = DigitlCalculation

if primeiroDigito > 9:
    primeiroDigito = 0
    primeiroDigito = str(primeiroDigito)
    concatenation = validateNumbers + primeiroDigito
else:
    primeiroDigito = str(primeiroDigito)
    concatenation = validateNumbers + primeiroDigito

somador_2 = 0
multiplicador_2 = 11

for number in concatenation:
    result = int(number) * multiplicador_2
    multiplicador_2 -= 1
    somador_2 += result

DigitlCalculation = 11 - (somador_2 % 11)
segundoDigito = DigitlCalculation

if segundoDigito > 9:
    segundoDigito = 0


primeiroDigito = str(primeiroDigito)
segundoDigito = str(segundoDigito)

juntar = primeiroDigito + segundoDigito
validateNumbers = cpf[9:11]

if juntar == validateNumbers:
    print('\033[34mCPF VÁLIDO\033[m')
else:
    print('\033[31mCPF INVÁLIDO\033[m')

name  = input('Olá, seja bem vindo, qual o seu nome?')
anoNasc = input('Muito bem {}, em qual ano você nasceu?'.format(name))
mesNasc = input('{}, em que mês você nasceu?'.format(name))
diaNasc = input('Finalmente, qual foi o dia do seu nascimento {}?'.format(name))
print('Então {}, você nasceu em {}/{}/{}, está correto?'.format(name, diaNasc, mesNasc, anoNasc))

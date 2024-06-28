[09:29] Joao Vitor Carlos De Almeida Araujo
claudiaNotas = [10, 7, 5, 6]
joaoNotas = [3, 5, 6, 5]
thiagoNotas = [10, 7, 7, 9]
samuelNotas = [10, 9, 9, 8]
 
# Faz a média das notas do bimestre
claudiaMedia = sum(claudiaNotas ) / 4
joaoMedia = sum(joaoNotas) / 4
thiagoMedia = sum(thiagoNotas) / 4
samuelMedia = sum(samuelNotas ) / 4
 
# Determina se o aluno passou ou não de acordo com o valor da sua média
if claudiaMedia >= 5:
    claudiaAprovacao = 'Aprovado'
else:
    claudiaAprovacao = 'Reprovado'
 
if joaoMedia >= 5:
    joaoAprovacao = 'Aprovado'
else:
    joaoAprovacao = 'Reprovado'
   
if thiagoMedia >= 5:
    thiagoAprovacao = 'Aprovado'
else:
    thiagoAprovacao = 'Reprovado'
   
if samuelMedia >= 5:
    samuelAprovacao = 'Aprovado'
else:
    samuelAprovacao = 'Reprovado'
   
# Mostra no terminal todos os valores pedidos
print('===\tNota média dos alunos\t===')
print(f'Claudia: {claudiaMedia}\t{claudiaAprovacao}\nJoão: {joaoMedia}\t{joaoAprovacao}\nThiago: {thiagoMedia}\t{thiagoAprovacao}\nSamuel: {samuelMedia}\t{samuelAprovacao} ')
 
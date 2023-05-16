print('='*90)
print('Lista de candidatos / suas respectivas notas'.upper())                                   
                                             #1 #4 #7 #10
candidatos =       [{'Nome':'José', 'Nota':'e5_t3_p7_s8'},  
                    {'Nome':'Augusto', 'Nota':'e4_t5_p8_s7'},     # os : devem estar fora das aspas para que entenda a atribuição
                    {'Nome':'Simone', 'Nota':'e5_t5_p9_s8'},      # dos índices ('Nome', 'Nota') aos seus valores ('José', 'eX_tX_pX_sX')
                    {'Nome':'Patricia', 'Nota':'e4_t6_p8_s5'},
                    {'Nome':'Matheus', 'Nota' : 'e4_t4_p7_s8'}] 

print('='*90)
# a função def foi criada no intuito de armazenar os inputs das notas que serão pedidas ao usuário
def nota_candidato(e_nota, t_nota, p_nota, s_nota):
    candidato_aprovado = []

# defini o nome 'busca', pois o objetivo da função é buscar a nota dos candidatos na lista para percorrer o loop para verificação
# dentro da lista de 'candidatos'
    for index, busca in enumerate(candidatos):
        
        nome = busca['Nome']    # as variáveis 'nome' e 'nota' guardam os valores que serão devolvidos na 'busca', que após 
        nota = busca['Nota']    # acessar os índices dentro do colchetes, retornarão os valores correspondentes a eles, 
        print('-'*90)           # por ex.: Nome: Matheus
        print(f'Candidato: {index}: {nome},  Nota: {nota}')
        print('=' * 90)
# loop desta linha foi realocado
        conv_e = int(nota[1])
        conv_t = int(nota[4])
        conv_p = int(nota[7])
        conv_s = int(nota[10])
        

    # correção do uso do operador: aqui é realizado a comparação da nota mínima inserida pelo usuário com a nota do candidato pré-disponível,
    # se a nota mínima exigida for maior que a nota do candidato, ele é excluído da lista e não entra no .append()
        if e_nota <= conv_e and t_nota <= conv_t and p_nota <= conv_p and s_nota <= conv_s:
            candidato_aprovado.append(busca)
    print('\033[92mSigla: e = entrevista, t = exame teórico, p = exame prático, s = soft skills\033[92m')
    print('-'*90)
    
# aqui o if not está sendo usado por questão de praticidade e também de ordem, para testar se a condição
# da lista é verdadeira ou falsa e ser executada somente se/ou nenhum candidato corresponder e ser impresso somente se verdadeiro.
    if not candidato_aprovado:
       print('\033[91mNENHUM CANDIDATO CORRESPONDE A ESTES CRITÉRIOS\033[91m')
       print('-'*90)

    # loop para percorrer os candidatos já verificados e adicionados na lista e imprime os resultados dados como verdadeiros
    for busca in candidato_aprovado:
        if True:
            print(f'Candidato Aprovado:\nNome: {busca["Nome"]}, Nota: {busca["Nota"]}')
        print('-' * 90)

    return candidato_aprovado 
## o retorno sempre deve estar em último lugar em relação aos loops e verificação, 
#pois somente assim será possível pegar os resultados de forma adequada


## input para buscar os candidatos através dos critérios das notas 
e_nota = int(input('Qual o valor mínimo do resultado da entrevista? '))
t_nota = int(input('Qual o valor mínimo do exame teórico? '))
p_nota = int(input('Qual o valor mínimo do exame prático? '))
s_nota = int(input('Qual a nota mínima das habilidades de soft skills? '))


# após toda a etapa de verificação, aqui chamamos a função para nos entregar o resultado dos aprovados e os atribui para a lista vazia
candidato_aprovado = nota_candidato(e_nota, t_nota, p_nota, s_nota)

## CORREÇÕES NECESSÁRIAS NO CÓDIGO: Sem quebras, porém o sistema de verificação não está condizendo os valores,
# o que faz dar erro na checagem e não retorna o resultado satisfatório, o retorno é sempre o últio elemento
# quando a verificação é positiva, excluindo outros candidatos possíveis. (corrigido)

# CORREÇÕES POSSÍVEIS: Sistema de fatiamento para conversão de str > int (corrigido)

#=========================================================================================================================#
## NOVAS CORREÇÕES: a ideia e mecânica do sistema é funcional, porém, considerando que esta lista poderia ter 50, 100 ou mais candidatos,
# o ideal seria fornecer o resultado a parte, no rodapé do código. 
#=========================================================================================================================#

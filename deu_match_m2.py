
   ## Lista de candidatos e suas respectivas notas                                   
                                             #1 #4 #7 #10
candidatos =       [{'Nome':'José', 'Nota':'e5_t3_p7_s8'},  
                    {'Nome':'Augusto', 'Nota':'e4_t5_p8_s7'},     # os : devem estar fora das aspas para que entenda a atribuição
                    {'Nome':'Simone', 'Nota':'e5_t4_p9_s8'},      # dos índices ('Nome', 'Nota') aos seus valores ('José', 'eX_tX_pX_sX')
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
        print('-'*90)
    print('Sigla: e = entrevista, t = exame teórico, p = exame prático, s = soft skills')
    print('=' * 90)

    # este loop foi criado para percorrer as strings, buscar as casas de valores numéricos no índice de 'notas' para realizar sua conversão para inteiro
    for notas in candidatos:
        conv_e = int(notas['Nota'][1])
        conv_t = int(notas['Nota'][4])
        conv_p = int(notas['Nota'][7])
        conv_s = int(notas['Nota'][10])
        #print(f'Nota de entrevista: {conv_e}, nota teórica: {conv_t}, nota prática: {conv_p}, nota soft skills: {conv_s}')

    # aqui faremos a comparação das notas das strings convertidas em int, junto com a nota pedida nos inputs
    if e_nota >= conv_e and t_nota >= conv_t and p_nota >= conv_p and s_nota >= conv_s:
        candidato_aprovado.append(notas)
        print(f'O candidato: {nome} corresponde a este requisito com a nota {nota}')
    elif e_nota < conv_e and t_nota < conv_t and p_nota < conv_p and s_nota < conv_s:
        print('Nenhum candidato corresponde a este requisito')

    # após a verificação, ele joga o candidato para dentro da lista candidato_aprovado
    return candidato_aprovado


## input para buscar os candidatos através dos critérios das notas 
e_nota = int(input('Qual o valor mínimo do resultado da entrevista? '))
t_nota = int(input('Qual o valor mínimo do exame teórico? '))
p_nota = int(input('Qual o valor mínimo do exame prático? '))
s_nota = int(input('Qual a nota mínima das habilidades de soft skills? '))


# após toda a etapa de verificação, aqui chamamos a função para nos entregar o resultado dos aprovados e os atribui para a lista vazia
candidato_aprovado = nota_candidato(e_nota, t_nota, p_nota, s_nota)

## CORREÇÕES NECESSÁRIAS NO CÓDIGO: Sem quebras, porém o sistema de verificação não está condizendo os valores,
# o que faz dar erro na checagem e não retorna o resultado satisfatório, o retorno é sempre o últio elemento
# quando a verificação é positiva, excluindo outros candidatos possíveis. 
# CORREÇÕES POSSÍVEIS: Sistema de fatiamento para conversão de str > int
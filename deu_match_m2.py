print('='*90)
print('Digite as notas abaixo para realizar a busca dos candidatos'.upper())                                   
                                             #1 #4 #7 #10
candidatos =       [{'Nome':'José', 'Nota':'e5_t3_p7_s8'},  
                    {'Nome':'Augusto', 'Nota':'e4_t5_p8_s7'},     
                    {'Nome':'Simone', 'Nota':'e5_t5_p9_s8'},      
                    {'Nome':'Patricia', 'Nota':'e4_t6_p8_s5'},
                    {'Nome':'Matheus', 'Nota' : 'e4_t4_p7_s8'}] 

print('='*90)
# função para armazenar as notas que serão pedidas ao usuário
def nota_candidato(e_nota, t_nota, p_nota, s_nota):
    candidato_aprovado = []

    # buscando a nota dos candidatos na lista 
    for busca in (candidatos):
        
        nome = busca['Nome']     
        nota = busca['Nota']             
        
        nota_e = int(nota[1])
        nota_t = int(nota[4])
        nota_p = int(nota[7])
        nota_s = int(nota[10])
        

        # comparação da nota do candidato com a nota mínima inserida pelo usuário
        if e_nota <= nota_e and t_nota <= nota_t and p_nota <= nota_p and s_nota <= nota_s:
            candidato_aprovado.append(busca)
    print('-'*90)        
    print('\033[34mSigla: e = entrevista, t = exame teórico, p = exame prático, s = soft skills')
    print('-'*90)
    
    # testando se a condição da lista é verdadeira ou falsa e ser impresso somente se verdadeiro. 
    if not candidato_aprovado:
       print('\033[91mNENHUM CANDIDATO CORRESPONDE A ESTES CRITÉRIOS')
       print('-'*90)

    # verificando os candidatos adicionados na lista
    for busca in candidato_aprovado:
        if True:
            print(f'\033[92mCandidato Aprovado:\nNome: {busca["Nome"]}, Nota: {busca["Nota"]}')
        print('-' * 90)

while True:
        
# entrada para buscar as notas dos candidatos
    e_nota = int(input('Qual o valor mínimo do resultado da entrevista? '))
    t_nota = int(input('Qual o valor mínimo do exame teórico? '))
    p_nota = int(input('Qual o valor mínimo do exame prático? '))
    s_nota = int(input('Qual a nota mínima das habilidades de soft skills? '))

# chamando a função para nos entregar o resultado dos aprovados 
    candidato_aprovado = nota_candidato(e_nota, t_nota, p_nota, s_nota)
    
    resposta = input('\033[0;0mDeseja realizar uma nova busca? (S/N)  ')
    if resposta.upper() != 'S':
        break



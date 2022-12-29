import random
'''
 # IDÉIAS PARA UM PROJETO VERDADEIRO #
 · colocar função de níveis(fácil, médio, díficil)
 · colocar a função de chances → (pronto)
 · colocar um temporizador
 · colocar um layout
 · colocar um sistema de palavras random → (pronto)
 · colocar escolha de idioma
 · aumentar a quantidade de palavras criando um programa separado só para essa função
 · adicionar sistema de pontos quando estiver jogando
'''
secret_words = ['gato', 'rato', 'caminhão', 'paralelepípedo', 'chuva', 'rua', 'hidrocarboneto', 'universo' ]
choosen_word = random.choice(secret_words)
    

right_letters = ''

x = True
y = True
game_points = 0

    
while x:
    print(f'palavra com {len(choosen_word)} letras.')
    attempts = 10



    while y:
        print(f'Você tem {attempts} tentativas')
        letter = input('escreva letra: ')
    
        if len(letter) > 1:
            print('Somente uma letra.')
            continue
        
        if not letter or letter == ' ':
            print('Insira uma letra.')
            continue

        
        if letter in choosen_word:
            right_letters += letter
        
        
        if letter not in choosen_word:
            attempts -= 1
            
            if attempts <= 0:
                
                y = False
                # break
        

        formed_word = ''
        for letter in choosen_word:
            if letter in right_letters:
                formed_word += letter
            else:
                formed_word += '*'

        if formed_word == choosen_word:
            print(f"parabéns! você acertou! a palavra: {formed_word} ")
            game_points += 1

            y = False
    
        print(formed_word)
    
    
    z = True
    while z:
       
        question = input(f'Seu total de pontos até agora foi {game_points}.Você quer continuar/Reiniciar o jogo?(S/n): ')
       
       
        if question.upper() == 'S':
            right_letters = ''
            choosen_word = random.choice(secret_words)
            y = True
            z = False
        
        
        elif not question or question == ' ':
            print('Digite "S" para "sim" e "n" para "não"')
        
        
        elif question.upper() == 'N':
            print('Obrigado por jogar!')
            z = False
            x = False


        '''
        BUGS A SEREM CORRIGIDOS:
        1º: Quando dá continuidade no jogo após a segunda palavra, ele guarda as letras anteriores
        Correção: Ver e corrigir porque a variável não está sendo limpa (Resolvido)
        
        2º: Após a pergunta se deseja jogar de novo, se digitar algo fora dos paramêtros do if ele volta pra cima
        '''

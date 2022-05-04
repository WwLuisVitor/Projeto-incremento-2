opçao=-1
tipop=0
manifestaçoes=['1#luis#reclamaçao#sem agua no bebedouro','2#pedro#sugestão#intervalo para lanche','3#bruno#elogio#excelente professor']
protocolo=len(manifestaçoes)+1
tipo=['reclamaçao','sugestão','elogio']
while opçao !=7:
 print()
 print('Ouvidoria faculdade CBA')
 print()
 print('1) Listar todas as manifestações')
 print('2) Listar todas as sugestões')
 print('3) Listar todas as reclamações')
 print('4) Listar todos os elogios')
 print('5) Enviar uma nova manifestação')
 print('6) Pesquisar protocolo por número')
 print('7) Sair')
 opçao=int(input('digite sua opçao '))
 print()
 if opçao>7 or opçao<1:
     print('opção invalida')
 if opçao==1: # Listar todas as manifestações disponiveis
     print('Essas sao todas as manifestações disponíveis no momento')
     print()
     for manifestaçao in manifestaçoes: 
      listasaida=manifestaçao.replace('#',' - ') # Puxando os dados armazenados na variável"manifestaçao" e utilizando o replace para printar os dados separados por um "-".
      print('Código '+ listasaida)
 elif opçao==2: # Listar apenas as sugestões removendo a palavra "sugestões" no print final.
     print('Essas sao todas as sugestões no momento')
     print()
     for manifestaçao in manifestaçoes: 
       manifestaçaoquebrado=manifestaçao.split('#')
       if tipo[1]==manifestaçaoquebrado[2]:
          manifestaçaoquebrado.pop(2) # Removendo a palavra "sugestões" através do comando pop.
          print('Código', end=' ') # Utilizando o comando end para printar horizontalmente.
          for i in manifestaçaoquebrado:
              print('- '+ i, end=' ') 
          print()
 elif opçao==3: # Listar apenas as reclamações removendo a palavra "reclamações" no print final.
     print('Essas sao as reclamações no momento')
     print()
     for reclamaçao in manifestaçoes:
         reclamaçaoquebrado=reclamaçao.split('#')
         if tipo[0]==reclamaçaoquebrado[2]:
             reclamaçaoquebrado.pop(2)
             print('Código', end='')
             for i in reclamaçaoquebrado:
                 print('- '+i, end=' ')
             print()
 elif opçao==4: # Listar apenas os elogios removendo a palavra "elogios" no print final.
     print('Esses são os elogios até agora')
     print()
     for elogio in manifestaçoes:
         elogioquebrado=elogio.split('#')
         if tipo[2]==elogioquebrado[2]:
             elogioquebrado.pop(2)
             print('Código',end='')
             for i in elogioquebrado:
                 print('- '+i,end=' ')
             print()
 elif opçao==5: # Enviar uma manifestação nova.
    protocolo=len(manifestaçoes)+1
    name=input('digite seu nome ') # Requisitando o nome do criador da manifestação.
    while tipop<1 or tipop>3: # Requisitando o tipo de manifestação, garantindo que o cliente vai inserir um valor válido atravésdo while.
     tipop=int(input('digite o tipo do problema, considerando 1 para reclamaçãoo 2 para sugestão e 3 para elogio '))
     if tipop < 1 or tipop > 3:
            print('Tipo de manifestação inválido: Repetir o processo!')
    descriçaoproblema=input('descreva a manifestação ') # Requisitando a descrição da manifestação.
    dadosproblema=str(protocolo)+'#'+name+'#'+tipo[tipop-1]+'#'+descriçaoproblema # Armazenando os dados separados por "#".
    manifestaçoes.append(dadosproblema) # Adicionando os dados do cliente na lista "manifestaçoes" através do comando append.
 elif opçao==6:
     pesquisa=-1 # Criando uma variável para garantir o inicio do while.
     tamanhoprotocolo=len(manifestaçoes)
     while pesquisa <=0 or pesquisa>tamanhoprotocolo: # Requisitando o número do protocolo à ser pesquisado garantindo que o cliente irá inserir um valor válido através da utilização do while.
         pesquisa=int(input('Digite o numero do protocolo para pesquisar a respeito do mesmo: '))
         if pesquisa <= 0 or pesquisa > (tamanhoprotocolo):
             print('Não foi encontrado nenhum protocolo com esse número.')
             break # Se o cliente nao inserir um valor válido irá apresentar a mensagem de erro e então voltar ao menu inicial.
     print()
     pesquisadigitado=pesquisa
     for pesquisatemp in manifestaçoes:
         pesquisaquebrado=pesquisatemp.split('#')
         if int(pesquisaquebrado[0])==(pesquisadigitado):
             print('Código',end='')
             for i in pesquisaquebrado:
                 print('- '+i,end=' ')
print('Saindo...')
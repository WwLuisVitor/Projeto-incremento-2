opçao=0
tipop=0
pesquisa=0
manifestaçoes=['1#luis#reclamaçao#sem agua no bebedouro','2#pedro#sugestão#intervalo para lanche','3#bruno#elogio#excelente professor']
protocolo=len(manifestaçoes)+1
tipo=['reclamaçao','sugestão','elogio']
problema=['não tem agua no bebedouro','nao tem luz na sala']
nome=['Pedro','daniel']
while opçao !=7:
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
 if opçao>7 or opçao<1:
     print('opção invalida')
 if opçao==1:
     print('Essas sao todas as manifestações disponíveis no momento')
     for manifestaçao in manifestaçoes: 
      listasaida=manifestaçao.replace('#',' - ')
      print('Código '+ listasaida)
 if opçao==2:
     print('Essas sao todas as sugestões no momento')
     for manifestaçao in manifestaçoes: 
       manifestaçaoquebrado=manifestaçao.split('#')
       if tipo[1]==manifestaçaoquebrado[2]:
          manifestaçaoquebrado.pop(2)
          print('Código', end=' ')
          for i in manifestaçaoquebrado:
              print('- '+ i, end=' ')
          print()
 if opçao==3:
     print('Essas sao as reclamações no momento')
     for reclamaçao in manifestaçoes:
         reclamaçaoquebrado=reclamaçao.split('#')
         if tipo[0]==reclamaçaoquebrado[2]:
             reclamaçaoquebrado.pop(2)
             print('Código', end='')
             for i in reclamaçaoquebrado:
                 print('- '+i, end=' ')
         print()
 if opçao==4:
     print('Esses são os elogios até agora')
     for elogio in manifestaçoes:
         elogioquebrado=elogio.split('#')
         if tipo[2]==elogioquebrado[2]:
             elogioquebrado.pop(2)
             print('Código',end='')
             for i in elogioquebrado:
                 print('- '+i,end=' ')
         print()
 if opçao==5:
    protocolo=len(manifestaçoes)+1
    name=input('digite seu nome ')
    while tipop<1 or tipop>3:
     tipop=int(input('digite o tipo do problema, considerando 1 para reclamaçãoo 2 para sugestão e 3 para elogio '))
     if tipop < 1 or tipop > 3:
            print('Tipo de manifestação inválido: Repetir o processo!')
    descriçaoproblema=input('descreva a manifestação ')
    dadosproblema=str(protocolo)+'#'+name+'#'+tipo[tipop-1]+'#'+descriçaoproblema
    manifestaçoes.append(dadosproblema)
    print(manifestaçoes)
 
 if opçao==6:
     while pesquisa<len(manifestaçoes) or pesquisa>len(manifestaçoes):
         pesquisa=int(input('Digite o numero do protocolo para pesquisar a respeito do mesmo: '))
         if pesquisa<len(manifestaçoes) or pesquisa>len(manifestaçoes):
          print('Não foi encontrado nenhum protocolo com esse número.')
         pesquisac=pesquisa
         for pesquisa in manifestaçoes:
             pesquisaquebrado=pesquisa.split('#')
             if int(pesquisaquebrado[0])==pesquisac:
                 print('Código',end='')
             for i in pesquisaquebrado:
                  print('- '+i,end=' ')
         
     

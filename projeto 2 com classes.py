opçao=-1
dados=[]
listatipos=['reclamaçao','sugestao','elogio']
class manifestacao:
 codigo=0
 nome=''
 tipo=0
 descriçao=''
while opçao !=7:
 print()
 print('Ouvidoria faculdade CBA')# Começo do Menu
 print()
 print('1) Listar todas as manifestações')
 print('2) Listar todas as sugestões')
 print('3) Listar todas as reclamações')
 print('4) Listar todos os elogios')
 print('5) Enviar uma nova manifestação')
 print('6) Pesquisar protocolo por número')
 print('7) Sair')# Fim do Menu
 opçao=int(input('digite sua opçao '))
 print()
 if opçao>7 or opçao<1:
     print('opção invalida')
 if opçao==1: # Listar todas as manifestações disponiveis
      print('Essas sao todas as manifestações disponíveis no momento')
      for sugest in dados:
       printtotal=str(sugest.codigo)+' - '+str(sugest.nome)+' - '+str(sugest.tipo)+' - '+str(sugest.descriçao)# Organizando um print que junta os elementos do objeto
       print(printtotal)# Printando a variável ja organizada.
      print()
 if opçao==2:
     print('Lista de todas as sugestões')
     for sugest in dados:
         if sugest.tipo ==listatipos[1]:
             printtotal=str(sugest.codigo)+' - '+str(sugest.nome)+' - '+str(sugest.descriçao)
             print(printtotal)
 if opçao==3:
     print('Lista de todas as reclamações')
     for reclam in dados:
         if reclam.tipo ==listatipos[0]:
             printtotal=str(reclam.codigo)+' - '+str(reclam.nome)+' - '+str(reclam.descriçao)
             print(printtotal)
 if opçao==4:
     print('Lista de todos os elogios')
     for elog in dados:
         if elog.tipo ==listatipos[2]:
             printtotal=str(elog.codigo)+' - '+str(elog.nome)+' - '+str(elog.descriçao)
             print(printtotal)
 if opçao==5:
        tipo=-1   
        codigo=len(dados)+1
        nome=input('digite seu nome: ')
        while tipo<1 or tipo>3:
            tipo=int(input('digite o tipo do problema, considerando 1 para reclamaçãoo 2 para sugestão e 3 para elogio '))
            if tipo<1 or tipo>3:
             print('tipo inválido')
        descrição=input('descreva sua solicitaçao: ')
        objeto1=manifestacao()# Criando um objeto e relacionando com a classe manifestacao.
        objeto1.nome=nome
        objeto1.tipo=listatipos[tipo-1]
        objeto1.descriçao=descrição
        objeto1.codigo=codigo
        dados.append(objeto1)# Enviando o objeto ja com os dados recebidos nos inputs para a lista dados.
 if opçao==6:
     pesquisa=-1 # Criando uma variável para garantir o inicio do while.
     tamanhoprotocolo=len(dados)
     while pesquisa <=0 or pesquisa>tamanhoprotocolo: # Requisitando o número do protocolo à ser pesquisado garantindo que o cliente irá inserir um valor válido através da utilização do while.
         pesquisa=int(input('Digite o numero do protocolo para pesquisar a respeito do mesmo: '))
         if pesquisa <= 0 or pesquisa > (tamanhoprotocolo):
             print('Não foi encontrado nenhum protocolo com esse número.')
             break
     for pesq in dados:
         if pesq.codigo == pesquisa:
             printtotal=str(pesq.codigo)+' - '+str(pesq.nome)+' - '+str(pesq.tipo)+' - '+str(pesq.descriçao)
             print(printtotal)
print('Saindo...')
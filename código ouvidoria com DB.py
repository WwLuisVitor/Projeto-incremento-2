from operacoesbd import *
open=abrirBancoDados('localhost','Luis','Luis072212','ouvidoria') # Opening the database
option=-1
typelist=['Reclamation','Suggestion','Compliment']
while option !=7:
 print()
 print('Ouvidoria faculdade CBA')# Menu start
 print()
 print('1) List all manifestations')
 print('2) List all suggestions')
 print('3) List all reclamations')
 print('4) List all Compliments')
 print('5) Send a new manifestation')
 print('6) Search for a manifestation with protocol numbem')
 print('7) Leave')# End of the menu
 option=int(input('Type your option '))
 print()
 if option>7 or option<1:
     print('invalid option')
 if option==1: # Listing all manifestations
      print('These are all the manifestations on our system at the moment')
      print()
      listall="SELECT * FROM clientdata"
      result=listarBancoDados(open,listall)
      for i in result:
          itotal=str(i[0])+' - '+i[1]+' - '+i[2]+' - '+i[3]
          print (itotal)
 if option==2: # Listing all suggestions
     print('These are all the suggestions on our system at the moment')
     print()
     listall="SELECT * FROM clientdata WHERE manifesttype='Suggestion'"
     result=listarBancoDados(open,listall)
     for i in result:
         itotal=str(i[0])+' - '+i[2]+' - '+i[3]
         print(itotal)
 if option==3: # Listing all reclamations
     print('These are all the reclamations on our system at the moment')
     print()
     listall="SELECT * FROM clientdata WHERE manifesttype='Reclamation'"
     result=listarBancoDados(open,listall)
     for i in result:
         itotal=str(i[0])+' - '+i[2]+' - '+i[3]
         print(itotal)
 if option==4: # Listing all compliments
     print('These are all the compliments on our system at the moment')
     print()
     listall="SELECT * FROM clientdata WHERE manifesttype='Compliment'"
     result=listarBancoDados(open,listall)
     for i in result:
         itotal=str(i[0])+' - '+i[2]+' - '+i[3]
         print(itotal)
 if option==5: # Sending a new manifestation to the database
        type=-1   
        name=input('type your name: ')
        while type<1 or type>3:
            type=int(input('considering 1 for reclamation, 2 for suggestion and 3 for compliment enter the type of manifestation: '))
            if type<1 or type>3:
             print('invalid type')
        description=input('describe your solicitation: ')
        insertdb="insert into clientdata(manifesttype,username,manifestdescription) values(%s, %s, %s)"
        informations=(typelist[type-1],name,description)
        insertNoBancoDados(open,insertdb,informations)
 if option==6: # Searching a manifestation using protocol number
     listall="SELECT protocol FROM clientdata"
     protocols=listarBancoDados(open,listall)
     search=-1 # Creating a variable to ensure the while loop
     protocollenght=len(protocols)
     while search <=0 or search>protocollenght:
         search=int(input('Type the protocol number to search it: '))
         if search <= 0 or search > (protocollenght):
             print('There is no manifestation with this protocol number, try again.')
             break
     searchusingprotocol="SELECT * FROM clientdata WHERE protocol="+str(search)
     resultsearch=listarBancoDados(open,searchusingprotocol)
     for i in resultsearch:
         itotal=str(i[0])+' - '+i[1]+' - '+i[2]+' - '+i[3]
         print(itotal)
print('Leaving...')
encerrarBancoDados(open) # Closing the database
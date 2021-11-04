## API Shodan

###  Consulta API Shodan en Python

###### 1. Realitza un petit programa que pregunti una ip a l'usuari i mostri la informació d'aquesta IP rebuda des de l'API de shodan.
1. Importar llibreries

![llibreriesShodan](/Imatges/shodan/llibreriesShodan.png)

2. Com extraure la api key de shodan.
  - Entrar a la pàgina https://www.shodan.io/ i crear un compte.
  - Un cop creat el compte, entrar a account i copiar
  
    ![acountshodan](/Imatges/shodan/acountshodan.png)
  
  - Un cop copiat la api key, hem de crear una variable anomenada api, on posarem la key. 
  
    ![apikey](/Imatges/shodan/apikey.png)
  
  
3. Demanar al usuari una ip
  
    ![ipUsuari](/Imatges/shodan/ipUsuari.png)
  
4. Bucle per mostrar la informació trobada:

  
    ![bucleShodan](/Imatges/shodan/bucleShodan.png)
  

6. Quina informació mostrem?
  
  -Domini i la ip, amb els ports que l'api ha trobat oberts.
 
   ![informacioIp](/Imatges/shodan/informacioIp.png)
   
###### 2.Modifica l'script per a que mostri únicament els noms de domini associats a la Ip i els ports oberts que ha trobat Shodan.
  
###### 3.Afegeix una funció que a partir de la informació anterior ens digui quin servei hi ha en cadascun dels ports oberts trobats.
   Afegirem la següent funció:
   
   ![llibreriesShodanSocket](/Imatges/shodan/llibreriesShodanSocket.png)
   
   Per a que funcioni la funcio "socket." s'ha de importar la llibreria socket.
   
   ![funcioSocket](/Imatges/shodan/funcioSocket.png)
   
###### 4. Afegeix una funció on l'usuari pugui escriure el nom d'un servei (per exemple proftp) i es mostri un resultats amb ips i ports on s'hi pugui trobar aquest servei segons els resultats de Shodan.
   
   
   
   

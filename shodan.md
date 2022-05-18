# Shodan


Un cop hem entrat a l'opció de shodan, ens demanarà l'api. Al [manual tècnic](https://github.com/2ASIX-2021-22/ProjecteJSD/wiki/07.-Shodan), mostrem com s'aconsegueix l'api de shodan.

![image](https://user-images.githubusercontent.com/80519737/168890367-c2372262-65f0-4f35-b7c2-6b9d0e3e3c2c.png)



## 2  Consulta a Shodan en Python


### 1. L'aplicació pregunta una ip a l'usuari i mostra els ports oberts d'aquesta IP. 
El que fa el programa es buscar a la base de dades de shodan i retorna els ports 

La ip que demana es la IP pública.

![image](https://user-images.githubusercontent.com/80519737/169052421-efc4c5e7-2c3a-412c-969f-9c3d6c38d641.png)

###### 2.Modifica l'script per a que mostri únicament els noms de domini associats a la Ip i els ports oberts que ha trobat Shodan.
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
   

  
###### 3.Afegeix una funció que a partir de la informació anterior ens digui quin servei hi ha en cadascun dels ports oberts trobats.
   Afegirem la següent funció:
   
   ![ImportSocket](/Imatges/shodan/ImportSocket.png)
   
   Per a que funcioni la funcio "socket." s'ha de importar la llibreria socket.
   
   ![funcioSocket](/Imatges/shodan/funcioSocket.png)
   
###### 4. Afegeix una funció on l'usuari pugui escriure el nom d'un servei (per exemple proftp) i es mostri un resultats amb ips i ports on s'hi pugui trobar aquest servei segons els resultats de Shodan.

   ![codi](/Imatges/shodan/ex4codi.png)
   
   Captura  
   
   ![funcioSocket](/Imatges/shodan/ex4.png)
   
   

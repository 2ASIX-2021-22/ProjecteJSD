# Shodan

## Què és Shodan?

**[Shodan](https://www.shodan.io/)** és un **motor de cerca** que permet a l'usuari trobar, gràcies a l'especificació per filtres, diferents tipus d'equips (routers, servidors, etc.) connectats a Internet.

## Com funciona l'eina?

Un cop hem entrat a l'opció de shodan, ens demanarà l'api. Al [manual tècnic](https://github.com/2ASIX-2021-22/ProjecteJSD/wiki/07.-Shodan), mostrem com s'aconsegueix l'api de shodan.

![image](https://user-images.githubusercontent.com/80519737/168890367-c2372262-65f0-4f35-b7c2-6b9d0e3e3c2c.png)

### Opció 1. Consulta a Shodan en Python

L'aplicació pregunta una ip a l'usuari i mostra els ports oberts d'aquesta IP. 

El que fa el programa es buscar a la base de dades de shodan i retorna els ports 

La ip que demana es la IP pública.

![image](https://user-images.githubusercontent.com/80519737/169052421-efc4c5e7-2c3a-412c-969f-9c3d6c38d641.png)

L'aplicació ens pregunta el servei, i ens fa una búsqueda a la base de dades de shodan.
El que fa el programa es mostrar tota la informació que hi ha a la base de dades sobre el servei que hem demanat i ens retorna els resultats per pantalla. 

**NOTA:** Si tenim el bot configurat, retornarà els resultats al telegram. 

![resultat_terminal](https://user-images.githubusercontent.com/80519737/169094485-64d7f67a-038f-437c-aac8-97ba15b85fe6.png)

![resultat_telegram](https://user-images.githubusercontent.com/80519737/169094810-d70fad7c-16ba-43c1-8bfd-b59ffa3669f5.png)





# The Harvester

## Què és The Harvester?

The Harvester és una eina per recol·lectar informació pública a la web. Aprèn com funciona per anticipar-te a atacs d'enginyeria social.

És una eina per aconseguir informació sobre emails, subdominis, hosts, noms d'empleats, ports oberts, banners, etc. des de fonts públiques com són els motors de cerca, servidors PGP, la xarxa social LinkedIn i la base de dades de SHODAN ( Cercador semblant a Google però amb la diferència que no indexa contingut, sinó que registra qualsevol dispositiu connectat a Internet).

![image](https://user-images.githubusercontent.com/80519737/169096715-f2888767-d59e-40b3-9786-7afd5b8aac22.png)

## Instruccions d'instal·lació:

Per començar, caldria crear un CSE de Google i afegir la nostra API Key de google i l'identificador del CSE generat.

En segon lloc, hem d'especificar la nostra API Key de Shodan al fitxer shodansearch.py del projecte. (https://github.com/laramies/theHarvester/issues/747)

També, crearem el fitxer api-keys.yaml (https://github.com/ben000000/theHarvester/blob/master/api-keys.yaml)

Hem d'instal·lar la llibreria requests de Python `pip install requests`

I per descomptat tenir Python instal·lat (**2.7 recomanat**)

Un cop completats els passos anteriors, descarreguem el projecte `{git clone https://github.com/laramies/theHarvester.git}`

## Com utilitzar l'eina?

Seleccionem l'**opció 2** del menú principal.

## Un cop hem entrat a la opcio 2, apareixerà el següent menú:

![image](https://user-images.githubusercontent.com/80519737/169096134-76fab5a2-b7f9-4a6f-bd96-720656c883fd.png)

Tenim dues opcions disponibles

**Opció 1: Execució**

El programa, esta automatitzat per a que l'usuari sols tingui que introduïr el domini al qual volem atacar, i els resultats que volem que ens retorni.

![image](https://user-images.githubusercontent.com/80519737/169097723-e6d60a1f-4ea9-406a-8739-9aac0c175a32.png)

**NOTA:** The harvester, té diferents opcions de búsqueda, així que nosaltres hem escollit la millor opció per al nostre treball. Més informació a la wiki. 

![resultat_terminal](https://user-images.githubusercontent.com/80519737/169097941-11434fbd-e06d-4676-bdc3-0d882977fc76.png)

**Opció 2: Mostrar els resultats**

Aquesta opció, copia els últims resultats que hem obtingut al elegir la primera opció "Execució", i els envia al Telegram mitjançant el bot.

![image](https://user-images.githubusercontent.com/80519737/169098347-0e0830e8-0562-43b4-917f-3a6dea12f5f2.png)

El resultat, l'envia en un fitxer xml. Així, hauríem d'obtenir aquest resultat:

![image](https://user-images.githubusercontent.com/80519737/169098659-41c057d8-c010-43fa-84a4-b3bb7c05b5b5.png)





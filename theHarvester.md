
## The Harvester

# The Harvester és una eina per recol·lectar informació pública a la web. Aprèn com funciona per anticipar-te a atacs d'enginyeria social.

### Què és The Harvester?

És una eina per aconseguir informació sobre emails, subdominis, hosts, noms d'empleats, ports oberts, banners, etc. des de fonts públiques com són els motors de cerca, servidors PGP, la xarxa social LinkedIn i la base de dades de SHODAN ( Cercador semblant a Google però amb la diferència que no indexa contingut, sinó que registra qualsevol dispositiu connectat a Internet).

### Instruccions d'instal·lació:

Per començar, caldria crear un CSE de Google i afegir la nostra API Key de google i l'identificador del CSE generat.

En segon lloc, hem d'especificar la nostra API Key de Shodan al fitxer shodansearch.py del projecte. (https://github.com/laramies/theHarvester/issues/747)

També, crearem el fitxer api-keys.yaml (https://github.com/ben000000/theHarvester/blob/master/api-keys.yaml)

Hem d'instal·lar la llibreria requests de Python `pip install requests`

I per descomptat tenir Python instal·lat (**2.7 recomanat**)

Un cop completats els passos anteriors, descarreguem el projecte `{git clone https://github.com/laramies/theHarvester.git}`

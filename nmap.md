# NMAP

## Com fer una cerca a NMAP utilitzant la nostra aplicació?

Molt fàcil! Anirem al menú principal, i escollirem l'**opció 7**.

![image](https://user-images.githubusercontent.com/80519737/169173661-5f7fc27d-7913-495b-937d-a8401532ad90.png)

## Com utilitzar l'eina?

### Opció 1. Escaneig IP's de la xarxa

Busca amb l'eina NMAP, tots els dispositius connectats a la xarxa.

![image](https://user-images.githubusercontent.com/80519737/169173906-f2366ae3-6ae9-4982-89c7-7a76c4891d1c.png)

### Opció 2. Ports a través d'una IP disponible

Busca amb l'eina NMAP, els ports oberts d'un dispositiu.

![image](https://user-images.githubusercontent.com/80519737/169174410-f75b7c1e-2c9e-4e5e-b1d7-13c8a930999c.png)

### Opció 3. Versions serveis

Busca amb l'eina NMAP, de tots ports oberts que hi han, les versions i serveis que està utilitzant el dispositiu atacat. 

I ho mostra amb **format CSV** per facilitar la lectura a l'usuari.

![image](https://user-images.githubusercontent.com/80519737/169174779-7db10b6c-6c80-40eb-8ece-6bd387c5da51.png)

### Opció 4. Vulnerabilitats CVE

Mitjançant els scripts **nmap-vulners** i **vulscan** i amb tota la potència de l'eina NMAP busca les vulnerabilitats que podem tenir al dispositiu en qüestió.

![nmap_vuln1](https://user-images.githubusercontent.com/92753159/169496523-c9f355a1-6054-4c1d-8f2c-ebece9a9a08e.png)
![nmap_vuln2](https://user-images.githubusercontent.com/92753159/169496652-3330d564-9da1-48a4-b9d7-a1866608cbe9.png)

**NOTA:** Tots aquests resultats arribaran al bot de Telegram si està configurat.

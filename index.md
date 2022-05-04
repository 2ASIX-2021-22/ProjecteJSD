## Benvingut a la documentació de l'usuari

### Descargar el repositori del github per instal·lar la app.

Un cop descarregat el projecte del github.
`git clone git@github.com:2ASIX-2021-22/ProjecteJSD.git`

### Automatització de instal·lació de recursos

Tenim un script al projecte anomenat: **scriptexecuciodocker.sh**

Que fa script?

* Automatiitza l'actualització del sistema
`sudo apt update`

* Instal·la els tres paquets de docker
`sudo apt install docker docker.io docker-compose`
* Construeix l'app
`sudo docker build -t {name_app} /path/to/Dockerfile`
* Mostra les imatges que tenim
`sudo docker images`
* Arranca l'app
`sudo docker run -it app`

[Muntatge Raspberry Pi 4](https://2asix-2021-22.github.io/ProjecteJSD/muntatgeraspberrypi)

[Docker](https://2asix-2021-22.github.io/ProjecteJSD/Docker)

[API Shodan](https://2asix-2021-22.github.io/ProjecteJSD/apishodan)

[The Harvester](https://2asix-2021-22.github.io/ProjecteJSD/theHarvester)

[uDork](https://2asix-2021-22.github.io/ProjecteJSD/uDork)

[Osintgram](https://2asix-2021-22.github.io/ProjecteJSD/Osintgram)

[Socket](https://2asix-2021-22.github.io/ProjecteJSD/Socket)

[Nmap](https://2asix-2021-22.github.io/ProjecteJSD/Socket)

[SSH-AUDIT](https://2asix-2021-22.github.io/ProjecteJSD/SSH-Audit)


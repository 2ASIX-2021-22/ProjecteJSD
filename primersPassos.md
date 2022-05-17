# [Primers passos](https://2asix-2021-22.github.io/ProjecteJSD/)
## Descargar el repositori del github per instal·lar la app.

Un cop descarregat el projecte del github.
`git clone https://github.com/2ASIX-2021-22/ProjecteJSD.git`

Captura mostrant el procés:

![image](https://user-images.githubusercontent.com/80519737/168882764-e1fbf2ca-2abe-4726-8849-e452d11d59c6.png)

Un cop clonat el repositori, tenim que configurar el bot de telegram. (Les seves funcions ja estàn implementades als scripts)

## Bot de Telegram
### [Primer pas. Creació del bot](https://github.com/2ASIX-2021-22/ProjecteJSD/wiki/05.-Bot-de-Telegram)
### Segon pas. Introducció de les credencials
Entrarem al fitxer **bot_telegram.py**
Modificarem el contingut de les variables **idBot** i **idGrupo** tal i com s'explica a la [wiki](https://github.com/2ASIX-2021-22/ProjecteJSD/wiki/05.-Bot-de-Telegram#enviem-missatges-a-telegram-mitjan%C3%A7ant-python).

## Automatització de instal·lació de recursos

Tenim un script al projecte anomenat: **scriptexecuciodocker.sh**

Per executar l'script, s'ha d'accedir al terminal, al directori descarregat, i executar la següent ordre:

`./scriptexecuciodocker.sh`

Si et dona errors de permisos, es tenen que otorgar **permisos d'execució (+x)**.

# Auditoria SSH

## Què és SSH-Audit?

**[SSH-Audit](https://github.com/jtesta/ssh-audit)** és una eina per a l'auditoria de configuració de **servidor** i **client** ssh.

Per realitzar auditories SSH hem escollit SSH-Audit ja què, és una eina senzilla, intuitiva però, a la vegada molt potent per extreure tots els resultats que ens interesen.

## Com realitzem una auditoria SSH amb la nostra aplicació?

Molt fàcil, anirem al menú principal, i escollirem l'**opció 3**.

![image](https://user-images.githubusercontent.com/80519737/169099657-16579727-91c8-4f0e-8d83-b90aa7c2d63d.png)

## Com utilitzar l'eina?

### Opció 1: Auditoria completa

El funcionament del programa és molt senzill, simplement escollim l'opció, que volem provar en aquest cas, l'**auditoria completa** i podrem veure els resultats tal i com es mostra a la imatge.

![auditoria_completa](https://user-images.githubusercontent.com/92753159/169493068-a379f002-1cc5-47c4-bf17-772c1bd32291.png)

Al tenir el bot de Telegram configurat, podem veure que ens enviar un fitxer .txt amb els resultats obtinguts.

![resultat_telegram](https://user-images.githubusercontent.com/80519737/169101033-f7c8d78d-e00e-4ef3-8a60-a131ac03034f.png)

### Opció 2: Auditoria 'FAILS'

Si escollim la segona opció només ens mostrarà els **fails (errors)**.

![fails](https://user-images.githubusercontent.com/56296299/169371666-b5fb1aac-c91b-4027-ae97-3dab48e0a0ae.png)

Igual que al punt anterior s'enviaran els resultats al bot del Telegram.

![tele_fails](https://user-images.githubusercontent.com/56296299/169372643-5fdf6ae4-cf39-4256-a86a-cbb5647f8f6f.png)

### Opció 3: Auditoria 'WARNS'

Si escollim la tercera opció només ens mostrarà els **warns (warnings)**.

![warns](https://user-images.githubusercontent.com/56296299/169371728-99a95d8b-b23f-4f21-8348-fe861d69c21e.png)

I enviarà els resultats al bot del Telegram.

![tele_warns](https://user-images.githubusercontent.com/56296299/169372701-c986d8b6-e583-491a-afc3-c626465febb7.png)

### Opció 4: Auditoria 'INFO'

L'última opció ens mostrarà **informació (info)** dels serveis, algoritmes...

![info](https://user-images.githubusercontent.com/56296299/169371795-30acbda3-7736-4302-9bc6-db0806ba9e94.png)

També, ens arribaran els resultats al bot de Telegram.

![tele_info](https://user-images.githubusercontent.com/56296299/169372661-f8e360b1-8379-4bf5-bc02-1651340800b4.png)

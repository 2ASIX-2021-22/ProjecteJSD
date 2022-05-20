# Ennumeració

## Que fa Enum4linux?

**[Enum4linux](https://www.kali.org/tools/enum4linux/)** és una eina que ens permetrà enumerar informació del **servei Samba**. Intenta oferir una funcionalitat similar a enum.exe que abans estava disponible per a sistemes Windows.

## Com obtenim informació dels nostres serveis SAMBA amb la nostra aplicació?

Escollirem l'**opció 8** de la nostra aplicació.

![enum_menu](https://user-images.githubusercontent.com/92753159/169560173-81091df9-29ab-4b91-bd1b-147710cbd964.png)

## Com utilitzar l'eina?

### Opció 1: Auditoria completa

Introduïrem una **IP** i ens mostrarà tota la informació referent a **Samba**, **controladors de domini**, **usuaris**, **carpetes compartides**...

![1-1](https://user-images.githubusercontent.com/92753159/169564751-0c8acecd-554a-4ef4-a496-2d273c251d53.png)

Ens arribaran els resulats al bot de Telegram, amb un fitxer .txt.

![1-2](https://user-images.githubusercontent.com/92753159/169565488-c8fc26d9-4314-4c97-8393-98659d57178f.png)

### Opció 2: Llistar usuaris

Si seleccionem la segona opció ens mostrarà els usuaris referents al **servei Samba**.

![2-1](https://user-images.githubusercontent.com/92753159/169564767-8d0a4e0e-0d51-42c8-a342-9088f06ccd13.png)

S'enviaràn el bot de Telegram.

![2-2](https://user-images.githubusercontent.com/92753159/169565620-31e1a780-e0cd-4912-8117-9b530ad6edf9.png)

### Opció 3: Auditoria S.O.

I l'última opció ens mostrarà les versions del **servei Samba** i el tipus de servei.

![3-1](https://user-images.githubusercontent.com/92753159/169565633-b19135cd-45cb-4a98-869d-7daf6d4d9437.png)

També, ens arribaran els resultats al bot de Telegram.

![3-3](https://user-images.githubusercontent.com/92753159/169565640-d437a40c-6bf8-4a3a-9873-9591f9c9d7e5.png)

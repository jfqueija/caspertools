#   Summary

## Versión Español

La finalidad de esta librería es la de proporcionar una navegación anónima. 

El objetivo de este desarrollo, es el aprendizaje. No nos hacemos responsables del uso indebido de la mismas para fines que no sean puramente lectivos.

*   __Documento de control versiones:__

Versión |   Autor   |   Publicada   |   Enlace      |   Descripción
------- |   ------  |   ----------- |   ---------   |   --------
0.1     |   José Fº |   Sí          |   [pip](https://pypi.org/project/caspertools/)         |   En esta versión disponemos de la función request_get que haciendo uso de la librería requests y a través del método get, obtendrá la respuesta de una página web que enviemos por parámetro. 


### Configuración/Instalación Tor

Para poder hacer uso de la librería, debemos instalar previamente Tor en nuestras máquinas. Para ello, vamos a seguir los siguientes pasos:

1.  Update del sistema:

    ```sudo apt update```

2.  Instalación de Tor:

    ```sudo apt install -y tor```

3.  Comprobamos el estado del servicio tras la instalación:

    ```service tor status```
    * cannot read PID file /var/run/tor/tor.pid

4.  Editamos el fichero de configuración de Tor:

    ```sudo gedit /etc/tor/torrc```
    o
    ```sudo nano /etc/tor/torrc```

    Buscamos la entrada: 
    
    ```HashedControlPassword```

    Eliminamos el símbolo # que la precede. 

    Hacemos lo mismo con las siguientes entradas:

    ```CookieAuthentication```
    ```ControlPort```

    Respecto a la entrada del HashedControlPassword. Para generar el hash que debemos incluir, será necesario generar uno nuevo a partir del siguiente comando:

    ```tor --hash-password my_password```

    Importante: es muy conveniente guardar este password ya que será el que usaremos en la librería de caspertools.

5.  Arracamos el servicio de tor:

    ```service tor start```

6.  Instalación de netcat: Instalaremos esta librería para comprobar que todo está corercto.

    ```sudo apt install -y netcat```

    Tras la instalación, ejecutaremos el siguiente comando:

    ```echo -e 'AUTHENTICATE' | nc 127.0.0.1 9051```

    Nos debería retornar los siguiente:

    >(UNKNOWN) [127.0.0.1] 9051 (?) : Connection refused

    Esto es debido a que estamos haciendo uso del proxy sin el password generado en el punto 4. Probamos de nuevo incluyendo el password:

    ```echo -e 'AUTHENTICATE "my password"' | nc 127.0.0.1 9051```

    En este caso, nos retornará:

    >250 OK

Nota: Si hemos ejecutado correctamente los pasos indicados, ya disponemos de Tor instalado y preparado para ser usado desde nuestra librería caspertools.

### Como usar caspertools


>   Caspertools internamente usa la librería stem para regenerar las IPs a través de TOR. En caso de problemas con la librería de caspertools, se recomienda la instalación manual de stem haciendo uso del comando:

```pip install stem```

>   Caspertools internamente usa la librería requests para realizar las solicitudes por http/s. En caso que problemas con la librería, se recomienda la instalación manual de requests haciendo uso del comando:

```pip install requests```


Para usar la librería de navegación oculta, debemos importar el módulo, para ello, agregremos la siguiente línea a nuestro proyecto:

```from caspertools.hiddenav import TorIp```

Declararemos una nueva variable que corresponderá a la clase TorIp 

```tor = TorIp(<Tor Password>,<Tor Port>,<Local Proxy>)```

En la clase TorIp disponemos de las siguientes funciones:

1.  __renew_ip()__: Con esta función podemos testear que la IP haya cambiado, es decir, solicitamos una nueva IP.
2.  __request_get(<urlTarget>)__:   Esta función nos permite consultar una web con navegación oculta.


Nota: 
>   Actualmente solo está disponible el método get. En próximas versión se implementará también el verbo post así como el uso con librerías como urllib.


## English Version

The objective of this library is made easy hidden navigation.

This development is only for learn. We are not responsible for the incorrect use for finished.

*   __Documento de control versiones:__

Version |   Author  |   Published   |   Link        |   Description
------- |   ------  |   ----------- |   ---------   |   --------
0.1     |   José Fº |   Yes         |   [pip](https://pypi.org/project/caspertools/)       |   In this version we have the request_get function that by using the requests library and through the get method, you will get the response of a web page that we send by parameter.



### Tor Setup / Installation

In order to use the library, we must previously install Tor on our machines. To do this, we will follow the following steps:

1.  Sistem update:

    ```sudo apt update```

2.  Tor Installation:

    ```sudo apt install -y tor```

3.  We check the service status after installation:

    ```service tor status```
    * cannot read PID file /var/run/tor/tor.pid

4.  Edit the Tor configuration file:

    ```sudo gedit /etc/tor/torrc```
    or
    ```sudo nano /etc/tor/torrc```

    We look for the entrance:
    
    ```HashedControlPassword```

    We remove the # symbol that precedes it.

    We do the same with the following entries:

    ```CookieAuthentication```
    ```ControlPort```

    Regarding the entry of the HashedControlPassword. To generate the hash that we must include, it will be necessary to generate a new one from the following command:

    ```tor --hash-password my_password```

    Important: it is very convenient to save this password as it will be the one we will use in the caspertools library.

5.  We start the tor service:

    ```service tor start```

6.  Netcat installation: We will install this library to verify that everything is correct.

    ```sudo apt install -y netcat```

    After installation, we will execute the following command:

    ```echo -e 'AUTHENTICATE' | nc 127.0.0.1 9051```

    We should return the following:

    >(UNKNOWN) [127.0.0.1] 9051 (?) : Connection refused

    This is because we are using the proxy without the password generated in point 4. We test again including the password:

    ```echo -e 'AUTHENTICATE "my password"' | nc 127.0.0.1 9051```

    In this case, it returns us:

    >250 OK

Note: If we have executed the indicated steps correctly, we already have Tor installed and prepared to be used from our caspertools library.

### How to use caspertools


>   Caspertools internally uses the stem library to regenerate IPs through TOR. In case of problems with the caspertools library, manual installation of stem using the command is recommended:

```pip install stem```

>   Caspertools internally uses the requests library to make requests by http / s. In case of problems with the library, manual installation of requests by using the command is recommended:

```pip install requests```


To use the hidden navigation library, we must import the module, for this, we will add the following line to our project:

```from caspertools.hiddenav import TorIp```

We will declare a new variable that corresponds to the TorIp class

```tor = TorIp(<Tor Password>,<Tor Port>,<Local Proxy>)```

In the TorIp class we have the following functions:

1.  __renew_ip()__: With this function we can test that the IP has changed, that is, we request a new IP.
2.  __request_get(<urlTarget>)__:   This function allows us to consult a website with hidden navigation.


Note: 
>   Only the get method is currently available. In the next version, the post verb will be implemented as well as the use with libraries such as urllib.

#   Summary

## Versión Español

La finalidad de esta librería es la de proporcionar una navegación anónima. 

El objetivo de este desarrollo, es el aprendizaje. No nos hacemos responsables del uso indebido de la mismas para fines que no sean puramente lectivos.

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




## English Version

The objective of this library is made easy hidden navigation.

This development is only for learn. We are not responsible for the incorrect use for finished.


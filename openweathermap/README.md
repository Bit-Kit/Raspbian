# OpenWeatherMap
\- to usługa, która dostarcza bieżące dane pogodowe, dane historyczne i prognozy pogodowe. Udostępnia API do tworzenia własnych aplikacji.

## Użyte biblioteki:

* **[PyOWM](https://pyowm.readthedocs.io/en/latest/usage-examples-v2/weather-api-usage-examples.html#owm-weather-api-version-2-5-usage-examples)** - kliencka biblioteka OpenWeatherMap
* **[I2C_LCD_driver](https://gist.github.com/DenisFromHR/cc863375a6e19dce359d)** - biblioteka I2C do wyświetlacza HD44780 
* **[datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime)** - biblioteka do manipulacji czasem

## Instalowanie bibliotek:

PyOWM:  
 
    $ pip3 install pyowm
    
I2C_LCD_driver (Należy pobrać plik z repozytorium):
  
    https://gist.github.com/DenisFromHR/cc863375a6e19dce359d
  
## Moja implementacja:

[my_open_weather_map.py](my_open_weather_map.py)
  
## Automatyczne uruchomienie na Raspberry Pi przy starcie:
Utwórz plik w:

    /etc/init.d
    
Zawartość pliku może być taką:

    #! /bin/sh
    ### BEGIN INIT INFO
    # Provides:          weather
    # Required-Start:    $all
    # Required-Stop:
    # Default-Start:     2 3 4 5
    # Default-Stop:
    # Short-Description: :)
    ### END INIT INFO

    echo "start init"
    sleep 10
    python3 /home/pi/<twój_skrypt.py> &  #Ścieżka do twójego skryptu
    exit 0

Zmień prawo dostępu utworzonego pliku:

    chmod 777 <twój_plik>

Dodaj plik do systemu startowego "update-rc.d":

    update-rc.d weather defaults

---
### Źródła <a name="zrodla"></a>
* [I2C HD44780 do Raspberry PI](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/)
* [OpenWeatherMap API guide](https://openweathermap.org/guide)
* [DenisFromHR_Github](https://gist.github.com/DenisFromHR)
* [PyOWM dokumentacja](https://pyowm.readthedocs.io/en/latest/index.html#installation)
* [Opis update-rc.d](http://manpages.ubuntu.com/manpages/bionic/pl/man8/update-rc.d.8.html)

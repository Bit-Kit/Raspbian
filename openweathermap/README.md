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
  
## Automatyczne uruchomienie na Raspberry Pi:

...


---
### Źródła <a name="zrodla"></a>
* [I2C HD44780 do Raspberry PI](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/)
* [OpenWeatherMap API guide](https://openweathermap.org/guide)
* [DenisFromHR_Github](https://gist.github.com/DenisFromHR)
* [PyOWM dokumentacja](https://pyowm.readthedocs.io/en/latest/index.html#installation)

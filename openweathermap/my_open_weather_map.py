import time
import datetime
import I2C_LCD_driver                      #Biblioteka wyświetlacza HD44780 LCD opartego o interfejs I2C 
from pyowm import OWM                      #Biblioteka OpenWeatherMap

mylcd = I2C_LCD_driver.lcd()               #Inicjalizacja wyświetlacza
API_key = 'xxxxxxxxxxxxxxxxxxxxxxxx'       #Wprowadź własny klucz API, otrzymany po rejestracji na stronie
owm = OWM(API_key)

cu =  owm.weather_at_place('Twoje_miasto,PL')       
fc = owm.three_hours_forecast('Twoje_miasto,PL')

#Funkcja kolejkowania wiadomości do wyświetlacza
def i2c_send(itime_forecast,itemp_forecast,istatus_forecast,ihumidity_forecast,itime_current,itemp_current,istatus_current,ihumidity_current):
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Prognoza: " + str(itime_forecast) + ":00", 1)
    mylcd.lcd_display_string("Temp:" + str(itemp_forecast)+ " ",2 )
    time.sleep(3.5)

    mylcd.lcd_clear()
    mylcd.lcd_display_string("Prognoza: " + str(itime_forecast) + ":00", 1)
    mylcd.lcd_display_string(str(istatus_forecast) + " ",2 )
    time.sleep(3.5)

    mylcd.lcd_clear()
    mylcd.lcd_display_string("Prognoza: " + str(itime_forecast) + ":00", 1)
    mylcd.lcd_display_string("Wilgotnosc:" + str(ihumidity_forecast) + "%",2 )
    time.sleep(3.5)

    mylcd.lcd_clear()
    mylcd.lcd_display_string("Teraz: " + str(itime_current)+ "  ",1 )
    mylcd.lcd_display_string("Temp:" + str(itemp_current) + " ",2 )
    time.sleep(3.5)

    mylcd.lcd_clear()
    mylcd.lcd_display_string("Teraz: " + str(itime_current)+ "  ",1 )
    mylcd.lcd_display_string(str(istatus_current) + " ",2 )
    time.sleep(3.5)

    mylcd.lcd_clear()
    mylcd.lcd_display_string("Teraz: " + str(itime_current)+ "  ",1 )
    mylcd.lcd_display_string("Wilgotnosc:" + str(ihumidity_current)+ "%",2 )
    time.sleep(3.5)
    
while(True):
    try:
        while (True):
            if(owm.is_API_online() == True):
                    current_datetime = datetime.datetime.now()
                    #print("cur_dattime:" + str(current_datetime))
                    forecast_time = current_datetime + datetime.timedelta(hours=6)
                    current_time = current_datetime.time()
                    #print("cur" + str(current_time))
                    curr_object = cu.get_weather()
                    forecast_object = fc.get_weather_at(forecast_time)

                    time_forecast = forecast_object.get_reference_time(timeformat='date')
                    #Zmienne zawierające dane o temperaturze
                    temp_forecast = forecast_object.get_temperature(unit='celsius')
                    temp_curr = curr_object.get_temperature(unit='celsius')
                    #Zmienne zawierające dane o pogodzie
                    status_forecast = forecast_object.get_detailed_status()
                    status_curr = curr_object.get_detailed_status()
                    #Zmienne zawierające dane o poziomie wilgotności
                    humidity_forecast = forecast_object.get_humidity()
                    humidity_curr = curr_object.get_humidity()

                    float_temp_forecast = temp_forecast["temp"]
                    float_temp_curr = temp_curr["temp"]
    
                    #print("Temp_current: " + str(float_temp_curr))
                    #print("Temp_forecast: " + str(float_temp_forecast))
                    #Zmienne zawierające czas wywołania prognozy
                    time_i2c_forecast = time_forecast.hour
                    time_i2c_curr = str(current_time.hour) + ':' + str(current_time.minute)
                    i2c_send(time_i2c_forecast,float_temp_forecast,status_forecast,humidity_forecast,time_i2c_curr,float_temp_curr,status_curr,humidity_curr)
                    time.sleep(1)
                            else:
                                print("Brak polaczenia!!!")
                                mylcd.lcd_clear()
                                mylcd.lcd_display_string("Teraz: " + str(time_i2c_curr)+ "  ",1 )
                                mylcd.lcd_display_string("Brak polaczenia ",2 )
                                time.sleep(15)
    except:
        print("EXCEPTION!!!")
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Blad",2 )
        time.sleep(15)
        #mylcd.lcd_clear()
    






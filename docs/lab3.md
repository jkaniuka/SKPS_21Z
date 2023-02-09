# SKPS 19.11.2021 - Laboratorium 3 :computer:  

Laboratorium rozpoczęliśmy od podłączenia _RaspberryPi_ do komputera, zasilania oraz internetu (po uprzednim sprawdzeniu stanu połączeń przez Prowadzącego). Kolejnym krokiem było dokończenie ćwiczeń wykorzystujących GPIO wraz z sensorami/efektorami z laboratorium 2.

## Buzzer
Pracując na systemie ratunkowym mogliśmy wykorzystywać bibliotekę _RPi.GPIO_. Napisaliśmy prosty program, który generował modulowany sygnał dźwiękowy przez 5 sekund (ze zmienną częstotliwością). ➡️ plik `gpio_snd.py`


Schemat ideowy podłączenia buzzera do RPi:  
    <img src="uploads/5f673c3a3ea12b4f36ce4072e1da08dc/image.png" alt="drawing" width="400" height="400"/>

## Switch
Przećwiczyliśmy również obsługę GPIO jako wejścia. Podłączyliśmy zewnętrzny przycisk oraz uruchomiliśmy wewnętrzny rezystor PULL-UP. Po wciśnięciu guzika, na konsoli szeregowej pojawiał się stosowny komunikat. ➡️ plik `gpio_in.py`

Schemat ideowy podłączenia zewnętrznego przycisku do RPi:  
    <img src="uploads/66cf0f960e14f00027109de87189d5ab/image.png" alt="drawing" width="400" height="400"/>


Przygotowaliśmy również programy do obsługi czujnika odległości (`zad_5.py`) oraz akcelerometru (`zad_6.py`), lecz z powodu ograniczeń czasowych przeszliśmy do kompilacji własnych pakietów w OpenWRT. 

## OpenWRT
- Zaczęliśmy od pobrania SDK zgodnie z instrukcją na stronie przedmiotu.  
- Wykorzystując 'make menuconfig' wybraliśmy przykładowe pakiety do kompilacji.  
- Skompilowany pakiet przerzuciliśmy na RPi korzystając z serwera HTTP :earth_americas:.  
- Po zainstalowani pakietu uruchomił się pożądany program - świadczy to o poprawności przeprowadzonej przez nas konfiguracji 👍


## Własne pakiety w OpenWRT
Za cel obraliśmy napisanie prostego programu ( w C++) z zadaniem migania diodą z poziomu OpenWRT. Punktem wyjścia do dalszych prac był dla nas pakiet przykładowy. Po zmodyfikowaniu odpowiednich plików okazało się, że należy pobrać bibliotekę _WiringPi_.  
  
Pobraliśmy ją zgodnie z instrukcją z https://github.com/nmaas87/rpi-openwrt-packages i zaznaczyliśmy w _make menuconfig_ odpowiednie pakiety. Kompilacja z wykorzystaniem wspomnianej biblioteki przebiegła pomyślnie, lecz z powodu końca zajęć nie udało się już przenieść pakietu na RPi. 
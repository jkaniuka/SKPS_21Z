## Wymagania projektowe:   
Tworzony w ramach projektu system powinien albo integrować dane z przynajmniej dwóch
czujników, albo realizować sterowanie elementem wykonawczym (np. LED, LCD,
serwomechanizm) na podstawie sygnałów odbieranych z czujnika. Przynajmniej jeden z wykorzystanych podzespołów powinien używać interfejsu I2C lub SPI. W celu testowania i monitorowania pracy tworzonego systemu, powinien on zapewniać możliwość komunikacji przez sieć TCP/IP.  

## Cel i założenia:
W ramach projektu postanowiono zbudować system, który realizuje sterowanie elementami wykonawczymi (serwomechanizmem oraz diodą LED) na podstawie stanu zewnętrznych przycisków (pierwotnie przycisków na klawiaturze membranowej 4x4). Ponieważ przynajmniej jeden z wykorzystanych podzespołów powinien używać interfejsu I2C lub SPI, dodano do projektu wyświetlacz LCD 2x16. Wykorzystano konwerter poziomów logicznych dla wyświetlacza ze sterownikiem HD44780, ponieważ musi być on zasilany z napięcia 5V.

## Opis funkcji jakie pełni system:
System zasadniczo składa się z dwóch, głównych elementów: cześć sprzętowej oraz interfejsu użytkownika. Z poziomu panelu sterowania na komputerze PC można sterować diodą, zmieniać tryb pracy systemu (sterowanie z poziomu panelu, lub z poziomu zewnętrznych przycisków) oraz zadawać wypełnienie sygnału PWM do sterowania serwomochanizmem. Na wyświetlaczu LCD wyświetla się aktualna wartość wypełnienia PWM. Do RaspberryPi podłączono również trzy, zewnętrzne przyciski, które pozwalają na zmianę trybu pracy serwa (automatyczne rozpędzanie, a następnie hamowanie lub tryb manualny). W trybie manualnym używa się pozostałych dwóch przycisków - kliknięcie pierwszego zwiększa wartość wypełnienia PWM o +0.5%, a drugiego zmniejsza tę wartość o -0.5%. W interfejsie użytkownika wyświetla się aktualizowany na bieżąco wykres sygnału PWM. Dodano również okno rejestrujące ingerencje użytkownika - wyświetlana jest informacja o wartości sygnału PWM oraz informacja o naciśnięciu danego przycisku wraz ze stemplem czasowym.

## Schemat części sprzętowej:

![image](uploads/c4907df38d2efaa46e1a8fd3868da815/image.png)


## Opis zastosowanych rozwiązań (+literatura):

* Komunikacja z wyświetlaczem - _driver_, który obsługuje komunikację z wyświetlaczem, oparty jest o protokół I2C. Aby poprawnie obsługiwać wyświetlacz LCD skorzystaliśmy z customowej biblioteki **RaspLCDDriver**. Wykorzystuje ona moduł jądra _i2c-dev_. Używaliśmy pierwszej magistrali I2C na pinach 3 (SDA 1)oraz 5 (SCL 1) w płytce _RaspberryPi_. Aby móc poprawnie połączyć się na magistrali I2C, należało najpierw sprawdzić adres pod jakim zgłasza się sterownik wyświetlacza. Dokonaliśmy tego komendą:    
`i2cdetect -y 1`   
Wyświetlacz zgłosił się poprawnie pod adresem `0x27`. Następnie mogliśmy wykorzystać bibliotekę do wyświetlania komunikatów na ekranie.

* Sterowanie I/O - aby uzyskać dostęp do obsługi pinów GPIO, wykorzystaliśmy polecaną przez Prowadzących bibliotekę **libgpiod**. Wzorując się przykładami autorów wspomnianej biblioteki, mogliśmy sterować wyjściami oraz odczytywać stan wejść w programie. Biblioteka została użyta w celu sterowania diodą LED, obsługi przycisków i generowania sygnału PWM.

* Generator PWM - w celu poprawnego sterowania prędkością obrotową serwa musieliśmy wygenerować software'owy sygnał PWM. Aby generator był stabilny, utworzyliśmy osobny **wątek**, który nieustannie zajmuje się generowaniem sygnału na określonym pinie z zadanym wypełnieniem. Generator opiera się na naprzemiennym ustawianiu na wybranym pinie GPIO wartości logicznych 0 oraz 1 z odpowiednim okresem przy wykorzystaniu modułu libgpiod.

* Komunikacja z komputerem - zrealizowaliśmy prostą komunikację z komputerem w oparciu o **sockety**. Komputer do którego była podłączona płytka _RaspberryPi_ był serwerem, natomiast sama płytka była klientem. Komunikacja z serwerem, a szczególnie oczekiwanie na jego żądania, powinna odbywać się bez opóźnień. Spełniliśmy to wymaganie poprzez utworzenie kolejnego wątku, który zajmuje się tylko oczekiwaniem na wiadomości z serwera.

* https://man7.org/linux/man-pages/
* https://libgpiod-dlang.dpldocs.info/gpiod.html
* https://github.com/monotok/RaspLCDDriver
* https://www.geeksforgeeks.org/tcp-server-client-implementation-in-c/?fbclid=IwAR20MFiq2IEE9PwkRTXtxr87-mDW7fhmCLcMdMCydeoEmNDtmAGS-1Gsfhk
* https://pymotw.com/2/socket/tcp.html?fbclid=IwAR2zj6oylEKK6yndhSTZwy5r11O0cJGFQMXyBwc2xwDv96wUByNJdbR6az0

## Schematyczne przedstawienie całego systemu:
![image](uploads/3590fef03982c35fb51ed7f555832dd2/image.png)
## Struktura mechanizmu komunikacji: 
![image](uploads/43a169e3d834e63248a48f2bd98ca729/image.png)

## Napotkane problemy:  
* zadawanie zbyt dużych wartości wypełnia sygnału PWM powodowało gwałtowne zmniejszenie jasności ekranu LCD z powodu zbyt dużego poboru prądu (nie używano dodatkowego zasilacza np. do serwomechanizmu - wszystkie peryferiale zasilano bezpośrednio z RaspberryPi) 


## Metody testowania stworzonego rozwiązania:  
Na ostatnich zajęciach przetestowano działanie całego systemu:
*  wszystkie trzy przyciski działały poprawnie
*  wartość wypełnienia PWM wyświetlana na ekranie LCD była na bieżąco aktualizowana (np. po wciśnięciu odpowiedniego przycisku)
*  serwomechanizm zatrzymywał się przy wypełnieniu PWM = 15%
*  panel operatorski działał prawidłowo i umożliwiał m.in. włączenie/wyłączenie diody
*  komunikacja pomiędzy komputerem i RPi również działała prawidłowo

## Zdjęcia:
<div align="center">
 <img src="uploads/7193ce5e957db1d6f54de8b7dcb9b311/image.png"/> 
 <img src="uploads/cbc95fe4265de143062a57957f2c2ea6/image.png"/> 
</div>

## Filmy :film_projector: - [link do filmu](https://drive.google.com/file/d/1voAXFOp_HdNxVKS13TqZxOZjEw8is6sm/view?usp=sharing)

## Wnioski/podsumowanie:  

Wykonany projekt spełnia nasze założenia, poprawnie realizuje zadania w ramach systemu OpenWRT wraz z toolchainem SDK. Pomimo początkowych trudności udało nam się uruchomić działający mini system do sterowania serwem wraz z wyświetlaczem LCD. Zadania wykonują się w 3 wątkach co pozwala na niezależną i stabilną pracę systemu. Raspberry jest responsywne i szybko reaguje na wciśnięcie przycisków oraz wydawane przez komputer polecenia. Serwo pracuje zgodnie z oczekiwaniami, zmieniając swoją prędkość obrotową, co świadczy o poprawnej implementacji generatora PWM. Wykonany system może być bazą do bardziej skomplikowanych projektów. Wiedza zdobyta podczas realizacji powierzonego nam zadania pozwala na samodzielne stworzenie prostych systemów wbudowanych z wykorzystaniem komputera Raspberry PI 4B w oparciu o dystrybucję OpenWRT oraz implementację programów języku C.

## Informacja o strukturze katalogów w repozytorium oraz instrukcję odtworzenia (zbudowania i uruchomienia) projektu z kodów źródłowych i konfiguracji.
1) Kompilujemy pakiet w SDK wpisując kolejno poniższe komendy:    
:warning: **Etap kompilacji może zostać pominięty - w repozytorium jest dostępny skompilowany pakiet.**  
```
export LANG=C
scripts/feeds update skps
scripts/feeds install -p skps -a
make menuconfig
make package/demo_full/compile
```
2) Wynikowy katalog **.ipk** będący rezultatem kompilacji znajdziemy w podkatalogu _/bin_ folderu, gdzie znajduje się SDK.  
3) Przerzucamy skompilowany pakiet na RPi wykorzystując _python'owy_ serwet HTTP:  
Na stacji roboczej uruchamiamy serwer:  
`python3 -m http.server`  
Na RPi pobieramy pakiet ze wskazanej lokalizacji  
`wget http://<host ip>:8000/<path>`  
4) Instalujemy nowy pakiet :  
```
opkg install demo_full_1.0-1_aarch64_cortex-a72.ipk
```
5) Na komputerze PC uruchamiamy plik serwera _TCP/IP_ _skps_gui.py_ komendą `python skps_gui.py` (GUI wyświetli się dopiero po uruchomieniu programu na RPi - do tego czasu serwer TCP/IP jest w stanie oczekiwania na połączenie od klienta).
6) Uruchamiamy program na RaspberryPi poleceniem `demo_full` wpisanym w konsoli, gdzie korzystamy z OpenWRT.


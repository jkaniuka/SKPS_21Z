# SKPS 17.12.2021 - Laboratorium 5 :computer:  

Laboratorium rozpoczęliśmy od podłączenia _RaspberryPi_ do komputera, zasilania oraz internetu (po uprzednim sprawdzeniu stanu połączeń przez Prowadzącego). Kolejnym krokiem była kontynuacja prac nad zadaniem projektowym.

## Temat projektu :page_with_curl: :thinking:  
W ramach projektu będziemy budować system, który realizuje sterowanie elementami wykonawczymi (serwomechanizmem oraz diodą LED) na podstawie danych z czujnika (przycisków na klawiaturze membranowej 4x4). Ponieważ przynajmniej jeden z wykorzystanych podzespołów powinien używać interfejsu I2C lub SPI, dodamy do projektu wyświetlacz LCD 2x16. Wykorzystamy konwerter poziomów logicznych dla wyświetlacza ze sterownikiem HD44780, ponieważ musi być on zasilany z napięcia 5V.  


## Opracowanie schematu budowanego układu: 
Schemat układu budowanego w ramach projektu został wykonany w programie _Fritzing_. 
![image](uploads/9d0ddc25652ee8dd233c6dd980179e70/image.png)

**Komentarz**: Na powyższym schemacie użyliśmy diody LED zamiast serwomechanizmu. Stwierdziliśmy, że będzie to bezpieczniejsze rozwiązanie, które pozwoli na sprawdzenie poprawności działania zaimplementowanego _PWM_. Po pozytywnych wynikach testów dołączyliśmy serwomechanizm równolegle z diodą LED. Mając na uwadze rosnący pobór prądu w miarę wzrostu liczby elementów elektronicznych w układzie postanowiliśmy wyłączyć podświetlenie wyświetlacza LED zdejmując odpowiednią zworkę. 

Złożony podczas laboratorium układ prezentował się następująco:  
<div align="center">
 <img src="uploads/29f264de48091c5f04194ab3b3c34be2/image.png" width="400" height="400"/> 
</div>


## Opis implementacji: :floppy_disk:   
Na podstawie pakietu przygotowanego przez Prowadzącego stworzyliśmy własny pakiet `demo_all`. Korzystając z mechanizmu _opkg install_ dodano brakujące pakiety np. _gpiod-tools_, _i2c-tools_. Udało się połączyć ze sterownikiem wyświetlacza LCD i wyświetlać na nim procent wypełnienia PWM sterującego silnikiem oraz diodą LED. Zaczęto również implementować obsługę przejścia z trybu automatycznego na tryb ręczny poprzez naciśnięcie odpowiedniego przycisku na klawiaturze matrycowej.


## Instrukcja kompilacji, wgrywania pakietu na RPi oraz uruchamiania:  
1) Kompilujemy pakiet w SDK wpisując kolejno poniższe komendy:   
```
export LANG=C
scripts/feeds update skps
scripts/feeds install -p skps -a
make menuconfig
make package/demo_all/compile
```
2) Wynikowy katalog **.ipk** będący rezultatem kompilacji znajdziemy w podkatalogu _/bin_ folderu, gdzie znajduje się SDK.  
3) Przerzucamy skompilowany pakiet na RPi wykorzystując _python'owy_ serwet HTTP:  
Na stacji roboczej uruchamiamy serwer:  
`python3 -m http.server`  
Na RPi pobieramy pakiet ze wskazanej lokalizacji  
`wget http://<host ip>:8000/<path>`  
4) Usuwamy poprzednio "stary" pakiet z RPi, instalujemy nowy i ruchamiamy:  
```
rm demo_all_1.0-1_aarch64_cortex-a72.ipk  
opkg remove demo_all
opkg install demo_all_1.0-1_aarch64_cortex-a72.ipk
demo all
```

 

## Sprawdzenie działania przygotowanego pakietu: 

Film prezentujący funkcjonalności **prototypu**:  
<div align="center">
 <img src="uploads/253e763de5f134d9c450202de90d53aa/servo_cut.mp4" width="100" height="100"/> 
</div>

## Testy komunikacji TCP/IP z wykorzystaniem transmisji przez _Sockety_ :telephone_receiver:  
Istotną częścią projektu jest zbieranie danych pomiarowych i prezentowanie ich w interfejsie
graficznym na komputerze PC. Program na RPi powinien korzystać z połączenia sieciowego do
archiwizacji zebranych danych i do sterowania realizowanym algorytmem (np. ustawianie
parametrów, zmiana trybu pracy). Stwierdziliśmy, że dobrym rozwiązaniem będzie oparcie komunikacji na _socketach_. Przed laboratorium przygotowano dwa przykładowe pliki w języku C: `client.c` oraz `server.c`. Plik serwera skompilowano i uruchomiono na komputerze PC - po otwarciu _socketu_ czekał on na połączenie klienta. Główną cześć programu _client.c_ umieszczono w pliku `demo_all.c`, gdzie znajduje się cały system sterowania. 
  
Test nawiązania połączenia i wymiany komunikatów zakończył się pomyślenie :ok_hand:. RPi przesłało komunikat znakowy do PC, a PC przesłał w odpowiedzi komunikat do RPi. 

## Do zrobienia :tools: :
Na ostatnich zajęciach laboratoryjnych skupimy się na dopracowaniu systemu sterowania serwomechanizem poprzez różne przyciski na klawiaturze membranowej. Postaramy się również przeprowadzić testy działania interfejsu użytkownika (GUI).


  


 




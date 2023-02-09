# SKPS 3.12.2021 - Laboratorium 4 :computer:  

Laboratorium rozpoczęliśmy od podłączenia _RaspberryPi_ do komputera, zasilania oraz internetu (po uprzednim sprawdzeniu stanu połączeń przez Prowadzącego). Kolejnym krokiem było dokończenie ćwiczeń wykorzystujących GPIO wraz z sensorami/efektorami z laboratorium 3.

## Kompilacja własnego pakietu :hammer: 
Na podstawie pakietu przygotowanego przez Prowadzącego stworzyliśmy własny pakiet (`demo_led`). Początkowo chcieliśmy oprzeć eksperymenty na bibliotece [_WiringPi_](https://github.com/nmaas87/rpi-openwrt-packages). Napotkaliśmy niestety wiele problemów - program z naszego pakietu "nie widział" tej biblioteki. Nie znaleźliśmy też instrukcji/dokumentacji opisującej ewentualny sposób kompilacji pobranej paczki z biblioteką _WiringPi_. Postanowiliśmy więc zmienić bibliotekę do obsługi GPIO na `libgpiod`. Pobranie, konfigurację oraz kompilację pakietu `libgpiod` przeprowadziliśmy zgodnie z instrukcją ze strony przedmiotu. 
Wykorzystywane kolejno polecenia:  
- [pobranie skompresowanego pakietu](https://downloads.openwrt.org/releases/21.02.1/targets/bcm27xx/bcm2711/openwrt-sdk-21.02.1bcm27xx-bcm2711_gcc-8.4.0_musl.Linux-x86_64.tar.xz)  
`scripts/feeds update`  
`scripts/feeds install libgpiod`  
`make menuconfig` - konfiguracja zgodnie z instrukcją   
`make package/libgpiod/compile -j8`  

Długotrwała kompilacja zakończyła się niestety błędem :warning: 
  
## Rozwiązywanie błędów kompilacji pakietu :thinking:    
1. Należało zmodyfikować zawartość pliku _Makefile_ dodając linie:      
`LIBS=-lgpiod`    
`DEPENDS:=+libgpiod` w sekcji _define Package/$(PKG_NAME)_      
2. Następnie z linii poleceń wpisano kolejno komendy:   
`make package/libgpiod/clean -j1 V=s`   
`make package/libgpiod/compile -j1 V=s`   
`make package/demo_led/clean -j1 V=s` 

Finalnie kompilacja powiodła się :heavy_check_mark:   

## Planowany temat projektu :page_with_curl:  
W ramach projektu planujemy zrealizować system, który realizuje sterowanie elementem wykonawczym (serwomechanizmem) na podstawie danych z czujnika (przycisków _microswitch_). Ponieważ przynajmniej jeden z wykorzystanych podzespołów powinien używać interfejsu I2C lub SPI, dodamy do projektu wyświetlacz LCD 2x16. Wykorzystamy konwerter I2C dla wyświetlacza ze sterownikiem HD44780.  

Schemat ideowy projektu:  
    <img src="https://user-images.githubusercontent.com/80155305/217686351-6cb0931f-6e4f-45ae-8819-8fca5cbb42b3.png" alt="drawing" width="600" height="400"/>
   





# SKPS 5.11.2021 - Laboratorium 2 :computer:  

Laboratorium rozpoczęliśmy od podłączenia RaspberryPi do komputera, zasilania oraz internetu (po uprzednim sprawdzeniu stanu połączeń przez Prowadzącego). Kolejnym krokiem była instalacja środowiska OpenWRT:

### Instalacja OpenWRT :arrow_double_down:

W terminalu wpisywaliśmy kolejno poniższe komendy:  

`wget https://downloads.openwrt.org/releases/21.02.1/targets/bcm27xx/bcm2711/openwrt-21.02.1-bcm27xx-bcm2711-rpi-4-ext4-factory.img.gz`    

:exclamation: Przy próbie pobierania OpenWRT pojawił się problem z uczelnianym serwerem DNS, przez co musieliśmy zmodyfikować plik */etc/resolv.conf*, aby umożliwić dostęp do powyższej witryny.

`gzip -d openwrt-21.02.1-bcm27xx-bcm2711-rpi-4-ext4-factory.img.gz`    

`sudo losetup -P -f openwrt-21.02.1-bcm27xx-bcm2711-rpi-4-ext4-factory.img; losetup -l`  

`sudo dd if=/dev/loop0p1 of=/dev/mmcblk0p3 bs=4096`    
`sudo dd if=/dev/loop0p2 of=/dev/mmcblk0p4 bs=4096`    
`sudo resize2fs /dev/mmcblk0p4`  
`sudo sfdisk -d /dev/mmcblk0 > tp`    

`sudo sfdisk --no-reread /dev/mmcblk0 < tp1`  

`sudo reboot -h now`  

### Po restarcie systemu musieliśmy skorygować konfigurację sieci :earth_americas: :

`vi /etc/config/network`  

`/etc/init.d/network reload`    

### Korzystając z menedżera pakietów w OpenWRT mogliśmy pobrać inny edytor :page_facing_up:  (np. *nano*) do edycji plików na potrzebę kolejnych zadań w ramach laboratorium:  

`opkg update`   

`opkg install sfdisk nano` 

### Komunikacja z zewnętrznymi układami poprzez GPIO:  

Pobraliśmy następujące pakiety wspomagające pracę z modułami komunikującymi się np. poprzez SPI czy I2C:  
- gpiod-tools  
- i2c-tools  
- spi-tools  

### Miganie diodą z poziomu konsoli:  
Podłączyliśmy diodę poprzez rezystor zgodnie z poniższym schematem:  
    <img src="https://user-images.githubusercontent.com/80155305/217685224-194ce376-655e-4a0b-9ae3-a45b8a25cbb9.png" alt="drawing" width="400" height="400"/>



**Program konsolowy:** 
<img src="https://user-images.githubusercontent.com/80155305/217685256-3180f9fa-fd9c-4c49-bf36-b742ef83e39a.png" alt="drawing" width="500" height="100"/>


Z powodu braku dokumentacji i ograniczonych funkcjonalności pakietu *gpiod-tools* oraz utrudnionego doinstalowywania potrzebnych bibliotek z z poziomu OpenWRT zdecydowaliśmy się przywrócić system ratunkowy i korzystać z modułu RPi.GPIO. 
Procedura przywracania systemu:   
`sfdisk -d /dev/mmcblk0 > tp`    

Zmiana kolejności patrycji w tablicy partycji, a następnie:  

`sfdisk --no-reread /dev/mmcblk0 < tp`  

### Programy w Pythonie :snake: pisane z poziomu systemu ratunkowego (kody źródłowe w katalogu */cw2*:  

**Zadanie 1**    
10-krotne włączenie i wyłączenie diody LED.

**Zadanie 2**     
Płynna zmiana jasności LED z wykorzystaniem funkcji *sin(x)*  

**Zadanie 3**     
Zmiana jasności diody LED z wykorzystaniem PWM  

### Filmy prezentujące działanie programów :movie_camera: :  
### 1) - miganie ON/OFF
### 2) - wykorzystanie PWM  

<img src="https://user-images.githubusercontent.com/80155305/217685354-7b375dac-a503-4c9b-b07a-715dd608bced.png" alt="drawing" width="300" height="300"/>  <img src="https://user-images.githubusercontent.com/80155305/217685400-bcba2188-0157-4453-98bf-52f9083a2fff.png" alt="drawing" width="300" height="300"/>








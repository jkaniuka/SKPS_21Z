# SKPS 22.10.2021 - Laboratorium 1 :computer:

### Po podłączeniu sprzętu do komputera przystąpiliśmy do konfiguracji wpisując poniższą komendę:  
  
`tio /dev/ttyUSB0` -> pozwoliła ona na podłączenie się do terminala UART.

## Kompilacja obrazu Linuxa :penguin: z *initramfs* (ramdysk startowy):  

`make raspberrypi4_64_defconfig` (wykorzystaliśmy domyślną konfigurację)  
`make menuconfig` - wprowadziliśmy ustawienia wypisane poniżej    
  
Ustawienia:  
- Toolchain --> Toolchain type: External toolchain  
- W menu “Filesystem images” uaktywniamy opcję “cpio the root filesystem” i włączamy dla niej
kompresję gzip. Uaktywniamy opcję “initial RAM filesystem...". Możemy wyłączyć tworzenie głównego systemu plików w formacie ext2/3/4. Po tych zmianach wskazana jest pełna rekompilacja systemu (make clean all)  
  
`make clean all`    

Pobieramy odbraz na RPi i restartujemy płytkę:  
`curl tftp://10.42.0.1/Image --output Image`    
`sudo cp Image /images/`    
`rm Image`    
ewentualne sprawdzenie: `ls /`   
`sudo reboot -h now`    
`fatload mmc 0:3 ${kernel_addr_r} Image`    
`booti ${kernel_addr_r}  - ${fdt_addr}`    

  
## Kompilacja obrazu Linuxa :penguin: bez *initramfs*:  

`make raspberrypi4_64_defconfig`    
`make menuconfig`  
  
W menu zaznaczamy : Toolchain --> Toolchain type: External toolchain. Włączamy kompresję obrazu (w menuconfig buildroota) -> Filesystem Images (włączamy cpio + kompresja gzip + ext2/3/4)    
Nastepnie `make`    
(błędy związane z brakiem miejsca -> postepowaliśmy zgodnie z instrukcją do Laboratorium 1 i podwoiliśmy rozmiar partycji *boot*).   
  
Kopiujemy pliki na serwer TFTP:  
(ctrl+C ctrl+V z /tmp -> /tftp)  
Następnie pobraliśmy skopiowane pliki na RPi:    
`curl tftp://10.42.0.1/Image --output Image`    
`curl tftp://10.42.0.1/rootfs.ext4 --output rootfs.ext4`    

Wgrywamy obraz na RPi:  
`sudo cp Image /images/`    
`sudo dd if=rootfs.ext4 of=/dev/mmcblk0p4 bs=4096`    
`sudo reboot -h now`    
`fatload mmc 0:3 ${kernel_addr_r} Image`    
`setenv bootargs console=tty1 console=ttyAMA0,115200 root=/dev/mmcblk0p4 rootfstype=ext4 rootwait`    
`booti ${kernel_addr_r}  - ${fdt_addr}`  

## Efekt pracy :  
Zarówno uruchomienie *z initramfs*, jak i *bez initramfs* przebiegło pomyślnie :ok_hand:. Razem z Prowadzącym utworzyliśmy na RPi plik text.txt i wykonaliśmy reboot. Po ponownym uruchomieniu RPi plik został zachowany, co potwierdza prawidłowość przeprowadzonej przez nas konfiguracji.

## Uwaga :warning: 
Po zmianie z initramfs na bez initramfs wgranie na RPi przebiegło pomyślnie. Okazało się jednak, że Buildroot nie przebudował *kernela* po tej zmianie. Należało wpisać `make clean all` + `make` i ponownie wgrać pliki na kartę SD w RPi. 

## Do zrobienia :arrow_forward: :  
W ramach kolejnego laboratorium pozostało nam zbudowanie obrazu Linuxa dla maszyny wirtualnej i uruchomienie go na Qemu.




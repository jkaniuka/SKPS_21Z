# SKPS 14.01.2022 - Laboratorium 6 :computer:  

## Prace projektowe poczynione w domu przed laboratorium:
Przed ostatnimi zajęciami laboratoryjnymi poprawiono drobne błędy implementacyjne, zidentyfikowano problemy sprzętowe (z klawiaturą membranową) oraz przygotowano interfejs graficzny (GUI) na wzór panelu operatorskiego/panelu sterowania.

## Modyfikacja schematu, kompletowanie elementów:
Zajęcia rozpoczęto od modyfikacji schematu w programie _Fritzing_. Dodano do niego serwomechanizm oraz dodatkową diodę LED (zieloną). Zmieniono także kolory kabli, aby ułatwić sprawdzenie poprawności połączeń sprzętowych.   

Finalnie schemat budowanego systemu wyglądał w następujący sposób:
<div align="center">
 <img src="uploads/f73ccdc4bb57c07001ea056142dda108/image.png" width="600" height="400"/> 
</div>

<div align="center">
 <img src="uploads/9130a7b5721e127830ccda496c572d27/image.png"/> 
</div>


## Napotkane problemy: 
W projekcie wykorzystano klawiaturę membranową 4x4. Używane były z niej jednak jedynie 3 przyciski. Okazało się, że wyprowadzenia klawiatury są podpisane odwrotnie niż na schematach dostępnych w Internecie. Jeden przycisk działał prawidłowo, a reszta była nie była responsywna (pomimo zastosowania rezystorów _pull-up_). Podjęto więc decyzję o zamianie klawiatury na trzy osobne przyciski z wbudowanym rezystorem podciągającym. Po tej zmianie wykrywane były już wciśnięcia wszystkich użytych przycisków :+1:. 


## Opis implementacji (zmiany względem laboratorium 5): :floppy_disk:  
Projekt został wzbogacony o interfejs graficzny (wzorowany na panel operatorski). Do wykonania _GUI_ użyto biblioteki _Tkinter_. Do komunikacji pomiędzy stacją roboczą (komputerem) a RaspberryPi wykorzystano **sockety TCP/IP**.   Z poziomu GUI można włączyć/wyłączyć zieloną diodę, zmienić tryb sterowania systemem (tryb ręczny i automatyczny) oraz zadać wypełnienie PWM. RaspberryPi przesyła do komputera aktualną wartość wypełnienia PWM oraz _logi_ opisujące, kiedy i który przycisk został wciśnięty.  


## Sprawdzenie działania systemu:  
Pod koniec zajęć system został zaprezentowany Prowadzącemu. Udało się osiągnąć założone cele dotyczące funkcjonalności systemu. Film prezentujący działanie systemu został umieszczony w dokumentacji końcowej projektu.





  


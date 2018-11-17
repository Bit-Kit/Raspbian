# FTP serwer na Raspberry Pi

### Cel:
Celem jest stworzenie serwera FTP na Raspberry Pi z możliwością dostępu __bez autoryzacji__.
Ponieważ moje urządzenie docelowe ma ograniczoną funkcjonalność w przesyłaniu plików i nie może korzystać z logowanej sesji FTP,
potrzebowałem rozwiązanie, które by sprawiło przesyłanie plików po FTP, ale z ogólnie dostępnego foldera.

### Hardware/Software:
* Raspberry Pi 3 model B WiFi Bluetooth 1GB RAM 1,2GHz
* System operacyjny: Raspbian GNU/Linux 9.4
* Wersja Kernel: 4.14.62-v7+

### Instalacja
Instalujemy pakiet vsftpd.conf:

    sudo apt-get install vsftpd
    
Dalej przeprowadzamy konfigurację:

    sudo nano /etc/vsftpb.conf
    
Zmieniamy następne pozycje:

   listen=NO
   listen_ipv6=YES
   anonymous_enable
   

 



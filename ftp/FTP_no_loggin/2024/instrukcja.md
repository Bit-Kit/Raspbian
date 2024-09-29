# FTP na Raspberry Pi do celów multimedialnych (nie dokończone)

### Cel:
Celem jest stworzenie serwera FTP na Raspberry Pi z możliwością dostępu __bez autoryzacji__.


### Hardware/Software:
* Raspberry Pi 4 model B	B WiFi DualBand Bluetooth 2GB RAM 1,8GHz
* System operacyjny: Raspbian GNU/Linux 9.4 
* Wersja Kernel: 4.14.62-v7+ 
## Czynności przygotowawcze
### Pliki do pobrania
* [Aktualna wercja Raspbian](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-32-bit)
* [Aplikacja "Etcher" dla zapisania obrazu Raspbian na kartę SD](https://etcher.balena.io/)

### Ustawienia systemowe
Po uruchomieniu systemu należy wykonać aktualizację pakietów:

    sudo apt-get update   
    sudo apt-get upgrade
Przechodzimy do konfiguracji systemu raspbian

    sudo raspi-config

### Konfiguracja sieci
## Instalacja pakietu vsftpd
Instalacja pakietu vsftpd:
    
    sudo apt-get install vsftpd
    
Przeprowadzenie konfiguracji vsftpd.conf:

    sudo nano /etc/vsftpb.conf
    
Zmieniamy następne pozycje:
```
   listen=NO    #Opcja YES pozwoli VSFTPD działać bez pomocy inetd/xinetd.
   
   listen_ipv6=YES    #Włączamy nasłuchiwanie protokołu Ipv6
   
   anonymous_enable=YES    #Zezwolamy na anonimowy dostęp
   
   no_anon_password=YES    #Wyłączamy żądanie hasła dla anonimowych użytkowników
   
   anon_root=/var/ftp/    #Wskazujemy ściężkę dla anonimowych użytkowników
   
   local_enable-NO    #Oznacza, że ​​każdy normalny użytkownik wymieniony w /etc/passwdpliku może się zalogować.
   
   write_enable=YES    #Zezwalamy na zapisywanie plików
   
   anon_upload_enable=YES    #Zezwalamy na pobieranie plików dla anonimowych użytkowników
   
   anon_mkdir_write_enable=YES    #Zezwalamy anonimowym użytkownikom na tworzenie folderów
   
   dirmessage_enable=YES    #Opcja YES wyświetla wiadomość z pliku .message użytkownikom,
   którzy weśli do katalogu
   
   use_localtime=YES    #Przy YES vsftpd wyświetli listę katalogów z czasem w lokalnej strefie czasowej.
   Domyślnie wyświetla się GMT.
   
   xferlog_enable=YES    #Zezwalamy na zapisywanie logów
   
   connect_from_port_20=YES    #Ustalamy port wychodzących połączeń z serwera na 20
   
   secure_chroot_dir=/var/run/vsftpd/empty  #
   
   pam_service_name=vsftpd    #Wskazujemy PAM serwis
   
   rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem    #Tu jest ścieżka do certyfikatu SSL
   
   rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key    #Tu jest ścieżka do prywatnego klucza SSL
   
   ssl_enable=NO    #Wyłączamy certyfikacje SSL
   ```
Reszta pozostaje zakomentowana. W następnym kroku tworzymy folder do plików:
   
    sudo mkdir /var/ftp
        
Udzielamy wspólny dostęp do folderu:
   
    sudo chmod 755 /var/ftp
   
Zmieniamy właściciela foldera na "ftp":

    sudo chown ftp:ftp /var/ftp
    
Resetujemy usługe:

    sudo service vsftpd restart 
    
## Montowanie nośnika przenośnego

---
### Źródła <a name="zrodla"></a>

* [www.raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2018/05/creating-ftp-server-with-raspberry-pi/)
* [dug.net.pl](https://dug.net.pl/tekst/158/konfiguracja_serwera_vsftpd_z_wirtualnymi_uzytkownikami_w_bazie_db4_/)
* [FTP vs SMB](https://cloudinfrastructureservices.co.uk/ftp-vs-smb-whats-the-difference-performance-speed-security/)

 



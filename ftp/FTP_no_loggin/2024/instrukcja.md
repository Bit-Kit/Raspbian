# FTP na Raspberry Pi do celów multimedialnych (nie dokończone)

### Cel:
Celem jest stworzenie serwera FTP na Raspberry Pi z możliwością dostępu __bez autoryzacji__.


### Hardware/Software:
* Raspberry Pi 4 model B WiFi DualBand Bluetooth 2GB RAM 1,8GHz
* System operacyjny: Debian GNU/Linux 11 (lsb_release -a) 
* Wersja Kernel: 6.1.21-v8+ (uname -r)
## Czynności przygotowawcze
### Pliki do pobrania
* [Aktualna wercja Raspbian](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-32-bit)
* [Aplikacja "Etcher" dla zapisania obrazu Raspbian na kartę SD](https://etcher.balena.io/)
* [PuTTY](https://www.putty.org/)

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

## Dodanie użytkownika dla pracy ftp (w przypadku jeśli nie utworzono automatycznie podczas instalacji vsftpd)

    sudo mkdir /var/ftp
    sudo mkdir /home/ftp
    
Tworzymy użytkownika ftp z -u najniższą wartością UID

    sudo useradd -m -u 118  -s /usr/sbin/nologin ftp
    sudo chmod a-w /var/ftp

Dodajemy usera ftp do grupy ftp:

    sudo usermod -a -G ftp ftp
    
Sprawdzamy poprawność parametrów konta ftp:

    sudo cat /etc/passwd
    sudo id ftp

Powinno wyglądać przykładowo tak:

    ftp:x:117:125:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin

## Dodadnie użytkownika anonimowego oraz folderu wspólnego:

    sudo useradd -m  -s /usr/sbin/nologin useranonim             #Tworzymy użytkownika "useranonim"
    sudo passwd useranonim                                       #Zadajemy hasło takie jak login
    sudo chown root /var/ftp                                     #Główny folder powinien mieć właściciela root i zakaz zapisu
    sudo chmod -w /var/ftp                                       #Główny folder powinien mieć zakaz zapisu
    sudo mkdir /var/ftp/pobranie                                 #Tworzymy folder wspólny
    sudo chmod a+rwx /var/ftp/pobranie/                          #Nadajemy folderowi uprawnienia
    sudo chown useranonim:ftp /var/ftp/pobranie                  #Zmieniamy właściciela wspólnego foldera na "useranonim"
    sudo chmod g+s /var/ftp/pobranie/                            #Parametr dzięki któremu wszystkie tworzone foldery w pobranie/ będą przypisywane "useranonim"


    sudo id useranonim

Przeprowadzenie konfiguracji vsftpd.conf:

    sudo nano /etc/vsftpb.conf
    
Zmieniamy następne pozycje:
```
   listen=YES    #Opcja YES pozwoli VSFTPD działać bez pomocy inetd/xinetd.
   
   listen_ipv6=NO    #Włączamy nasłuchiwanie protokołu Ipv6
   
   anonymous_enable=YES    #Zezwolamy na anonimowy dostęp

   local_enable=YES
    
   write_enable=YES

   ?no_anon_password=YES    #Wyłączamy żądanie hasła dla anonimowych użytkowników

   anon_upload_enable=YES    #Zezwalamy na pobieranie plików dla anonimowych użytkowników
   
   anon_mkdir_write_enable=YES    #Zezwalamy anonimowym użytkownikom na tworzenie folderów
 
   use_localtime=YES         #Przy YES vsftpd wyświetli listę katalogów z czasem w lokalnej strefie czasowej.
   Domyślnie wyświetla się GMT.

   xferlog_enable=YES

   connect_from_port_20=YES

   chown_uploads=YES

   chown_username="anonimUser"

   chroot_local_user=YES

   chroot_list_enable=YES

   pam_service_name=vsftpd

   ```
Reszta pozostaje zakomentowana. 
Na samym końcu dodajemy:
```

anon_root=/home/ftp
local_root=/home/"anonimUser"
nopriv_user="anonimUser"
allow_writeable_chroot=YES
```

W następnym kroku tworzymy folder do plików:
   
    sudo mkdir /var/ftp
        
Udzielamy wspólny dostęp do folderu:
   
    sudo chmod 755 /var/ftp
   
Zmieniamy właściciela foldera na "ftp":

    sudo chown ftp:ftp /var/ftp
    
Resetujemy usługe:

    sudo service vsftpd restart  
    sudo service vsftpd status

## Rozwiązywanie problemów:
Sprawdzamy porty (ftp - 21)

    sudo ss -lt


How to Solve the VSFTPD 500 OOPS Error - 
## Montowanie nośnika przenośnego
Sprawdzamy podłączone nośniki:

    sudo fdisk -l
    sudo mkdir /home/ftp/pendrive
    
Folder powinien mieć uprawnienia:

    sudo chmod a-w /home/ftp/

    

Montujemy nasz nośnik w systemie ntfs do /home/ftp/pendrive

    sudo mount -t ntfs -o rw /dev/sda1 /home/ftp/pendrive

---
### Źródła <a name="zrodla"></a>

* [www.raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2018/05/creating-ftp-server-with-raspberry-pi/)
* [dug.net.pl](https://dug.net.pl/tekst/158/konfiguracja_serwera_vsftpd_z_wirtualnymi_uzytkownikami_w_bazie_db4_/)
* [FTP vs SMB](https://cloudinfrastructureservices.co.uk/ftp-vs-smb-whats-the-difference-performance-speed-security/)
* [Artykuł](https://www.lissyara.su/articles/freebsd/programms/vsftpd/)
* [Artykuł_2-informacja_na_temat_dostępności_wspólnego_folderu](https://unixforum.org/viewtopic.php?t=81575)
 



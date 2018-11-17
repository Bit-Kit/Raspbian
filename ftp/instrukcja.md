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
```
   listen=NO
   listen_ipv6=YES
   anonymous_enable=YES
   no_anon_password=YES
   anon_root=/var/ftp/
   local_enable-NO
   write_enable=YES
   anon_upload_enable=YES
   anon_mkdir_write_enable=YES
   dirmessage_enable=YES
   use_localtime=YES
   xferlog_enable=YES
   connect_from_port_20=YES
   secure_chroot_dir=/var/run/vsftpd/empty
   pam_service_name=vsftpd
   rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
   rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
   ssl_enable=NO
   ```
Reszta pozostaje zakomentowana. W następnym kroku tworzymy folder do plików:
   
    sudo mkdir /var/ftp
        
Udzielamy wspólny dostęp do folderu:
   
    sudo chmod 755 /var/ftp
   
Zmieniamy właściciela foldera na "ftp":

    sudo chown ftp:ftp /var/ftp


 



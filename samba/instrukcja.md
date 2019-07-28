# Udostępnianie zasobów Raspberry Pi w sieci

##### Krok po kroku:

Instalujemy pakiet SAMBA na urządzeniu:
	
    sudo apt-get install samba
   
Ustalamy hasło logowania do zasobów:

	sudo smbpasswd -a pi
  
Konfigurujemy plik *smb.conf*:

	sudo nano /etc/samba/smb.conf
    
*Uwaga:*

	workgroup = (twoja_grupa_robocza) default "WORKGROUP"
   
Pod wierszem ***[global]*** dopisujemy:

	security = user
	encrypt passwords = true
	map to guest = bad user
	guest account = nobody
   
Następnie, na końcu pliku tworzymy obszar udostępniania:

	[usbstorage]
    path = /mnt/usbstorage/
	writeable = yes
	read only = no
	browseable = yes

Po zapisaniu resetujemy usługę SAMBA:

	sudo /etc/init.d/samba restart
    
Źródło: <http://dmitrysnotes.ru/raspberry-pi-3-organizaciya-setevogo-dostupa-k-fajlam-cherez-samba>

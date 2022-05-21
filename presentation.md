###Presentation

##Empire Powershell Server Setup:

	$ sudo apt install powershell-empire		# install package
	$ sudo powershell-empire server 		# run server

Empire Powershell also comes by default with Kali linux, which you can easily run in virtual box after installing the virtual box package for it here:

https://www.kali.org/get-kali/#kali-virtual-machines

##Default Server Credentials:

	Username: empireadmin
	Password: password123

##Connecting to Server via Starkiller GUI Interface:
	
We will be explaining how to break into your own machine so everything will be done locally.

##On the linux vm:

	$ cd /opt
	$ sudo git clone https://github.com/BC-SECURITY/Empire.git
	$ cd Empire
	$ sudo ./setup/install.sh


	$ ifconfig -a					# get the local IP address for the eth0 network interface
	$ 

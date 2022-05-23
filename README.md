# Hack Yourself With Powershell Empire

###### By Steven Rakhmanchik and Israel Pina
---
## "What'd you guys make?"

Our project demonstrates the capabilities of Powershell Empire, how it works, and how you can (but shouldn't) use it.

## "What is Powershell Empire?"

Powershell Empire is a tool that helps create payloads in order to gain access to systems.

### "Wait, what?"

Powershell Empire is essentially a hacking tool. It allows one to create customized payload files to help gain access to someone else's computer once the user [victim] opens said file on their machine. 

### "What's a payload?"

A payload is a file that contains malicious code used to establish a backdoor into the victim's system and often to also establish persistence on said system. They often go undetected because they run in the background of the victim's system.

### "Wow, really? How do I do this?"

See our [PRESENTATION.md file](https://github.com/israelpina004/final_project_empirekillers/blob/master/presentation.md). (We do not encourage any illegal activity!)

### "Tell me more!"

Like how to download Powershell Empire and Starkiller? Sure.

If you have Kali Linux, all it takes is the command:

	$ sudo apt install powershell-empire

On other systems, run these commands:

	$ git clone https://github.com/BC-SECURITY/Empire.git
	$ cd Empire
	$ sudo ./setup./install.sh

This will grab the Empire repository from github and install Empire on your system. Follow the instructions carefully.

To run Empire on Kali Linux, simply run the 
	
	$ powershell-empire

command. For other systems, the following is shown once installation is complete:

	$ Run the following commands in separate terminals to start Empire
	./ps-empire server
	./ps-empire client
	source ~/.bashrc to enable nim

Installing Starkiller is much simpler. All Starkiller is is a GUI application for Empire. All it takes is going to [this link](https://github.com/BC-SECURITY/Starkiller/releases) and downloading the "starkiller.Setup.1.10.0.exe" file.

## "So how was the work distribution like?"

See our [WORKLOG.md file](https://github.com/israelpina004/final_project_empirekillers/blob/master/WORKLOG.md).https://github.com/israelpina004/final_project_empirekillers/blob/master/WORKLOG.md

## "This all sounds really cool."

Thanks! That's because it is.

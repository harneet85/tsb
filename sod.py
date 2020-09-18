####### Python script Created and Maintained by - Harneet Singh - harneesi@in.ibm.com
####### code name- thor
####### v-1
####### Files - sod.py , sod.sh , lib/connect.py , lib/servername.py
####### Dir - lib
import os,sys
import subprocess
from termcolor import colored
from subprocess import PIPE
from tabulate import tabulate
import colorama
import platform
from getpass import getpass
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),'lib'))
from serverlist import *
import connect


head=["Server","Port ok/nok","DiskSize ok/nok"]
port=[]
command=""
hostcount=0
disksize="90"
user=""
passw=""
dirname="sodout"
colorama.init()
enable="yes"


#######

def inputuser():
	global user
	global passw
	global enable
	enable=raw_input("Credentials same for all server or not ? y/n ").lower()
	while not ( len(enable) == 1 and ( enable == "y" or enable == "n" )):
		print("Incorrect input, try again")
		enable=raw_input("Credentials same for all server or not ? y/n").lower()
	if enable == "y":
		user=raw_input("Provide your username : ")
		passw=getpass()

def dircreate():
	if not os.path.exists(dirname):
		os.mkdir(dirname)
	if not os.path.exists("report"):
		os.mkdir("report")

def dirremove():
	if os.path.exists(dirname):
		os.rmdir(dirname)



#### Method to set color according to system
def setcolor(i):
	global colo
	if i.find("od")>=0:
		colo="on_blue"
	elif i.find("jb0")>=0:
		colo='on_magenta'
	elif i.find("ti")>=0:
		colo='on_grey'
	else:
		colo="on_yellow"

### MAIN Method

def work(host):
	for i in host:
		count=0
		global hostcount
		global command
		global port
		global summary
		global user
		global passw
		global enable
		hostcount=hostcount+1
		rfilename="/tmp/"+user+"."+i
		lfilename="./"+dirname+"/"+i
		setcolor(i)
		print colored("\n_______________________%s %s ______________created by harneesi@in.ibm.com\n"%(hostcount,i),'white',colo,attrs=['bold'])
		diclen=len(host[i])
		c0="uname"
		if enable == "n" :
                	user=raw_input("Provide your username for server "+i+" ")
                	passw=getpass()


		connobj=connect.conn()
		connobj.conexe(i,user,passw)
		sysname=connobj.command(c0).rstrip("\n")
                if i=="es4jb04bsab":
                        for x in host[i]:
                                command=command+"|\:"+x+"$"
                        command=command+"'|grep -i '172.18.215.45"
                elif sysname.find("AIX")>=0:
                        for x in host[i]:
                                command=command+"|\."+x+"$"
                else:
                        for x in host[i]:
                                command=command+"|\:"+x+"$"
                c1="hostname >"+rfilename+";netstat -an |grep -i listen| grep -iv tcp6| awk '{print $4}'|egrep -i '99999"+command+"'>>"+rfilename
                c2="echo Disk space >>"+rfilename+";df -Pm|sed 's?%??g'| awk '$(NF-1) > "+disksize+" {print $0}'>>"+rfilename+""
		connobj.command(c1)
		connobj.command(c2)
		connobj.recieve(rfilename,lfilename)
		pFound=colored("All OK",'green')
		print colored(" --- Ports information --(os - %s )-- "%(sysname),'white',colo,  attrs=['bold'])	
		for x in host[i]:
			colored("\t ---- PORTS ---- ",'green')
			with open(lfilename, 'r') as f:
				for line in f:
					if x in line:                
						count=count+1
						print colored("\t"+i+"\t "+x+"\t "+host[i][x]+"\t FOUND \t"+line.rstrip("\n"),'green')
							
								#port.append([i,x,host[i][x],colored("FOUND",'green')])
						break
					if line.find("Filesystem")>=0:
						#print(line)
						print colored("\t"+i+"\t "+x+"\t "+host[i][x]+"\t NOT FOUND \t",'red')
						break

		if count==diclen:
			#print colored("\t ALL Ports verified OK",'green', 'on_grey', ['blue', 'blink'])
			print colored("\t ALL Ports verified OK \t",'white', 'on_green', attrs=['blink','bold'])
		else:
			print colored("\t ----SOMETHING WRONG -----", 'white','on_red',attrs=['blink','bold'])
			pFound=colored("Ports has Issue",'red')
		print("\t Ports found =%s Ports required =%s"%(count,diclen))
		port.append([i,pFound])


		print colored(" --- Disk Info: More then "+disksize+" ---- ",'white',colo,  attrs=['bold'])
		with open(lfilename, 'r') as f:
			for line in f:
				dfound=False
				if "Filesystem" in line:		
					for line in f:
						colored("\t ---Disk more than "+disksize+"---- ",'green')
						print(line.rstrip("\n"))
						if len(line)>5:
							dfound=True
			arrlen=len(port)
			newarr=port[arrlen-1]
			if dfound:
				newarr.append(colored("FileSystem more than "+disksize,'red'))
			else:
				newarr.append(colored("FileSystem OK",'green'))
			


		print("\n")
		command=" "
#		os.remove(lfilename)

##### Method to print summary
def tabprint():
	print("----------Summary-------------- ")
	print(tabulate(port,head,tablefmt="pretty"))


##### MAIN Execution starts

#inputuser()
dircreate()
work(papyrus)
work(jboss)
#work(jboss2)
work(treasury)
work(ondemand)
tabprint()
#dirremove()

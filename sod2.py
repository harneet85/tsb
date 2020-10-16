####### Python script Created and Maintained by - Harneet Singh - harneesi@in.ibm.com
####### code name- thor
####### v-2, date 23 Sep 2020
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


head=["Server","Port ok/nok","DiskSize ok/nok","URL ok/nok","Process ok/nok"]
port=[]
command1=""
hostcount=0
disksize="90"
user="in0090g5"
passw="Wizard12345"
dirname="sodout"
colorama.init()
enable="yes"
c4=""
c1=""
rfilename=""
command4=""


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

def urlcommand(hosturl):
	global c4
	global command4
	c4=""
	command4=""
	for i in hosturl:
		if i.find("url")>=0:
			command4=command4+"echo checking "+hosturl[i]+">>"+rfilename+";echo""| awk '{print \"\t"+i+"\t\t"+str(hosturl[i])+" \" system(\"wget "+str(hosturl[i])+" 2>&1| egrep 'OK'\") }' >> "+rfilename+";"
		c4="echo ---- URL CHECKING ------ >> "+rfilename+";"+command4
	#return c4

def processcommand(hosturl):
        global c5
        global command5
        c5=""
        command5=""
        for i in hosturl:
                if i.find("process")>=0:
                        #command5=command5+"echo checking "+hosturl[i]+">>"+rfilename+";echo""| awk '{print \"\t"+i+"\t\t"+str(hosturl[i])+" \" system(\"wget "+str(hosturl[i])+" 2>&1| egrep 'OK'\") }' >> "+rfilename+";"
                        command5=command5+"a=`echo "+i+"| awk -F\"_\" '{system(\"ps -ef | grep -i \"$2)}'|grep -v grep|wc -l`; echo "+i+" $a  >> "+rfilename+";"
	c5="echo ---- Process CHECKING ------ >> "+rfilename+";"+command5+"echo ---- Process End----- >>"+rfilename

def portcommand(hostin,sysnamein):
	global command1
	global c1
	if hostin=="es4jb04bsab":
		for x in host:
			if x.find("url")>=0 or x.find("process")>=0:
				continue
			command1=command1+"|\:"+x+"$"
		command1=command1+"'|grep -i '172.18.215.45"
	elif sysnamein.find("AIX")>=0:
		for x in hostin:
			if x.find("url")>=0 or x.find("process")>=0:
				continue
			command1=command1+"|\."+x+"$"
	else:
		for x in hostin:
			if x.find("url")>=0 or x.find("process")>=0:
				continue
			command1=command1+"|\:"+x+"$"
	c1="hostname >"+rfilename+";netstat -an |grep -i listen| grep -iv tcp6| awk '{print $4}'|egrep -i '99999"+command1+"'>>"+rfilename

### MAIN Method

def work(host):
	for i in host:
		count=0
		diclen=0
		global hostcount
		global command
		global port
		global summary
		global user
		global passw
		global enable
		global rfilename
		hostcount=hostcount+1
		rfilename="/tmp/"+user+"."+i
		lfilename="./"+dirname+"/"+i
		setcolor(i)
		print colored("\n_______________________%s %s ______________created by harneesi@in.ibm.com\n"%(hostcount,i),'white',colo,attrs=['bold'])
		c0="uname"
		if enable == "n" :
                	user=raw_input("Provide your username for server "+i+" ")
                	passw=getpass()


		connobj=connect.conn()
		connobj.conexe(i,user,passw)
		sysname=connobj.command(c0).rstrip("\n")
		portcommand(host[i],sysname)
                c2="echo Disk space >>"+rfilename+";df -Pm|sed 's?%??g'| awk '$(NF-1) > "+disksize+" {print $0}'>>"+rfilename+""
		connobj.command(c1)
		connobj.command(c2)
        	urlcommand(host[i])
		processcommand(host[i])
		connobj.command(c4)
		connobj.command(c5)
		connobj.recieve(rfilename,lfilename)
		pFound=colored("All OK",'green')
		print colored("\t--- Ports information --(os - %s )-- "%(sysname),'white',colo,  attrs=['bold'])	
		for x in host[i]:
			if x.find("url")>=0 or x.find("process")>=0:
				continue

			diclen=diclen+1	
			colored("\t ---- PORTS ---- ",'green')
			with open(lfilename, 'r') as f:
				for line in f:
					if x in line:                
						count=count+1
						print colored("\t"+i+"\t "+x+"\t "+host[i][x]+"\t FOUND \t"+line.rstrip("\n"),'green')
						break
					if line.find("Filesystem")>=0:
						print colored("\t"+i+"\t "+x+"\t "+host[i][x]+"\t NOT FOUND \t",'red')
						break

		if count==diclen:
			print colored("\t ALL Ports verified OK \t",'white', 'on_green', attrs=['blink','bold'])
		else:
			print colored("\t ----SOMETHING WRONG -----", 'white','on_red',attrs=['blink','bold'])
			pFound=colored("Ports has Issue",'red')
		print("\t Ports found =%s Ports required =%s"%(count,diclen))
		port.append([i,pFound])

############## disk info #############

		print colored("\t--- Disk Info: More then "+disksize+" ---- ",'white',colo,  attrs=['bold'])
		dfound=False
		with open(lfilename, 'r') as f:
			for line in f:
				if "Filesystem" in line:		
					for line in f:
						if "URL" in line:
							break
						print("\t"+line.rstrip("\n"))
						if len(line)>5:
							dfound=True

			arrlen=len(port)
			newarr=port[arrlen-1]
			if dfound:
				newarr.append(colored("FileSystem more than "+disksize,'red'))
			else:
				newarr.append(colored("FileSystem OK",'green'))



################# URL CHECKING ######### 
		ufound=True
		ufound2=False
                print colored("\t--- URL Info ---- ",'white',colo,  attrs=['bold'])
                with open(lfilename, 'r') as f:
                        for line in f:
                                if "URL" in line:
                                        for line in f:
                                                if line.find("Process CHECKING")>=0:
                                                        break
						if line.find("checking")>=0 or line.find("response")>=0:
							continue
						if len(line)>5:
							ufound2=True
                                                	if line.rstrip("\n")[-1]=="1":
                                                       		ufound=False
								print colored(line.rstrip("\n")+"\t\t NOT OK",'red')
							else:
								print colored(line.rstrip("\n")+"\t\t OK",'green')

                        arrlen=len(port)
                        newarr=port[arrlen-1]
                        if ufound:
                                if ufound2:
					newarr.append(colored("URL OK",'green'))
					print colored("\t ALL URL verified OK \t",'white', 'on_green', attrs=['blink','bold'])
				else:
					print("\tNo URL to check")
					newarr.append(colored("No URL set"))
                        else:
                                newarr.append(colored("URL not OK",'red'))
				print colored("\t ----SOMETHING WRONG -----", 'white','on_red',attrs=['blink','bold'])

################ PROCESS Checking

                pfound=True
		pfound2=False
                print colored("\t--- Process Info ---- ",'white',colo,  attrs=['bold'])
                with open(lfilename, 'r') as f:
                        for line in f:
                                if "Process" in line:
					for line in f:
						if line.find("Process CHECK")>=0:
							continue
						if line.find("Process End")>=0:
							break
						n=line.split(" ")[0]
						n2=line.rstrip("\n").split(" ")[1]
						if host[i][n]==n2:
							print colored("\t"+n+"\t requiredValue: "+host[i][n]+" ValueFound: "+n2,'green')	
						else:
							print colored("\t"+n+"\t required value"+host[i][n]+" Value found"+n2,'red')
							pfound=False
						if len(line)>7:
							pfound2=True
							#print("line : ",len)


                        arrlen=len(port)
                        newarr=port[arrlen-1]
			#print(pfound2)
                        if pfound:
				if pfound2:
                                	newarr.append(colored("Processes OK",'green'))
					print colored("\t ALL Process verified OK \t",'white', 'on_green', attrs=['blink','bold'])
				else:
					print colored("\tNo processes set")
					newarr.append(colored("No process set"))
                        else:
                                newarr.append(colored("Process not OK",'red'))
				print colored("\t ----SOMETHING WRONG -----", 'white','on_red',attrs=['blink','bold'])

#####################


			


		print("\n")
		command=" "
		command4=""
		os.remove(lfilename)
	if connect.ssh:
		connect.ssh.close()

##### Method to print summary
def tabprint():
	print("\t----------Summary-------------- ")
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
dirremove()
print("\tJBOSS server scheduled to stop at 06:00 CEST and start at 07:00 CEST, Mon - Fri")
print("\tPapyrus is scheduled to restart every Sunday at 05:00 CEST ")



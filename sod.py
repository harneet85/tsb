import os,sys
import subprocess
#import connect
from termcolor import colored
from subprocess import PIPE
#from collections import OrderedDict 
from tabulate import tabulate

papyrus= {
"uk1py01tsb":{"19050":"IPAM","19051":"DC","19049":"NODE01"},
"uk1py03tsb":{"19021":"NODE01","19022":"NODE02","19023":"NODE03","19024":"NODE04","80":"HTTP","666":"HTTP","443":"HTTPS"},
"uk1py05tsb":{"19025":"NODE05","19026":"NODE06","19027":"NODE07","19028":"NODE08","80":"HTTP","666":"HTTP","443":"HTTPS"},
"uk1py07tsb":{"19029":"NODE09","19030":"NODE10","19031":"NODE11","80":"HTTP","666":"HTTP","443":"HTTPS"},
"uk2py01tsb":{"19050":"IPAM","19051":"DC","19049":"NODE01"},
"uk2py03tsb":{"19021":"NODE01","19022":"NODE02","19023":"NODE03","19024":"NODE04","80":"HTTP","666":"HTTP","443":"HTTPS"},
"uk2py05tsb":{"19025":"NODE05","19026":"NODE06","19027":"NODE07","19028":"NODE08","80":"HTTP","666":"HTTP","443":"HTTPS"},
"uk2py07tsb":{"19029":"NODE09","19030":"NODE10","19031":"NODE11","80":"HTTP","666":"HTTP","443":"HTTPS"},
}
ondemand={
"uk1od01tsb":{"9080":"server1","9081":"server2","9082":"server3"},
"uk1od11tsb":{"9080":"server1","9081":"server2","9082":"server3"},
"uk2od01tsb":{"9080":"server1","9081":"server2","9082":"server3"}
}
jboss={
"es4jb04bsab":{"4448":"Jboss", "3873":"Jboss", "39490":"Jboss", "33286":"Jboss", "3528":"Jboss", "8009":"Jboss", "4457":"Jboss", "1098":"Jboss", "1099":"Jboss", "1100":"Jboss", "1101":"Jboss", "39886":"Jboss", "53232":"Jboss", "27377":"Jboss", "8083":"Jboss", "8565":"Jboss", "46261":"Jboss", "48537":"Jboss", "7900":"Jboss", "34364":"Jboss", "4444":"Jboss", "39612":"Jboss", "4445":"Jboss", "4446":"Jboss", "4447":"Jboss"}
}
treasury={
"uk1ti01tsb":{"1416":"MQMGR QMPRO"},
"uk1ti11tsb":{"1416":"MQMGR QMTSBGOS"}
}

head=["Server","Port ok/nok","DiskSize ok/nok"]
port=[]
command=""
hostcount=0

def work(host):
	for i in host:
		count=0
		global hostcount
		global command
		global port
		global summary
		hostcount=hostcount+1
		fileName="./sodout/"+i
		if i.find("od")>=0:
			colo="on_blue"
		elif i.find("jb0")>=0:
			colo='on_magenta'
		elif i.find("ti")>=0:
			colo='on_grey'
		else:
			colo="on_yellow"
		#print colored("_______________________%s %s__________________________"%(hostcount,i),'on_yellow')
		print colored("\n_______________________%s %s______________created by harneesi@in.ibm.com\n"%(hostcount,i),'white',colo,attrs=['bold'])
		for x in host[i]:
			command=command+"|\."+x+"$"
		if i=="es4jb04bsab":
			for x in host[i]:
				command=command+"|."+x+"$"
		else:
			for x in host[i]:
				command=command+"|\."+x+"$"
		diclen=len(host[i])
		cc="printf '\n'; netstat -an |grep -i listen| grep -iv tcp6| awk '{print \$4}'|egrep -i '99999"+command+"';printf '\n\n';df -m|sed 's?%??g'| awk '\$4 > 80 {print \$0}'"
			
		aa="toxsocks /home/harneet/PycharmProjects/tsb1/venv/bin/python /home/harneet/PycharmProjects/tsb1/main.py "+i+" \""+cc+"\""
		outfile = open(fileName,"w") #same with "w" or "a" as opening mode
		subprocess.call(aa, stdout=outfile,shell=True)
		pFound=colored("All OK",'green')
		for x in host[i]:
			with open(fileName, 'r') as f:
				for line in f:
					if i in line:                
						outnum=-1
						for line in f:
							outnum=line.find(x)
							colored("\t ---- PORTS ---- ",'green')
							if outnum>=0:
								count=count+1
								print colored("\t"+i+"\t "+x+"\t "+host[i][x]+"\t FOUND \t"+line.rstrip("\n"),'green')
								
								#port.append([i,x,host[i][x],colored("FOUND",'green')])
								break
							if line.find("Filesystem")>=0:
								#print(line)
								break
						if outnum<0:
							print colored("\t"+i+"\t "+x+"\t "+host[i][x]+"\t NOT FOUND \t"+line.rstrip("\n"),'red')
							#port.append([i,x,host[i][x],colored("NOT FOUND",'red')])

		if count==diclen:
			#print colored("\t ALL Ports verified OK",'green', 'on_grey', ['blue', 'blink'])
			print colored("\t ALL Ports verified OK \t",'white', 'on_green', attrs=['blink','bold'])
		else:
			print colored("\t ----SOMETHING WRONG -----", 'white','on_red',attrs=['blink','bold'])
			pFound=colored("Ports has Issue",'red')
		print("\t Ports found =%s Ports required =%s"%(count,diclen))
		port.append([i,pFound])


		print colored(" --- Disk Info: More then 80% ---- ",'white',colo,  attrs=['bold'])
		with open(fileName, 'r') as f:
			for line in f:
				dfound=False
				if "Filesystem" in line:		
					for line in f:
						colored("\t ---Disk more than 80%---- ",'green')
						print(line.rstrip("\n"))
						if len(line)>5:
							dfound=True
			arrlen=len(port)
			newarr=port[arrlen-1]
			if dfound:
				newarr.append(colored("FileSystem more than 80",'red'))
			else:
				newarr.append(colored("FileSystem OK",'green'))



		print("\n")
		command=" "
def tabprint():
	print("----------Summary-------------- ")
	#print(tabulate(port,tablefmt="fancy_grid"))
	print(tabulate(port,head,tablefmt="pretty"))

#work(papyrus)
#work(ondemand)
#work(jboss)
work(treasury)
tabprint()

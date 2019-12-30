import time
import stat
import commands
import socket
import struct
import re
import os
import sys
from pathlib import Path


#SYS_BOOT_TIME = int(open('/proc/stat').read().split('btime ')[1].split()[0])
h1=open('c1pu.txt','w')
l1=open('cpu10.txt','w')
g1=open('cpu11.txt','w')
m1=open('cpu12.txt','w')
n1=open('cpu13.txt','w')
open('out.txt','w')
open('out1.txt','w')
open('out2.txt','w')
open('out3.txt','w')
interval=1
def CpuUti():
	#print ("\nThe CPU utilizations are:\n")
	h=open('cpu.txt','w')
	l=open('cpu0.txt','w')
	g=open('cpu1.txt','w')
	m=open('cpu2.txt','w')
	n=open('cpu3.txt','w')
	h1=open('c1pu.txt','a')
	l1=open('cpu10.txt','a')
	g1=open('cpu11.txt','a')
	m1=open('cpu12.txt','a')
	n1=open('cpu13.txt','a')
	with open('/proc/stat','r') as f:
		for line in f:		
			if line.startswith('cpu'):
				#print(line)		
				col_list=line.split()
				prev_usertime=col_list[1]
				#print(prev_usertime)
				prev_systime=col_list[3]
				prev_idle=col_list[4]
				time.sleep(interval)
				with open('/proc/stat','r') as a:
					for li in a:		
						if li.startswith('cpu'):
							col_list1=li.split()
							if(col_list1[0]==col_list[0]):
								curr_usertime=col_list1[1]
								#print(curr_usertime)
								curr_systime=col_list1[3]
								curr_idle=col_list1[4]
				delu=int(curr_usertime)-int(prev_usertime)
				#print(delu)
				dels=int(curr_systime)-int(prev_systime)
				deli=int(curr_idle)-int(prev_idle)
				deno=int(dels)+int(delu)+int(deli)
				sys_uti=(((float(delu)+float(dels))/float(deno))*100.00)
				sys_mode=((float(dels)/float(deno))*100)
				User_mode=((float(delu)/float(deno))*100)
				if col_list[0]=='cpu':
					#print('h')
					h.write(str(sys_uti))
					h.write('\n')
					h1.write(str(sys_uti))
					h1.write('\n')
					h.write(str(sys_mode))
					h.write('\n')
					h.write(str(User_mode))
					h.write('\n')
				if col_list[0]=='cpu0':
					#print('l')
					l.write(str(sys_uti))
					l.write('\n')
					l1.write(str(sys_uti))
					l1.write('\n')
					l.write(str(sys_mode))
					l.write('\n')
					l.write(str(User_mode))
					l.write('\n')
				if col_list[0]=='cpu1':
					#print('g')
					g.write(str(sys_uti))
					g.write('\n')
					g1.write(str(sys_uti))
					g1.write('\n')
					g.write(str(sys_mode))
					g.write('\n')
					g.write(str(User_mode))
					g.write('\n')
				if col_list[0]=='cpu2':
					#print('m')
					m.write(str(sys_uti))
					m.write('\n')
					m1.write(str(sys_uti))
					m1.write('\n')
					m.write(str(sys_mode))
					m.write('\n')
					m.write(str(User_mode))
					m.write('\n')
				if col_list[0]=='cpu3':
					#print('n')
					n.write(str(sys_uti))
					n.write('\n')
					n1.write(str(sys_uti))
					n1.write('\n')
					n.write(str(sys_mode))
					n.write('\n')
					n.write(str(User_mode))
					n.write('\n')
				#print col_list[0],": %.2f"%sys_uti
				#print 'User Mode : %.2f'%sys_mode
				#print 'System Mode :%.2f'%User_mode
				#print '\n'
				#print sys_uti
def meminfo():
	with open('/proc/stat','r') as f:
		for line in f:		
			if line.startswith('intr'):
				col_list=line.split()
				prev_intr=col_list[1]
				#print(prev_intr)
				time.sleep(interval)
				with open('/proc/stat','r') as b:
					for li in b:
						if li.startswith('intr'):
							col_list1=li.split()
							curr_intr=col_list1[1]
							#print(curr_intr)
				delintr=(int(curr_intr)-int(prev_intr))
				sys_intr=float(delintr)/float(interval)
				with open('out.txt','w') as cpuout:
					print >>cpuout, "\nThe Number of interrupts per interval time are:%.2f" %float(sys_intr)

	with open('/proc/stat','r') as f:
		for line in f:		
			if line.startswith('ctxt'):
				col_list=line.split()
				prev_ctxt=col_list[1]
				#print(prev_ctxt)
				time.sleep(interval)
				with open('/proc/stat','r') as c:
					for li in c:
						if li.startswith('ctxt'):
							col_list1=li.split()
							curr_ctxt=col_list1[1]
							#print(curr_ctxt)
				ctxt=(float(curr_ctxt)-float(prev_ctxt))/float(interval)
				with open('out.txt','a') as cpuout:
					print >>cpuout, "\nThe Number of Context switches per interval time are:",float(ctxt)
	with open('/proc/meminfo','r') as f:
		for line in f:		
			if line.startswith('MemFree:'):
				col_list=line.split()
				prev_freemem=(int(col_list[1])/1000.00)
				#print(prev_freemem)
				time.sleep(interval)
				with open('/proc/meminfo','r') as d:
					for li in d:
						if li.startswith('MemFree:'):
							col_list1=li.split()
							curr_freemem=(int(col_list1[1])/1000.00)
							#print(curr_freemem)
				availmem=(float(curr_freemem)-float(prev_freemem))/float(2)
				with open('out.txt','a') as cpuout:
					print >>cpuout,"\nThe Available memory is:",float(abs(availmem)),"MB" 
				mem_util=((float(total_mem)-float(curr_freemem))/float(total_mem))*100.0
				with open('out.txt','a') as cpuout:
					print >>cpuout, "\nThe Memory Utilization percentage is:%.2f" %float(abs(mem_util)) 
			if line.startswith('MemTotal:'):
				col_list=line.split()
				total_mem=(int(col_list[1])/1000.00)
				with open('out.txt','a') as cpuout:
					print >>cpuout, "\nThe Total memory is:",float(total_mem),"MB"
def diskstats():
	with open('/proc/diskstats','r') as f:
		for line in f:		
			col_list=line.split()
			if not (col_list[2].find('sda')):
				#print("\n\n")
				#print (col_list[2])
				prev_read=col_list[3]
				#print(col_list[3])
				prev_write=col_list[7]
				#print(col_list[7])
				prev_bread=col_list[5]
				#print(col_list[5])
				prev_bwrite=col_list[9]
				#print(col_list[9])
				time.sleep(interval)
				with open('/proc/diskstats','r') as e:
					for li in e:
						col_list1=li.split()
						if not (col_list1[2].find('sda')):
							if(col_list[2]==col_list1[2]):
								#print(col_list1[2])
								curr_read=col_list1[3]
								#print(col_list1[3])
								curr_write=col_list1[7]
								#print(col_list1[7])
								curr_bread=col_list1[5]
								#print(col_list1[5])
								curr_bwrite=col_list1[9]
								#print(col_list1[9])
				with open('out1.txt','a') as cpuout:
					print >>cpuout, float(abs(int(prev_read)-int(curr_read))/float(interval))
					print >>cpuout, float(abs(int(prev_write)-int(curr_write))/float(interval))
					print >>cpuout, float(abs(int(prev_bread)-int(curr_bread))/float(interval))
					print >>cpuout, float(abs(int(prev_bwrite)-int(curr_bwrite))/float(interval))

def GetPrgName(top,inode):										
		for line in os.listdir(top):
			for li in line.split('\n'):
				#print(li)
				pathname = top+'/'+li
				#print(pathname)
				p=pathname.split("/")
				if(p[2].isdigit()):
					try:
						for line in os.listdir(pathname):
							for li in line.split('\n'):
								if(li=='fd'):
									pathname1=pathname+'/'+li
									#print(pathname1)
									for line in os.listdir(pathname1):
										for li in line.split('\n'):

											pathname2 =pathname1+'/'+li
											#print(pathname2)
											st=os.stat(pathname2)
											ino=st.st_ino
											#print (ino)
											#print(inode)
											if int(inode)==int(ino):
												#print (ino)
												pathname=pathname+'/comm'
												with open(pathname) as f:
													for line in f:
														return line
					except:
						continue
def NetStats():
	with open('/proc/net/tcp','r') as f:
		count=0
		for line in f:
			col_list=line.split()
			if col_list[3]=='01':
				# print(col_list[3])
				count+=1 
		with open('out2.txt','a') as cpuout:
				print >>cpuout, "\nThe number of Active Established TCP connections are:",count
	with open('/proc/net/dev','r') as f:
		for line in f:
			if line.startswith('w'):
				col_list=line.split()
				precv=col_list[1]
				#print(precv)
				ptran=col_list[5]
				#print(ptran)
				prevb=precv+ptran
				#print(prevb)
				time.sleep(interval)
				with open('/proc/net/dev','r') as f:
					for li in f:
						if li.startswith('w'):
							col_list1=li.split()
							crecv=col_list[1]
							#print(crecv)
							ctran=col_list[5]
							#print(ctran)
							currb=crecv+ctran
							#print(currb)
				'''with open('/proc/net/dev','r') as f:
					for line in f:
						if line.startswith('e'):
							line=line.split(':')
							eth=line[0]
				ethname='ethtool '+eth
				with open(ethname,'r') as f:
					for line in f:
						if line.startswith('Speed'):
							print line'''		
				bandwidth=10
				delta=(int(currb)-int(prevb))/int(bandwidth)
				with open('out2.txt','a') as cpuout:
					print >>cpuout, "\nNetowrk Utilization:",delta

	with open('/proc/net/tcp','r') as f:
		count=0
		for line in f:
			col_list=line.split()
			if not line.startswith('sl'):
				if(col_list[3]=='01'):
					count+=1
					with open('out2.txt','a') as cpuout:
						print >>cpuout, "\nTCP Connection ",count
				#print(col_list[9])
					uid=col_list[7]
					inode=col_list[9]
					#print ('inode:'+inode)
					with open('/etc/passwd','r') as h:
						for li in h:
							col_list1=li.split(":")
							if (col_list1[2]==uid):
								with open('out2.txt','a') as cpuout:
									print >>cpuout, "UserName:",col_list1[0]
					PrgName=GetPrgName('/proc',inode)
					with open('out2.txt','a') as cpuout:
							print >>cpuout, "Program Name:",PrgName
					try:
						col=col_list[1].split(':')
						#print(col[0])
						addr=socket.inet_ntoa(struct.pack("!L",int(col[0],16)))				
						#print(addr)
						host,alias,addlist=socket.gethostbyaddr(addr)
						with open('out2.txt','a') as cpuout:
							print >>cpuout, 'Source Address:'+host
					except:
						with open('out2.txt','a') as cpuout:
							print >>cpuout,'Source Address:None'
					try:
						col=col_list[2].split(':')
						#print(col[0])
						addr=socket.inet_ntoa(struct.pack("!L",int(col[0],16)))				
						#print(addr)
						host,y,z=socket.gethostbyaddr(addr)
						with open('out2.txt','a') as cpuout:
							print >>cpuout, 'Destination Address:'+host+'\n'
					except:
						with open('out2.txt','a') as cpuout:
							print >>cpuout, 'Destination Address:None\n'
	
def perprocess():
	with open('/proc/stat','r') as f:
		for line in f:		
			if line.startswith('cpu'):
				#print(line)		
				col_list=line.split()
				prev_usertime=col_list[1]
				#print(prev_usertime)
				prev_systime=col_list[3]
				prev_idle=col_list[4]
				time.sleep(interval)
				with open('/proc/stat','r') as a:
					for li in a:		
						if li.startswith('cpu'):
							col_list1=li.split()
							if(col_list1[0]==col_list[0]):
								curr_usertime=col_list1[1]
								#print(curr_usertime)
								curr_systime=col_list1[3]
								curr_idle=col_list1[4]
				delu=int(curr_usertime)-int(prev_usertime)
				#print(delu)
				dels=int(curr_systime)-int(prev_systime)
				deli=int(curr_idle)-int(prev_idle)
				deno=int(dels)+int(delu)+int(deli)
	for line in os.listdir('/proc'):
		for li in line.split('\n'):
			#print(li)
			pathname = '/proc/'+li
			#print(pathname)
			p=pathname.split("/")
			if(p[2].isdigit()):
				#try:		
				with open('out3.txt','a') as cpuout:
					print >>cpuout, '\nProcess:'+p[2]
				pathname1=pathname+'/stat'
				#print(pathname1)
				with open(pathname1,'r') as f:
					for line in f:
						line=line.split(' ')
						PrevUtime=line[13]
						Prevstime=line[14]
						#PrevItime=((time.time()-SYS_BOOT_TIME)-(float(PrevUtime+Prevstime)))
						#print(PrevUtime)
						#print(Prevstime)
						#print line[21]
						time.sleep(5)
						for line in os.listdir('/proc'):
							for li in line.split('\n'):
								#print(li)
								pathname2 = '/proc/'+li
								if(pathname==pathname2):
									p1=pathname2.split("/")
									if(p1[2].isdigit()):		
										with open(pathname1,'r') as f:
											for line in f:
												pathname1=pathname2+'/stat'
												#print(pathname1)
												with open(pathname1,'r') as f:
													for line in f:
														line=line.split(' ')
														CurrUtime=line[13]
														CurrStime=line[14]
														virtualmem=float(line[22])/1000.00
														Phm=int(line[23])/128
														#print(Phm)
														#print(CurrUtime)
														#print(CurrStime)
														pathname1=pathname2+'/comm'
											for line in open(pathname1,'r'):
												Prgname=line
												#print(line)
											pathname1=pathname2+'/status'
											with open(pathname1,'r') as Usern: 
												for li in Usern:
													if li.startswith('Uid'):
														#print li
														uname=li.split('\t')
														#uname[1].strip('\t')
														#print uname[1]
									delu=abs(int(PrevUtime)-int(CurrUtime))
									dels=abs(int(Prevstime)-int(CurrStime))
									#deli=abs(int(PrevItime)-int(CurrItime))
									#print(deli)
									#deno=int(dels)+int(delu)+int(deli)
									sys_uti=(((float(delu)+float(dels))/float(deno))*100.00)
									sys_mode=((float(dels)/float(deno))*100.00)
									User_mode=((float(delu)/float(deno))*100.00)
									with open('out3.txt','a') as cpuout:
										print >>cpuout,'User Mode : %.2f'%User_mode
										print >>cpuout,'System Mode :%.2f'%sys_mode
										print >>cpuout,'Overall utilization:%.2f'%sys_uti
										vir_mem=float(virtualmem)/8000000.00
										print >>cpuout,"Virtual memory :%.2f MB"%vir_mem
										print >>cpuout,'Program Name:',Prgname
									with open('/etc/passwd','r') as h:
										for li in h:
											col_list1=li.split(":")
											if (col_list1[2]==uname[1]):
												uname=col_list1[0]
									with open('out3.txt','a') as cpuout:
										print >>cpuout, "UserName:",uname
									total_mem=3952.072
									PhM=(float(Phm)/float(total_mem)*100)
									#print PhM
									with open('out3.txt','a') as cpuout:
										print >>cpuout, "Physical Memory Utilization:%.2f"%PhM
						
				'''except:	
					with open('out3.txt','a') as cpuout:
						print >>cpuout, "Physical Memory Utilization:0.00"
'''	


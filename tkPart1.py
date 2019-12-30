import Tkinter as tk
from OSProjectPart1 import * 
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as AN
from matplotlib import style
matplotlib.use("TkAgg")
from itertools import count
import time

style.use("ggplot")

window=tk.Tk()
window.title('Task Manager')

f=Figure(figsize=(5,5),dpi=100)
a=f.add_subplot(111)

def animate(i):
	CpuUti()
	with open('c1pu.txt', 'r') as fin:
   		 data = fin.read().splitlines(True)
		 #print(data)
		 if len(data)==5:
		 	with open('c1pu.txt', 'w') as fout:
			 	fout.writelines(data[1:])
	graph_data_cpu=open('c1pu.txt','r').read()
	lines=graph_data_cpu.split('\n')
	x_cpu=[]
	y_cpu=[]
	count=0
	for line in lines:
		count=count+1
		if len(line)>0:
			#x,y=line.split(',')
			x_cpu.append(count)
			y_cpu.append(float(line))
	with open('cpu10.txt', 'r') as fin:
   		 data = fin.read().splitlines(True)
		 #print(data)
		 if len(data)==5:
		 	with open('cpu10.txt', 'w') as fout:
			 	fout.writelines(data[1:])
	#print(x_cpu)
	#print(y_cpu)
	graph_data_cpu0=open('cpu10.txt','r').read()
	lines=graph_data_cpu0.split('\n')
	x_cpu0=[]
	y_cpu0=[]
	count=0
	for line in lines:
		count=count+1
		if len(line)>0:
			#x,y=line.split(',')
			x_cpu0.append(count)
			y_cpu0.append(float(line))
	with open('cpu11.txt', 'r') as fin:
   		 data = fin.read().splitlines(True)
		 #print(data)
		 if len(data)==5:
		 	with open('cpu11.txt', 'w') as fout:
			 	fout.writelines(data[1:])
	#print(x_cpu0)
	#print(y_cpu0)
	graph_data_cpu1=open('cpu11.txt','r').read()
	lines=graph_data_cpu1.split('\n')
	x_cpu1=[]
	y_cpu1=[]
	count=0
	for line in lines:
		count=count+1
		if len(line)>0:
			#x,y=line.split(',')
			x_cpu1.append(count)
			y_cpu1.append(float(line))
	with open('cpu12.txt', 'r') as fin:
   		 data = fin.read().splitlines(True)
		 #print(data)
		 if len(data)==5:
		 	with open('cpu12.txt', 'w') as fout:
			 	fout.writelines(data[1:])
	#print(x_cpu1)
	#print(y_cpu1)
	graph_data_cpu2=open('cpu12.txt','r').read()
	lines=graph_data_cpu2.split('\n')
	x_cpu2=[]
	y_cpu2=[]
	count=0
	for line in lines:
		count=count+1
		if len(line)>0:
			#x,y=line.split(',')
			x_cpu2.append(count)
			y_cpu2.append(float(line))
	#print(x_cpu2)
	#print(y_cpu2)
	with open('cpu13.txt', 'r') as fin:
   		 data = fin.read().splitlines(True)
		 #print(data)
		 if len(data)==5:
		 	with open('cpu13.txt', 'w') as fout:
			 	fout.writelines(data[1:])
	graph_data_cpu3=open('cpu13.txt','r').read()
	lines=graph_data_cpu3.split('\n')
	x_cpu3=[]
	y_cpu3=[]
	count=0
	for line in lines:
		count=count+1
		if len(line)>0:
			#x,y=line.split(',')
			x_cpu3.append(count)
			y_cpu3.append(float(line))
	#print(x_cpu3)
	#print(y_cpu3)
	a.clear()
	a.plot(x_cpu,y_cpu,color='red',label='cpu')
	a.plot(x_cpu0,y_cpu0,color='yellow',label='cpu1')
	a.plot(x_cpu1,y_cpu1,color='green',label='cpu2')
	a.plot(x_cpu2,y_cpu2,color='blue',label='cpu3')
	a.plot(x_cpu3,y_cpu3,color='black',label='cpu4')
	a.legend()
	a.set(xlabel='Time(Last 5 Seconds)',ylabel='CPU Utilization %')
	
def new():
	window1=tk.Tk()
	window1.title("CPU Utilizations")
	window1.geometry("1000x800")

	fr3=tk.Frame(window1,bg='gray')
	fr3.place(relx=0.1,rely=0.1,relwidth=0.5,relheight=0.5)

	'''scroll=tk.Scrollbar(window1,orient='vertical')
	scroll.pack(side="right",fill='y')'''

	canvas=FigureCanvasTkAgg(f,fr3)
	canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
	ani=AN.FuncAnimation(f,animate,interval=1000)
	canvas.draw()

	fr4=tk.Frame(window1)
	fr4.place(relx=0.1,rely=0.7,relwidth=0.8,relheight=0.2)
	
	window5=tk.Tk()
	window5.title("Memory Utilization")
	window5.geometry("500x500")
	meminfo()
	dataf=open("out.txt")
	data=dataf.read()
	l2=tk.Label(window5,text=data)
	l2.pack()
	
	def mem1():
		meminfo()
		#threading.Timer(3.0,mem1).start()
		dataf=open("out.txt")
		data=dataf.read()
		#l2=tk.Label(window5,text=data)
		l2.configure(text=data)
		window5.update()
		dataf.close()
		

	l1=tk.Label(fr4,text='CPU')
	l1.grid(row=0,column=1)
	
	l1=tk.Label(fr4,text='CPU0')
	l1.grid(row=0,column=2)

	l1=tk.Label(fr4,text='CPU1')
	l1.grid(row=0,column=3)
	
	l1=tk.Label(fr4,text='CPU2')
	l1.grid(row=0,column=4)
	
	l1=tk.Label(fr4,text='CPU3')
	l1.grid(row=0,column=5)
	
	l1=tk.Label(fr4,text='CPU Utilization')
	l1.grid(row=1,column=0)

	l1=tk.Label(fr4,text='User Mode')
	l1.grid(row=2,column=0)
	
	l1=tk.Label(fr4,text='System Mode')
	l1.grid(row=3,column=0)
	
	l11=[]
	l12=[]
	l13=[]
	l14=[]
	l15=[]
	with open('cpu.txt','r') as cpu:
		i=1
		for line in cpu:
			l11.append(tk.Label(fr4,text=line))
			l11[i-1].grid(row=i,column=1)
			i=i+1
	
	with open('cpu0.txt','r') as cpu:
		i=1
		for line in cpu:
			l12.append(tk.Label(fr4,text=line))
			l12[i-1].grid(row=i,column=2)
			i=i+1
		
	with open('cpu1.txt','r') as cpu:
		i=1
		for line in cpu:
			l13.append(tk.Label(fr4,text=line))
			l13[i-1].grid(row=i,column=3)
			i=i+1
		
	with open('cpu2.txt','r') as cpu:
		i=1
		for line in cpu:
			l14.append(tk.Label(fr4,text=line))
			l14[i-1].grid(row=i,column=4)
			i=i+1
			
	with open('cpu3.txt','r') as cpu:
		i=1
		for line in cpu:
			l15.append(tk.Label(fr4,text=line))
			l15[i-1].grid(row=i,column=5)
			i=i+1

	def cpuupdates():	
		with open('cpu.txt','r') as cpu:
			i=1
			for line in cpu:
				l11[i-1].configure(text=line)				
				i=i+1
	
		with open('cpu0.txt','r') as cpu:
			i=1
			for line in cpu:
				l12[i-1].configure(text=line)
				i=i+1
		
		with open('cpu1.txt','r') as cpu:
			i=1
			for line in cpu:
				l13[i-1].configure(text=line)
				i=i+1
		
		with open('cpu2.txt','r') as cpu:
			i=1
			for line in cpu:
				l14[i-1].configure(text=line)
				i=i+1
			
		
		with open('cpu3.txt','r') as cpu:
			i=1
			for line in cpu:
				l15[i-1].configure(text=line)
				i=i+1
		fr4.update()
		time.sleep(3)
		mem1()
		cpuupdates()
	
	cpuupdates()	
		

'''def mem():
	window5=tk.Tk()
	window5.title("Memory Utilization")
	window5.geometry("500x500")
	meminfo()
	dataf=open("out.txt")
	data=dataf.read()
	l2=tk.Label(window5,text=data)
	l2.pack()

	def mem1():
		meminfo()
		#threading.Timer(3.0,mem1).start()
		dataf=open("out.txt")
		data=dataf.read()
		#l2=tk.Label(window5,text=data)
		l2.configure(text=data)
		window5.update()
		time.sleep(3)
		dataf.close()
		mem1()
		
	mem1()
	window5.mainloop()'''

def diskstats1():
	window2=tk.Tk()
	window2.title("Disk I/O")
	window2.geometry("800x500")

	fr5=tk.Frame(window2)
	fr5.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

	diskstats()
	l2=tk.Label(fr5,text='sda1')
	l2.grid(row=0,column=1)

	l2=tk.Label(fr5,text='sda2')
	l2.grid(row=0,column=2)

	l2=tk.Label(fr5,text='sda3')
	l2.grid(row=0,column=3)

	l2=tk.Label(fr5,text='sda4')
	l2.grid(row=0,column=4)

	l2=tk.Label(fr5,text='sda5')
	l2.grid(row=0,column=5)
	
	l2=tk.Label(fr5,text='sda6')
	l2.grid(row=0,column=6)

	l2=tk.Label(fr5,text='sda7')
	l2.grid(row=0,column=7)

	l2=tk.Label(fr5,text='sda8')
	l2.grid(row=0,column=9)

	l2=tk.Label(fr5,text='sda9')
	l2.grid(row=0,column=9)

	l2=tk.Label(fr5,text='sda10')
	l2.grid(row=0,column=10)

	l2=tk.Label(fr5,text='Reads')
	l2.grid(row=1,column=0)

	l2=tk.Label(fr5,text='Writes')
	l2.grid(row=2,column=0)
	
	l2=tk.Label(fr5,text='Block Reads')
	l2.grid(row=3,column=0)

	l2=tk.Label(fr5,text='Block Writes')
	l2.grid(row=4,column=0)
	
	def dstat():
		diskstats()
		k=0
		with open('out1.txt','r') as outfile:
			for line in outfile:
				if k==40:
					break
				l2[k].configure(text=line)
				k=k+1
		window2.update()
		time.sleep(3)
		dstat()

	l2=[]

	with open('out1.txt','r') as outfile:
		k=0		
		i=1
		j=1
		for line in outfile:
			if i==5:
				i=1
				j=j+1
			if j==11:
				break;
			l2.append(tk.Label(fr5,text=line))
			l2[k].grid(row=i,column=j)
			i=i+1
			k=k+1
		
	dstat()

def NetStats1():
	window3=tk.Tk()
	window3.title("Network I/O")
	window3.geometry("800x500")
	
	NetStats()	
	
	fr6=tk.Frame(window3)
	fr6.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
	
	scroll=tk.Scrollbar(fr6,orient='vertical')
	scroll.pack(side="right",fill='y')

	dataf=open("out2.txt")
	data=dataf.read()
	dataf.close()
	l3=tk.Label(fr6,text=data)
	l3.pack()

	def net1():
		NetStats()
		#threading.Timer(3.0,mem1).start()
		dataf=open("out2.txt")
		data=dataf.read()
		#l2=tk.Label(window5,text=data)
		l3.configure(text=data)
		fr6.update()
		time.sleep(3)
		dataf.close()
		net1()
		
	net1()


def perprocess1():
	window4=tk.Tk()
	window4.title("Process")
	window4.geometry("800x500")
	
	perprocess()	
	
	fr7=tk.Frame(window4)
	fr7.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
	
	scroll=tk.Scrollbar(fr7,orient='vertical')
	scroll.pack(side="right",fill='y')

	dataf=open("out3.txt")
	data=dataf.read()
	dataf.close()
	l4=tk.Label(fr7,text=data)
	l4.pack()
	
	def per1():
		perprocess()
		#threading.Timer(3.0,mem1).start()
		dataf=open("out3.txt")
		data=dataf.read()
		#l2=tk.Label(window5,text=data)
		l4.configure(text=data)
		fr7.update()
		time.sleep(3)
		dataf.close()
		per1()
		
	per1()

canvas=tk.Canvas(window,height=600,width=600)
canvas.pack()

fr1=tk.Frame(window,bg='gray')
fr1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

fr2=tk.Frame(window,bg='#1f1f14')
fr2.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.8)

b1=tk.Button(fr1,text="CPU and Memory",command=new)
b1.place(relx=0.3,rely=0.2,relwidth=0.5)

b2=tk.Button(fr1,text="Disk I/O ",command=diskstats1)
b2.place(relx=0.3,rely=0.4,relwidth=0.5)

b3=tk.Button(fr1,text="Network I/O",command=NetStats1)
b3.place(relx=0.3,rely=0.6,relwidth=0.5)

b4=tk.Button(fr1,text="Process",command=perprocess1)
b4.place(relx=0.3,rely=0.8,relwidth=0.5)

label=tk.Label(fr2,text="Menu",fg='white',bg='#1f1f14',font=50)
label.place(relx=0.3,rely=0.5)

window.mainloop() 

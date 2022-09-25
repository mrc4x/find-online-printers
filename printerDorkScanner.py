from googlesearch import search
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('printer finder'))

print("""
1)find random printers
2)find edu printers
coded by merc4n..
""")
giris = int(input("1 or 2: "))
if giris == 1:
    query = str("inurl:/hp/device/this.LCDispatcher")
    for i in search(query, tld="com", num=1000, stop=1000, pause=2):
        print(i)
    query = str("inurl:/hp/device/this.LCDispatcher?nav=hp.Config")
    for i in search(query, tld="com", num=1000, stop=1000, pause=2):
        print(i)

if giris ==2:
   
    query = str("inurl:/hp/device/this.lcdispatcher site:.edu ")
    for i in search(query, tld="com", num=1000, stop=1000, pause=2):
        print(i)
    query = str("inurl:/hp/device/this.LCDispatcher?nav=hp.Config site:.edu")
    for i in search(query, tld="com", num=1000, stop=1000, pause=2):
        print(i)

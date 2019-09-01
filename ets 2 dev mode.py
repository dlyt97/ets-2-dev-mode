pc_name = 'DULE' #PC NAME
def dc97():
    x=int(input('1-Default or 2-Developer 1 & Console 1:\n'))
    if x == 1:
        try:
            f=open('C:\\Users\\'+pc_name+'\\Documents\\Euro Truck Simulator 2\\config.cfg','r')
        except:
            print('ne postoji config.cfg fajl...')
        try:
            fajl=f.read()
        except:
            print('ne moze da se cita config.cfg fajl...')
        try:
            jed=fajl.replace('uset g_developer "1"','uset g_developer "0"')
        except:
            print('ne moze da se zameni developer iz 0 u 1...')
        try:
            dva=jed.replace('uset g_console "1"','uset g_console "0"')
        except:
            print('ne moze da se zameni console iz 0 u 1...')
        try:
            ff=open('C:\\Users\\'+pc_name+'\\Documents\\Euro Truck Simulator 2\\config.cfg','w')
        except:
            print('ne moze da se kreira config.cfg fajl...')
        try:
            ff.write(dva)
        except:
            print('ne moze da se zapise config.cfg fajl...')
        ff.close()
        print(dva)
    if x == 2:
        try:
            f=open('C:\\Users\\'+pc_name+'\\Documents\\Euro Truck Simulator 2\\config.cfg','r')
        except:
            print('ne postoji config.cfg fajl...')
        try:
            fajl=f.read()
        except:
            print('ne moze da se cita config.cfg fajl...')
        try:
            jed=fajl.replace('uset g_developer "0"','uset g_developer "1"')
        except:
            print('ne moze da se zameni developer iz 0 u 1...')
        try:
            dva=jed.replace('uset g_console "0"','uset g_console "1"')
        except:
            print('ne moze da se zameni console iz 0 u 1...')
        try:
            ff=open('C:\\Users\\'+pc_name+'\\Documents\\Euro Truck Simulator 2\\config.cfg','w')
        except:
            print('ne moze da se kreira config.cfg fajl...')
        try:
            ff.write(dva)
        except:
            print('ne moze da se zapise config.cfg fajl...')
        ff.close()
        print(dva)
dc97()

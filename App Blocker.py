#=======================================================================
version = '||> V_9.9 by RTG2717'
#=======================================================================
'Not adviced to run from IDLE ... run in console direltly from file explorer.'
#=======================================================================

import os
import time
import pickle
from datetime import date

#=======================================================================
#=======================================================================

#setup()
def setup():
    try:
        os.system('cls')
        print('*****PLEASE WAIT*****')
        os.system('pip install pyttsx3') #for text to speech

        import pyttsx3

        if os.path.isfile("congrats.mp3")==False:
            speaker=pyttsx3.init()
            text='Congrats! you have completed your set time.'
            speaker.save_to_file(text,'congrats.mp3')
            speaker.setProperty('volume',1.0)
            speaker.runAndWait()

        if os.path.isfile("start.mp3")==False:
            speaker=pyttsx3.init()
            text='Your set time has arrived and the app blocker has been started.'
            speaker.save_to_file(text,'start.mp3')
            speaker.setProperty('volume',1.0)
            speaker.runAndWait()

        if os.path.isfile("goingtostart.mp3")==False:
            speaker=pyttsx3.init()
            text='You have set a block time which is going to start in 15 minutes. I repeat. You have set a block time which is going to start in 15 minutes.'
            speaker.save_to_file(text,'goingtostart.mp3')
            speaker.setProperty('volume',1.0)
            speaker.runAndWait()

        if os.path.isfile("record.exe")==False:
            f=open('record.exe','wb')
            l=[{'Target':'Not Set','DateOfFirstRun':time.strftime(('%d'+'/'+'%m'+'/'+'%Y'),time.localtime())},('Time_Set(Minutes)','Completed','Date','Apps_Blocked','Points_Earned','Total_Points')]
            pickle.dump(l,f)
            f.close()

    except Exception as e:
        os.system('cls')
        os.system('color 04')
        print('****************************************************************************************')
        print('Error:',e)
        print('''>>>This error might be temporary, caused because of version difference.
>>>Try restarting the code.''')
        print('****************************************************************************************')
        enter=input("Press enter to continue.")
        quit()


#=======================================================================
#=======================================================================

#checking for requirements
if os.path.isfile("congrats.mp3")==False or os.path.isfile("goingtostart.mp3")==False or os.path.isfile("start.mp3")==False or os.path.isfile("record.exe")==False:
    os.system('color 0e')
    print('========================================================================================')
    print("You don't meet the requirements for this program. Please give few seconds and the required modules and files will be made.")
    print('========================================================================================')
    print("Internet Connection might be needed.")
    print('========================================================================================')
    print("Starting in 10 seconds.")
    time.sleep(10)
    os.system('cls')
    print('========================================================================================')    
    print('========================================================================================')
    print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
    print('Strating Now.')
    print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
    print('========================================================================================')
    print('========================================================================================')
    time.sleep(1)
    setup()

#=======================================================================
#=======================================================================

#code
def START(futuretime=0):
    try:
        os.system('cls')
        os.system('color 0a')
        f=open('record.exe','rb+')
        l=pickle.load(f)
        f.close()

#taking all inputs
        if len(l[0])==2:
            print('========================================================================================')
            print('========================================================================================')
            print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
            print("No Blocklists Available.")
            print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
            print('========================================================================================')
            print('========================================================================================')
            enter=input('Press Enter To Continue.')
            ASK()
        x=list(l[0].keys())
        print('========================================================================================')
        print('========================================================================================')
        print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
        for i in x:
            if i!='Target' and i!='DateOfFirstRun':
                print(i,"=>",l[0][i])
        print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
        print('========================================================================================')
        print('========================================================================================')
        bno=int(input("Enter number of Blocklist to use : "))
        apps=l[0][bno]
        print('========================================================================================')
        t_end=int(input('Enter time in minutes to block : '))
        lefttime=t_end
        t_for_score=t_end * 60
        score=t_for_score
        

#confirm
        os.system('cls')
        print('========================================================================================')
        print('''You gave the following inputs ...
Start After :''',futuretime,'''minutes
Apps to Block :''',apps,''' 
Total Time Set :''',lefttime,'''minutes or''',round((lefttime/60),3),"hours.")
        print("Score that can be earned on Completion :",(score+futuretime))
        print('========================================================================================')
        y=input('Are you sure to Continue? (y/n) : ')
        if y in ['y','Y']:
            print('...')
        elif y in ['n','N']:
            ASK()
        else:
            os.system('cls')
            os.system('color 004')
            print('****************************************************************************************')
            print("Invalid Choice.")
            print('****************************************************************************************')
            enter=input('Press Enter To Continue.')
            ASK()

#saving the scores --- 1
        f=open('record.exe','rb+')
        l=pickle.load(f)
        f.close()
        f=open('record.exe','rb+')
        if type(l[-1][-1])==str:
            total_score=(score+futuretime)*(-1)
        else:
            total_score=int(l[-1][-1])-(score+futuretime)
        l1=((t_for_score/60),'NO',time.strftime(('%d'+'/'+'%m'+'/'+'%Y'),time.localtime()),apps,(score+futuretime)*(-1),total_score)
        l.append(l1)
        pickle.dump(l,f)
        f.close()

#future time
        futuretime=futuretime*60
        if futuretime>0:
            os.system('cls')
            os.system('color 0f')
            print('The blocker will start ',(futuretime/60),'minutes after',time.strftime(('%I'+':'+'%M'+' '+'%p'),time.localtime()))
            if futuretime>=900:
                time.sleep(futuretime-900)
                os.system("goingtostart.mp3")
                os.system("cls")
                print('The blocker will start 15 minutes after',time.strftime(('%I'+':'+'%M'+' '+'%p'),time.localtime()))
                time.sleep(900)
                os.system("start.mp3")
            elif futuretime>0 and futuretime<900:
                time.sleep(futuretime)
                os.system("start.mp3")
        futuretime=int(futuretime/60)

#running the main code
        os.system('cls')
        os.system('color 0a')
        t_end=time.time()+t_end*60
        starttime=time.strftime(('%I'+':'+'%M'+' '+'%p'),time.localtime())
        while time.time()<t_end:
            os.system('cls')
            print('========================================================================================')
            print('========================================================================================')
            print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
            print("Time Set :",round((t_for_score/60),3),"minutes or",round((t_for_score/3600),3),"hours from",starttime)
            print("Score that can be earned on Completion :",(score+futuretime))
            print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
            print('========================================================================================')
            print('========================================================================================')
            print('***LOG***')
            print('PLease ignore any "Process Not Found" errors.')
            for i in apps:
                command='taskkill /F /IM "{}"'.format(i)
                os.system(command)
            time.sleep(10)
        os.system('cls')
        os.system('color 0b')
        print('========================================================================================')
        print('========================================================================================')
        print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
        print('Time Left : 0.0 minutes >>> COMPLETED')
        print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
        print('========================================================================================')
        print('========================================================================================')
        os.system("congrats.mp3")

#saving the scores --- 2
        f=open('record.exe','rb+')
        l=pickle.load(f)
        f.close()
        f=open('record.exe','rb+')
        l.pop() #removing last uncompleted score
        if type(l[-1][-1])==str:
            total_score=(score+futuretime)
        else:
            total_score=int(l[-1][-1])+(score+futuretime)
        l1=((t_for_score/60),'YES',time.strftime(('%d'+'/'+'%m'+'/'+'%Y'),time.localtime()),apps,(score+futuretime),total_score)
        l.append(l1)
        pickle.dump(l,f)
        f.close()
        if type(l[0]['Target'])==int:
            if l[0]['Target']<=total_score:
                print('========================================================================================')
                print('========================================================================================')
                print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
                print('****** Congrats! You have completed your target. *****')
                print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
                print('========================================================================================')
                print('========================================================================================')

#Exception        
    except Exception as e:
        os.system('cls')
        os.system('color 04')
        print('****************************************************************************************')
        print('Error:',e)
        print('****************************************************************************************')

#=======================================================================
#=======================================================================

#ASK
def ASK():
    global version
    os.system('cls')
    os.system('color 0d')
    print(version)
    print('========================================================================================')
    print('========================================================================================')
    ask=(input('''Choose the option you want to do (1,2,3...)
1  =  Start Blocker Now.
2  =  Start Blocker After A Break.
3  =  Show Total Points.
4  =  Show All Records.
5  =  Get Applicable Name Of Some App.
6  =  Edit Blocklist(s).
7  =  Set Target.
8  =  Check Target.
9  =  Clear Target.
10 =  Remove Old Records.
x  =  Close.
Enter your choice : '''))

#1
    if ask=='1':
        START()
        print('========================================================================================')
        print('========================================================================================')
        print('========================================================================================')
        enter=input('Press Enter To Continue.')
        ASK()

#2
    elif ask=='2':
        try:
            os.system('cls')
            os.system('color 0a')
            print('========================================================================================')
            print('This will set a time after which the blocker will start.')
            print("You will get extra points if you don't cancel the the blocker in between.")
            print('========================================================================================')
            choice=(input('''Select a Break time
1 = 5 Minutes.
2 = 15 Minutes.
3 = 30 Minutes.
4 = 45 Minutes.
5 = 1 Hour.
Enter your choice : '''))
            if choice=='1':
                futuretime=5
            elif choice=='2':
                futuretime=15
            elif choice=='3':
                futuretime=30
            elif choice=='4':
                futuretime=45
            elif choice=='5':
                futuretime=60
            else:
                os.system('cls')
                os.system('color 04')
                print('****************************************************************************************')
                print("Invalid Choice.")
                print('****************************************************************************************')
                enter=input('Press Enter To Continue.')
                ASK()
            START(futuretime)
            print('========================================================================================')
            print('========================================================================================')
            print('========================================================================================')
            enter=input('Press Enter To Continue.')
            ASK()
        except Exception as e:
            os.system('cls')
            os.system('color 04')
            print('****************************************************************************************')
            print('Error:',e)
            print('****************************************************************************************')
            enter=input('Press Enter To Continue.')
            ASK()

#3    
    elif ask=='3':
        f=open('record.exe','rb+')
        l=pickle.load(f)
        f.close()
        os.system('cls')
        os.system('color 0a')
        print('========================================================================================')
        print('========================================================================================')
        print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
        print('Total Points : ',l[-1][-1] if type(l[-1][-1])==int else print('No Scores Yet'))
        print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
        print('========================================================================================')
        print('========================================================================================')
        enter=input('Press Enter To Continue.')
        ASK()

#4
    elif ask=='4':
        f=open('record.exe','rb+')
        l=pickle.load(f)
        f.close()
        os.system('cls')
        os.system('color 0a')
        print('========================================================================================')
        print('========================================================================================')
        print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
        n=0
        for i in l:
            if n==0:
                n=1
            else:
                print(i)
        print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
        print('========================================================================================')
        print('========================================================================================')
        print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
        if type(l[-1][-1])==int:
            hrs=int(l[-1][-1])/3600
            days=hrs/24
            date1=l[0]['DateOfFirstRun']
            l1=date1.split('/')
            date2=time.strftime(('%d'+'/'+'%m'+'/'+'%Y'),time.localtime())
            l2=date2.split('/')
            date1=date(int(l1[2]),int(l1[1]),int(l1[0]))
            date2=date(int(l2[2]),int(l2[1]),int(l2[0]))
            dayzz=(date2-date1).days
            print("You have focused :",round(hrs,2),"hours","or",round(days,2),"days")
            print("In last",dayzz,"Day(s)")
        print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
        print('========================================================================================')
        print('========================================================================================')
        enter=input('Press Enter To Continue.')
        ASK()

#5
    elif ask=='5':
        os.system('cls')
        os.system('color 0a')
        print('========================================================================================')
        print('========================================================================================')
        print('This tool is for finding the applicable name of an app for this program.')
        print('This name can be different from the orginal name of the app in some cases.')
        print('Run the app whose name you want to get and then press enter.')
        print('========================================================================================')
        enter=input("Press Enter to continue.")
        os.system('cls')
        print('========================================================================================')
        print('========================================================================================')
        print('''Now, your PC will open Task Manager(You may need to press on more details).
.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.
1...Right click the name of any desired app.
2...Press 'Go To Details' option (If the option is unclickable/grayed out then press expand first).
./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.
Now the applicable name of your app will be highlighted :D
========================================================================================
========================================================================================
 
 
.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.
This program can not block File Explorer or any other app that requires Administrator Permissions.
./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.
''')
        enter=input('Press Enter To Continue.')
        os.system('taskmgr.exe')
        enter=input('Press Enter To Continue.')
        ASK()

#6
    elif ask=='6':
        try:
            os.system('cls')
            os.system('color 0d')
            print('========================================================================================')
            print('========================================================================================')
            print('========================================================================================')
            ask=(input('''Choose the option you want to do (1,2,3...)
1  =  Show Existing Blocklist(s).
2  =  Create New Blocklist.
3  =  Delete A Blocklist.
4  =  Edit Existing Blocklist.
x  =  Go Back.
Enter your choice : '''))
            if ask=='1':
                os.system('cls')
                os.system('color 0a')
                f=open('record.exe','rb+')
                l=pickle.load(f)
                f.close()
                if len(l[0])==2:
                    print('========================================================================================')
                    print('========================================================================================')
                    print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
                    print("No Blocklists Available.")
                    print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
                    print('========================================================================================')
                    print('========================================================================================')
                    enter=input('Press Enter To Continue.')
                    ASK()
                x=list(l[0].keys())
                print('========================================================================================')
                print('========================================================================================')
                print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
                for i in x:
                    if i!='Target' and i!='DateOfFirstRun':
                        print(i,"=>",l[0][i])
                print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
                print('========================================================================================')
                print('========================================================================================')
                enter=input("Press Enter to continue.")
            elif ask=='2':
                os.system('cls')
                os.system('color 0a')
                f=open('record.exe','rb+')
                l=pickle.load(f)
                f.close()
                f=open('record.exe','rb+')
                x=list(l[0].keys())
                bno=1
                if len(x)>2:
                    bno+=x[-1]
                apps=[]
                app=''
                while app not in ['x','X']:
                    print("Current List :",bno,'=>',apps)
                    print('========================================================================================')
                    app=input('''Enter name of an app to add to list or Press 'x' to stop adding.
(also add type of app with its name) : ''')
                    if app not in ['x','X']:
                        apps.append(app)
                    os.system('cls')
                l[0][bno]=apps
                pickle.dump(l,f)
                f.close()
                os.system('cls')
                print('========================================================================================')
                print('========================================================================================')
                print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
                print("New Blocklist Created.")
                print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
                print('========================================================================================')
                print('========================================================================================')
                enter=input('Press Enter To Continue.')
            elif ask=='3':
                os.system('cls')
                os.system('color 0a')
                f=open('record.exe','rb+')
                l=pickle.load(f)
                f.close()
                f=open('record.exe','rb+')
                if len(l[0])==2:
                    print('========================================================================================')
                    print('========================================================================================')
                    print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
                    print("No Blocklists Available.")
                    print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
                    print('========================================================================================')
                    print('========================================================================================')
                    enter=input('Press Enter To Continue.')
                    ASK()
                x=list(l[0].keys())
                print('========================================================================================')
                print('========================================================================================')
                print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
                for i in x:
                    if i!='Target':
                        print(i,"=>",l[0][i])
                print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
                print('========================================================================================')
                print('========================================================================================')
                bno=int(input("Enter number of blocklist to delete : "))
                l[0].pop(bno)
                pickle.dump(l,f)
                f.close()
                os.system('cls')
                print('========================================================================================')
                print('========================================================================================')
                print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
                print("Selected Blocklist Has Been Deleted.")
                print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
                print('========================================================================================')
                print('========================================================================================')
                enter=input('Press Enter To Continue.')
            elif ask=='4':
                os.system('cls')
                os.system('color 0a')
                f=open('record.exe','rb+')
                l=pickle.load(f)
                f.close()
                f=open('record.exe','rb+')
                if len(l[0])==2:
                    print('========================================================================================')
                    print('========================================================================================')
                    print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
                    print("No Blocklists Available.")
                    print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
                    print('========================================================================================')
                    print('========================================================================================')
                    enter=input('Press Enter To Continue.')
                    ASK()
                x=list(l[0].keys())
                print('========================================================================================')
                print('========================================================================================')
                print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
                for i in x:
                    if i!='Target':
                        print(i,"=>",l[0][i])
                print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
                print('========================================================================================')
                print('========================================================================================')
                bno=int(input("Enter number of Blocklist to edit : "))
                os.system('cls')
                os.system('color 0d')
                print('========================================================================================')
                print('========================================================================================')
                print('========================================================================================')
                ask2=(input('''Choose the option you want to do (1,2,3...)
1  =  Add An App.
2  =  Remove An App.
x  =  Go Back.
Enter your choice : '''))
                if ask2=='1':
                    os.system('cls')
                    os.system('color 0a')
                    apps=l[0][bno]
                    app=''
                    while app not in ['x','X']:
                        print("Current List :",bno,'=>',apps)
                        print('========================================================================================')
                        app=input('''Enter name of an app to add to list or Press 'x' to stop adding.
(also add type of app with its name) : ''')
                        if app not in ['x','X']:
                            apps.append(app)
                        os.system('cls')
                    l[0][bno]=apps
                    pickle.dump(l,f)
                    f.close()
                    os.system('cls')
                    print('========================================================================================')
                    print('========================================================================================')
                    print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
                    print("New Apps Added.")
                    print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
                    print('========================================================================================')
                    print('========================================================================================')
                    enter=input('Press Enter To Continue.')
                elif ask2=='2':
                    os.system('cls')
                    os.system('color 0a')
                    apps=l[0][bno]
                    app=''
                    while app not in ['x','X']:
                        con=1
                        print("Current List :",bno,'=>',apps)
                        print('========================================================================================')
                        app=input('''Enter name of an app to remove from list or Press 'x' to stop removing.
(write complete name ensuring case-sensitivity) : ''')
                        if app not in apps:
                            con=0
                        if app not in ['x','X'] and con==1:
                            apps.remove(app)
                        os.system('cls')
                    l[0][bno]=apps
                    pickle.dump(l,f)
                    f.close()
                    os.system('cls')
                    print('========================================================================================')
                    print('========================================================================================')
                    print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
                    print("Selected Apps Have Been Removed.")
                    print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
                    print('========================================================================================')
                    print('========================================================================================')
                    enter=input('Press Enter To Continue.')
                elif ask2 in ['x','X']:
                    ASK()
                else:
                    os.system('cls')
                    os.system('color 04')
                    print('****************************************************************************************')
                    print("Invalid Choice.")
                    print('****************************************************************************************')
                    enter=input('Press Enter To Continue.')
                    ASK()
            elif ask in ['x','X']:
                ASK()
            else:
                os.system('cls')
                os.system('color 04')
                print('****************************************************************************************')
                print("Invalid Choice.")
                print('****************************************************************************************')
                enter=input('Press Enter To Continue.')
                ASK()
            ASK()
        except Exception as e:
            os.system('cls')
            os.system('color 04')
            print('****************************************************************************************')
            print('Error:',e)
            print('****************************************************************************************')
            enter=input('Press Enter To Continue.')
            ASK()
 
#7
    elif ask=='7':
        try:
            os.system('cls')
            os.system('color 0a')
            f=open('record.exe','rb+')
            l=pickle.load(f)
            f.close()
            f=open('record.exe','rb+')
            l[0]['Target']=int(input('Enter your new Target Score : '))
            pickle.dump(l,f)
            f.close()
            os.system('cls')
            print('========================================================================================')
            print('========================================================================================')
            print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
            print('Target set to :',l[0]['Target'])
            print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
            print('========================================================================================')
            print('========================================================================================')
            enter=input('Press Enter To Continue.')
            ASK()
        except Exception as e:
            os.system('cls')
            os.system('color 04')
            print('****************************************************************************************')
            print('Error:',e)
            print('****************************************************************************************')
            enter=input('Press Enter To Continue.')
            ASK()

#8
    elif ask=='8':
        try:
            os.system('cls')
            os.system('color 0a')
            f=open('record.exe','rb+')
            l=pickle.load(f)
            f.close()
            print('========================================================================================')
            print('========================================================================================')
            print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
            print('Your Target :',l[0]['Target'])
            if type(l[0]['Target'])==int and type(l[-1][-1])==int:
                print('Completed :',l[0]['Target']<=int(l[-1][-1]))
                if l[0]['Target']>int(l[-1][-1]):
                    remaining=l[0]['Target']-int(l[-1][-1])
                    print('Score Remaining to Target :',remaining,' (',round(remaining/3600,1),'hrs )')
            elif type(l[0]['Target'])==int :
                remaining=l[0]['Target']
                print('Score Remaining to Target :',remaining,' (',round(remaining/3600,1),'hrs )')
            print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
            print('========================================================================================')
            print('========================================================================================')
            enter=input('Press Enter To Continue.')
            ASK()
        except Exception as e:
            os.system('cls')
            os.system('color 04')
            print('****************************************************************************************')
            print('Error:',e)
            print('****************************************************************************************')
            enter=input('Press Enter To Continue.')
            ASK()

#9
    elif ask=='9':
        os.system('cls')
        os.system('color 0a')
        print('****************************************************************************************')
        y=input('Do you really want to clear your target? (y/n) : ')
        if y in ['y','Y']:
            f=open('record.exe','rb+')
            l=pickle.load(f)
            f.close()
            f=open('record.exe','rb+')
            l[0]['Target']='Not Set'
            pickle.dump(l,f)
            f.close()
            os.system('cls')
            print('========================================================================================')
            print('========================================================================================')
            print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
            print('Target Cleared.')
            print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
            print('========================================================================================')
            print('========================================================================================')
            enter=input('Press Enter To Continue.')
        elif y in ['n','N']:
            print('ok')
        else:
            os.system('cls')
            os.system('color 04')
            print('****************************************************************************************')
            print("Invalid Choice.")
            print('****************************************************************************************')
            enter=input('Press Enter To Continue.')
        ASK()

#10
    elif ask=='10':
        os.system('cls')
        os.system('color 0a')
        f=open('record.exe','rb+')
        l=pickle.load(f)
        f.close()
        if type(l[-1][-1])==str:
            os.system('cls')
            os.system('color 04')
            print('****************************************************************************************')
            print("No Scores Found.")
            print('****************************************************************************************')
            enter=input('Press Enter To Continue.')
            ASK()
        f=open('record.exe','rb+')
        if l[2]!='<Older Records Have Been Removed.>':
            l.insert(2,'<Older Records Have Been Removed.>')
        latest_date=l[-1][2]
        lll=l[:3]
        NoOfRecofLatestDate=0
        for i in l[3:]:
            if str(i[2])==str(latest_date):
                lll.append(i)
                NoOfRecofLatestDate+=1
        if lll==l:
            f.close()
            os.system('cls')
            os.system('color 04')
            print('****************************************************************************************')
            print("All records are of same date so none can can be removed now.")
            print('****************************************************************************************')
            enter=input('Press Enter To Continue.')
            ASK()
        if NoOfRecofLatestDate==1:
            f.close()
            os.system('cls')
            os.system('color 04')
            print('****************************************************************************************')
            print("There's only one record from the latest date, deleting old records now might cause miscalculation of scores.")
            print('****************************************************************************************')
            enter=input('Press Enter To Continue.')
            ASK()
        print('****************************************************************************************')
        print('''This will remove all records except records from the last date.''')
        print('****************************************************************************************')    
        y=input('Do you want to continue? (y/n) : ')
        if y in ['y','Y']:
            pickle.dump(lll,f)
            f.close()
            os.system('cls')
            print('========================================================================================')
            print('========================================================================================')
            print('.\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/.')
            print('Old records have been removed.')
            print('./\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\.')
            print('========================================================================================')
            print('========================================================================================')
            enter=input('Press Enter To Continue.')
        elif y in ['n','N']:
            print('ok')
        else:
            os.system('cls')
            os.system('color 04')
            print('****************************************************************************************')
            print("Invalid Choice.")
            print('****************************************************************************************')
            enter=input('Press Enter To Continue.')
        ASK()

#x
    elif ask in ['x','X']:
        quit()

#else
    else:
        os.system('cls')
        os.system('color 04')
        print('****************************************************************************************')
        print("Invalid Choice.")
        print('****************************************************************************************')
        enter=input('Press Enter To Continue.')
        ASK()

#=======================================================================
#=======================================================================

ASK()

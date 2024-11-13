import glob, Tkinter, tkFileDialog, datetime, os
from decimal import Decimal

##os.chdir("/home/pi/Biologic")
#directory = tkFileDialog.askdirectory()
root = Tkinter.Tk()
root.withdraw()
root.update()
os.chdir(tkFileDialog.askdirectory())


Ewe = []
Eindex = 10
Ns = []
Nindex = 7
Q_Qo = []
Qindex = 10
UUT_CP = {}
UUT_GCPL = {}

def appendCP(filename, UUT_CP):

    name = filename.split("_")
    #ID = (name[0]+"_"+name[1]+"_"+name[2]+"_"+name[3]+"_"+name[len(name)-3]+"_"+name[len(name)-2]+"_"+name[len(name)-1])
    #newfile.write(ID.rstrip(".mpt")+"\t")
    ID = (name[0]+"_"+name[1]+"_"+name[2]+"_"+name[3]+"_"+name[len(name)-1]).rstrip(".mpt")
    #F = open(filename,"a+")
    ha = open(filename,"a+").readlines()
    found = False
    nodata = False
    Ns = []
    Ewe = []
    #I = 0.000020
    #V1 = 0
    #V2 = 0

    for line in ha:
        words = line.split("\t")

        if 'mode' in line:
            Ns.append(words[Nindex-1])
            Ewe.append(words[Eindex-1].rstrip('\n'))
            found = True
        elif found == True:
                Ns.append(words[Nindex-1])
                Ewe.append(words[Eindex-1].rstrip('\n'))

    i=1
    for i in range(len(Ns)):
        if int(Ns[-1]) < 3:
            #newfile.write("No data \n\n")
            break
        elif i == len(Ns)-1:
            break
        elif ((Ns[i] == '2') and (Ns[i+1] == '3')):
            #UUT[ID] = 
            #newfile.write(Ewe[i]+"\t")
            #V1 = float(Ewe[i])
            V1 = Ewe[i]
        elif ((Ns[i] == '3') and (Ns[i+1] == '4')):
            #newfile.write(Ewe[i]+"\t")
            #V2 = float(Ewe[i])
            V2 = Ewe[i]
            R = (float(V1)-float(V2))/0.000020  # 20uA pulse
            #newfile.write(str(R)+"\n\n")
            UUT_CP[ID] = V1 + ", " + V2 + ", " + str(R)
    open(filename,"a+").close()

def appendGCPL(filename,UUT_GCPL):

    name = filename.split("_")
    ID = (name[0]+"_"+name[1]+"_"+name[2]+"_"+name[3]+"_"+name[len(name)-1]).rstrip(".mpt")
    #newfile.write(ID.rstrip(".mpt")+"\t")
    #F = open(filename,"a+")
    ha = open(filename,"a+").readlines()
    found = False

    for line in ha:
        words = line.split("\t")

        if 'mode' in line:
            Q_Qo.append(words[Qindex-1].rstrip('\n'))
            found = True
        elif found == True:
            Q_Qo.append(words[Qindex-1].rstrip('\n'))

    #newfile.write(Q_Qo[-1]+ "\n\n")
    try:
        UUT_GCPL[ID] = str("{:.6E}".format(Decimal(str(abs(float(Q_Qo[-1]))))))

    except Exception:
        pass
    
    #print (Q_Qo[-1])
    open(filename,"a+").close()


## Main starts here
mmddyy = datetime.date.today()
mmddyy = mmddyy.strftime('%m%d%y')
count = 1

for file in glob.glob("*_TestSummary_*"):
    count += 1
    print count

with open(mmddyy+"_TestSummary_"+str('{:02d}'.format(count))+".csv","w+") as newfile:

    for file in glob.glob("*01_CP_*.mpt"):
        appendCP(file,UUT_CP)
        print ("found one!")

    #newfile.write("\n\n")

    for file in glob.glob("*03_GCPL_*.mpt"):
        appendGCPL(file, UUT_GCPL)
        print ("found another one!")


    print "Filename, V0, V1, R, Qo"
    newfile.write("Filename, V0, V1, R, Qo\n")
    for files in UUT_CP.iterkeys():
        try:
            print (files + ", " + UUT_CP[files] + ", " + UUT_GCPL[files])
            newfile.write(files + ", " + UUT_CP[files] + ", " + UUT_GCPL[files] + "\n") 
        
        except:
            print (files + ", " + UUT_CP[files])
            newfile.write(files + ", " + UUT_CP[files] + "\n")





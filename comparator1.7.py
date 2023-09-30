from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os


class Comparator:
    def __init__(self):
        self.file = ' '
        self.reportName =' '
        self.fileName = ' '
        self.report = ()
        self.allReports = []
        self.commonContacts = []
        self.reportDestination = ' '
        

    def readAlleapReports(self):
        
        self.report = open(self.file, "r", encoding="utf-8")
        self.report = self.report.read()
        self.report = self.report.split('<tbody><tr>')
        self.report = self.report[1]
        self.report = self.report.split('</tr></tbody>')
        self.report = self.report[0]
      
        self.report = self.report.replace('</td></tr><tr><td>','</td><td>')
        self.report = self.report.split('</td><td>')
       
        self.report.pop(0)
        self.report = self.report[::5]
        self.report = list(set(self.report))
        while("" in self.report):
            self.report.remove("")            
       
           
        #remove all special characters and islower
        #print(self.report)
        self.report = (self.fileName, self.report)
        self.allReports.append(self.report)
        self.report = ()
        #return a filename and an array of strings
        #needs to be optimized


    def readilleapReports(self):
        
        self.report = open(self.file, "r", encoding="utf-8")
        self.report = self.report.read()
        self.report = self.report.split('<tbody><tr>')
        self.report = self.report[1]
        self.report = self.report.split('</tr></tbody>')
        self.report = self.report[0]
      
        self.report = self.report.split('</td><td>')
     
        self.report = self.report[4::10]
        
        self.report = list(set(self.report))
        while("" in self.report):
            self.report.remove("")            
       
           
        #remove all special characters and islower
        #print(self.report)
        self.report = (self.fileName, self.report)
        self.allReports.append(self.report)
        self.report = ()
        #return a filename and an array of strings
        #needs to be optimized
        
    

    def compareReports(self):
      
    
        data = ()
        MasterMultipleReports = ()
        same = {}

        for i in range(0,len(self.allReports)):
            for x in range(0,len(self.allReports)):
                if(i == x or i == x-1):
                    continue
                else:
                    same = set(self.allReports[i][1]).intersection(self.allReports[x][1])
                   
                    if(same != set()):
                        multipleSameReports = []
                        multipleSameReports.append(i)
                        multipleSameReports.append(x)
                        multipleSameReports.sort()
                        data = (multipleSameReports,same)
                        self.commonContacts.append(data)

                        
        
        # Loop iterates through all of the contacts to find any similarites and inserts them in to common contacts              
        
       
        finalContactsList = []
        newLength = 0
    
        b = list()
        lengthcommon = len(self.commonContacts)
        while newLength != lengthcommon:
            lengthcommon = len(self.commonContacts)
            for i in range(0,lengthcommon):
                for x in range(0,lengthcommon):
                    if(i == x ):
                        continue
                    else:
                        same = set(self.commonContacts[i][1]).intersection(self.commonContacts[x][1])
                    
                        if(same != set()):
                     
                            
                            multipleSameReports = []
                            
                            self.commonContacts[i][0] + self.commonContacts[x][0]
                        
                            multipleSameReports = self.commonContacts[i][0] + self.commonContacts[x][0]
                           
                            multipleSameReports = list(set(multipleSameReports)) 
                            #print(self.commonContacts[i][0])
                            MasterMultipleReports = (multipleSameReports,same)
                           
                            if MasterMultipleReports not in self.commonContacts:
                                self.commonContacts.append(MasterMultipleReports)
        
            newLength = len(self.commonContacts)               
        
                        # Iterates through all of the common contacts to fine more than 2 reports share common value it shows REVIEW THIS PRINTING MANY DUPLICATES
                        #need to iterate a until the length of common contacts doesnt change

        
        length = len(self.commonContacts)
        for i in range(0,length):
                for x in range(0,length):
                    if(i == x):
                        continue
                    else:
                        if set(self.commonContacts[i][1]) == set(self.commonContacts[x][1]) :
                        
                            if set(self.commonContacts[i][0]).issubset(set(self.commonContacts[x][0])):
                                b.append(self.commonContacts[i])

        
       
        for i in b:
            if i in self.commonContacts:
                self.commonContacts.remove(i)
            
      
          
     
    def browseFiles(self):

        filename = filedialog.askopenfilename(initialdir = "/", 
                                            title = "Select a File")
 
        self.fileName = os.path.basename(filename)
        self.file = filename

    def browseReportDestination(self):

        path = filedialog.askdirectory(initialdir = "/", 
                                            title = "Select a File")
 
        self.reportDestination = path + '/report.html'

        print(self.reportDestination)

       
       

    def getFileName(self):
        return self.fileName
    
    def printReport(self):

        
        x = [x[0] for x in self.commonContacts]
        print(x)
      
   
        finalReport = []
        Numbers = ""
        ReportString = ''
        
       
        
        for i in range(0,len(self.commonContacts)):
            #print(z[i])
           
            iteration= self.commonContacts[i][1]
            iteration = list(iteration)
            for j in iteration:   
                Numbers= Numbers + "<li>" + str(j) + "</li>" 
                #z = Numbers
          
            if len(x[i]) == 2:
                finalReport.append(str(self.allReports[x[i][0]][0]) + " <----> " + str(self.allReports[x[i][1]][0]) + "</br> <ul>" + str(Numbers) + "</ul>" )
                Numbers = ''
                print("running")
            else:
                allReports = " "
                for j in range(0,len(x[i])):
                    if j == len(x[i])-1 :
                        allReports = allReports + self.allReports[x[i][j]][0]
                    else:
                        allReports = allReports + self.allReports[x[i][j]][0] + " <----> "
                finalReport.append(allReports + "</br> <ul>" + str(Numbers) + "</ul>" )
                    


        ReportString = str(finalReport)
        ReportString = ReportString[2:]
        ReportString = ReportString[:-2]
        ReportString = ReportString.replace("', '","")
        print(ReportString)



        f = open(self.reportDestination, 'w', encoding= 'utf-8')
        html_template = """<html>
        <head>
        <title>Comparator</title>
        </head>
        <body>
        <h2>Welcome To Comparator it worked</h2>
        
        
        """ + ReportString
        
        """
       <ul> </body>
        </html>
        """
        
       
        # writing the code into the file
        f.write(html_template)
        
        # close the file
        f.close()

        #<p>Default code + """ + str(finalReport) + """+ has been loaded into the Editor.</p>
        
    

def main():
    
    p1 = Comparator()
    root = tk.Tk()
    var = IntVar()


    def readFiles(var,top):
        print(var)
        if var == '1':
            p1.browseFiles() 
            p1.readAlleapReports()
        if var == '2':
            p1.browseFiles() 
            p1.readilleapReports()

        top.destroy()
    
    def sel():
        selection = "You selected the option " + str(var.get())
        print(selection)
        

    def open_popup(Output):
        top= Toplevel(root)
        top.geometry("750x250")
        top.title("Child Window")
        var.set(1)
        R1 = Radiobutton(top, text="Alleap Contacts.html", variable=var, value=1,
                  command=sel)
        R1.pack( anchor = W )

        R2 = Radiobutton(top, text="Illeap Contacts.html", variable=var, value=2,
                        command=sel)
        R2.pack( anchor = W )

       # R3 = Radiobutton(top, text="Cellebrite XML", variable=var, value=3,
      #                  command=sel)
       # R3.pack( anchor = W)

        label = Label(top)
        label.pack()
        btn = tk.Button(top, text="Add Files", command=lambda: readFiles(str(var.get()),top))
        btn.pack()
        Output.insert(END, 'Files Loaded\n')
        

        
    def compareFiles(Output):
        p1.compareReports()
        p1.printReport()
        Output.insert(END, 'Report Generated\n') 



    root.title("Welcome to Comparator")
    root.geometry("380x400")
   
    Output = Text(root, height = 5,
              width = 25,
              bg = "light cyan")

    btn3 = tk.Button(root, text="Add Files", command=lambda: open_popup(Output))
    
    btn4 = tk.Button(root, text="Select Report Destination", command=lambda: p1.browseReportDestination())
  
    btn2 = tk.Button(root, text="Compare Contacts", command=lambda: compareFiles(Output))
 
 
    

    btn3.pack()
    btn4.pack()
    btn2.pack()
    Output.pack()
      
 
    root.mainloop()



if __name__=="__main__":
    main()



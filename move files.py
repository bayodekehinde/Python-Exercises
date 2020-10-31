import os                                       #import os module
import shutil                                   #import shutil module
def move_files(source):
    
    '''This function get the files from a folder and arrange them according to their extension and saves the file in
a  folder accordingly'''
    #declaring empty lists for saving the files according to their extension
    pdf_files=[]
    docx_files=[]
    py_files=[]
    doc_files=[]
    
    for roots,dirs,files in os.walk(source):    #looping through the download folder in the system to get the roots, directoctories and file name in the folder
        for file in files:                      #looping through the files
            if file.endswith('.pdf'):           #check file with .pdf extension
                pdf_files.append(os.path.join(roots,file)) #save the path of the file to the pdf_folder
        
            if file.endswith('.docx'):
                docx_files.append(os.path.join(roots,file))
        
            if file.endswith('.py'):
                py_files.append(os.path.join(roots,file))
                

            if file.endswith('.doc'):
                doc_files.append(os.path.join(roots, file))
            

            
    try:                                                         #try moving the file and check if there is an error
        for file in pdf_files:                                   #loop through the list of pdf files
            print("Moving file to '.pdf' folder")
            shutil.move(file, r'C:\Users\user\downloads\.pdf')   #move the file to the pdf folder in the system
    except:
        shutil.Error                                            
        print("file already exist in  folder")
        
    try:
    
        for file in docx_files:
            print("moving file to '.docx' folder")
            shutil.move(file, r'C:\Users\user\downloads\.pdf')
    except:
        shutil.Error
        print("file exists")

    try:
        for file in py_files:
            print("moving file to '.py' folder")
            shutil.move(file, r'C:\Users\user\downloads\.py')
    except:
        shutil.Error
        print("file exists")

    try:
        for file in doc_files:
            print("moving file to '.doc' folder")
            shutil.move(file, r'C:\Users\user\downloads\.doc')
    except:
        shutil.Error
        print("File exists in desgnated folder")
   

    

move_files(r'C:\Users\user\downloads')              #call the function



   




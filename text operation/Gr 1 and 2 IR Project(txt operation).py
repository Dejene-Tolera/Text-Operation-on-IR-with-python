print("                                                                     ")
print("                                                                     ")
print("*********************************************************************")
print("*****  WELL COME TO INFORMATION STORAGE AND RETRIEVAL PROJECT  ******")
print("*********************************************************************")
print("_____________________________________________________________________")
print("                                                                     ")

i=10;
while(i!=0):
    choose=input('   Press 1 for Tokenization\n   Press 2 for Puctuation removal\n   Press 3 for Stopword Removal\n   Press 4 for Upper case\n   Press 5 for Lower case\n   Press 6 for Read all data\n   Press 7 for Read some line of data\n   Press 8 for Group 1 and 2 Information\n   Press 9 for Exit\n   *************Enter Option*************\n')
    if choose=='1':
        with open('SportData.txt','r+') as myfile:
            file=myfile.read()
        with open('Punctuation.txt','r+') as puctuation:
            puct=puctuation.read()
        for m in puct:
            file = file.replace(m," ")
        myList=[]
        myList.extend(file.split())
        for i in myList:
            print(i,end='\n')

    elif choose=='2':
        with open('SportData.txt','r+') as myfile:
            file=myfile.read()
        with open('Punctuation.txt','r+') as puctuation:
            puct=puctuation.read()
        for m in puct:
            file = file.replace(m," ")
        myList=[]
        myList.extend(file.split())
        for i in myList:
            print(i,end='\n')
        

    
    elif choose=='3':
        
        with open('SportData.txt','r+') as myfile1:
             file1=myfile1.read()
        with open('stopwords.txt','r+') as stopword:
            stop=stopword.read()
        with open('Punctuation.txt','r+') as puctuation:
            puct=puctuation.read()
        for m in puct:
            file1 = file1.replace(m," ")
        myList=[]
        myList.extend(file1.split())
        for word in myList:
            if word not in stop:
                print(word,end='\n')


    elif choose=='4':
        with open('SportData.txt','r') as myfile:
            file=myfile.read()
        myList=[]
        myList.extend(file.split())
        for i in myList:
            print(i.upper(),end='\n')
    
    elif choose=='5':
        with open('SportData.txt','r+') as myfile:
            file=myfile.read()
        myList=[]
        myList.extend(file.split())
        for i in myList:
            print(i.lower(),end='\n')

    elif choose=='6':
        file=open('SportData.txt','r+')
        fileall=file.read()
        print(fileall)
        file.close()

    elif choose=='7':
        file=open('SportData.txt','r+')
        fileall=file.readlines()
        print("first line")
        print(fileall[0])
        file.close()
       


    elif choose=='8':
        print("          Wolkite University         ")
        print("     College of Computing and Informatics    ")
        print("     Department of Information System  ")
        print("         Group 1 & 2 Member   ")
        print('   Name                                       Id No')
        print('____________________________________________________')
        print('1.Dejene Tolera                              136/11')
        print('2.Dheresa Amante                             139/11')
        print('3.Dendea Tarekegn                            167/11')
        print('4.Getu Niguse                                149/11')
        print('5.Negussie Duba                              173/11')
        print('6.Gemechu Iyasu                              148/11')
        print('7.Aster Gemeda                               159/11')



    elif choose=='9':
        exit()

    else:
        print('Enter the correct options')






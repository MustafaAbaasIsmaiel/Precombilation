Code = open("Code.txt","r")
Cycles=input('PLEASE INSERT A NUMBER THAT REPRESENTS CYCLES ') #NUMBER OF CYCLES FOR DIV AND MUL TO GET THE OUTPUT READY
x= Code.readlines()
Stages=0;
length=len(x); #THE INPUT ARRAY LENGTH(HOW MANY INSTRUCTIONS)
q1=[] #THESE ARRAYS WILL BE USED LATER THROUGH THE CODE
q2=[]
q3=[]
q4=[]
Check=input('PLEASE PRESS 1 IF FORWARDING IS ASSUMED AND 2 IF NOT ')
if((Check != 1) and (Check !=2)):  #THIS IS TO CHECK WHETHER FORWARDING IS ASSUMED OR NOT
    print('THE VALUE YOU ENTERED IS NOT CORRECT, PLEASE TRY AGAIN')
if((Check ==2)):                   #GETTING THE NUMBER OF STAGES AFTER EXECUTION
   Stages=input('PLEASE ENTER HOW MANY STAGES ARE THERE AFTER THE DECODE STAGE ')
y=[[0 for i in range (2)] for j in range(length)] #AN ARRAY TO STORE THE INPUT INTO MULTI-DIMENTIONAL ARRAY, EACH ARRAY OF THEM IS HOLDING THE INSTRUCTION AND REGISTERS NAMES
z=[0 for i in range(length)] #AN ARRAY TO HOLD ONLY INSTRUCTIONS (TO LOOP ON LATER)
w=[0 for i in range(length)] #AN ARRAY TO HOLD REGISTERS NAMES (TO COMPARE BETWEEN IT'S ELEMNTS LATER)
for i in range(0,length):
    y[i]=x[i].split(" ")  #STORING IN Y-ARRAY
for i in range(0,length): #STORING IN Z-ARRAY
    z[i]=y[i][0]
for i in range(0,length): #STORING IN W-ARRAY
    w[i]=y[i][1]
for i in range(0,length): #LOOPING ON ALL INSTRUCTIONS
    q1.append(x[i])       #SORTING THE INPUT INTO Q1-ARRAY(WITH STALLS ADDED BELOW)
    q2.append(w[i])       #SORTING THE REGISTER-ARRAY INTO Q2-ARRAY(WITH STALLS ADDED BELOW-JUST TO MAKE THE LENGTH CONSISTANT)
    q3.append(z[i])       #SORTING THE INSTRUCTIONS-ARRAY INTO Q3-ARRAY(WITH STALLS ADDED BELOW-JUST TO MAKE THE LENGTH CONSISTANT)
    if(z[i]=='DIV' or z[i]=='MUL' and i<length-1): #LOOKING FOR DIV AND MUL
        for j in range(0,Cycles):                          #CHECKING DEPENDANCY TO ALL UPCOMING INSTRUCTIONS WITHING RANGE
            if(j+i<length-1):                              #CHECKING I'M STILL IN RANGE
                First=w[i].split(",");                     #COMPARING THE FIRST ELEMENT IN THE REGISTERS CORRESPONDS TO THE SEARCHED-FOR INSTRUCTION
                Second=w[i+1+j].split(",");                  #WITH THE SECOND AND THE THIRD ONE OF THE NEXT INSTRUCTION
                Second[2]=Second[2][:len(Second)-1];       #GETTING RID OF (/N) THAT'S SUPERIMPOSED TO THE END OF THE ARRAY
                if(First[0] in Second):
                    for k in range(j,Cycles+Stages):              #ADDING NUMBER OF STALLS TO Q1,Q2 AND Q3 ARRAYS DEPENDANT ON THE VALUE OF CYCLES
                        q1.append("STALL\n")
                        q2.append("STALL\n")
                        q3.append("STALL\n")
                    break;                                 #TO BREAK THE LOOP IF DEPENDANCY IS FOUND
leng=len(q1)  #GETTING THE NEW LENGTH
if(Check==1): #FORWARDING IS ASSUMED
    for i in range(0,leng): #LOOPING OVER THE NEW LENGTH
        q4.append(q1[i]) #SORTING THE MODIFIED ARRAY INTO Q4 FOR AGAIN RE-WORKING ON IT
        if(i<leng-1):       #TO CHECK IF THE LOAD IS NOT THE LAST INSTRUCTION
            if((q3[i]=='LOD' and q3[i+1]!='STO') and i<leng-1): #REPEATING THE ABOVE SEQUENCE FOR THE LOD INSTRUCTION
                First=q2[i].split(",");
                Second=q2[i+1].split(",");
                Second[2]=Second[2][:len(Second)-1];
                if(First[0] in Second[1:]):
                    q4.append("STALL\n")
                
if(Check==2):               #FORWARDING IS NOT ASSUMED             
    for i in range(0,leng): #LOOPING OVER THE NEW LENGTH
        q4.append(q1[i])    #SORTING THE MODIFIED ARRAY INTO Q4 FOR AGAIN RE-WORKING ON IT
        if(i<leng-1):       #TO CHECK IF THE LOAD IS NOT THE LAST INSTRUCTION
            if(((q3[i]=='LOD' and q3[i+1]!='STO') or q3[i]=='SUB' or q3[i]== 'ADD') and i<leng-1): #REPEATING THE ABOVE SEQUENCE FOR THE LOD,ADD AND SUB INSTRUCTIONS
                First=q2[i].split(",");
                Second=q2[i+1].split(",");
                Second[2]=Second[2][:len(Second)-1];
                if(First[0] in Second[1:]):
                    for u in range(0,Stages):
                        q4.append("STALL\n")
                
x[:]=q4    #RE-WRITTING IN X AFTER ADDING ALL THESE STALLS
New_Length=len(x);  
Output= open("Output.txt","w")
for i in range(0,New_Length):
    Output.write(x[i])
Output.close()

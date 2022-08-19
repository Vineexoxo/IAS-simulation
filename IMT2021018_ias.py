def binary(num,terms):          #this will convert the data to decimal.
    a=bin(num)
    a=a[2:len(a)]
    for i in range(0,terms-len(a)):
        a="0"+a
    return a

def integer(binary):
    binary=int(binary)
    int_val, i, n = 0, 0, 0
    while(binary != 0): 
        a = binary % 10
        int_val = int_val + a * pow(2, i) 
        binary = binary//10
        i += 1
    return int_val

def LOAD_M(X):                          #LOAD M(X)
    return "00000001"+binary(X,12)

def ADD_M(X):                           #ADD M(X)
    return "00000101"+binary(X,12)

def STOR_M(X):                          #STOR M(X)
    return "00100001"+binary(X,12)

def MUL_M(X):                           #MUL M(X)
    return "00001011"+binary(X,12)

def SUB_M(X):                           #SUB M(X)
    return "00000110"+binary(X,12)

def JUMP_M(X,Y):                        #JUMP M(X)
    if Y=="0:19":
        return "00001101"+binary(X,12)
    elif Y=="20:39":
        return "00001110"+binary(X,12)

def JUMP_Mplus(X):                   #JUMP+ M(20:39)
    return "00010000"+binary(X,12)


def assembler(a,b):
    return a+b

def halt():
    return  0
#FETCH CYCLE
#Memory AND Registers.
MAIN=list(range(0,1000))
MAR=""
MBR=""
IBR=""
IR=""
MQ=0               #MQ initially has value 0.
AC=0               #AC initially has value 0.

def fetch(bit):
    if bit[0:8]=="00000000":       #LHS IS EMPTY. EXECUTION ONLY ON RHS.
        IR=bit[20:28]
        MAR=bit[28:40]
        return str(IR),str(MAR)

    elif len(bit)==40:             # 40 bit instruction
        IBR=bit[20:40]             # storing 20 bit rhs instruction in IBR.
        IR=bit[0:8]                # storing 8 bit LHS opcode in IR.
        MAR=bit[8:20]              # storing 20 bit LHS address in MAR.
        return str(IBR),str(IR),str(MAR)
    
    elif len(bit)==20:             # If 20 bit instruction in IBR is present. That is, we are accessing the right hand instruction present in IBR.
        IR=bit[0:8]
        MAR=bit[8:20]
        return str(IR),str(MAR)

def execute(IR,address,store):
    address=integer(address)
    IR=str(IR)
    if IR=="00000001" :                     #If the control signal is LOAD M(X) , MBR stores the value of the address andd AC stores the sum.
        MBR=MAIN[address]
        store=MBR
        return MBR,store
    elif IR=="00000101":                      #If the control signal is ADD M(X), MBR stores the value of the address andd AC stores the sum.
        MBR=MAIN[address]
        store=store+MBR
        return MBR,store
    elif IR=="00100001":                    #For STOR M(X). MBR stores the value of address. AC goes to MAIN MEMORY.
        MAIN[address]=store
        MBR=MAIN[address]
        return MBR
    elif IR=="00001011":
        MBR=MAIN[address]                   #for Multiplication.
        store=store*MBR                     #40*40=80 bit data which is then stored into AC and MQ(written in main())
        return MBR,store
    elif IR=="00000110": 
        MBR=MAIN[address]                   #for Subtraction. SUM M(X).
        store=store-MBR 
        return MBR,store
    elif IR=="00010000":
        MBR=MAIN[address]
        if store<0:
            MBR=MBR[20:40]
            return MBR
        MBR=MBR[0:20]
        return MBR

print("Perform:")
print("1. Addition of 10 numbers")
print("2. Multiplication of two numbers")
print("3. Greater of two numbers")

a=int(input("enter operation:"))
#ADDITION.

if a==1:
    p1=int(input("enter number in location 100: "))                                   #user input from input/output.
    MBR=p1                                                                            #input stored in MBR.
    MAIN[100]=MBR                                                                     #then it goes to the main memory location 100.(address)
    p2=int(input("enter number in location 101: "))
    MBR=p2
    MAIN[101]=MBR                                                                     #value p2 goes to memory location 101.
    p3=int(input("enter number in location 102: "))
    MBR=p3
    MAIN[102]=MBR
    p4=int(input("enter number in location 103: "))
    MBR=p4
    MAIN[103]=MBR
    p5=int(input("enter number in location 104: "))
    MBR=p5
    MAIN[104]=MBR
    p6=int(input("enter number in location 105: "))
    MBR=p6
    MAIN[105]=MBR
    p7=int(input("enter number in location 106: "))
    MBR=p7
    MAIN[106]=MBR
    p8=int(input("enter number in location 107: "))
    MBR=p8
    MAIN[107]=MBR
    p9=int(input("enter number in location 108: "))
    MBR=p9
    MAIN[108]=MBR
    p10=int(input("enter number in location 109: "))
    MBR=p10
    MAIN[109]=MBR

    MAIN[1]=assembler(LOAD_M(100),ADD_M(101))                               #store the assembly code in memory location.
    MAIN[2]=assembler(ADD_M(102),ADD_M(103))
    MAIN[3]=assembler(ADD_M(104),ADD_M(105))
    MAIN[4]=assembler(ADD_M(106),ADD_M(107))
    MAIN[5]=assembler(ADD_M(108),ADD_M(109))
    MAIN[6]=assembler("00000000000000000000",STOR_M(200))

    #FETCH CYCLE-1
    PC=1                                                        #Set PC=1. Counter value
    MAR=PC
    MBR=MAIN[MAR]                                               #MBR stores value at address 1.ie, the 40 bit instruction.

    IBR,IR,MAR=fetch(MBR)[0],fetch(MBR)[1],fetch(MBR)[2]        #updating values of IBR, IR, MAR.
    #From IR we send control signals. This then executes programs.
    #EXECUTE CYCLE-1
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]           #updating values of MBR and AC.
    #We have successfully executed LHS,ie,loading in accumulator.

    #now the next instruction is in IBR. No memory access required.

    #FETCH CYCLE-2
    IR,MAR=fetch(IBR)[0],fetch(IBR)[1]         # Updating values of IR and MAR after adding the two numbers.
    #FROM IR we send control signals. This then executes the program.

    #EXECUTE CYCLE-2
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]

    #Second Instruction.
    #FETCH CYCLE-3
    PC=PC+1                                    # Increment value of PC. PC is a counter.
    MAR=PC
    MBR=MAIN[MAR]

    IBR,IR,MAR=fetch(MBR)[0],fetch(MBR)[1],fetch(MBR)[2]        #updating values of IBR, IR, MAR.
    #From IR we send control signals. This then executes programs.

    #EXECUTE CYCLE-3
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]           #updating values of MBR and AC.
    #We have successfully executed LHS,ie,loading in accumulator.

    #now the next instruction is in IBR. No memory access required.

    #FETCH CYCLE-4
    IR,MAR=fetch(IBR)[0],fetch(IBR)[1]         # Updating values of IR and MAR after adding the two numbers.
    #FROM IR we send control signals. This then executes the program.

    #EXECUTE CYCLE-4
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]

    #Third Instruction.
    #FETCH CYCLE-5
    PC=PC+1                                    # Increment value of PC. PC is a counter.
    MAR=PC
    MBR=MAIN[MAR]
    IBR,IR,MAR=fetch(MBR)[0],fetch(MBR)[1],fetch(MBR)[2]        #updating values of IBR, IR, MAR.
    #From IR we send control signals. This then executes programs.

    #EXECUTE CYCLE-5
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]           #updating values of MBR and AC.
    #We have successfully executed LHS,ie,loading in accumulator.

    #now the next instruction is in IBR. No memory access required.

    #FETCH CYCLE-6
    IR,MAR=fetch(IBR)[0],fetch(IBR)[1]         # Updating values of IR and MAR after adding the two numbers.
    #FROM IR we send control signals. This then executes the program.

    #EXECUTE CYCLE-6
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]

    #Fourth Instruction.
    #FETCH CYCLE-7
    PC=PC+1                                    # Increment value of PC. PC is a counter.
    MAR=PC
    MBR=MAIN[MAR]

    IBR,IR,MAR=fetch(MBR)[0],fetch(MBR)[1],fetch(MBR)[2]        #updating values of IBR, IR, MAR.
    #From IR we send control signals. This then executes programs.

    #EXECUTE CYCLE-7
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]           #updating values of MBR and AC.
    #We have successfully executed LHS,ie,loading in accumulator.

    #now the next instruction is in IBR. No memory access required.

    #FETCH CYCLE-8
    IR,MAR=fetch(IBR)[0],fetch(IBR)[1]         # Updating values of IR and MAR after adding the two numbers.
    #FROM IR we send control signals. This then executes the program.

    #EXECUTE CYCLE-8
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]

    #Fifth Instruction.
    #FETCH CYCLE-9
    PC=PC+1                                    # Increment value of PC. PC is a counter.
    MAR=PC
    MBR=MAIN[MAR]

    IBR,IR,MAR=fetch(MBR)[0],fetch(MBR)[1],fetch(MBR)[2]        #updating values of IBR, IR, MAR.
    #From IR we send control signals. This then executes programs.

    #EXECUTE CYCLE-9
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]           #updating values of MBR and AC.
    #We have successfully executed LHS,ie,loading in accumulator.

    #now the next instruction is in IBR. No memory access required.

    #FETCH CYCLE-10
    IR,MAR=fetch(IBR)[0],fetch(IBR)[1]         # Updating values of IR and MAR after adding the two numbers.
    #FROM IR we send control signals. This then executes the program.

    #EXECUTE CYCLE-10
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]

    #Sixth Instruction.
    #FETCH CYCLE-11
    PC=PC+1                                    # Increment value of PC. PC is a counter.
    MAR=PC
    MBR=MAIN[MAR]                              #MBR stores the 40bit instruction.
    IR,MAR=fetch(MBR)[0],fetch(MBR)[1]
    #IR sends control signals. This executes the program.

    #EXECUTE CYCLE-11
    #the sum is stored in AC. We now put the sum in memory location 200.
    MBR=execute(IR,MAR,AC)
    print("A1nswer stored in memory location 200:",MAIN[200])
    #Halt the program.
    halt()

#Multiplication.
elif a==2:
    p1=int(input("enter number in memory location 500: "))        #user input from input/output.
    MBR=p1                                                        #input stored in MBR.
    MAIN[500]=MBR                                          #then it goes to the main memory location 500.(address)
    p2=int(input("enter number in memory location 501: "))
    MBR=p2

    MAIN[501]=MBR                                          #value p2 goes to memory location 501.

    MAIN[3]=assembler(LOAD_M(500),MUL_M(501))              #Assembly language stored in memory location 3 and 4.
    MAIN[4]=assembler("00000000000000000000",STOR_M(10))

    #FETCH CYCLE-1
    PC=3                                                   #Set PC=3 as counter.
    MAR=PC                                                 #MAR stores PC value.
    MBR=MAIN[MAR]                                          #MBR stores the 40bit instruction

    IBR,IR,MAR=fetch(MBR)[0],fetch(MBR)[1],fetch(MBR)[2]   #IBR has 20 bit right instruction. IR has left opcode. MAR has left address.
    #From IR we send control signals.This then executes programs.

    #EXECUTE CYCLE-1.
    MBR,MQ=execute(IR,MAR,MQ)[0],execute(IR,MAR,MQ)[1]           #updating values of MBR and MQ.
    #We have successfully executed LHS, loading in MQ.

    #Now the next memory instruction is in IBR(right hand instruction). NO memory access required.

    #FETCH CYCLE-2.
    IR,MAR=fetch(IBR)[0],fetch(IBR)[1]                           #Updating values of IR and MAR.IR has opcode,MAR has memory.
    #From IR, we send control signals.

    #EXECUTE CYCLE-2.
    MBR,MQ=execute(IR,MAR,MQ)[0],execute(IR,MAR,MQ)[1]           #MBR stores the data in address 501 and MQ contains the multiplication product.
    tmp=binary(MQ,80)                                            #MULTIPLICATION gives 80 bit data, left 40 in AC and right 40 in MQ
    AC=integer(tmp[0:40])
    MQ=integer(tmp[40:80])

    
    #Second instruction.
    PC=PC+1                                                      #Increment the counter PC with one. This now stores the address of second instruction.
    MAR=PC
    #FETCH CYCLE-3
    MBR=MAIN[MAR]                              #MBR stores the 40bit instruction.
    IR,MAR=fetch(MBR)[0],fetch(MBR)[1]
    #IR sends control signals. This executes the program.

    #EXECUTE CYCLE-3
    #the sum is stored in AC. We now put the sum in memory location 10.
    MBR=execute(IR,MAR,MQ)
    print("product in memory location 10: ",MAIN[10])
    #Halt the program.
    halt()

elif a==3:
    a=int(input("enter number in location 100: "))                                   #user input from input/output.
    MBR=a                                                                            #input stored in MBR.
    MAIN[100]=MBR                                                                    #then it goes to the main memory location 100.(address)
    b=int(input("enter number in location 101: "))
    MBR=b
    MAIN[101]=MBR                                                                    #value p2 goes to memory location 101.
    MAIN[1]=assembler(LOAD_M(100),SUB_M(101))
    MAIN[2]=assembler("00000000000000000000",JUMP_Mplus(4))
    MAIN[4]=assembler(LOAD_M(100),LOAD_M(101))
    MAIN[3]=assembler("00000000000000000000",STOR_M(5))

    #FETCH CYCLE-1
    PC=1
    MAR=PC
    MBR=MAIN[MAR]

    IBR,IR,MAR=fetch(MBR)[0],fetch(MBR)[1],fetch(MBR)[2]         #IBR has 20 bit right instruction. IR has left opcode. MAR has left address.
    #From IR we send control signals.This then executes programs.
    #EXECUTE CYCLE-1
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]           #updating values of MBR and AC.
    #We have successfully executed LHS,ie,loading in accumulator.

    #now the next instruction is in IBR. No memory access required.

    #FETCH CYCLE-2
    IR,MAR=fetch(IBR)[0],fetch(IBR)[1]                           # Updating values of IR and MAR after adding the two numbers.
    #FROM IR we send control signals. This then executes the program.
    #EXECUTE CYCLE-2
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]

    #FETCH CYCLE-3
    PC=PC+1
    MAR=PC
    MBR=MAIN[MAR]

    IR,MAR=fetch(MBR)[0],fetch(MBR)[1]
    #IR sends control signals. This executes the program.
    #EXECUTE CYCLE-3
    MBR=execute(IR,MAR,AC)
    
    #FETCH CYCLE-4
    IR,MAR=fetch(MBR)[0],fetch(MBR)[1]
    #FROM IR we send control signals. This then executes the program. 
    #EXECUTE CYCLE-4
    MBR,AC=execute(IR,MAR,AC)[0],execute(IR,MAR,AC)[1]

    #Second instruction.
    PC=PC+1                                                      #Increment the counter PC with one. This now stores the address of second instruction.
    MAR=PC
    #FETCH CYCLE-5
    MBR=MAIN[MAR]                              #MBR stores the 40bit instruction.
    
    IR,MAR=fetch(MBR)[0],fetch(MBR)[1]
    #IR sends control signals. This executes the program.

    #EXECUTE CYCLE-5
    #the number is stored in AC. We now put the sum in memory location 5.
    MBR=execute(IR,MAR,AC)
    print("greater number in memory location 5:",MAIN[5])
    #Halt the program.
    halt()

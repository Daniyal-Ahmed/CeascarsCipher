#Simple program to solve a Caesar's Cipher. 
#Inputs can only be English letters.
#Uses frequency analysis to figure decrypt the message.


letterFrequency = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def Shifter(listInput, S):
    listTest = []
    ShiftOrd = 0
    for j in range(0,len(listInput)):
        
        if listInput[j] != ' ':
            InputOrd = ord(listInput[j])
            ShiftOrd = InputOrd + S
            
            if ShiftOrd > 90:
                A = ShiftOrd - 90
                ShiftOrd = 64 + A
            listTest.insert(j, chr(ShiftOrd))
            
        else:
            listTest.insert(j, ' ')
    return listTest

def CalculateFrequency(listTest):
    frequency = 0
    for i in range(0, len(listTest)):
        if listTest[i] != ' ':
            Ord = ord(listTest[i])
            Place = Ord - 65
            frequency += letterFrequency[Place]

        else:
            frequency = frequency
    return frequency

def Check(codeList):
    decodeList = []
    highestFrequency = 0
    frequency = 0
    for S in range(1, 27):
        shiftList = Shifter(codeList, S)
        
        frequency = CalculateFrequency(shiftList)
        
        if frequency >  highestFrequency:
            highestFrequency = frequency
            maxS = S
            decodeList = shiftList
          
            frequency = 0
        else:
            frequency = 0
    return decodeList
    

def Decode(code):
    codeList = list(code)
    msg = Check(codeList)
    message = ''
    for i in range(0, len(msg)):
        message = message + str(msg[i])
    return message
    

print("=============================================================")
print("Enter Message to Decode")
print("=============================================================")
input_message = input()
message = input_message.upper()
print("=============================================================")
print("CODED MESSAGE:  " + message)
print("=============================================================")
print("DECODED RESULT:", Decode(message))
print("=============================================================")
      
#print("DECODE: UIJT JT B TBNQMF MJOF PG UFYU GPS EFDSZQUJOH")
#print("RESULT:", Decode("UIJT JT B TBNQMF MJOF PG UFYU GPS EFDSZQUJOH"))


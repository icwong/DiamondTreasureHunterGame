#PROGRAM DESCRIPTION: THIS PROGRAM WILL ASK THE USER FOR PERSON INFORMATION AND INTEREST IN ORDER TO GENERATE A LUCKY NUMBER &
#A MESSAGE, BASED ON THE DATA THE USER PROVIDED US.

def welcome_message(): #non-fruitful function   #INTRODUCTION
    print "Weclome to the CMPT 120 Assignment #2 !" #SUBROUTINE  
    print
    print "Please follow the instructions"
    print "You will be given a lucky number and a message, based on the data you gave us!"
    print "-"* 30
    return
welcome_message()

#USER INPUTS
firstlast = raw_input("Please provide your first and last names, seperated by one space: ") # FIRST AND LAST NAME
print
address = raw_input("Please provide your address, numbers first, and then one space and the name of the street: ") # ADDRESS
print
sentence = raw_input("Please provide a sentence, with at least three to four words, seperated by one space: ") # SENTENCE
print
binary = raw_input("Please provide a binary number of 2 to 4 bits (ex.1001): ") #BINARY
print
charcode = raw_input("Please provide a two character code with any combination of letters, symbols or numbers: ") #CHARACTERCODE
print

# Calculation to obtain the lucky number

s01 = firstlast[0] #first letter of first name
s2 = firstlast.find(" ") #space between first name and last name
s3 = firstlast[s2 + 1] #first letter of last name

s4 = address.find(" ") #find first space from the address
s5 = address[s4 + 1] #first letter of the address
if (s5.isdigit()): #determines if street name starts with number
    s5a = "" #if number then remove
else:
    s5a = s5 #if letter then include
    
s6 = sentence[0] # first letter of first word
s7 = sentence.find(" ")
s8 = sentence[s7 + 1] # first letter of second word
s9 = sentence.find(" ", s7 + 1)
s10 = sentence[s9 + 1] #first letter of third word

    
s1 =  s01 + s3 + s5a + s6 + s8 + s10 #Result of s1
print "Contructing s1 ..."
print
print "TRACE - s1 is ....", s1
print
print "Calculating n1, n2, n3, n4 and lucky"
print

# to calculate the lucky number with intermediate steps:

# Obtaining n1
length = len(s1) # length of s11 result
import math #open up math folder basically 
rounded = round(math.pi, 3) #pi rounded to 3 fractional digits
ascii_firstletter = ord(firstlast[0]) # ascii of first 

sumoflra = length + rounded + ascii_firstletter #sum of length,rounded,ascii

print "*** n1 is...", sumoflra #n1
print

# Obtaining n2
z1 = address.find(" ") #find address space
z2 = address[:z1] #find the address number by assuming that they put a numerical value first 
subtracting_n1_address = (float(z2) - float(sumoflra))# address - n1
faddress = (subtracting_n1_address)#float n1
roundaddress = round(faddress,3) #round n1 to 3 decimals

print "TRACE substracting address - n1 is: ",roundaddress # no negative sign
print
absofaddress = abs(faddress) #abs value of float n1

import math
sqrtofaddress = math.sqrt(absofaddress) #sqrt of abs value of float to get n2
roundof = round(sqrtofaddress,3) # sqrt of abs value n2, 3 digit
print "*** n2 is...",roundof #n2
print

#Obtaining n3
t1 = str(roundof) # converts float(roundof) -> string [useable for slicing]
t2 = t1[0] #finding first digit of n2
t3 = t1.find(".") #finding the decimal digit of n2
t4 = t1[t3 + 1] #finding first fractional digit in n2
print "TRACE first digit in n2 is: ", t2 #first digit of n2
print "TRACE fractional digit in n2 is: ", t4 #first decimal digit of n2
print

addition = int(t2) + int(t4) #first digit + first decimal digit of n2
print "*** n3 is ... ", addition #n3
print
#Obtaining n4
str_add = str(addition) #making it into a string
len_add = len(str_add) #counting the length of the str_add

if (len_add == 1): #if the length of n3 is < 1 then...
    n4 = addition #if n3 is less than 1 digit then n4 = n3
    print "*** n4 is... :",str(n4) #n4
else: 
    fdfa = int(str_add[0]) #first digit from addition
    sdfa = int(str_add[1]) #second digit from addition
    sumfs = fdfa + sdfa #sum of first & second digit
    n4 = sumfs #making a variable
    print "*** n4 is... :",str(n4) # if n3 is greater than 1 digit then n4 is sum of two digits

print
#Finally the lucky number!
# odd = one
# even = zero

if (binary[-1] == "1"): #Determining if the last digit of the binary is equal to 1
    luckynumber1 = n4 #Equal to 1 = odd
    print "TRACE the binary number is odd, lucky number will be same as n4"
else:
    luckynumber1 = (n4 * 2) #Not equal to 1 = even
    print "TRACE the binary number is even, lucky number will be n4 * 2"

print
print "***YAY! The lucky number is... ", str(luckynumber1)
print

#Constructing the message!

m1 = firstlast[1] # Determines the first letter of the first name
m2 = m1.upper()  # converts m1 into an upper case
m3 = "!" * luckynumber1  # ! is based on what is your luckynumber multiply it

m4 = firstlast[-1] # Last letter of first name
m4a = address.lower()
m5 = m4a.find(m4) # finding last letter of first name if exist in the address

if (charcode.isalpha()): # Adding the 2 character code
    b1 = charcode
else:
    b1 = charcode[0]

m6 = str(m2) + str(luckynumber1) + str(m3) #constructing TRACE 1
m7 = str(m6) + str(m5) #constructing TRACE 2
m8 = str(m7) + str(b1) #constructing TRACE 3

m9 = str(m8) + str(s1) #adding the TRACE 3 message with s1
m10 = str(m9) 

e1 = len(m10) #determing the length of m9 basically since, m10 = m9
if (e1%2 == 0): #if it is even it is divisible by 2 and the end result is 0
    evenodd = "E" #gives letter E if even
else:
    evenodd = "O" #gives letter O if odd
    

print "TRACE so far, parts a,b,c, the message is...", m6
print "TRACE so far, parts a,b,c,d, the message is...",m7
print "TRACE so far, parts a,b,c,d,e the message is...", m8
print
print "Yay! the message is",m10 + evenodd
print
print "End of the program BYE!"






    
    













    












##############################################################################

def getOnlyDigits(txt):
   return getOnlyThisChars(txt,'0123456789')

def getOnlyLetters(txt):
   return getOnlyThisChars(txt,'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def getOnlyUpperLetters(txt):
   return getOnlyThisChars(txt,'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def getOnlyThisChars(txt,chars=''):
   return ''.join([ch for ch in str(txt) if ch in chars])

##############################################################################

def isVATCorrectFR(txt): # FRANCE
   if getOnlyLetters(txt).upper() not in ['','FR']: return False
   txt = getOnlyDigits(txt)
   return len(txt)==11 and txt[:2]==('0'+str((12+3*(int(str(txt)[2:])%97))%97))[-2:]

def isVATCorrectGB(txt): #GREAT BRITAIN
   if getOnlyLetters(txt).upper() not in ['','GB']: return False
   txt = getOnlyDigits(txt)   
   #tow last digits makes control sum
   importance=[8,7,6,5,4,3,2]
   checksum=0
   for ii in range(0,min(len(txt)-1,len(importance))): 
      checksum+= (ord(txt[ii])-48) * importance[ii]
   while(checksum>=0): checksum-=97 #sum must be negative
   return len(txt)==9 and txt[-2:]== ('0'+str(checksum*-1))[-2:]

def isVATCorrectPL(txt): # POLAND
   if getOnlyLetters(txt).upper() not in ['','PL']: return False
   txt = getOnlyDigits(txt)   
   #last digit is a control check, next modulo 11
   importance=[6,5,7,2,3,4,5,6,7]
   checksum=0
   for ii in range(0,min(len(txt)-1,len(importance))): 
      checksum+= (ord(txt[ii])-48) * importance[ii]
   return len(txt)==10 and txt[-1]==chr(checksum%11+48)

def isVATCorrectPT(txt): #PORTUGAL
   if getOnlyLetters(txt).upper() not in ['','PT']: return False
   txt = getOnlyDigits(txt)   
   #last digit is a control sum, next 11 minus modulo 11
   importance=[9,8,7,6,5,4,3,2]
   checksum=0
   for ii in range(0,min(len(txt)-1,len(importance))): 
      checksum+= (ord(txt[ii])-48) * importance[ii]
   return len(txt)==9 and txt[-1]==chr(11-checksum%11+48)

def isVATCorrectSE(txt): #SWEDEN
   if getOnlyLetters(txt).upper() not in ['','SE']: return False
   txt = getOnlyDigits(txt)   
   #-3 from end digit is a control sum, next 10 minus modulo 10
   importance=[2,1,2,1,2,1,2,1,2]
   sum_str=''
   for ii in range(0,min(len(txt)-3,len(importance))): 
      sum_str += str((ord(txt[ii])-48) * importance[ii])
   checksum = sum([int(x) for x in sum_str])
   return len(txt)==12 and txt[-3]==chr(10-checksum%10+48)

##############################################################################
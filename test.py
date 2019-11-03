from functions_ready import *

def getOnlyDigits(txt):
   return getOnlyThisChars(txt,'0123456789')

def getOnlyUpperLetters(txt):
   return getOnlyThisChars(txt,'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def getOnlyThisChars(txt,chars=''):
   return ''.join([ch for ch in str(txt) if ch in chars])

#testing
valid_numbers = [
   'GB 799769914','GB815382334','GB001514344','GB562235945', #GREAT BRITAIN
   'PT 136695973','PT506774287','PT,507,132,831','PT 507400011 ','PT507852605','PT508219612', #PORTUGAL
   'FR46340793959','FR 83,404,833,048','FR 03-784-359-069','FR44527865992 ', #FRANCE
   'SE136695975523','SE202100509101 ','SE 556101935601','SE556785615701', #SWEDEN
   'PL6331637013','PL768-000-24-66','PL 842-162-27-20',  #POLAND
   'ES 2135856252', #SPAIN
   'IT00000010215', #ITALY
   ]

invalid_numbers = ['FR1234234132','FR1111112223','FR16340793959','ffsefqwdwe','','][;];][','*','1112223334',9998]

print('')
for nr in valid_numbers+invalid_numbers:
   country_code = getOnlyUpperLetters(nr)[:2]
   digit_code = getOnlyDigits(nr)[:20]
   command = 'isVATCorrect%s("%s")' % (country_code, digit_code)
   try:
      if eval(command)!=True and nr in valid_numbers:
         print(' !!! Incorrect result for: %s %s (originally: %s) !!!' % (country_code, digit_code, nr))
   except:
      if nr not in invalid_numbers:
         print('ERROR // Unknown country code %s or incorrect function inside: %s' % (country_code, command))

print('Finally checked %d numbers (valid and invalid)' % len(valid_numbers+invalid_numbers))
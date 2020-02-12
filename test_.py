from isVATCorrect import *

assert isVATCorrectFR('FR46340793959') == True
assert isVATCorrectFR('FR 83,404,833,048') == True
assert isVATCorrectFR('FR 03-784-359-069') == True
assert isVATCorrectFR('FR44527865992 ') == True

assert isVATCorrectGB('GB 799769914') == True
assert isVATCorrectGB('GB815382334') == True
assert isVATCorrectGB('GB001514344') == True
assert isVATCorrectGB('GB562235945') == True

assert isVATCorrectPT('PT 136695973') == True
assert isVATCorrectPT('PT506774287') == True
assert isVATCorrectPT('PT,507,132,831') == True
assert isVATCorrectPT('PT 507400011 ') == True
assert isVATCorrectPT('PT507852605') == True
assert isVATCorrectPT('PT508219612') == True

assert isVATCorrectSE(136695975523) == True
assert isVATCorrectSE('SE136695975523') == True
assert isVATCorrectSE('SE202100509101 ') == True
assert isVATCorrectSE('SE 556101935601') == True
assert isVATCorrectSE('SE556785615701') == True

assert isVATCorrectPL(6331637013) == True
assert isVATCorrectPL('PL6331637013') == True
assert isVATCorrectPL('PL768-000-24-66') == True
assert isVATCorrectPL('PL 842-162-27-20') == True

#assert isVATCorrectES('ES 2135856252') == True
#assert isVATCorrectIT('IT00000010215') == True

assert isVATCorrectFR('FR1234234132') == False
assert isVATCorrectFR('FR1111112223') == False
assert isVATCorrectFR('FR16340793959') == False
assert isVATCorrectFR('ffsefqwdwe') == False
assert isVATCorrectFR('][;];][') == False
assert isVATCorrectFR('*') == False
assert isVATCorrectFR('1112223334') == False
assert isVATCorrectFR(9998) == False


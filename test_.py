from is_vat_correct import *

assert is_vat_number_correct_fr('FR46340793959') == True
assert is_vat_number_correct_fr('FR 83,404,833,048') == True
assert is_vat_number_correct_fr('FR 03-784-359-069') == True
assert is_vat_number_correct_fr('FR44527865992 ') == True

assert is_vat_number_correct_gb('GB 799769914') == True
assert is_vat_number_correct_gb('GB815382334') == True
assert is_vat_number_correct_gb('GB001514344') == True
assert is_vat_number_correct_gb('GB562235945') == True

assert is_vat_number_correct_pt('PT 136695973') == True
assert is_vat_number_correct_pt('PT506774287') == True
assert is_vat_number_correct_pt('PT,507,132,831') == True
assert is_vat_number_correct_pt('PT 507400011 ') == True
assert is_vat_number_correct_pt('PT507852605') == True
assert is_vat_number_correct_pt('PT508219612') == True

assert is_vat_number_correct_se(136695975523) == True
assert is_vat_number_correct_se('SE136695975523') == True
assert is_vat_number_correct_se('SE202100509101 ') == True
assert is_vat_number_correct_se('SE 556101935601') == True
assert is_vat_number_correct_se('SE556785615701') == True

assert is_vat_number_correct_pl(6331637013) == True
assert is_vat_number_correct_pl('PL6331637013') == True
assert is_vat_number_correct_pl('PL768-000-24-66') == True
assert is_vat_number_correct_pl('PL 842-162-27-20') == True

assert is_vat_number_correct_fr('FR1234234132') == False
assert is_vat_number_correct_fr('FR1111112223') == False
assert is_vat_number_correct_fr('FR16340793959') == False
assert is_vat_number_correct_fr('ffsefqwdwe') == False
assert is_vat_number_correct_fr('][;];][') == False
assert is_vat_number_correct_fr('*') == False
assert is_vat_number_correct_fr('1112223334') == False
assert is_vat_number_correct_fr(9998) == False


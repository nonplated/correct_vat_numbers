#https://romek.info/ut/translation.html#PL
#http://www.pruefziffernberechnung.de/
#https://www.braemoor.co.uk/software/vattestx.php
#https://stackoverflow.com/questions/33625770/check-vat-number-for-syntactical-correctness-with-regex-possible
#http://www.pruefziffernberechnung.de/S/SIREN.shtml

#not used yet
match_vat = r'''(?xi)^(
(AT)?U[0-9]{8} |                              # Austria
(BE)?0[0-9]{9} |                              # Belgium
(BG)?[0-9]{9,10} |                            # Bulgaria
(HR)?[0-9]{11} |                              # Croatia
(CY)?[0-9]{8}[A-Z] |                          # Cyprus
(CZ)?[0-9]{8,10} |                            # Czech Republic
(DE)?[0-9]{9} |                               # Germany
(DK)?[0-9]{8} |                               # Denmark
(EE)?[0-9]{9} |                               # Estonia
(EL)?[0-9]{9} |                               # Greece
ES[A-Z][0-9]{7}(?:[0-9]|[A-Z]) |              # Spain
(FI)?[0-9]{8} |                               # Finland
(FR)?[0-9A-Z]{2}[0-9]{9} |                    # France
(GB)?([0-9]{9}([0-9]{3})?|[A-Z]{2}[0-9]{3}) | # United Kingdom
(HU)?[0-9]{8} |                               # Hungary
(IE)?[0-9]{7}[A-Z]{1,2}   |                   # Ireland
(IE)?[0-9][A-Z][0-9]{5}[A-Z] |                # Ireland (2)
(IT)?[0-9]{11} |                              # Italy
(LT)?([0-9]{9}|[0-9]{12}) |                   # Lithuania
(LU)?[0-9]{8} |                               # Luxembourg
(LV)?[0-9]{11} |                              # Latvia
(MT)?[0-9]{8} |                               # Malta
(NL)?[0-9]{9}B[0-9]{2} |                      # Netherlands
(PL)?[0-9]{10} |                              # Poland
(PT)?[0-9]{9} |                               # Portugal
(RO)?[0-9]{2,10} |                            # Romania
(SE)?[0-9]{12} |                              # Sweden
(SI)?[0-9]{8} |                               # Slovenia
(SK)?[0-9]{10}                                # Slovakia
)$'''
'''
def isVATCorrectIT(txt): #ITALY ???
   #last digit is a control sum, next 10 minus modulo 10
   importance=[2,1,2,1,2,1,2,1]
   sum_str=''
   for ii in range(0,min(len(txt)-1,len(importance))): 
      sum_str += str((ord(txt[ii])-48) * importance[ii])
   checksum = sum([int(x) for x in sum_str])
   return len(txt)==8 and txt[-1]==chr(10-checksum%10+48)
'''

   #'IT A13 585 625', # dont know what it is
   #'PT507599470 ' #doesnt exists?



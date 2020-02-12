

# correct vat numbers
Functions to check is a VAT number is valid -- by calculating checksum.
There is no online checking. Just calculating checksum offline. 


## quick start
Ready to use functions you will find in:
```
isVATCorrect.py
```


## currently for countries: 
```
FR -- France
GB -- Great Britain
PL -- Poland
PT -- Portugal
SE -- Sweden
```


## usage
No needed to be clear input. 
For example:
```
isVATCorrectGB('123456789')                            # OK
isVATCorrectGB('GB123456789')                          # OK
isVATCorrectGB('GB 123-456-789')                       # OK
isVATCorrectGB('%^^^GB-123,456/789%*')                 # OK
isVATCorrectGB(123456789)                              # OK
isVATCorrectFR('GB-123,456/789%*') # OK, but will return False, GB not match FR 
```
In **test_.py** some examples and asserts.


## todo
* more countries


Autumn 2019 // Python 3

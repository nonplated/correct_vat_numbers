

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
No needed to clear input. Only STRING type is necessary.
For example:
```
isVATCorrectGB('123456789')                            # OK
isVATCorrectGB('GB123456789')                          # OK
isVATCorrectGB('GB 123-456-789')                       # OK
isVATCorrectGB('%^^^GB-123,456/789%*')                 # OK

isVATCorrectFR('GB-123,456/789%*')   # WRONG, GB not match FR 
isVATCorrectGB(123456789)            # WRONG, must be text format
```
In **test_.py** some examples and asserts.


## todo
* more countries


Autumn 2019 // Python 3

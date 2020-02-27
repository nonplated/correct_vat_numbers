

# correct vat numbers
Functions to check is a VAT number is valid -- by calculating checksum.
There is NO ONLINE checking. Just calculating checksum.


## quick start
Ready to use functions you will find in:
```
is_vat_correct.py
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
is_vat_number_correct_gb('123456789')                            # OK
is_vat_number_correct_gb('GB123456789')                          # OK
is_vat_number_correct_gb('GB 123-456-789')                       # OK
is_vat_number_correct_gb('%^^^GB-123,456/789%*')                 # OK
is_vat_number_correct_gb(123456789)                              # OK
is_vat_number_correct_fr('GB-123,456/789%*') # OK, but will return False, GB not match FR
```
In **test_.py** some examples and asserts.


## todo
* more countries


Autumn 2019 // Python 3

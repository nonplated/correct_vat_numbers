# correct vat numbers

Functions to check is a VAT number is valid -- by calculating checksum 

Ready to use functions you will find in:
```
functions_ready.py
```
## currently for countries: 
* FR -- France
* GB -- Great Britain
* PL -- Poland
* PT -- Portugal
* SE -- Sweden

## usage
You should clear input argument "txt" before use (for example by using: *getOnlyDigits()* and *getOnlyUpperLetters()* from "functions_ready.py"). For good results "txt" should have only digits as a text format (ex. '123456789').
For example:
```
isVATCorrectGB('123456789')                            # OK
isVATCorrectGB(getOnlyDigits('GB 123-456-789'))        # OK
isVATCorrectGB(getOnlyDigits('%^^^GB-123,456/789%*'))  # OK

isVATCorrectGB(123456789)         # Wrong, must be text format
isVATCorrectGB('GB123456789')     # Wrong, use only digits
```
In *text.py* you'll find some more examples.

## TODO

* more countries

2019 // Autumn // Python 3

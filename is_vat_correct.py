##############################################################################


def get_only_digits(txt):
    return get_only_selected_chars(txt, '0123456789')


def get_only_letters(txt):
    return get_only_selected_chars(txt, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')


def get_only_upper_letters(txt):
    return get_only_selected_chars(txt, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def get_only_selected_chars(txt, chars=''):
    return ''.join([ch for ch in str(txt) if ch in chars])

##############################################################################


def is_vat_number_correct_fr(txt):  # FRANCE
    txt = str(txt)
    if get_only_letters(txt).upper() not in ['', 'FR']:
        return False
    txt = get_only_digits(txt)
    is_correct = len(txt) == 11 and txt[:2] == (
        '0'+str((12+3*(int(str(txt)[2:]) % 97)) % 97))[-2:]
    return is_correct


def is_vat_number_correct_gb(txt):  # GREAT BRITAIN
    txt = str(txt)
    if get_only_letters(txt).upper() not in ['', 'GB']:
        return False
    txt = get_only_digits(txt)
    # tow last digits makes control sum
    importance = [8, 7, 6, 5, 4, 3, 2]
    checksum = 0
    for ii in range(0, min(len(txt)-1, len(importance))):
        checksum += (ord(txt[ii])-48) * importance[ii]
    while(checksum >= 0):
        checksum -= 97  # sum must be negative
    is_correct = len(txt) == 9 and txt[-2:] == ('0'+str(checksum*-1))[-2:]
    return is_correct


def is_vat_number_correct_pl(txt):  # POLAND
    txt = str(txt)
    if get_only_letters(txt).upper() not in ['', 'PL']:
        return False
    txt = get_only_digits(txt)
    # last digit is a control check, next modulo 11
    importance = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    checksum = 0
    for ii in range(0, min(len(txt)-1, len(importance))):
        checksum += (ord(txt[ii])-48) * importance[ii]
    is_correct = len(txt) == 10 and txt[-1] == chr(checksum % 11+48)
    return is_correct


def is_vat_number_correct_pt(txt):  # PORTUGAL
    txt = str(txt)
    if get_only_letters(txt).upper() not in ['', 'PT']:
        return False
    txt = get_only_digits(txt)
    # last digit is a control sum, next 11 minus modulo 11
    importance = [9, 8, 7, 6, 5, 4, 3, 2]
    checksum = 0
    for ii in range(0, min(len(txt)-1, len(importance))):
        checksum += (ord(txt[ii])-48) * importance[ii]
    is_correct = len(txt) == 9 and txt[-1] == chr(11-checksum % 11+48)
    return is_correct


def is_vat_number_correct_se(txt):  # SWEDEN
    txt = str(txt)
    if get_only_letters(txt).upper() not in ['', 'SE']:
        return False
    txt = get_only_digits(txt)
    # -3 from end digit is a control sum, next 10 minus modulo 10
    importance = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    sum_str = ''
    for ii in range(0, min(len(txt)-3, len(importance))):
        sum_str += str((ord(txt[ii])-48) * importance[ii])
    checksum = sum([int(x) for x in sum_str])
    is_correct = len(txt) == 12 and txt[-3] == chr(10-checksum % 10+48)
    return is_correct

##############################################################################

from custom_exceptions.invalid_values import InvalidValues

def compare(str1, str2):
    """compare strings.

    params:
    str1 -- string version 1
    str2 -- string version 2
    the strings are a dot seperated integers.

    return:
    1 if str1 = str2
    0 if str1 > str1
    -1 if str1 < str2

    raise invalidValues exception if non integer value provided
    """
    try:
        str_v1 = int(''.join(str1.split('.')))
        str_v2 = int(''.join(str2.split('.')))
        if str_v2 == str_v1 and len(str1) == len(str2):
            return 1
        elif str_v1 > str_v2 or len(str_v1) > str(srt_v2):
            return 0
        else:
            return -1
    except Exception:
        raise InvalidValues(f'invalid params. can not compare {str1} to {str2}')

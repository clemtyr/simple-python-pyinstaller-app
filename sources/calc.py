'''
The 'calc' library contains the 'add2' function that takes 2 values and adds
them together. If either value is a string (or both of them are) 'add2' ensures
they are both strings, thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add2' function is a float, it must be done so
in quotes (i.e. as a string).
'''

# If 'value' is not an integer, convert it to a float and failing that, a string.
def conv(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

# The 'add2' function itself
def add2(arg1, arg2):
    # Convert 'arg1' and 'arg2' to their appropriate types
    arg1conv = conv(arg1)
    arg2conv = conv(arg2)
        # If either 'arg1' or 'arg2' is a string, ensure they're both strings.
    if isinstance(arg1conv, str) or isinstance(arg2conv, str):
        arg1conv = str(arg1conv)
        arg2conv = str(arg2conv)
    return arg1conv + arg2conv



def substract(arg1conv,arg2conv):
    result = ""
    if isinstance(arg2conv,str) and isinstance(arg1conv,str):
        arg1conv_cut = list(arg1conv)
        arg2conv_cut = list(arg2conv)
        for lettre in arg1conv_cut:
            if lettre in arg2conv_cut:
                all_index = []
                for i in range(0, len(arg1conv_cut)) : 
                    if arg1conv_cut[i] == lettre : 
                        all_index.append(i)
                minimum = min(all_index)
                arg1conv_cut.pop(minimum)
                arg1conv_cut.insert(minimum,"")
                arg2conv_cut.remove(lettre)
        for lettre_restante in arg1conv_cut:
            result += str(lettre_restante)
        return result
    if isinstance(arg2conv,str) == True:
        try:
            arg2conv = float(arg2conv)
        except ValueError:
            return arg1conv
    elif isinstance(arg1conv,str) == True:
        try:
            arg2conv = float(arg1conv)
        except ValueError:
            return arg1conv
    else:
        return round(arg1conv - arg2conv,15)
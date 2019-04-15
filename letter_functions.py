
# Kerning is defined by the space in between letters. Just one column
def kerning():
    return "0"

# The 'space' is defined as an extra column after a word usually
def load_space(row):
    return ""

# The A is defined as 
#  X
# X X
# XXX
# X X
def load_A(row):
    arr = ["010", "101", "111", "101", "101"]
    return arr[row]

# The B is defined as 
# XX
# X X
# XX
# X X
# XX
def load_B(row):
    arr = ["110", "101", "110", "101", "110"]
    return arr[row]

# The C is defined as 
#  XX
# X
# X
# X
#  XX
def load_C(row):
    arr = ["011", "100", "100", "100", "011"]
    return arr[row]

# The D is defined as 
#  XX
# X
# X
# X
#  XX
def load_D(row):
    arr = ["110", "101", "101", "101", "110"]
    return arr[row]

# The T is defined as 
# XXX
#  X
#  X
def load_T(row):
    arr = ["111", "010", "010", "010", "010"]
    return arr[row]
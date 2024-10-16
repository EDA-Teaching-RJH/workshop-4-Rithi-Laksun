# converting camel case input into snake case output

def main(name):

    return ''.join(['_'+i.lower() if i.isupper() 
                    else i for i in name]).lstrip('_')
name = input("What's your full name?")
print(name)

# using isupper() checks if input has upper cases 
# lstrip() removes whitespaces
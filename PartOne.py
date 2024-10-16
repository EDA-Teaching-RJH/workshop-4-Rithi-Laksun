
#converting camel case input into snake case output

def main(name):
    fullname = [name[0].lower()]
    for a in name[1:]:
        if a in ('ABCDEFGHIJKLMNOPQRSTUVWYZ') or a in (' '):
            fullname.append('_')  #puts underscore
            fullname.append(a.lower())  # lowers the cases
        else:
            fullname.append(a)
    return ''.join(fullname)
name = input("What's your full name?")
print(main(name))
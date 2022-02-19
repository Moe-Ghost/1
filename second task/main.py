import re

def msg_catcher(path):
    res = []
    
    try:
        f = open(path, 'r')
    except FileNotFoundError:
        return "incorrect filename"

    type = input("Enter msg type: ")
    if type not in ['I', 'W', 'E', 'A']:
        return 'incorrect msg type'
    if type == 'A':
        reg = r'[M][V][F][0-9]{5}[IWE]'
    else:
        reg = fr'[M][V][F][0-9]{{5}}{type}'
        reg = re.compile(reg)
    
    with open(path) as f:
        for line in f:
            if re.search(reg, line):
                msg = line.split()
                res.append({'msg' :msg[0],
                            'type': msg[0][-1],
                            'text': ' '.join(msg[1:])})
    return res
    

path = input('Enter path to the file: ')
print(msg_catcher(path))



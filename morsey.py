code = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', ' ': '/'
        }

decode = dict((v, k) for (k,v) in code.items())

def translate(morsecode):
    output = []
    splittext = morsecode.split()
    for morsel in splittext:
        output.append(decode[morsel])
    readout = ''.join(output)
    print readout

def morsify(englesh):
    codeout = []
    listing = list(englesh)
    for letter in listing:
        codeout.append(code[letter])
    morsecule = ' '.join(codeout)
    print morsecule


translate(".... . .-.. .-.. --- / .--. ..- -. .. - .- / - .... .. ... / .. ... / -- --- .-. ... . / -.-. --- -.. . / ..-. --- .-. / .... . .-.. .-.. --- / .--. ..- -. .. - .-")

morsify("HELLO PUNITA THIS IS MORSE CODE FOR HELLO PUNITA")

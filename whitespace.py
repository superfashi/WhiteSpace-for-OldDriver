# -*- encode: utf-8 -*-
# Author: SuperFashi
import binascii
import getopt
import sys
import os

Formore = 0

def writeFile(message, path):
    file = open(path, 'w')
    file.write(message)
    file.close()

def readFile(path):
    ret = ''
    file = open(path).readlines()
    for line in file:
        ret += line
    return ret

def readWS(white):
    ret = ''
    for char in white:
        if char == ' ':
            ret += '0'
        elif char == '	':
            ret += '1'
    return ret

def writeWS(bin):
    ret = ''
    for char in bin:
        if char == '0':
            ret += ' '
        elif char == '1':
            ret += '	'
        if Formore:
            ret += '+'
    return ret

def toBin(text):
    bits = bin(int(binascii.hexlify(text), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def toStr(bin):
    hex_string = '%x' % int(bin, 2)
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1))).decode('utf-8')

def usage():
    print('Watch the code yourself please!')
    exit()

if __name__ == '__main__':
    encrypt = 0
    decrypt = 0
    inputPath = 0
    outputPath = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'haedi:o:', ['help', 'advanced', 'encrypt', 'decrypt', 'input=', 'output='])
    except:
        usage()
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-e', '--encrypt'):
            encrypt = True
        elif opt in ('-d', '--decrypt'):
            decrypt = True
        elif opt in ('-i', '--input'):
            if os.path.exists(arg):
                inputPath = arg
            else:
                print('You have entered a wrong input path!')
                usage()
        elif opt in ('-o', '--output'):
            outputPath = arg
        elif opt in ('-a', '--advanced'):
            Formore = True
    if encrypt and decrypt:
        usage()
    if encrypt:
        if not inputPath:
            print('Please enter some secret code:')
            text = raw_input()
        else:
            text = readFile(inputPath)
        try:
            encryptedText = writeWS(toBin(text))
        except Exception, e:
            print('Encrypt success...fully failed due to ' + e + ' .')
            print('Try to check your input file!')
            usage()
        print('Encrypt finished!')
        if not outputPath:
            print('Please completely copy all the *invisible* things down below:')
            print(encryptedText)
        else:
            writeFile(encryptedText, outputPath)
            print('Please check your file to get some *invisible* things')
    elif decrypt:
        if not inputPath:
            print('Please enter some *blanks* here:')
            white = raw_input()
        else:
            white = readFile(inputPath)
        try:
            text = toStr(readWS(white))
        except Exception, e:
            print('Decrypt success...fully failed due to ' + e + ' .')
            print('Try to check your input file!')
            usage()
        if not outputPath:
            print('Here\'re some messages:')
            print(text)
        else:
            writeFile(text, outputPath)
            print('You can now see the original texts.')
    else:
        usage()
            

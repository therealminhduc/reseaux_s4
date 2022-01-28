#CRC = controle de redondance / cyclic redundancy check

def calc_crc(message, generateur, degre='0000'):
    #M x G = CRC
    message = message + degre 
    message = list(message)
    generateur = list(generateur)

    for i in range(len(message) - len(degre)):
        if message[i] == '1':
            for j in range(len(generateur)):
                message[i+j] = str((int(message[i+j]) + int(generateur[j])) %2)
    return ''.join(message[-len(degre):])

print('===============Test===============')
message = '1100100100'
generateur = '10011'
print "message a l'entree : ", message
print "generateur : ", generateur

degre = calc_crc(message,generateur)
print 'CRC :', degre

import pylablib
ID = 'Thorlabs.list_kinesis_devices()'
from pylablib.devices import Thorlabs
def translate(s):
    output=''
    for character in s:
        temp=''
        if character.isdigit():
            c=0
        elif ord(character)==32:
            output+='1111 '
        else:
            с=87
        character=ord(character)-c
        while character > 0:
            temp += str(character % 3)
            character //= 3
        output+=temp[::-1].rjust(4,'0')+' '
    print('encode: ',output)
    encodetogrd(output)

def encodetogrd(s):
    output = ''
    grader = {
        '0': 45,
        '1': 67.5,
        '2': 90,
        ' ':''
    }
    for character in s:
        output+=grader[character]
        move(grader[character])
    print('Angle array: ', output)

def move(grad):
    Thorlabs.list_kinesis_devices()
    stage = Thorlabs.KinesisMotor(ID)
    stage.move_to(grad)


def calibration():
    stage = Thorlabs.KinesisMotor(ID)
    stage.home(sync=True)

if __name__=="__main__":
    while True:
        translate(input('Enter your string:'))
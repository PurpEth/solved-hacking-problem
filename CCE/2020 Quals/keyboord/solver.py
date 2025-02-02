# ((usb.transfer_type == 0x01) && (frame.len == 72)) && !(usb.capdata == 00:00:00:00:00:00:00:00)
# export to keyboard.csv in WireShark
# cat keyboard.csv | cut -d "," -f 7 | cut -d "\"" -f 2 | grep -vE "Leftover Capture Data" > hexoutput.txt

mappings = { 0x04:"A",  0x05:"B",  0x06:"C", 0x07:"D", 0x08:"E", 0x09:"F", 0x0A:"G",  0x0B:"H", 0x0C:"I",  0x0D:"J", 0x0E:"K", 0x0F:"L", 0x10:"M", 0x11:"N",0x12:"O",  0x13:"P", 0x14:"Q", 0x15:"R", 0x16:"S", 0x17:"T", 0x18:"U",0x19:"V", 0x1A:"W", 0x1B:"X", 0x1C:"Y", 0x1D:"Z", 0x1E:"1", 0x1F:"2", 0x20:"3", 0x21:"4", 0x22:"5",  0x23:"6", 0x24:"7", 0x25:"8", 0x26:"9", 0x27:"0", 0x28:"\n", 0x2a:"[DEL]",  0X2B:"    ", 0x2C:" ",  0x2D:"-", 0x2E:"=", 0x2F:"[",  0x30:"]",  0x31:"\\", 0x32:"~", 0x33:";",  0x34:"'", 0x36:",",  0x37:"." }

myKeys = open("hexoutput.txt")

log = ""

for line in myKeys:
    byteArray = bytearray.fromhex(line.strip())
    
    byte = byteArray[2]
    if byte == 0:
        continue

    keyVal = int(byte)
    if keyVal in mappings:
        print(mappings[keyVal])
        log += mappings[keyVal]
    else:
        print("No map found for this value: " + str(keyVal))

print(log)

arr = [0x63, 0x62, 0x67, 0x31, 0x34, 0x37, 0x36, 0x7c, 0x63, 0x6c, 0x73, 0x69, 0x63, 0x62, 0x7c, 0x6b, 0x4f, 0x61, 0x73, 0x70, 0x7f, 0x70, 0x62, 0x48, 0x7d, 0x78, 0x69, 0x62, 0x43, 0x42, 0x41, 0x46, 0x45, 0x40, 0x4a, 0x02, 0x59]

flag = ''
for i in range(37):
    flag += chr(arr[i] ^ i)
print(flag)

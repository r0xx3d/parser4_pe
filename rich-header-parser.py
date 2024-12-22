import textwrap

def xor(data, key):
    return bytearray( ((data[i]^key[i%len(key)]) for i in range(0,len(data))))

def reverse_endiannes(data):
    tmp = [data[i:i+8] for i in range(0,len(data),8)]

    for i in range(len(tmp)):
        tmp[i] = "".join(reversed([tmp[i][x:x+2] for x in range(0,len(tmp[i]),2)]))
        return "".join(tmp)

richdata = input("Enter hex data from rich header: ")
data = bytearray.fromhex(data)
richkey = input("Enter key for data: ")
key = bytearray.fromhex(richkey)

rich_header = (xor(data,key)).hex()
rich_header = textwrap.wrap(rich_header,16)

for i in range(2,len(rich_header)):
    tmp = textwrap.wrap(rich_header[i],8)
    f1 = reverse_endiannes(tmp[0])
    f2 = reverse_endiannes(tmp[1])
    print("{} {} : {}.{}.{}".format(f1,f2,str(int(f1[0:4],16)), str(int(f2,16)) ))
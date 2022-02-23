
mapowanie_d = {
    '1' : 'a',
    '2' : 'b',
    '3' : 'c',
    '4' : 'd',
    '5' : 'e',
}

mapowanie_e = {
    'a' : '1',
    'b' : '01',
    'c' : '001',
    'd' : '0001',
    'e' : '00001',
}

# i = 0
# while i < len(str):
#     if i+n < len(str):
#         chunks.append(str[i:i+n])
#     else:
#         chunks.append(str[i:len(str)])
#     i += n
# print(chunks)

    # chunks = ['{s:08}'.format(s=bits_str[i : i + n]) for i in range(0, len(bits_str), n)]


def pars_encoded_text(text):
    lines = text.split(b'\n')
    number_of_garbage_bits = int(lines[0].decode('utf-8'))
    print(type(number_of_garbage_bits), number_of_garbage_bits)

    print(lines[1])
    values = []
    for c in lines[1]:
        print(f"{c:08b}")
        values.append(f"{c:08b}")
    if number_of_garbage_bits and len(values):
        values[-1] = values[-1][0:-number_of_garbage_bits]
    return ''.join(values)


def get_bits(bits_str:str):
    byte_lenght = 8
    chunks = [bits_str[i : i + byte_lenght]for i in range(0, len(bits_str), byte_lenght)]

    chunks = []
    for i in range(0, len(bits_str), byte_lenght):
        sub_str = bits_str[i : i + byte_lenght]
        chunks.append(sub_str)
    
    if len(chunks[-1]) < byte_lenght:
        garbage_bits = byte_lenght - len(chunks[-1])
        chunks[-1] = chunks[-1] + '0' * garbage_bits
    return chunks, garbage_bits


def bits_to_bytes(bytes_list):
    return bytearray([int(byte, 2) for byte in bytes_list])

def save_to_file(file_name, output_bytes, number_of_garbage_bits):
    with open(file_name, 'wb') as out_f:
        out_f.write(bytes(str(number_of_garbage_bits), 'utf-8'))
        out_f.write(b'\n')
        out_f.write(output_bytes)

def load_from_file(file_name):
    with open(file_name, 'rb') as in_f:
        print("Reading data from : ", file_name)
        data = in_f.read()
        return data



def zadanie1():
    x = '111111110000000011'
    bits, garbage_bits = get_bits(x)
    print(garbage_bits)
    print(bits)
    output_bytes = bits_to_bytes(bits)
    print("output_bytes", output_bytes)
    zadanie_file = 'zadanie_output'
    save_to_file(zadanie_file, output_bytes, garbage_bits)
    loaded_data = load_from_file(zadanie_file)
    parsed_data = pars_encoded_text(loaded_data)
    print(parsed_data)

def main():
    x = '111111110000000011'
    n = 8

    chunks = ['{s:08}'.format(s=x[i : i + n]) for i in range(0, len(x), n)]

    print(chunks)
    for e in chunks:
        print(int(e, 2))

    sotred_codes = bytearray([int(e, 2) for e in chunks])
    print(sotred_codes)

    with open("spr.txt.bin", 'wb') as out_f:
        out_f.write(b'Witam\n')
        out_f.write(sotred_codes)

    with open("spr.txt.bin", 'rb') as in_f:
        content = in_f.read()
        lines = content.split(b'\n')
        print(lines)
        pars_encoded_text(lines[1])
# main()
zadanie1()

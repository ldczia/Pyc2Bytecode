import marshal
import dis

def disassemble_pyc_file(pyc_file_path):
    with open(pyc_file_path, 'rb') as f:
        f.seek(16)  
        code = marshal.load(f)
    
    with open('bytecode.txt', 'w') as out_file:
        dis.dis(code, file=out_file)

pyc_file_path = input("pyc dosyasının adını gir : ")
disassemble_pyc_file(pyc_file_path)
print("bytecode dosya dizinine çıkartılmıştır. 'bytecode.txt' ")
input('Devam etmek için bir tuşa basın...')
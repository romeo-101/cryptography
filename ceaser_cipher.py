d={'a':1,'b':2, 'c':3,'d':4, 'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
def encrypt(key):
    t=input("Enter the plain text in small : ").lower()
    result=[]
    for i in t:
        x=d[i]
        y=x + key
        if y > 26 :
            y=y-26
        c=[k for k, v in d.items() if v == y]
        if c:
            result.append(c[0])
    cipher_text = ''.join(result)
    print(f"Cipher text : {cipher_text}")

def decrypt(key):
    result=[]
    for i in c_text:
        x = d[i]
        y=x-key
        if y < 1:
            y=y+26
        c=[k for k, v in d.items() if v ==y]
        if c:
            result.append(c[0])
    plain_text = ''.join(result)
    print(f"Plain text : {plain_text} for key : {key}")
opt = int(input("Encrpyt=1 or Decrypt=2 :"))
key=input("Enter the key : (If you don't know the key, Enter no) :")
if opt == 1 :
    encrypt(int(key))
elif opt == 2 :
    c_text=input("Enter cipher text :").lower()
    if key == "no" :
        for i in range(1,27):
            decrypt(i)
    elif key.isdigit():
        decrypt(int(key))
    else:
        print("INVALID OPTION")
else:
    print("INVALID OPTION")

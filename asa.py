a = 10 
b = 2
c = a%b
print(c)
print(type(a))
print(type(b))
print(type(c))

testar = False
print( type(testar))
if (not testar):
    print("teste desativado")
    
else: 
    if( c == 1  ):
       print("impar")
    elif( c == 0):
       print("par")

    elif( c == -1):
       print("negative")
    else: 
       print("error")
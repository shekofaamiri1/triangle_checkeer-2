x=int(input("Enter x:"))
y=int(input("Enter y:"))
z=int(input("Enter z"))
if x <y+z and y <x+z and z <x+y:
    
    print("it can be triangle!")
if x==y and y==z and z==x:
        
    print("motasavi azla.")
if x==y or y==z or z==x:
        
    print("motasavi asaqian.")
     
    if x!=y or y!=z or z!=x:
        
        print("mokhtalive azla.")
        
        
v1 = "first string"        
v2 = "second string"                
v3= v1
v1=v2
v2=v3   
print(v1)
print(v2)

#smart move 

v1 = "on srting"
v2 = "second string"
v1, v2 = v2, v1
print(v1)
print(v2)
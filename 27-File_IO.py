
# If we don't pass any mode
# 'r' mode is the default mode

# Modes 

# 'r'-- Read  (rt)
# 'w'-- Write  (wt)
# 'a'-- Append  (at)
# 'c'  -- create (ct)

# Apart from modes we also need
# to specify how we want to handle the file

# 't'  text 
# 'b'  binary  (rb) (wb)  (ab)  (cb) [Images pdfs etc]


# Read a text file

# f=open('test.txt','r')

# text=f.read()


# print(text)
# f.close()


# Writing to a file

# f=open('test.txt','w')

# f.write("Hello World !")

# f.close()


# Append in a file

# f=open('test.txt','a')

# f.write("Hello")

# f.close()



# readline() 
# Reads single line from file
# If we want to read multile lines use loop

# Print marks of 3 students in 3 subjects
# 56,45,67
# 12,34,63
# 13,64,23
# f=open('test.txt','r')

# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         break
#     m1=line.split(',')[0]
#     m2=line.split(',')[1]
#     m3=line.split(',')[2]
#     print(f"Marks of student {i} in M1 is {m1} in M2 is {m2} in M3 is {m3}")


# writelins() 
# Write single line from file

# f=open('test.txt','w')

# lines=['line1\n','line2\n','line3\n']
# f.writelines(lines)

# We can also use 

# lines=['line1','line2','line3']
# for line in lines:
#     f.write(line+"\n")

# f.close()




f=open("test.txt",'r')

i=0
while True:
    line=f.readline()
    if(i==0):
        i=i+1
        continue

    dataArr=line.split(",")

    if(len(dataArr)>=3):
        prod=line.split(",")[0]
        region=line.split(",")[1]
        sales=line.split(",")[2]
        print("Product Name: ",prod)
        print("Region Name: ",region)
        print("Sales : ",sales)
    if not line:
        break
    i=i+1

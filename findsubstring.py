string="1212121121"
substring="121"
x=string.find(substring)
count=0


for i in range(x,len(string)-len(substring)+1):
    if string[i:i+len(substring)]==substring:
        count=count+1

print(count)

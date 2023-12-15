with open('countries.txt', 'r') as first:
        content1 = first.read()


with open('hello.txt', 'r') as second:
        content2 = second.read()


with open('allproducts.txt', 'w') as output:
        output.write(content1 + "\n")
        output.write(content2 + "\n")
        
        
        
        
        

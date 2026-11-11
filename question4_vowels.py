str=input("Enter a Name: ");
count=0;
for i in str:
    if i in 'aeiouAEIOU':
        count = count + 1;
print("Number of vowels in the given name is: ", count);
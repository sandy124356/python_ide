def palindrome(input):
    length = len(input)
    palindromes = []
    for x in range(2,length+1):
        min = 0
        high = x
        while high < length+1:
            testString = input[min:high]
            if(len(testString)%2==0):
                midPoint = len(testString)//2
                if( testString[0:midPoint] == testString[midPoint:][::-1] ):
                    palindromes.append(testString)
            else:
                midPoint = len(testString)//2
                if(testString[0:midPoint] == testString[(midPoint+1):][::-1]):
                    palindromes.append(testString)
            min = min+1
            high = high + 1
    return palindromes

print(palindrome("ninanin"))
print(palindrome("nnn"))
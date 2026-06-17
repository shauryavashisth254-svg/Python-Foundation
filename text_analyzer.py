#Mini Project after Module 4
#Challenge
'''
Input: any sentence from the user

Output:
1. Word count
2. Character count (with spaces)
3. Character count (without spaces)
4. Uppercase version
5. Title case version
6. Reversed sentence (word by word)
7. Palindrome check (ignore spaces + case)
8. Does it start with a vowel? (startswith)
9. Does it contain the word 'python'? (in operator)
'''

statement = (input("Enter any sentence you like: "))
statement_0 = statement.split()
print(statement_0)
print(len(statement_0))                                  #1
print(len(statement))                                    #2
statement_1 = statement.replace(" ", "")
print(statement_1)
print(len(statement_1))                                  #3
print(statement.upper())                                 #4
print(statement.title())                                 #5
print(statement[::-1])                                   #This is character-by-character reverse
stat = statement.split()        #This splits the words of statement in list of words
reversed_stat = stat[::-1]      #This reverses the list
glued_stat = " ".join(reversed_stat) #This join words back with spaces, thus converting the list back into a string statement.
print(glued_stat)                                        #6 : This is word-by-word reverse
statement_2 = statement_1.lower()
statement_3 = statement_2[::-1]
print(statement_2 == statement_3)                        #7
print(statement_2.startswith(('a', 'e', 'i', 'o', 'u'))) #8
print("python" in statement_2)                           #9
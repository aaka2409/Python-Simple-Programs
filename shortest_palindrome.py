#Shortest Palindrome
#You are given a string s. You can convert s to a palindrome by adding characters in front of it.
#Print the shortest palindrome you can find by performing this transformation.
s = input("Input string: ")
rev = s[::-1]
long = s + "#" + rev
temp = [0 for i in long]
# i is suffix boundary and j is prefix boundary in KMP table
for i in range(1, len(long)):
  j = temp[i-1]
  while(j > 0 and long[i] != long[j]):
    j = temp[j-1]
    if(long[i] == long[j]):
      temp[i] = j+1
print("Shortest palindrome:", rev[0: len(s) - temp[len(long) - 1]] + s)
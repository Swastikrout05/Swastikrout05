class Solution:
   def dictionary(self, words):
      s = "".join(word[0].upper() + word[1:].lower() for word in
words)
      return s[0].lower() + s[1:]
ob = Solution()
words = ["Hi","Hello","HelloWorld", "HiWorld", "HelloWorldWideWeb", "HelloWWW"]
print(ob.dictionary(words))
def longestLength(a):
    max1 = len(a[0])
    temp = a[0]
 
    # for loop to traverse the list
    for i in a:
        if(len(i) > max1):
 
            max1 = len(i)
            temp = i
 
    print("The word with the longest length is:", temp,
          " and length is ", max1)
 
 
# Driver Program
a = ["Hi","Hello","HelloWorld", "HiWorld", "HelloWorldWideWeb", "HelloWWW"]
longestLength(a)
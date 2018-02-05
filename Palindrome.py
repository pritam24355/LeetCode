class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list1=[]
        
        
        if(x==0):
            return True
        elif(x>0):
            
            list1.append(str(x))
            list1=list1[0][::-1]
            
            list1=int(list1)
            
            return x==list1
            
        else:
            return False
           
            
        
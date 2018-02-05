class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        string1=str(x)
        list1=[]
        list3=[]
        list1.append(string1)
        print("hey")
        print(list1)
        if list1[0][0]=="-":
            print("in here")
            list2=list1[0][1:]
            print(list2)
            list3=list2[::-1]
            print(list3)
            if list3[0][0]=="0":
                list3=list3[1:]
            list4=int(list3)
            list4=list4*-1
            
            if -2**32<=list4<=2**32:
                return list4
            else:
                return 0
    
        else:
            print("here here")
            list2=list1[0][::-1]
            print("hey look",list2)
            if list2[0][0]=="0":
                list2=list2[1:]
            list3=int(list2)
            
            
            if -2**32<=list3<=2**32:
                return list3
            else:
                return 0
    
    
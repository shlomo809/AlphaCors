def main():
    my_num=[5,6,7,14,152,60693]
    num =0
    for i in range(100): 
        num = num + i + 1
        if(i < 6 ):
            
            d = IsPrimeNumber(my_num[i])
            print(d)
            
        
        
def IsPrimeNumber(x):
      
    
    
       
    
        for j in range(2,x-1):
           
            if(x % j == 0):
               
                return False
            return True   
        
            
           
    


if (__name__ == "__main__"):
    main()

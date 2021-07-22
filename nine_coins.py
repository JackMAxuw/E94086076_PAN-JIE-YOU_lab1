#!/usr/bin/env python
# coding: utf-8

# In[21]:


class Nine_Coins:
    
    # define initial constructor
    def __init__(self, num):
        self.num = int(num)
        
        # use "format" to convert num to binary and convert it to string
        # also give it the length: 9  
        self.binary = str(format(self.num, "b")).zfill(9)
        
    # define repersentative while calling 'object_name' 
    def __repr__(self):
        
        # convert '1' and '0' to 'T' and 'H'
        str_c = str()
        i = 0
        for i in range(0, 9):
            if self.binary[i] == '0':
                str_c = str_c + 'H'
            else:
                str_c = str_c + 'T'
        
        return f"Nine_Coins: {str_c}"
        
    # define toss function to flip the coins
    def toss(self):
        import random
        self.num = random.randint(0, 512)
        self.binary = str(format(self.num, "b")).zfill(9)
    
    # define __str__ while calling "print(object_name)"
    def __str__(self):
        return f"binary: {self.binary} and decimal: {self.num}"


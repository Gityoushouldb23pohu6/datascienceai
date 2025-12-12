# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 22:06:30 2025

@author: arnav
"""



'''

data preprocessing : 
    import the data 
    clean the data 
    split into training testing 
    
    
    modelling : 
        build the model 
        train the model 
        make predictions 
        
        
    evaluation : 
        calculation of performance metrics 
        make a verdict 
        


///////////////

separating a part of the data before we do anything (20 percent test set and 80 percent is our train test)

the test set will have no relation to the built model and will just be used to make predictions 

we make the predictions of the prices using the model and the test set .


However as we come to know the actual prices we can make a comparision between the predicted value and the exsisting value .
This will determine the performance of the model 




//////////////

feature scaling :
    
    feature scaling is always applied to columns 
    
    types of feature scaling : 
        
        normalisation , standardisation 
        
        
  1) normalisation : 
     
   -we end up with value between 0 and 1 .
   - we subtract all the values with the minimum value available  .
   
  2) standardisation : 
   - we subtract by mean and divide by the standard deviation 
    
   - the values we get are between -3 and 3 .
   
   
   --> 
   
     why we need feature scaling ? 
     -> if we have three people and we want to group the middle person with one of the other two ... for this we need to compare the characteristics of the middle one with the other two .
     comparision of characteristics will be easier if we have some standard  value -> thus feature scaling 
   
   
   //////////
   
   
   
   
   
    
'''










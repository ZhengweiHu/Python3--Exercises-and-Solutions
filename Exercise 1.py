#------------Exercise 1-----------------#
'''
(Remove mutiple items from a given list at one time)

The fruit supplier offers:
'apple','banana','pear','pineapple','cherry','watermelon','strawberry','grape', and 'Mango' 
But the fruit shop does not want to purchase: 'cherry', 'pear' and 'Mango'

Hints:
list.del and list.remove could only remove one item, we here 
consider for(...in...if...) method to filter unconcerned items 

'''

#------------Solution 1-----------------#

Fruit = ['apple','banana','pear','pineapple','cherry','watermelon','strawberry','grape','Mango']
Fruit_unlike = ['cherry', 'pear', 'Mango']
Fruit_purchase = [i for i in Fruit if i not in Fruit_unlike]
print (Fruit_purchase)
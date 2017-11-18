# Tiffi Westcott
# 10% - 20% - 30% Sale
#I'm so proud! I love problem solving :)

import random

userInput =  raw_input('What does the original item cost?: $')
orig = float(userInput)

randpercent = random.randint(1,3)
percent = float(randpercent)

if randpercent == 1:
    print 'Congrats! Discount Percentage:'
    print 'Original Price: $', userInput 
    one = float(.1)
    tax_off1 = orig * one
    new_price1 = orig - tax_off1
    print "Total savings (amount off): $", tax_off1
    print "Total, new price: $", new_price1
    print 'You save: $', tax_off1
    print "Compared to your old price of $", userInput

elif randpercent == 2:
    print 'Discount percentage:'
    print 'Original Price: $', userInput 
    two = float(.2)
    tax_off2 = orig * two
    new_price2 = orig - tax_off2
    print "Total savings (amount off): $", tax_off2
    print "Total, new price: $", new_price2
    print 'You save: $', tax_off2
    print "Compared to your old price of $", userInput

elif randpercent == 3:
    print 'Discount percentage: 30%'
    print 'Original Price: $', userInput 
    three = float(.3)
    tax_off3 = orig * three
    new_price3 = orig - tax_off3
    print "Total savings (amount off): $", tax_off3
    print "Total, new price: $", new_price3
    print "You save: $", tax_off3
    print "Compared to your old price of $", userInput

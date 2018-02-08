cart = {"Small Coffee": 0, "Medium Coffee" : 0, "Mondo Coffee" : 0, "Chocolate Chip Muffin" : 0,"Pot of Tea": 0, "Hot Chocolate" : 0, "Water": 0, "Organic Water": 0}
prices = {"Small Coffee": 1.25, "Medium Coffee": 1.49, "Mondo Coffee": 1.99, "Chocolate Chip Muffin": 2.74, "Pot of Tea": 1.99, "Hot Chocolate": 1.49, "Water": 1.99, "Organic Water": 3.99}
conversion = {1: "Small Coffee", 2: "Medium Coffee", 3: "Mondo Coffee", 4: "Chocolate Chip Muffin", 5: "Pot of Tea", 6: "Hot Chocolate", 7: "Water", 8: "Organic Water"}
while True:
    print ("---------------------------------------------------")
    print ("The Java Shoppe Menu:")
    print ("\t1.)Brewed Coffee\n\t2.)Chocolate Chip Muffin\n\t3.)Pot of Tea\n\t4.)Hot Chocolate\n\t5.)Water\n\t6.)Organic Water\n\t7.)View Prices/Discounts\n\t8.)Check out/Print Receipt")
    prompt = int(input("What item number would you like to choose? "))
    if prompt == 1:
        print ("What size coffee would you like?\n\t1.)Small\n\t2.)Medium\n\t3.)Mondo")
        size = int(input("Enter Size: "))
        quantity = int(input("how many would you like?"))
        if size == 2:
            prompt = 2
        elif size == 3:
            prompt = 3
    elif prompt > 1 and prompt < 7:
        prompt = prompt + 2
        quantity = int(input("how many would you like?"))
    elif prompt == 7:
        for item in prices:
            print (item)
        print ("Discount: buy a Mondo Coffee and a Chocolate Chip Muffin and get $1.75 off! \nBuy an Organic Water and get a free Chemistry Textbook! (limit 1 per person)")
    elif prompt == 8:
        break
    cart[conversion[prompt]] = cart[conversion[prompt]] + quantity
i = 0
totalPrice = 0
numberOfDiscounts = 0
while i < 8:
    i = i + 1
    totalPrice += cart[conversion[i]] * prices[conversion[i]]
if cart["Mondo Coffee"] > 1 and cart["Chocolate Chip Muffin"] > 1:
    if cart["Mondo Coffee"] > cart["Chocolate Chip Muffin"]:
        totalPrice = totalPrice - (1.75 * cart["Chocolate Chip Muffin"])
        numberOfDiscounts = cart["Chocolate Chip Muffin"]
    elif cart["Mondo Coffee"] < cart["Chocolate Chip Muffin"]:
        totalPrice = totalPrice - (1.75 * cart["Mondo Coffee"])
        numberOfDiscounts = cart["Mondo Coffee"]
    else:
        totalPrice = totalPrice - (1.75 * cart["Mondo Coffee"])
        numberOfDiscounts = cart["Mondo Coffee"]
totalTax = totalPrice * 0.08
finalPrice = totalPrice + totalTax
print ("Your Bill:")
j = 0
while j < 8:
    j = j + 1
    if cart[conversion[j]] > 0:
        print("\t", cart[conversion[j]], conversion[j],"$", prices[conversion[j]] * cart[conversion[j]])
print ("-------------------------------------------------------\n\t", numberOfDiscounts, "Mondo Muffin Discount(s)", numberOfDiscounts * 1.75)
if cart[conversion[8]] > 0:
    print ("\t1 Free Chemistry Textbook", "0.00" )
print ("-------------------------------------------------------")
print ("\tSubtotal: ", totalPrice)
print ("8% Java Tax: ", totalTax)
print ("Total: ", finalPrice)
change = int(input("How much are you paying? "))
totalChange = finalPrice - change
print ("Your change is: ", abs(totalChange))

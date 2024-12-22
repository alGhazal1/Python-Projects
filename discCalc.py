price = float(input('Enter the item price:'))
discount_percent = float(input('Enter the discount:'))


def calculate_discount():

    if discount_percent >= 20:
        discounted_amnt = price * (discount_percent/100)
        final_price = price - discounted_amnt
        return final_price
    else:
        return price


final_price = calculate_discount()

if final_price != price:
    print(f"The final price after discount is: {final_price}")
else:
    print('No discount given for the item')


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = (discount_percent / 100) * price
        new_price = price - discount
        return new_price
    else:
        return price

def main():
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percentage)
    
    if final_price == original_price:
        print("No discount applied. Final price: ", final_price)
    else:
        print("Final price after applying", discount_percentage, "% discount: ", final_price)

if __name__ == "__main__":
    main()

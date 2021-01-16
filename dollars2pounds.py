print("How much in Dollars are you wishing to convert?")
dollars = input()
pounds = float(dollars)/1.36793
pounds = round(pounds,2)
print(f"This comes to roughly £{pounds}")
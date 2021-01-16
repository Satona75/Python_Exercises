print("How much in pounds do you wish to convert into US Dollars?")
pounds = input()
dollars = float(pounds)*1.36
dollars = round(dollars,2)
print(f"This works out to be ${dollars}")
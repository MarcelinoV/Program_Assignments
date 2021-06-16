# declare dictionary of foods

# STEP 2
food_prices = {"Chicken": 1.59, 
               'Beef': 2,
               'Pork': 3,
               'Tofu': 4}

# STEP 3
video_games = {'Halo': 'Shooter',
               'FIFA 21': 'Sport',
               'It Takes Two': 'Adventure',
               'Outlast II': 'Horror'}

# EXAMPLE STUFF
#print("Halo is a", video_games['Halo'])

# STEP 4
chicken = food_prices['Chicken']
beef = food_prices['Beef']
pork = food_prices['Pork']
tofu = food_prices['Tofu']


print('The price of chicken is', '$'+str(chicken))
print('The price of beef is', beef)
print('The price of pork is', pork)
print('The price of tofu is', tofu)


# STEP 6
print('The price of chicken before price increase is', '$'+str(chicken))

food_prices["Chicken"] = 3
chicken = food_prices['Chicken']

print('The price of chicken after the price increase is', '$'+str(chicken))



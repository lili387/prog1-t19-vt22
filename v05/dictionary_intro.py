victor_name = "Victor"
victor_age = 23
victor_length = 195

victor = {} # en dictionary
victor["namn"] = victor_name
victor["ålder"] = victor_age
victor["längd"] = victor_length

print(victor) # skriver ut alla nycklar/värden i victor

linus_name = "Linus"
linus_age = 40
linus_length = 184

linus = {} # en till dictionary, samma nycklar
linus["namn"] = linus_name
linus["längd"] = linus_length
linus["ålder"] = linus_age

# vi kan indexera med "ålder" för att få ut victors och linus ålder
print(victor["ålder"] + linus["ålder"]) 
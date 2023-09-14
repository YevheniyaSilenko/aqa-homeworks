
casino_blacklist = {"John Kuper", "Alice Smith", "Bob Dylan", "Eve Polna"}
poker_blacklist = {"Alice Smith", "Bob Dylan", "Chris Lee", "Eve Polna"}
alcohol_blacklist = {"John Kuper", "Chris Lee", "Eve Polna", "Frank Sinatra"}

common_blacklist = casino_blacklist & poker_blacklist & alcohol_blacklist

# Print the names that are on all three blacklists
print("People on all three blacklists:")
for name in common_blacklist:
    print(name)


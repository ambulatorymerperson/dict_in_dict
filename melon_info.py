"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices


# def print_melon(name, seedless, price):
#     """Print each melon."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print "{}s {} seeds and are ${:.2f}".format(name, have_or_have_not, price)

melon_dict = {}
for i in melon_names:
    melon_dict[melon_names[i]] = {'melon seedlessness': melon_seedlessness[i], 'melon price':
    melon_prices[i]}

print melon_dict

for name in melon_dict:
    print "{}".format(name)
    for key, value in melon_dict[name].items():
        print "   {}: {}".format(key, value)
    
    print "   flesh color: {}".format(melon_dict[name].get('flesh color'))
    print "   weight: {}".format(melon_dict[name].get('weight'))
    print "   rind: {}\n.".format(melon_dict[name].get('rind'))



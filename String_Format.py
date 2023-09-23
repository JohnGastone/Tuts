# String Formatting allows us to manipulate parts of a string per some particular needs.

# In python we use format() method to apply String formatting

# String Formatting in ACTION

text = "Bei ya maharage ni shillingi 5000 "  # A full string

crop = "Maharage"
currency = "shillingi za kitanzania"
price = 5000
text_formatted = "Bei ya {} ni {} {}"

print(text_formatted.format(crop, currency, price))

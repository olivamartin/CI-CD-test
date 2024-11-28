class Dictionary:
    #Create an empty dictionary
    def __init__(self):
        self.values = {}
    
    #Assign the entry with the value to the dictionary
    def newentry(self, key, value):
        self.values[key] = value

    #Look for the key and return the value if exists
    def look(self, key):
        if key in self.values.keys():
            return self.values[key]
        else:
            return "Can't find entry for " + key

def get_total_costs(costs_dict, items, tax):
    #Verify instances of the input parameters 
    if not isinstance(costs_dict, dict):
            raise ValueError("First argument must be a dictionary.")
    if not isinstance(items, list):
            raise ValueError("Second argument must be a list.")
    if not isinstance(tax, (int, float)):
            raise ValueError("Tax must be a number.")
    
    try:
        acum = 0
        #Get the value of every item or 0 if it's not in costs
        for item in items:
            acum += costs_dict.get(item, 0)
        return round(acum * (1 + tax),2)
    except Exception as e:
        raise RuntimeError(f"Error calculating total costs: {e}")

def new_word(words):
    formed_word = ''
        # Iterate over each word in the list 'words' and its index
    for i, word in enumerate(words):
        # Ensure the word is long enough to access the character at position 'i'
        formed_word += word[i]
    return formed_word




        
import unittest
from tasks import Dictionary, get_total_costs, new_word

class TestDictionary(unittest.TestCase):
    # Set up initial state with a Dictionary instance and a sample entry
    def setUp(self):
        self.d = Dictionary()
        self.d.newentry('Apple', 'A fruit that grows on trees')

    # Test case for adding a new entry and ensuring it can be looked up
    def test_newentry(self):
        self.d.newentry('Grape', 'A small, round fruit used to make wine')
        # Ensure that the 'Grape' entry is correctly added and can be looked up
        self.assertEqual(self.d.look('Grape'),'A small, round fruit used to make wine')

    # Test case for looking up an existing entry
    def test_lookup_existing(self):
         # Ensure that the 'Apple' entry returns the correct definition
        self.assertEqual(self.d.look('Apple'),'A fruit that grows on trees')

    # Test case for looking up a non-existent entry
    def test_lookup_notexistent(self):
        # Ensure that looking up a non-existent entry returns the appropriate message
        self.assertEqual(self.d.look('Banana'),"Can't find entry for Banana")

class TestGetTotalCosts(unittest.TestCase):  
    # Set up initial state with a sample costs dictionary
    def setUp(self):
        self.costs = {'socks': 5, 'shoes': 60, 'sweater': 30}

    # Test case for calculating total costs with valid items and tax
    def test_valid_items_with_tax(self):
        # Ensure the total cost for 'socks' and 'shoes' with a 9% tax is calculated correctly
        self.assertEqual(get_total_costs(self.costs, ['socks', 'shoes'], 0.09), 70.85)

    # Test case for calculating total costs with valid items and no tax
    def test_valid_items_no_tax(self):
        # Ensure the total cost for 'socks' and 'shoes' with no tax is calculated correctly
        self.assertEqual(get_total_costs(self.costs, ['socks', 'shoes'], 0), 65.00)

    # Test case for calculating total cost when the items list is empty
    def test_empty_items(self):
        # Ensure the total cost is zero when no items are provided
        self.assertEqual(get_total_costs(self.costs, [], 0.09), 0.00)

    # Test case for calculating total cost with invalid items (items not in the costs dictionary)
    def test_invalid_items(self):
        # Ensure the total cost is zero when items don't exist in the dictionary
        self.assertEqual(get_total_costs(self.costs, ['hat', 'scarf'], 0.09), 0.00)

    # Test case for calculating total cost with a mix of valid and invalid items
    def test_mixed_valid_and_invalid_items(self):
        # Ensure that valid items ('socks') are included in the total, and invalid items are ignored
        self.assertEqual(get_total_costs(self.costs, ['socks', 'hat'], 0.09), 5.45)

    # Test case for calculating total cost with negative tax
    def test_negative_tax(self):
        # Ensure the total cost is correctly calculated with a negative tax rate
        self.assertEqual(get_total_costs(self.costs, ['socks', 'shoes'], -0.1), 58.50)

    # Test case for calculating total cost when one of the items has zero cost
    def test_zero_cost_items(self):
        self.costs['hat'] = 0
        # Ensure the cost of the zero-cost item ('hat') does not affect the total cost
        self.assertEqual(get_total_costs(self.costs, ['socks', 'hat'], 0.09), 5.45)

    # Test case for invalid input: costs_dict is not a dictionary
    def test_invalid_input_not_a_dict(self):
        with self.assertRaises(ValueError):
            # Ensure that passing a non-dictionary as the first argument raises a ValueError
            get_total_costs("not_a_dict", ["socks"], 0.09)
    
    # Test case for invalid input: items is not a list
    def test_invalid_input_not_a_list(self):
        with self.assertRaises(ValueError):
            # Ensure that passing a non-list as the second argument raises a ValueError
            get_total_costs({}, "not_a_list", 0.09)
    
    # Test case for invalid input: tax is not a number
    def test_invalid_input_not_a_number(self):
        with self.assertRaises(ValueError):
         # Ensure that passing a non-numeric tax raises a ValueError
         get_total_costs({}, [], "not_a_number")

class TestNewWord(unittest.TestCase):  
    # Test case for valid input: first character of each word is taken to form the new word
    def test_valid_case_1(self):
        words = ["yodas", "best", "has"]
        # First character of "yodas" (y), second character of "best" (e), third character of "has" (s)
        self.assertEqual(new_word(words), "yes")
    
     # Test case for valid input: first character of each word is taken to form the new word
    def test_valid_case_2(self):
        words = ["apple", "banana", "cherry"]
        # First character of "apple" (a), second character of "banana" (a), third character of "cherry" (e)
        self.assertEqual(new_word(words), "aae")
    
    # Test case for valid input: first character of each word is taken to form the new word
    def test_valid_case_3(self):
        words = ["cat", "dog", "elephant"]
        # First character of "cat" (c), second character of "dog" (o), third character of "elephant" (e)
        self.assertEqual(new_word(words), "coe")
    
    # Test case for empty input: empty list should return an empty string
    def test_valid_case_with_empty_array(self):
        words = []
        self.assertEqual(new_word(words), "")  # Empty list should return an empty string
    
    # Test case for a single word: only the first character of the word should be returned
    def test_single_word_case(self):
        words = ["keyboard"]
        # First character of "keyboard" (k)
        self.assertEqual(new_word(words), "k")

if __name__ == '__main__':
    unittest.main()

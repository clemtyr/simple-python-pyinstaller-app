import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    Test the add function from the calc library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = calc.add2(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = calc.add2('10.5', 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string
        """
        result = calc.add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string)
        """
        result = calc.add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_string_and_number(self):
        """
        Test the addition of a string and a float returns them as one
        concatenated string (in which the float is converted to a string)
        """
        result = calc.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')


class Testsubstract(unittest.TestCase):
    def test_substract_integers(self):
        result = calc.substract(5,3)
        self.assertEqual(result,5-3)

    def test_substract_integers_from_string_should_unchanged_string(self):
        result = calc.substract("acda",48)
        self.assertEqual(result,"acda")

    def test_substract_string_contain_in_an_other_string_should_remove_the_party_of_the_string_string_substractor(self):
        result = calc.substract("","rdf")
        self.assertEqual(result,"")
    
    def test_float_substract_float(self):
        result = calc.substract(4.1,1.1)
        self.assertEqual(result,3.0)

        



if __name__ == '__main__':
    unittest.main(verbosity=0)

import unittest

STANDARD = 'STANDARD'
SPECIAL = 'SPECIAL'
REJECTED = 'REJECTED'


def sort(width, height, length, mass):
    """
    Sorts a package based on dimensions and mass.
    
    Parameters:
        width (int): Width in cm
        height (int): Height in cm
        length (int): Length in cm
        mass (int): Mass in kg
    
    Returns:
        str: One of "STANDARD", "SPECIAL", or "REJECTED"
    """
    is_bulky = False
    is_heavy = False
    volume = width*height*length

    if width >= 150 or height >= 150 or length >= 150 or volume >= 1000000:
        is_bulky = True

    if mass >= 20:
        is_heavy = True


    if is_bulky and is_heavy:
        return REJECTED
    
    if is_heavy or is_bulky:
        return SPECIAL
    
    return STANDARD

    
class TestSortFunction(unittest.TestCase):
    
    def test_standard_package(self):
        self.assertEqual(sort(50, 50, 50, 10), STANDARD)

    def test_bulky_by_volume(self):
        self.assertEqual(sort(100, 100, 100, 10), SPECIAL)  # Volume = 1,000,000

    def test_bulky_by_dimension(self):
        self.assertEqual(sort(150, 50, 50, 10), SPECIAL)

    def test_heavy_only(self):
        self.assertEqual(sort(50, 50, 50, 20), SPECIAL)

    def test_bulky_and_heavy(self):
        self.assertEqual(sort(200, 200, 200, 30), REJECTED)  # Definitely both

    def test_edge_case_just_under_bulky_and_heavy(self):
        self.assertEqual(sort(149, 149, 149, 19), SPECIAL)

    def test_edge_case_exactly_bulky_and_heavy(self):
        self.assertEqual(sort(150, 50, 50, 20), REJECTED)

    def test_bulky_by_volume_not_dimension(self):
        self.assertEqual(sort(100, 100, 100, 5), SPECIAL)  # Volume = 1,000,000

    def test_not_bulky_but_very_heavy(self):
        self.assertEqual(sort(10, 10, 10, 100), SPECIAL)

if __name__ == '__main__':
    unittest.main()

    


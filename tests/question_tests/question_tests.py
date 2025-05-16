import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from question_c.question_c import get_most_likely_ancestor_consensus 

# question c test
class TestGetMostLikelyAncestorConsensus(unittest.TestCase):

    def test_get_most_likely_ancestor_consensus(self):
        dna_string1 = "GATATATGCATATACTT"
        dna_string2 = "ATAT"
        
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        
        expected_result = (2, 4, 10)

        self.assertEqual(result, expected_result)
        
        position1, position2, position3 = result
        
        self.assertEqual(position1, 2)
        self.assertEqual(position2, 4)
        self.assertEqual(position3, 10)

if __name__ == '__main__':
    unittest.main()



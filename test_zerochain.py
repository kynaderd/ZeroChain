# test_zerochain.py
"""
Tests for ZeroChain module.
"""

import unittest
from zerochain import ZeroChain

class TestZeroChain(unittest.TestCase):
    """Test cases for ZeroChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZeroChain()
        self.assertIsInstance(instance, ZeroChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZeroChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

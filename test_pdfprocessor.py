# test_pdfprocessor.py
"""
Tests for PDFProcessor module.
"""

import unittest
from pdfprocessor import PDFProcessor

class TestPDFProcessor(unittest.TestCase):
    """Test cases for PDFProcessor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PDFProcessor()
        self.assertIsInstance(instance, PDFProcessor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PDFProcessor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

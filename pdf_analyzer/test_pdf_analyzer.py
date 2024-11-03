import unittest
from pdf_analyzer import preprocessing_text

class TestPreprocessingText(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(preprocessing_text(""), "")
        
    def test_punctuation_removal(self):
        self.assertEqual(preprocessing_text("Hello, world!"), "hello world")
        
    def test_whitespace_normalization(self):
        self.assertEqual(preprocessing_text("Hello   world"), "hello world")
        self.assertEqual(preprocessing_text("Hello\nworld"), "hello world")
        self.assertEqual(preprocessing_text("Hello\tworld"), "hello world")
        
    def test_case_normalization(self):
        self.assertEqual(preprocessing_text("HELLO WORLD"), "hello world")
        
    def test_mixed_characters(self):
        self.assertEqual(preprocessing_text("Hello 123!"), "hello 123")
        
    def test_only_punctuation(self):
        self.assertEqual(preprocessing_text("!!!"), "")
        
    def test_single_word(self):
        self.assertEqual(preprocessing_text("Python"), "python")

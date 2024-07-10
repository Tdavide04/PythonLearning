import unittest
from esercizi24 import Document, File, Email

class TestDocument(unittest.TestCase):
    def test_initial_text(self):
        doc = Document()
        self.assertEqual(doc.getText(), "")

    def test_set_text(self):
        doc = Document()
        doc.setText("Hello, world!")
        self.assertEqual(doc.getText(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()

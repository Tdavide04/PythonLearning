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

    def test_get_text(self):
        doc = Document()
        doc.getText()

    def test_isInText(self):
        doc = Document()
        doc.setText("Ciao 23")
        doc.isInText("23")

class TestEmail(unittest.TestCase):
    def test_getText(self):
        email = Email()
        email.setText("Hello")
        self.assertEqual(email.getText(), "Hello")

    def test_writeToFile(self):
        email = Email()
        email.setText("Hellooo my friend")
        email.writeToFile()
        r = open("document.txt", "r")
        f = r.read()
        r.close()
        self.assertEqual(f"Da: , A: \nTitolo: \nMessagio: {email.getText()}", f)

if __name__ == "__main__":
    unittest.main()

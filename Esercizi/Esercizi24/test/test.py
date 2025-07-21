import unittest
from TestiDigitali import Document, File, Email

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
        self.assertEqual(email.getText(), "Da: , A: \nTitolo: \nMessagio: Hello")

    def test_writeToFile(self):
        email = Email()
        email.setText("Hellooo my friend")
        email.writeToFile()
        r = open("document.txt", "r")
        f = r.read()
        r.close()
        self.assertEqual(f, "Hellooo my friend")

    def test_isInText(self):
        email = Email()
        email.setText("I Love Python")
        email.isInText("Love")

class TestFile(unittest.TestCase):
    def test_getText(self):
        file = File()
        email = Email()
        email.setText("Something is going wrong")
        email.writeToFile()
        file.leggiTestoDaFile()
        self.assertEqual(file.getText(), "Percorso: /home/user/VscodeprojectDavide/PythonLearning/Esercizi/Esercizi24/document.txt \nContenuto: Something is going wrong")

class TestFile(unittest.TestCase):
    file = File()
    file.setText("I dont know what to say")
    file.isInText("dont")

if __name__ == "__main__":
    unittest.main()

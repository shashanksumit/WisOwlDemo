from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import pdfplumber
from docx import Document
import re
import string
# from yourmodule.reader import clean_text - if it is in different file


class DocumentReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.text = ""

    def read(self):
        ext = os.path.splitext(self.filepath)[1].lower()
        if ext == '.txt':
            self.text = self._read_txt()
        elif ext == '.pdf':
            self.text = self._read_pdf()
        elif ext == '.docx':
            self.text = self._read_docx()
        else:
            raise ValueError(f"Unsupported file type: {ext}")
        
        self.text = clean_text(self.text)
        return self.text

    def _read_txt(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading txt file: {e}")
            return ""

    def _read_pdf(self):
        text = ""
        try:
            with pdfplumber.open(self.filepath) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
        except Exception as e:
            print(f"Error reading pdf file: {e}")
        return text

    def _read_docx(self):
        text = ""
        try:
            doc = Document(self.filepath)
            for para in doc.paragraphs:
                text += para.text + "\n"
        except Exception as e:
            print(f"Error reading docx file: {e}")
        return text
    
def clean_text(text):
        # Lowercase everything
        text = text.lower()

        # Remove URLs (optional)
        text = re.sub(r'http\S+|www\S+', '', text)

        # Remove emails (optional)
        text = re.sub(r'\S+@\S+', '', text)

        # Remove digits (optional: keep if important)
        text = re.sub(r'\d+', '', text)

        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Remove multiple spaces & newlines
        text = re.sub(r'\s+', ' ', text)

        # Strip leading/trailing spaces
        return text.strip()
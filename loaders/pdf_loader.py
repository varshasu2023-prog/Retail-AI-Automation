import fitz  # PyMuPDF

class PDFLoader:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        text = ""

        try:
            pdf = fitz.open(self.pdf_path)

            for page in pdf:
                text += page.get_text()

            pdf.close()

        except Exception as e:
            print("Error:", e)

        return text


if __name__ == "__main__":
    loader = PDFLoader("data/products.pdf")
    document = loader.extract_text()

    print(document[:1000])
import fitz

def load_pdf(file_path):
    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text

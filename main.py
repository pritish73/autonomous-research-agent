import os
import fitz

FOLDER = "papers"

for file in os.listdir(FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(FOLDER, file)

        doc = fitz.open(pdf_path)

        text = ""

        for page in doc:
            text += page.get_text()

        pages = len(doc)
        doc.close()

        lines = [line.strip() for line in text.split("\n") if line.strip()]

        title = lines[0] if lines else "Unknown Title"

        print("\n" + "=" * 60)
        print("FILE :", file)
        print("TITLE:", title)
        print("PAGES:", pages)
        print("=" * 60)

        print("\nPREVIEW:\n")
        print(text[:500])

        print("\n")
from docx import Document

doc = Document("Invitation.docx")
text = doc.paragraphs[1]

prior_paragraph = text.insert_paragraph_before(text='Jan Kowalski', style=None)
doc.save("Invitation.docx")
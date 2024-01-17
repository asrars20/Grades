from docx import Document
import json

def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_test_result_letter(student_data, template_path):
    doc = Document(template_path)

    # Replace data placeholders
    for paragraph in doc.paragraphs:
        if 'STUDENT_NAME' in paragraph.text:
            paragraph.text = paragraph.text.replace('STUDENT_NAME', student_data["Student Name"])
        if 'TEST_DATE' in paragraph.text:
            paragraph.text = paragraph.text.replace('TEST_DATE', student_data["Date"])

    doc.save(f'result_letter_for_{student_data["Student Name"]}.docx')

# Load test data
test_data = load_test_data('ncempt_mock_test_data/test_data.json')

# Generate letters for individual students
template_path = 'path_to_template.docx'
for student in test_data:
    generate_test_result_letter(student, template_path)

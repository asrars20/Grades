from docx import Document
import json
import datetime

def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def replace_placeholders(paragraph, student_data):
    if 'current_date' in paragraph.text:
        paragraph.text = paragraph.text.replace('current_date', datetime.datetime.now().strftime('%Y-%m-%d'))
    if 'STUDENT_NAME' in paragraph.text:
        paragraph.text = paragraph.text.replace('STUDENT_NAME', student_data["Student Name"])
    for i in range(1, 6):
        placeholder = f'x{i}'
        if placeholder in paragraph.text:
            paragraph.text = paragraph.text.replace(placeholder, str(student_data.get(placeholder, '')))

def replace_additional_paragraphs(paragraph, student_data):
    # Check for additional paragraph placeholders like 'par_2', 'par_3', etc.
    for key in student_data:
        if key.startswith('par_') and key in paragraph.text:
            paragraph.text = student_data[key]

def replace_specific_table_placeholders(table, student_data):
    # Placeholder patterns for question objectives, correct answers, and student answers
    obj_placeholders = [f'obj{i}x' for i in range(1, 33)]
    ac_placeholders = [f'ac{i}x' for i in range(1, 33)]
    ans_placeholders = [f'a{i}x' for i in range(1, 33)]

    for row in table.rows:
        for cell in row.cells:
            for placeholder in obj_placeholders + ac_placeholders + ans_placeholders:
                if placeholder in cell.text:
                    cell.text = cell.text.replace(placeholder, str(student_data.get(placeholder, '')))

def generate_test_result_letter(student_data, template_path):
    doc = Document(template_path)

    # Replace data placeholders in paragraphs
    for paragraph in doc.paragraphs:
        replace_placeholders(paragraph, student_data)
        replace_additional_paragraphs(paragraph, student_data)
    
    # Replace specific placeholders in the table
    for table in doc.tables:
        replace_specific_table_placeholders(table, student_data)

    doc.save(f'result_letter_for_{student_data["Student Name"]}.docx')

# Load test data
test_data = load_test_data('test_data.json')

# Generate letters for individual students
template_path = 'student_letter_template.docx'
for student in test_data:
    generate_test_result_letter(student, template_path)

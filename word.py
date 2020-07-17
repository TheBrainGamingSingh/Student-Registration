from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.table import WD_ALIGN_VERTICAL

from docx.shared import Pt
document = Document()

p = document.add_paragraph()
p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('Punjab Engineering College, Chandigarh\n(Deemed To Be University)\n\n')
run.bold = True
font = run.font
font.name = 'Times New Roman'
font.size = Pt(24)

run = p.add_run('STUDENT REGISTRATION FORM\n\n')
run.bold = True
font = run.font
font.name = 'Times New Roman'
font.size = Pt(18)

p = document.add_paragraph()
p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

student_id = '17103022'
student_name = 'Manpreet Singh Juneja'

open_ele = ''
dec1 = ''
dec2 = ''

p.add_run('Student ID: ')
p.add_run('{}\t\t\t'.format(student_id)).bold = True

p.add_run('Name: ')
p.add_run('{}\n'.format(student_name)).bold = True

p.add_run('Department: CSE\t\t')
p.add_run('Academic Session: 2020-21\t')
p.add_run('Semester: 7th\t')


records = (	
			(1, '1', 'A'),
			(2, '2', 'B'),
			(3, '3', 'C'),
			(4, 'CSN441', 'Major Project')
		  )

table = document.add_table(rows=1, cols=3)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = table.rows[0].cells
headers[0].text = 'Sr. No.'
headers[1].text = 'Course ID'
headers[2].text = 'Course Name'

for cell in headers:
	cell.vertical_allignment = WD_ALIGN_VERTICAL.CENTER

for sr_no, course_id, course_name in records:
    tds = table.add_row().cells
    tds[0].text = str(sr_no)
    tds[1].text = course_id
    tds[2].text = course_name


document.add_page_break()
document.save('{}.docx'.format(student_id))

import random
from fpdf import FPDF

# Sample question bank
question_bank = [
    {
        'question': 'Qual é o número da porta padrão para o PostgreSQL?',
        'options': ['A) 3306', 'B) 5432', 'C) 1521', 'D) 1433'],
        'answer': 'B'
    },
    {
        'question': 'Qual comando é usado para criar um novo banco de dados no PostgreSQL?',
        'options': ['A) CREATE DATABASE nome_bd;', 'B) CREATE nome_bd;', 'C) NEW DATABASE nome_bd;', 'D) ADD DATABASE nome_bd;'],
        'answer': 'A'
    },
    {
        'question': 'Como listar todas as tabelas em um banco de dados PostgreSQL?',
        'options': ['A) SHOW TABLES;', 'B) LIST TABLES;', 'C) SELECT * FROM tables;', 'D) \dt'],
        'answer': 'D'
    },
    {
        'question': 'Qual é o comando para fazer backup de um banco de dados PostgreSQL?',
        'options': ['A) pg_dump nome_bd > backup.sql', 'B) backup nome_bd > backup.sql', 'C) dump nome_bd > backup.sql', 'D) pg_backup nome_bd > backup.sql'],
        'answer': 'A'
    },
    {
        'question': 'Qual tipo de dado é usado para armazenar um texto grande no PostgreSQL?',
        'options': ['A) VARCHAR', 'B) TEXT', 'C) CHAR', 'D) STRING'],
        'answer': 'B'
    },
    {
        'question': 'Como adicionar uma nova coluna a uma tabela existente no PostgreSQL?',
        'options': ['A) ALTER TABLE nome_tabela ADD nome_coluna tipo_dado;', 'B) MODIFY TABLE nome_tabela ADD nome_coluna tipo_dado;', 'C) CHANGE TABLE nome_tabela ADD nome_coluna tipo_dado;', 'D) UPDATE TABLE nome_tabela ADD nome_coluna tipo_dado;'],
        'answer': 'A'
    },
    {
        'question': 'Qual é o propósito do tipo de dado SERIAL no PostgreSQL?',
        'options': ['A) Armazenar texto grande', 'B) Gerar valores inteiros únicos automaticamente', 'C) Armazenar dados binários', 'D) Armazenar data e hora'],
        'answer': 'B'
    },
    {
        'question': 'Qual comando é usado para excluir um banco de dados no PostgreSQL?',
        'options': ['A) DROP DATABASE nome_bd;', 'B) DELETE DATABASE nome_bd;', 'C) REMOVE DATABASE nome_bd;', 'D) ERASE DATABASE nome_bd;'],
        'answer': 'A'
    },
    {
        'question': 'Como criar um novo usuário no PostgreSQL?',
        'options': ['A) CREATE USER nome_usuario;', 'B) ADD USER nome_usuario;', 'C) NEW USER nome_usuario;', 'D) REGISTER USER nome_usuario;'],
        'answer': 'A'
    },
    {
        'question': 'Qual função é usada para contar o número de linhas em uma tabela no PostgreSQL?',
        'options': ['A) SUM()', 'B) COUNT()', 'C) TOTAL()', 'D) AVG()'],
        'answer': 'B'
    }
]

def generate_test(question_bank, num_questions):
    if num_questions > len(question_bank):
        raise ValueError("Number of questions requested exceeds the available questions in the bank.")

    return random.sample(question_bank, num_questions)

def export_to_pdf(selected_questions, test_number, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Test {test_number}", ln=True, align='C')
    pdf.ln(10)  # Add a blank line

    for i, question in enumerate(selected_questions, 1):
        pdf.cell(200, 10, txt=f"Question {i}: {question['question']}", ln=True)
        for option in question['options']:
            pdf.cell(200, 10, txt=option, ln=True)
        pdf.cell(200, 10, txt="", ln=True)  # Add a blank line between questions

    pdf.output(filename)

def generate_multiple_tests(question_bank, num_tests, num_questions_per_test):
    test_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(num_tests):
        selected_questions = generate_test(question_bank, num_questions_per_test)
        test_number = test_letters[i]
        filename = f'../out/tests/test_{test_number}.pdf'
        export_to_pdf(selected_questions, test_number, filename)
        print(f"Test {test_number} with {num_questions_per_test} questions has been generated and saved as '{filename}'")

# Generate 4 tests
generate_multiple_tests(question_bank, num_tests=4, num_questions_per_test=len(question_bank))

from PIL.ImageChops import offset
from flask import Flask, render_template, request, jsonify, redirect, url_for
import psycopg2
import json
import math

from user_database import create_registration_and_request_tr

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrations')
def display_table():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset for pagination
    offset = (page - 1) * per_page

    # Retrieve total rows count
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"  # Replace with your actual password
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM view_registration")
    total_rows = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    # Calculate total pages
    total_pages = math.ceil(total_rows / per_page)

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"  # Replace with your actual password
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM view_registration OFFSET {offset} LIMIT {per_page}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Retrieve success_message and error_message from query parameters
    success_message = request.args.get('success_message')
    error_message = request.args.get('error_message')

    # Pass data, pagination parameters, and messages to the template
    return render_template('table.html', data=data, page=page, per_page=per_page,
                           total_pages=total_pages, success_message=success_message,
                           error_message=error_message)

if __name__ == '__main__':
    app.run()

@app.route('/add_registration', methods=['GET'])
def add_registration():
    return render_template('registration_form.html')

@app.route('/add_registration', methods=['POST'])
def submit_registration():
    employeerolebranch_id = request.form['employeerolebranch_id']
    registrationtype_id = request.form['registrationtype_id']
    technicalcheck_id = request.form['technicalcheck_id']

    success_message = None
    error_message = None

    try:
        ret_id = None  # Initialize ret_id

        # Call the function with the out_ret_id parameter
        create_registration_and_request_tr(employeerolebranch_id, registrationtype_id, technicalcheck_id)

        if ret_id is not None:
            success_message = "Registration inserted successfully."
        else:
            error_message = "Failed to insert registration."
    except psycopg2.Error as e:
        error_message = str(e)

    return redirect(url_for('display_table', success_message=success_message, error_message=error_message))

@app.route('/technical')
def display_table2():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset for pagination
    offset = (page - 1) * per_page

    # Retrieve total rows count
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM view_technical")
    total_rows = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    # Calculate total pages
    total_pages = math.ceil(total_rows / per_page)

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM view_technical OFFSET {offset} LIMIT {per_page}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data, pagination parameters, and total pages to the template
    return render_template('tableTeh.html', data=data, page=page, per_page=per_page, total_pages=total_pages)

@app.route('/add_technical', methods=['POST'])
def add_technical():
    chassis_number = request.form.get('chassis_number')
    engine_power = request.form.get('engine_power')
    name = request.form.get('name')
    ssn_or_tin = request.form.get('ssn_or_tin')
    type_technical = request.form.get('type_technical')
    technical_check_time = request.form.get('technical_check_time')
    failed_with_device = request.form.get('failed_with_device')

    # Perform the necessary database insertion here
    # Use the provided insert_passedTehnicalCheckForPerson function with the appropriate parameters

    # Display success message
    success_message = "Technical check added successfully."

    # Redirect back to the table with success message
    return redirect(url_for('display_table2', success=success_message))

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/employees')
def display_table3():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset for pagination
    offset = (page - 1) * per_page

    # Retrieve total rows count
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM employees_v")
    total_rows = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    # Calculate total pages
    total_pages = math.ceil(total_rows / per_page)

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM employees_v OFFSET {offset} LIMIT {per_page}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data, pagination parameters, and total pages to the template
    return render_template('tableEmp.html', data=data, page=page, per_page=per_page, total_pages=total_pages)

@app.route('/vehicle')
def display_table4():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset for pagination
    offset = (page - 1) * per_page

    # Retrieve total rows count
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM vehicle_v")
    total_rows = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    # Calculate total pages
    total_pages = math.ceil(total_rows / per_page)

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM vehicle_v OFFSET {offset} LIMIT {per_page}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data, pagination parameters, and total pages to the template
    return render_template('tableVeh.html', data=data, page=page, per_page=per_page, total_pages=total_pages)

@app.route('/company')
def display_table5():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset for pagination
    offset = (page - 1) * per_page

    # Retrieve total rows count
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM view_company")
    total_rows = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    # Calculate total pages
    total_pages = math.ceil(total_rows / per_page)

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM view_company OFFSET {offset} LIMIT {per_page}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data, pagination parameters, and total pages to the template
    return render_template('tableComp.html', data=data, page=page, per_page=per_page, total_pages=total_pages)

@app.route('/person')
def display_table6():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset for pagination
    offset = (page - 1) * per_page

    # Retrieve total rows count
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM view_person")
    total_rows = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    # Calculate total pages
    total_pages = math.ceil(total_rows / per_page)

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM view_person OFFSET {offset} LIMIT {per_page}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data, pagination parameters, and total pages to the template
    return render_template('tablePer.html', data=data, page=page, per_page=per_page, total_pages=total_pages)

@app.route('/admin1')
def display_table7():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset for pagination
    offset = (page - 1) * per_page

    # Retrieve total rows count
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM annualnumberofregistrationspertype")
    total_rows = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    # Calculate total pages
    total_pages = math.ceil(total_rows / per_page)

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM annualnumberofregistrationspertype OFFSET {offset} LIMIT {per_page}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data, pagination parameters, and total pages to the template
    return render_template('adminTable1.html', data=data, page=page, per_page=per_page, total_pages=total_pages)

@app.route('/admin2')
def display_table8():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset for pagination
    offset = (page - 1) * per_page

    # Retrieve total rows count
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM numberofactivevehiclesperbrand")
    total_rows = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    # Calculate total pages
    total_pages = math.ceil(total_rows / per_page)

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM numberofactivevehiclesperbrand OFFSET {offset} LIMIT {per_page}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data, pagination parameters, and total pages to the template
    return render_template('adminTable2.html', data=data, page=page, per_page=per_page, total_pages=total_pages)


@app.route('/admin3')
def display_table9():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset for pagination
    offset = (page - 1) * per_page

    # Retrieve total rows count
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM numberofcarsownedbyeachparty")
    total_rows = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    # Calculate total pages
    total_pages = math.ceil(total_rows / per_page)

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM numberofcarsownedbyeachparty OFFSET {offset} LIMIT {per_page}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data, pagination parameters, and total pages to the template
    return render_template('adminTable3.html', data=data, page=page, per_page=per_page, total_pages=total_pages)

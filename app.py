from flask import Flask, render_template, request, jsonify
import psycopg2
import json
import math

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
        password="RoseT123&&"
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
        password="RoseT123&&"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM view_registration OFFSET {offset} LIMIT {per_page}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data, pagination parameters, and total pages to the template
    return render_template('table.html', data=data, page=page, per_page=per_page, total_pages=total_pages)

if __name__ == '__main__':
    app.run()


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

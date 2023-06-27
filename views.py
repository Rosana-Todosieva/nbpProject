from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route('/registrations')
def display_table():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset and limit for pagination
    offset = (page - 1) * per_page
    limit = per_page

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()

    # Retrieve data from the view using pagination
    cursor.execute(f"SELECT * FROM view_registration OFFSET {offset} LIMIT {limit}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data and pagination parameters to the template
    return render_template('table.html', data=data, page=page, per_page=per_page)


@app.route('/technical')
def display_table():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset and limit for pagination
    offset = (page - 1) * per_page
    limit = per_page

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()

    # Retrieve data from the view using pagination
    cursor.execute(f"SELECT * FROM view_technical OFFSET {offset} LIMIT {limit}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data and pagination parameters to the template
    return render_template('tableTeh.html', data=data, page=page, per_page=per_page)

@app.route('/employees')
def display_table():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset and limit for pagination
    offset = (page - 1) * per_page
    limit = per_page

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()

    # Retrieve data from the view using pagination
    cursor.execute(f"SELECT * FROM employees_v OFFSET {offset} LIMIT {limit}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data and pagination parameters to the template
    return render_template('tableEmp.html', data=data, page=page, per_page=per_page)

@app.route('/vehicle')
def display_table():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset and limit for pagination
    offset = (page - 1) * per_page
    limit = per_page

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()

    # Retrieve data from the view using pagination
    cursor.execute(f"SELECT * FROM vehicle_v OFFSET {offset} LIMIT {limit}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data and pagination parameters to the template
    return render_template('tableVeh.html', data=data, page=page, per_page=per_page)

@app.route('/company')
def display_table():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset and limit for pagination
    offset = (page - 1) * per_page
    limit = per_page

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()

    # Retrieve data from the view using pagination
    cursor.execute(f"SELECT * FROM view_company OFFSET {offset} LIMIT {limit}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data and pagination parameters to the template
    return render_template('tableComp.html', data=data, page=page, per_page=per_page)

@app.route('/person')
def display_table():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset and limit for pagination
    offset = (page - 1) * per_page
    limit = per_page

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()

    # Retrieve data from the view using pagination
    cursor.execute(f"SELECT * FROM view_person OFFSET {offset} LIMIT {limit}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data and pagination parameters to the template
    return render_template('tablePer.html', data=data, page=page, per_page=per_page)

@app.route('/admin1')
def display_table():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset and limit for pagination
    offset = (page - 1) * per_page
    limit = per_page

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()

    # Retrieve data from the view using pagination
    cursor.execute(f"SELECT * FROM annualnumberofregistrationspertype OFFSET {offset} LIMIT {limit}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data and pagination parameters to the template
    return render_template('adminTable1.html', data=data, page=page, per_page=per_page)

@app.route('/admin2')
def display_table():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset and limit for pagination
    offset = (page - 1) * per_page
    limit = per_page

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()

    # Retrieve data from the view using pagination
    cursor.execute(f"SELECT * FROM novaBaza.public.numberofactivevehiclesperbrand OFFSET {offset} LIMIT {limit}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data and pagination parameters to the template
    return render_template('adminTable2.html', data=data, page=page, per_page=per_page)

@app.route('/admin3')
def display_table():
    # Retrieve pagination parameters from request query string
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the offset and limit for pagination
    offset = (page - 1) * per_page
    limit = per_page

    # Retrieve data from the view using pagination
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    cursor = conn.cursor()

    # Retrieve data from the view using pagination
    cursor.execute(f"SELECT * FROM novaBaza.public.numberofcarsownedbyeachparty OFFSET {offset} LIMIT {limit}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Pass data and pagination parameters to the template
    return render_template('adminTable3.html', data=data, page=page, per_page=per_page)

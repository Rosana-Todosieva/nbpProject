import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor

def create_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="novaBaza",
        user="postgres",
        password="RoseT123&&"
    )
    return conn

def execute_function(function_name, params=None):
    conn = create_connection()
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.callproc(function_name, params)
    cursor.close()
    conn.commit()
    conn.close()

def execute_procedure(procedure_name, params=None):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.callproc(procedure_name, params)
    cursor.close()
    conn.commit()
    conn.close()

def execute_query(query, params=None):
    conn = create_connection()
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.execute(query, params)
    results = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return results

def insert_passedTehnicalCheckForPerson(p_ssnortin, p_name, p_curraddress, p_isperson, p_lastname, p_birthdate, p_bornin, p_citizenship_id, p_model_id, p_statemanufactured, p_primarycolor, p_secondarycolor, p_vehiclesubcategory, p_manufactureyear, p_chassisnumber, p_enginenumber, p_enginepower, p_enginesize, p_mass, p_hashook, p_fronttyredimension, p_reartyredimension, p_owner, p_vehicle, p_datefrom, p_dateto, p_technicalchecktype_id, p_technicalcheck, p_description, p_timestamp, p_employeerolebranch_id):
    function_name = "insert_passedTehnicalCheckForPerson"
    params = (p_ssnortin, p_name, p_curraddress, p_isperson, p_lastname, p_birthdate, p_bornin, p_citizenship_id, p_model_id, p_statemanufactured, p_primarycolor, p_secondarycolor, p_vehiclesubcategory, p_manufactureyear, p_chassisnumber, p_enginenumber, p_enginepower, p_enginesize, p_mass, p_hashook, p_fronttyredimension, p_reartyredimension, p_owner, p_vehicle, p_datefrom, p_dateto, p_technicalchecktype_id, p_technicalcheck, p_description, p_timestamp, p_employeerolebranch_id)
    execute_function(function_name, params)

def insert_passedTehnicalCheckForCompany(p_ssnortin, p_name, p_curraddress, p_isperson, p_representor, p_model_id, p_statemanufactured, p_primarycolor, p_secondarycolor, p_vehiclesubcategory, p_manufactureyear, p_chassisnumber, p_enginenumber, p_enginepower, p_enginesize, p_mass, p_hashook, p_fronttyredimension, p_reartyredimension, p_owner, p_vehicle, p_datefrom, p_dateto, p_technicalchecktype_id, p_technicalcheck, p_description, p_timestamp, p_employeerolebranch_id):
    function_name = "insert_passedTehnicalCheckForCompany"
    params = (p_ssnortin, p_name, p_curraddress, p_isperson, p_representor, p_model_id, p_statemanufactured, p_primarycolor, p_secondarycolor, p_vehiclesubcategory, p_manufactureyear, p_chassisnumber, p_enginenumber, p_enginepower, p_enginesize, p_mass, p_hashook, p_fronttyredimension, p_reartyredimension, p_owner, p_vehicle, p_datefrom, p_dateto, p_technicalchecktype_id, p_technicalcheck, p_description, p_timestamp, p_employeerolebranch_id)
    execute_function(function_name, params)

def insert_fueltype(p_code, p_name):
    function_name = "insert_fueltype"
    params = (p_code, p_name)
    execute_function(function_name, params)

def update_fueltype(p_id, p_code, p_name):
    function_name = "update_fueltype"
    params = (p_id, p_code, p_name)
    execute_function(function_name, params)

def insert_vehiclemodel(p_vehiclebrand_id, p_name, p_wheelsnumber, p_axelnumber):
    function_name = "insert_vehiclemodel"
    params = (p_vehiclebrand_id, p_name, p_wheelsnumber, p_axelnumber)
    execute_function(function_name, params)

def update_vehiclemodel(p_id, p_vehiclebrand_id, p_name, p_wheelsnumber, p_axelnumber):
    function_name = "update_vehiclemodel"
    params = (p_id, p_vehiclebrand_id, p_name, p_wheelsnumber, p_axelnumber)
    execute_function(function_name, params)

def insert_vehiclebrand(p_name):
    function_name = "insert_vehiclebrand"
    params = (p_name,)
    execute_function(function_name, params)

def update_vehiclebrand(p_id, p_name):
    function_name = "update_vehiclebrand"
    params = (p_id, p_name)
    execute_function(function_name, params)

def insert_vehiclemodelwithfueltype(p_model_ld, p_fueltype_id):
    function_name = "insert_vehiclemodelwithfueltype"
    params = (p_model_ld, p_fueltype_id)
    execute_function(function_name, params)

def update_vehiclemodelwithfueltype(p_id, p_model_ld, p_fueltype_id):
    function_name = "update_vehiclemodelwithfueltype"
    params = (p_id, p_model_ld, p_fueltype_id)
    execute_function(function_name, params)

def insert_ownership(p_vehicle_id, p_owner, p_datefrom, p_dateto):
    function_name = "insert_ownership"
    params = (p_vehicle_id, p_owner, p_datefrom, p_dateto)
    execute_function(function_name, params)

def update_ownership(p_id, p_vehicle_id, p_owner, p_datefrom, p_dateto):
    function_name = "update_ownership"
    params = (p_id, p_vehicle_id, p_owner, p_datefrom, p_dateto)
    execute_function(function_name, params)

def delete_company_tr(p_id):
    procedure_name = "delete_company_tr"
    params = (p_id,)
    execute_procedure(procedure_name, params)


def delete_employee_tr(p_id):
    procedure_name = "delete_employee_tr"
    params = (p_id,)
    execute_procedure(procedure_name, params)

def delete_person_tr(p_id):
    procedure_name = "delete_person_tr"
    params = (p_id,)
    execute_procedure(procedure_name, params)


def add_address_tr(p_populatedarea_id, p_street_id, p_number):
    query = """
        INSERT INTO address (populatedarea_id, street_id, "number")
        VALUES (%s, %s, %s)
        RETURNING id;
    """
    params = (p_populatedarea_id, p_street_id, p_number)
    result = execute_query(query, params)
    address_id = result[0]['id'] if result else None
    return address_id


def add_branch_tr(p_name, p_location):
    query = """
        INSERT INTO branch ("name", "location")
        VALUES (%s, %s)
        RETURNING id;
    """
    params = (p_name, p_location)
    result = execute_query(query, params)
    branch_id = result[0]['id'] if result else None
    return branch_id

def add_company_tr(p_tin, p_name, p_curr_address_id, p_representor):
    query = """
        DECLARE
            tmp_party_id INTEGER;
            tmp_representor INTEGER;
        BEGIN
            INSERT INTO party (ssnortin, "name", curraddress, isperson)
            VALUES (%s, %s, %s, FALSE)
            RETURNING id INTO tmp_party_id;

            SELECT party_id INTO tmp_representor
            FROM person p
            WHERE p.party_id = %s;

            IF NOT FOUND THEN
                RAISE EXCEPTION 'No person with the id: %s was found', p_representor;
            END IF;

            INSERT INTO company (party_id, representor)
            VALUES (tmp_party_id, tmp_representor);

            RETURN tmp_party_id;
        END;
    """
    params = (p_tin, p_name, p_curr_address_id, p_representor, p_representor)
    result = execute_query(query, params)
    company_id = result[0]['id'] if result else None
    return company_id

def add_employee_tr(p_ssn, p_name, p_last_name, p_curr_address_id, p_birth_place_id, p_birth_date, p_citizenship_id, p_username, p_password):
    query = """
        DECLARE
            var_person_id INTEGER;
        BEGIN
            SELECT * INTO var_person_id
            FROM add_person_tr(p_ssn, p_name, p_last_name, p_curr_address_id, p_birth_place_id, p_birth_date, p_citizenship_id);

            INSERT INTO employee (person_id, username, "password")
            VALUES (var_person_id, p_username, p_password);

            RETURN var_person_id;
        END;
    """
    params = (p_ssn, p_name, p_last_name, p_curr_address_id, p_birth_place_id, p_birth_date, p_citizenship_id, p_username, p_password)
    result = execute_query(query, params)
    person_id = result[0]['id'] if result else None
    return person_id

def add_employeerolebranch_tr(p_branch_id, p_employee_id, p_role_id, p_fromdate):
    query = """
        INSERT INTO employeerolebranch (branch_id, employee_id, role_id, fromdate)
        VALUES (p_branch_id, p_employee_id, p_role_id, p_fromdate)
        RETURNING id;
    """
    params = (p_branch_id, p_employee_id, p_role_id, p_fromdate)
    result = execute_query(query, params)
    role_branch_id = result[0]['id'] if result else None
    return role_branch_id

def add_person_tr(p_ssn, p_name, p_last_name, p_curr_address_id, p_birth_place_id, p_birth_date, p_citizenship_id):
    query = """
        INSERT INTO party (ssnortin, "name", curraddress, isperson)
        VALUES (%s, %s, %s, true)
        RETURNING id;
    """
    params = (p_ssn, p_name, p_curr_address_id)
    result = execute_query(query, params)
    party_id = result[0]['id'] if result else None

    query = """
        INSERT INTO person (party_id, lastname, birthdate, bornin, citizenship_id)
        VALUES (%s, %s, %s, %s, %s);
    """
    params = (party_id, p_last_name, p_birth_date, p_birth_place_id, p_citizenship_id)
    execute_query(query, params)

    return party_id

def create_registration_and_request_tr(p_employeerolebranch_id, p_registrationtype_id, p_technicalcheck_id):
    query = """
        DO $$
        DECLARE
            var_vehicle_id INT;
            var_registration_id INT;
        BEGIN
            IF (SELECT COUNT(*) FROM active_employees_v e WHERE e.employeerolebranch_id = %s) <> 1 THEN
                RAISE EXCEPTION 'Employee for the given id: % does not exist or is not an active employee', %s;
            END IF;

            SELECT vehicle_id INTO var_vehicle_id FROM technicalcheck WHERE technicalcheck.id = %s;
            IF NOT FOUND THEN
                RAISE EXCEPTION 'No technicalcheck with id: % exists', %s;
            END IF;

            IF (SELECT COUNT(*) FROM registrationtype r WHERE r.id = %s) <> 1 THEN
                RAISE EXCEPTION 'No registrationtype with id: % exists', %s;
            END IF;

            INSERT INTO registration ("timestamp", vehicle_id, employeewithrole_id, registrationtype_id, technicalcheck_id)
            VALUES (now(), var_vehicle_id, %s, %s, %s)
            RETURNING id INTO var_registration_id;

            INSERT INTO request (serialnum, "timestamp", registration_id)
            VALUES ('AT-' || var_registration_id, now(), var_registration_id)
            RETURNING id;
        END
        $$;
    """
    params = (
        p_employeerolebranch_id,
        p_employeerolebranch_id,
        p_technicalcheck_id,
        p_technicalcheck_id,
        p_registrationtype_id,
        p_registrationtype_id,
        p_employeerolebranch_id,
        p_registrationtype_id,
        p_technicalcheck_id,
    )
    result = execute_query(query, params)
    ret_id = result[0][0] if result else None
    return ret_id

def add_role_tr(p_name, p_description):
    query = """
        INSERT INTO role ("name", description)
        VALUES (%s, %s)
        RETURNING id;
    """
    params = (p_name, p_description)
    result = execute_query(query, params)
    role_id = result[0][0] if result else None
    return role_id

def add_state_tr(p_code, p_name):
    query = """
        INSERT INTO state (code, "name")
        VALUES (%s, %s)
        RETURNING id;
    """
    params = (p_code, p_name)
    result = execute_query(query, params)
    state_id = result[0][0] if result else None
    return state_id

def add_street_tr(p_name):
    query = """
        INSERT INTO street ("name")
        VALUES (%s)
        RETURNING id;
    """
    params = (p_name,)
    result = execute_query(query, params)
    street_id = result[0][0] if result else None
    return street_id


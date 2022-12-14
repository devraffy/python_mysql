from mysqlConnection import *

pw = "devRaffy221989"
db = "school"

def main():
    connection = create_server_connection("localhost", "root", pw)
    query = "CREATE DATABASE school"
    create_database(connection, query)

def create_teacher_table():
    teacher_query = """
    CREATE TABLE teacher (
        teacher_id INT PRIMARY KEY,
        first_name VARCHAR(40) NOT NULL,
        last_name VARCHAR(40) NOT NULL,
        language_1 VARCHAR(3) NOT NULL,
        language_2 VARCHAR(3),
        dob DATE,
        tax_id INT UNIQUE,
        phone_no VARCHAR(20)
    );
    """
    connection = create_db_connection("localhost", "root", pw, db)
    execute_query(connection, teacher_query)

def create_tables():
    create_client_table = """
    CREATE TABLE client (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(40) NOT NULL,
    address VARCHAR(60) NOT NULL,
    industry VARCHAR(20)
    );
    """

    create_participant_table = """
    CREATE TABLE participant (
    participant_id INT PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    phone_no VARCHAR(20),
    client INT
    );
    """

    create_course_table = """
    CREATE TABLE course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(40) NOT NULL,
    language VARCHAR(3) NOT NULL,
    level VARCHAR(2),
    course_length_weeks INT,
    start_date DATE,
    in_school BOOLEAN,
    teacher INT,
    client INT
    );
    """

    db = "school"
    connection = create_db_connection("localhost", "root", pw, db)
    execute_query(connection, create_client_table)
    execute_query(connection, create_participant_table)
    execute_query(connection, create_course_table)

def alter_table():
    alter_participant = """
    ALTER TABLE participant
    ADD FOREIGN KEY(client)
    REFERENCES client(client_id)
    ON DELETE SET NULL;
    """

    alter_course = """
    ALTER TABLE course
    ADD FOREIGN KEY(teacher)
    REFERENCES teacher(teacher_id)
    ON DELETE SET NULL;
    """

    alter_course_again = """
    ALTER TABLE course
    ADD FOREIGN KEY(client)
    REFERENCES client(client_id)
    ON DELETE SET NULL;
    """

    create_takescourse_table = """
    CREATE TABLE takes_course (
    participant_id INT,
    course_id INT,
    PRIMARY KEY(participant_id, course_id),
    FOREIGN KEY(participant_id) REFERENCES participant(participant_id) ON DELETE CASCADE,
    FOREIGN KEY(course_id) REFERENCES course(course_id) ON DELETE CASCADE
    );
    """

    connection = create_db_connection("localhost", "root", pw, db)
    execute_query(connection, alter_participant)
    execute_query(connection, alter_course)
    execute_query(connection, alter_course_again)
    execute_query(connection, create_takescourse_table)

def populate_teacher():
    pop_teacher = """
    INSERT INTO teacher VALUES
    (1,  'James', 'Smith', 'ENG', NULL, '1985-04-20', 12345, '+491774553676'),
    (2, 'Stefanie',  'Martin',  'FRA', NULL,  '1970-02-17', 23456, '+491234567890'), 
    (3, 'Steve', 'Wang',  'MAN', 'ENG', '1990-11-12', 34567, '+447840921333'),
    (4, 'Friederike',  'M??ller-Rossi', 'DEU', 'ITA', '1987-07-07',  45678, '+492345678901'),
    (5, 'Isobel', 'Ivanova', 'RUS', 'ENG', '1963-05-30',  56789, '+491772635467'),
    (6, 'Niamh', 'Murphy', 'ENG', 'IRI', '1995-09-08',  67890, '+491231231232');
    """

    connection = create_db_connection("localhost", "root", pw, db)
    execute_query(connection, pop_teacher)

def populate_tables():
    pop_client = """
    INSERT INTO client VALUES
    (101, 'Big Business Federation', '123 Falschungstra??e, 10999 Berlin', 'NGO'),
    (102, 'eCommerce GmbH', '27 Ersatz Allee, 10317 Berlin', 'Retail'),
    (103, 'AutoMaker AG',  '20 K??nstlichstra??e, 10023 Berlin', 'Auto'),
    (104, 'Banko Bank',  '12 Betrugstra??e, 12345 Berlin', 'Banking'),
    (105, 'WeMoveIt GmbH', '138 Arglistweg, 10065 Berlin', 'Logistics');
    """

    pop_participant = """
    INSERT INTO participant VALUES
    (101, 'Marina', 'Berg','491635558182', 101),
    (102, 'Andrea', 'Duerr', '49159555740', 101),
    (103, 'Philipp', 'Probst',  '49155555692', 102),
    (104, 'Ren??',  'Brandt',  '4916355546',  102),
    (105, 'Susanne', 'Shuster', '49155555779', 102),
    (106, 'Christian', 'Schreiner', '49162555375', 101),
    (107, 'Harry', 'Kim', '49177555633', 101),
    (108, 'Jan', 'Nowak', '49151555824', 101),
    (109, 'Pablo', 'Garcia',  '49162555176', 101),
    (110, 'Melanie', 'Dreschler', '49151555527', 103),
    (111, 'Dieter', 'Durr',  '49178555311', 103),
    (112, 'Max', 'Mustermann', '49152555195', 104),
    (113, 'Maxine', 'Mustermann', '49177555355', 104),
    (114, 'Heiko', 'Fleischer', '49155555581', 105);
    """

    pop_course = """
    INSERT INTO course VALUES
    (12, 'English for Logistics', 'ENG', 'A1', 10, '2020-02-01', TRUE,  1, 105),
    (13, 'Beginner English', 'ENG', 'A2', 40, '2019-11-12',  FALSE, 6, 101),
    (14, 'Intermediate English', 'ENG', 'B2', 40, '2019-11-12', FALSE, 6, 101),
    (15, 'Advanced English', 'ENG', 'C1', 40, '2019-11-12', FALSE, 6, 101),
    (16, 'Mandarin f??r Autoindustrie', 'MAN', 'B1', 15, '2020-01-15', TRUE, 3, 103),
    (17, 'Fran??ais interm??diaire', 'FRA', 'B1',  18, '2020-04-03', FALSE, 2, 101),
    (18, 'Deutsch f??r Anf??nger', 'DEU', 'A2', 8, '2020-02-14', TRUE, 4, 102),
    (19, 'Intermediate English', 'ENG', 'B2', 10, '2020-03-29', FALSE, 1, 104),
    (20, 'Fortgeschrittenes Russisch', 'RUS', 'C1',  4, '2020-04-08',  FALSE, 5, 103);
    """

    pop_takescourse = """
    INSERT INTO takes_course VALUES
    (101, 15),
    (101, 17),
    (102, 17),
    (103, 18),
    (104, 18),
    (105, 18),
    (106, 13),
    (107, 13),
    (108, 13),
    (109, 14),
    (109, 15),
    (110, 16),
    (110, 20),
    (111, 16),
    (114, 12),
    (112, 19),
    (113, 19);
    """

    connection = create_db_connection("localhost", "root", pw, db)
    execute_query(connection, pop_client)
    execute_query(connection, pop_participant)
    execute_query(connection, pop_course)
    execute_query(connection, pop_takescourse)

if __name__ == "__main__":
    sql = '''
    INSERT INTO teacher (teacher_id, first_name, last_name, language_1, language_2, dob, tax_id, phone_no) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    
    val = [
    (7, 'Hank', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+491772345678'), 
    (8, 'Sue', 'Perkins', 'MAN', 'ENG', '1976-02-02', 22222, '+491443456432')
    ]

    connection = create_db_connection("localhost", "root", pw ,db)
    results = execute_list_query(connection, sql,val)

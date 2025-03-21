import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import mysql.connector
from urllib.parse import parse_qs
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Connect to the MySQL database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Sabiha@231101",  # Replace with your MySQL password
        database="personal_data"
    )
    cursor = conn.cursor()
    logging.info("Connected to MySQL database successfully!")
except mysql.connector.Error as err:
    logging.error(f"Error connecting to MySQL: {err}")
    exit(1)

# Create the persons table if it doesn't exist
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persons (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            telephone VARCHAR(15) NOT NULL,
            address VARCHAR(100) NOT NULL,
            age INT NOT NULL
        )
    ''')
    conn.commit()
except mysql.connector.Error as err:
    logging.error(f"Error creating table: {err}")
    exit(1)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/':
                # Serve the HTML form
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                

                with open('index.html', 'r') as file:
                    self.wfile.write(file.read().encode())
            elif self.path.startswith('/styles/'):
                # Serve static files (CSS)
                try:
                    file_path = os.path.join(os.getcwd(), self.path[1:])  # Full path to the file
                    with open(file_path, 'rb') as file:
                        self.send_response(200)
                        if self.path.endswith('.css'):
                            self.send_header('Content-type', 'text/css')
                        self.end_headers()
                        self.wfile.write(file.read())
                except FileNotFoundError:
                    self.send_error(404, "File Not Found")
            else:
                self.send_error(404, "Not Found")
        except Exception as e:
            logging.error(f"Error in GET request: {e}")
            self.send_error(500, "Internal Server Error")

    def do_POST(self):
        try:
            if self.path == '/submit':
                # Handle form submission
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length).decode('utf-8')
                data = parse_qs(post_data)

                # Extract form data
                name = data.get('name', [''])[0]
                surname = data.get('surname', [''])[0]
                telephone = data.get('telephone', [''])[0]
                address = data.get('address', [''])[0]
                age = data.get('age', [''])[0]

                # Validate data
                errors = []
                if not name:
                    errors.append("Name is required.")
                if not surname:
                    errors.append("Surname is required.")
                if not telephone or not telephone.isdigit() or len(telephone) != 8:
                    errors.append("Telephone must be 8 digits.")
                if not address:
                    errors.append("Address is required.")
                if not age or not age.isdigit():
                    errors.append("Age must be a number.")

                if not errors:
                    # Insert data into the database
                    try:
                        cursor.execute('''
                            INSERT INTO persons (name, surname, telephone, address, age)
                            VALUES (%s, %s, %s, %s, %s)
                        ''', (name, surname, telephone, address, age))
                        conn.commit()
                    except mysql.connector.Error as err:
                        logging.error(f"Error inserting data into MySQL: {err}")

                # Fetch all data from the database
                cursor.execute('SELECT name, surname, telephone, address, age FROM persons')
                rows = cursor.fetchall()

                # Generate HTML for the table
                table_rows = ""
                for row in rows:
                    table_rows += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"

                # Send response
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                with open('index.html', 'r') as file:
                    html_content = file.read()
                    updated_html = html_content.replace('<!-- Data will be populated here by the server -->', table_rows)
                    self.wfile.write(updated_html.encode())
            else:
                self.send_error(404, "Not Found")
        except Exception as e:
            logging.error(f"Error in POST request: {e}")
            self.send_error(500, "Internal Server Error")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
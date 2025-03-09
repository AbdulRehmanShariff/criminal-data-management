# Criminal Data Management

A comprehensive system designed for law enforcement agencies to efficiently manage criminal records.

## Overview

Criminal Data Management is a desktop application built with Python and Tkinter that allows users to store, retrieve, update, and delete criminal records. The system integrates with a MySQL database to provide reliable data storage and quick access to criminal information.

## Features

- **Criminal Record Management**: Add, update, delete, and view criminal records
- **Image Upload**: Attach and display criminal photographs
- **Search Functionality**: Find records by Case ID or Criminal Number
- **User-friendly Interface**: Intuitive GUI built with Tkinter
- **Database Integration**: Secure storage with MySQL

## Technology Stack

- **Frontend**: Python Tkinter
- **Database**: MySQL
- **Image Processing**: PIL (Python Imaging Library)

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/criminal-data-management.git
cd criminal-data-management
```

2. Install required packages:
```
pip install mysql-connector-python pillow
```

3. Set up MySQL database:
- Create a database named 'rs'
- Create a table 'criminal1' with the appropriate fields (see schema below)

4. Update database credentials in the code:
```python
# Update these credentials in the code
conn = mysql.connector.connect(host='localhost', username='your_username', password='your_password', database='rs')
```

## Database Schema

The application uses a table with the following structure:
- case_id
- criminal_no
- criminal_name
- nickname
- arrest_date
- date_of_crime
- address
- age
- occupation
- birthmark
- crime_type
- father_name
- gender
- wanted
- image (stores path to criminal's photo)

## Usage

1. Run the application:
```
python main.py
```

2. Use the interface to:
   - Add new criminal records
   - Update existing information
   - Upload criminal photographs
   - Search for specific records
   - View all criminal data

## Screenshots

[output_screenshot.png]

## Contributing++

Contributions to improve the system are welcome. Please feel free to fork the repository and submit pull requests.

## License

[MIT License

Copyright (c) 2025 [Rehman_shariff]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
]

## Contact

[9036069732] #whatsapp number

# email 

[rehmanshariff996@gmail.com]


# MySql
To create a database for your Criminal Management System application, you'll need to set up a MySQL database and create the necessary table. I'll walk you through the process step by step:
Step 1: Install MySQL if you haven't already
Make sure MySQL Server is installed on your computer. You can download it from the official MySQL website.
Step 2: Access MySQL
Open MySQL command line client or a tool like MySQL Workbench. Log in with your root credentials (using the password you have in your code: 'MySql Password').
Step 3: Create the Database
CREATE DATABASE rs;   #give any name for creating the database
USE rs;
Step 4: Create the Criminal Table
Based on the fields in your application, create the criminal1 table:   # after creating database then click on it and create a table, you can give any name for table 
CREATE TABLE criminal1 (
    case_id VARCHAR(50) PRIMARY KEY,
    criminal_no VARCHAR(50) NOT NULL,
    criminal_name VARCHAR(100) NOT NULL,
    nickname VARCHAR(100),
    arrest_date VARCHAR(50),
    date_of_crime VARCHAR(50),
    address VARCHAR(200),
    age VARCHAR(10),
    occupation VARCHAR(100),
    birthmark VARCHAR(100),
    crime_type VARCHAR(100),
    father_name VARCHAR(100),
    gender VARCHAR(10),
    wanted VARCHAR(10),
    image VARCHAR(255)
);
Step 5: Verify the Table Creation
DESCRIBE criminal1;  #if you get confused then watch somne youtube tutorials for better understand.


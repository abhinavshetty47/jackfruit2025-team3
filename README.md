# Secure Login System - Jackfruit Mini Project

🔹 Problem Statement
To design and implement a secure login system that allows users to register and log in using hashed passwords, and to record login attempts in a CSV file for audit purposes.

🔹 Features
- User registration with SHA-256 password hashing  
- Secure login verification  
- Logging each login attempt (Success / Failed)  
- Storing logs in CSV using pandas  
- Persistent storage of user credentials  
- Well-structured Python code using functions  

🔹 Technologies Used
- Python  
- hashlib  
- pandas  
- File handling  
- CSV logging  

🔹 Project Structure
jackfruit-miniproject/
│
├── code/
│ └── login_system.py
│
├── users.txt
├── login_logs.csv
└── README.md

🔹 How to Run the Project
1. Install required libraries:
   pip install pandas
2. Run the program:
   python login_system.py
3. Choose:
- `1` → Register user  
- `2` → Login user  
- `3` → Exit  

🔹 Output Examples
- User registration  
- User login validation  
- CSV logs like:
- 
Username,Status,Timestamp
  27ayushk,Success,2025-12-04 12:45
  27ayushk,Failed,2025-12-04 12:46
  27ayushk,Failed,2025-12-04 12:47
  27ayushk,Success,2025-12-04 12:48

🔹 Team Members
- Asif Parasappanavar – GitHub ID  
- Amrutgouda Patil – @amrutgoudapatil 
- Ayush K – @27ayushk  
- Abhinav Shetty – @abhinavshetty47
  
🔹 Mentor
**amikak@pes.edu (PES University)**


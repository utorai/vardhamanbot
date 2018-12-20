import requests
from bs4 import BeautifulSoup
import roman

class Scraper:
    def __init__(self):
        self.session = requests.Session()
        self.authenticated = False

    def authenticate(self, rollno, wak):
        if not self.authenticated:
            data = {
                'rollno' : rollno,
                'wak' : wak,
                'ok' : 'SignIn'
            }
            response = self.session.post('http://studentscorner.vardhaman.org', data)
            print()
            if not 'Content-Length' in response.headers:
                #print(response.headers)
                self.authenticated = True
    
    def getPeriods(self):
        if self.authenticated:
            conducted = 0
            attended = 0
            response = self.session.get('http://studentscorner.vardhaman.org/student_attendance.php')
            soup = BeautifulSoup(response.text, 'html.parser')
            for element in soup.find_all('th'):
                #print(element.decode_contents().strip())
                if(element.decode_contents().strip()== "Conducted"):
                    tr = element.parent
                    for td in tr.find_all("th")[1:]:
                        conducted += int(td.decode_contents().strip())
                if(element.decode_contents().strip()== "Attended"):
                    tr = element.parent
                    for td in tr.find_all("th")[1:]:
                            attended += int(td.decode_contents().strip())
            return (conducted,attended)
        
    def get_gpa(self, semester):
        if self.authenticated:
            semester_text = "Semester - " + roman.toRoman(semester)
            response = self.session.get('http://studentscorner.vardhaman.org/src_programs/students_corner/CreditRegister/credit_register.php')
            soup = BeautifulSoup(response.text, 'html.parser')
            for element in soup.find_all('th'):
                if element.decode_contents().strip() == semester_text:
                    for gpa_element in element.find_parent('tr').find_all_next():
                        if "Semester Grade Point Average" in gpa_element.decode_contents().strip():
                            gpa = float(gpa_element.contents[0].findChildren()[0].decode_contents().split("Semester Grade Point Average :")[1].strip())
                            break
            return gpa
        else:
            raise Exception("User authentication required for this feature.")
    
    def get_cgpa(self):
        if self.authenticated:
            response = self.session.get('http://studentscorner.vardhaman.org/src_programs/students_corner/CreditRegister/credit_register.php')
            soup = BeautifulSoup(response.text, 'html.parser')
            for element in soup.find_all('th'):
                if "Cumulative Grade Point Average" in element.decode_contents().strip():
                    cgpa = float(element.contents[0].decode_contents().split("Cumulative Grade Point Average :")[1].strip())
                    break
            return cgpa
        else:
            raise Exception("User authentication required for this feature.")

    def get_attendance(self):
        if self.authenticated:
            response = self.session.get('http://studentscorner.vardhaman.org/student_attendance.php')
            soup = BeautifulSoup(response.text, 'html.parser')
            for element in soup.find_all('th'):
                if element.decode_contents().strip() == 'Attendance Percentage':
                    attendance = element.findNext('th').contents[0].findChildren()[0].decode_contents()
                    return float(attendance)
        else:
            raise Exception("User authentication required for this feature.")
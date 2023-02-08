import connexion
import json

from connexion.exceptions import OAuthProblem
from models import DEPARTMENTS, GENDER, Student

#token auth
TOKEN_DB = {
    'asdf1234567890': {
        'uid': 100
    }
}

#data setup
results  = dict()
results["Students"] = []
results["Students"].append(Student("Anabelle",GENDER[1],"Data Analytics",DEPARTMENTS[0],"A"))
results["Students"].append(Student("Deniz",GENDER[0],"Data Analytics",DEPARTMENTS[0],"A"))
results["Students"].append(Student("Devika",GENDER[1],"Waste Treatment",DEPARTMENTS[1],"B"))
results["Students"].append(Student("Jeannette",GENDER[1],"Test Strategy",DEPARTMENTS[0],"A"))
results["Students"].append(Student("Bob",GENDER[0],"Waste Treatment",DEPARTMENTS[1],"C"))
results["Students"].append(Student("Jane",GENDER[1],"Biology",DEPARTMENTS[2],"A"))
results["Students"].append(Student("Frans",GENDER[1],"Biology",DEPARTMENTS[2],"A"))
results["Students"].append(Student("Dave",GENDER[0],"Data Analytics",DEPARTMENTS[1],"A"))
results["Students"].append(Student("Jim",GENDER[0],"Biology",DEPARTMENTS[2],"A"))

#api key authentication
def apikey_auth(token, required_scopes):
    info = TOKEN_DB.get(token, None)
    if not info:
        raise OAuthProblem('Invalid token')
    return info

#get all students
def get_all_students(user) -> str:
    output = []
    for student in results["Students"]:
        output.append(student.serialize())
    result = {'Students': output, 'Total': len(output)}
    return result

#get students by department
def get_students_by_department(department, user) -> str:
    output = []
    filter_result = [x for x in results["Students"] if x.department == department]
    for student in filter_result:
        output.append(student.serialize())
    result = {'Students': output, 'Total': len(output)}
    return result

#filter set 
def filter_set(data, search_string):
    def iterator_func(x):
        for v in x.values():
            if search_string in v:
                return True
        return False
    return filter(iterator_func, data)


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090)
    app.app.config['JSON_SORT_KEYS'] = False
    app.add_api('openapi.yaml', arguments={'title': 'Open API example'})
    app.run()
import random

def generate_random_student():
    names = ["Mohamed", "Hasan", "Saathath", "Vinoth", "Kumar", "Selva", "Joseph", "Gowtham", "Piyush"]

    return {
        "id": random.randint(1, 100),
        "name": random.choice(names),
        "Department": random.choice(["Computer Science", "Information Technology", "CSBS", "AIML"]),
        "grade": random.choice(["A", "B", "C", "D", "F"])
    }

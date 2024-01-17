import random
import datetime
import json
import copy
from testobject import TestObject
from mock_test import MockTest

def random_date():
    start_date = datetime.date(2023, 12, 31)
    end_date = datetime.date(2024, 1, 11)
    return start_date + datetime.timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())),
    )

def generate_random_info():

    test_data_instance = copy.deepcopy(TestObject)

    college_choices = ["001", "002", "003", "004", "005", "006", "007", "008",
                        "009", "010", "011", "012", "013", "014", "015", "016", None] # Question A, can be 001 - 016
    college_of_choice = random.choice(college_choices)
    test_data_instance["Background"]["College of Choice"] = college_of_choice

    # Question B
    first_major_choices = ["001", "002", "003", "004", "005", "006", "007", "008", "009", "010",
                        "011", "012", "013", "014", "015", "016", "017", "018", "019", "020",
                        "021", "022", "023", "024", "025", None]
    first_major = random.choice(first_major_choices)
    test_data_instance["Background"]["First Major"] = first_major
    if first_major != None:
        first_major_choices.remove(first_major)

    # Question C
    
    second_major_choices = first_major_choices
    second_major = random.choice(second_major_choices)
    test_data_instance["Background"]["Second Major"] = second_major

    # Question D
    class_enrolled_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", None]
    class_enrolled = random.choice(class_enrolled_choices)
    test_data_instance["Background"]["Class Enrolled"] = class_enrolled

    #Question E
    teacher_id = random.randint(1, 25)
    test_data_instance["Background"]["TeacherID"] = teacher_id

    # Question F
    class_periods = ["1", "2", "3", "4", "A", "B", "C", "D","First", "Second", "Third", "Fourth", None]
    class_period = random.choice(class_periods)
    test_data_instance["Background"]["Class Period"] = class_period

    # Question G
    after_graduation_choices = ["1", "2", "3", "4", "5", "6", "7", None]
    after_graduation = random.choice(after_graduation_choices)
    test_data_instance["Background"]["After Graduation"] = after_graduation

    # Question H
    amount_of_college_math_courses_choices = ["1", "2", "3", "4", "5", None]
    amount_of_college_math_courses = random.choice(amount_of_college_math_courses_choices)
    test_data_instance["Background"]["Amount of College Math Courses"] = amount_of_college_math_courses

    # Question I
    student_race_choices = ["1", "2", "3", "4", "5", "6", "7", "8", None]
    student_race = random.choice(student_race_choices)
    test_data_instance["Background"]["Race"] = student_race

    # Question J
    calculator_choices = ["1", "2", "3", "4", None]
    calculator = random.choice(calculator_choices)
    test_data_instance["Background"]["Calculator"] = calculator

    #Test Instance
    test_instance_id = random.randint(1, 1000000)
    test_data_instance["Test Instance"] = test_instance_id

    #Student Number
    student_number = random.choices([random.randint(1, 1000000), None], weights=[0.8, 0.2],k=1)[0]
    test_data_instance["Student Number"] = student_number

    #Date
    test_data_instance["Date"] = random.choices([random_date().isoformat(), None], weights=[0.8, 0.2],k=1)[0]

    #School Number
    school_number = random.choices([random.randint(10000, 99999), None], weights=[0.8, 0.2],k=1)[0]
    test_data_instance["School Number"] = school_number


    #Student Name
    student_name = "Test Student " + str(random.randint(1, 1000000))
    student_name = random.choices([student_name, None], weights=[0.8, 0.2],k=1)[0]
    test_data_instance["Student Name"] = student_name

    #Sex
    sex_choices = ["MALE", "FEMALE"]
    sex = random.choices([random.choice(sex_choices), None], weights=[0.8, 0.2],k=1)[0]
    test_data_instance["Sex"] = sex

    #Grade Level
    grade_level_choices = ["9", "10", "11", "12"]
    grade_level = random.choices([random.choice(grade_level_choices), None], weights=[0.8, 0.2],k=1)[0]
    test_data_instance["Grade Level"] = grade_level

    return test_data_instance

def generate_targeted_results(level_one_amount, level_two_amount, level_three_amount, level_four_amount):
    total = level_one_amount + level_two_amount + level_three_amount + level_four_amount
    created = 0

    questions = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8",
                "Q9", "Q10", "Q11", "Q12", "Q13", "Q14", "Q15", "Q16",
                "Q17", "Q18", "Q19", "Q20", "Q21", "Q22", "Q23", "Q24",
                "Q25", "Q26", "Q27", "Q28", "Q29", "Q30", "Q31", "Q32"]

    mockTest = MockTest
    test_results = []
    while created < total:
        while level_one_amount > 0:
            student_data = generate_random_info()
            correct_questions = random.sample(questions, k=random.randint(0, 11))
            #print(correct_questions)
            student_data["Expected Result"] = len(correct_questions)
            for question in questions:
                if question in correct_questions:
                    student_data["Questions"][question] = mockTest[question]["answer"]
                    correct_questions.remove(question)
                else:
                    answers = ["A", "B", "C", "D", "E", None]
                    answers.remove(mockTest[question]["answer"])
                    inccorect_answers = answers
                    student_data["Questions"][question] = random.choice(inccorect_answers)
            # Expected Result
            

            # Expected Grade
            student_data["Expected Grade"] = "1"

            test_results.append(student_data)
            created += 1
            level_one_amount -= 1


        while level_two_amount > 0:
            student_data = generate_random_info()
            correct_questions = random.sample(questions, k=random.randint(12, 16))
            #print(correct_questions)
            student_data["Expected Result"] = len(correct_questions)
            for question in questions:
                if question in correct_questions:
                    student_data["Questions"][question] = mockTest[question]["answer"]
                    correct_questions.remove(question)
                else:
                    answers = ["A", "B", "C", "D", "E"]
                    answers.remove(mockTest[question]["answer"])
                    inccorect_answers = answers
                    student_data["Questions"][question] = random.choice(inccorect_answers)
                

            # Expected Grade
            student_data["Expected Grade"] = "2"

            test_results.append(student_data)
            created += 1
            level_two_amount -= 1

        while level_three_amount > 0:
            student_data = generate_random_info()
            correct_questions = random.sample(questions, k=random.randint(17, 24))
            #print(correct_questions)
            student_data["Expected Result"] = len(correct_questions)
            for question in questions:
                if question in correct_questions:
                    student_data["Questions"][question] = mockTest[question]["answer"]
                    correct_questions.remove(question)
                else:
                    answers = ["A", "B", "C", "D", "E"]
                    answers.remove(mockTest[question]["answer"])
                    inccorect_answers = answers
                    student_data["Questions"][question] = random.choice(inccorect_answers)
                
            # Expected Grade
            student_data["Expected Grade"] = "3"
            
            test_results.append(student_data)
            created += 1
            level_three_amount -= 1

        while level_four_amount > 0:
            student_data = generate_random_info()
            correct_questions = random.sample(questions, k=random.randint(25, 32))
            #print(correct_questions)
            student_data["Expected Result"] = len(correct_questions)
            for question in questions:
                if question in correct_questions:
                    student_data["Questions"][question] = mockTest[question]["answer"]
                    correct_questions.remove(question)
                else:
                    answers = ["A", "B", "C", "D", "E"]
                    answers.remove(mockTest[question]["answer"])
                    inccorect_answers = answers
                    student_data["Questions"][question] = random.choice(inccorect_answers)
                

            # Expected Grade
            student_data["Expected Grade"] = "4"

            test_results.append(student_data)
            created += 1
            level_four_amount -= 1
        
    with open('test_data.json', 'w') as f:
        json.dump(test_results, f, indent=4)


generate_targeted_results(5,5,5,5)

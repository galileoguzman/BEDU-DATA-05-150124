import statistics

data = {
    'students': [
        {
            'name': 'Salvador Vizcaino',
            'class': 2015,
            'scores': [10, 9.8, 7, 7.8, 10, 8.9]
        },
        {
            'name': 'Edgar Torres',
            'class': 2015,
            'scores': []
        },
        {
            'name': 'Galileo Guzman',
            'class': 2015,
            'scores': [10, 8, 8, 6.9, 8.9, 8.9]
        },
        {
            'name': 'Liz Rueda',
            'class': 2015,
            'scores': []
        },
        {
            'name': 'Met Velasquez',
            'class': 2015,
            'scores': [10, 10, 9.8, 9.9, 9.9, 8.9]
        },
        {
            'name': 'Sofia Lopez',
            'class': 2015,
            'scores': [10, 10, 9.8, 9.9, 9.9, 8.9]
        },
        {
            'name': 'Mario Rueda',
            'class': 2015,
            'scores': [10, 10, 9.8, 9.9, 9.9, 8.9]
        },
        {
            'name': 'Mario Rueda',
            'class': 2014,
        }
    ]
}


def students_with_scores(student):
    scores = student.get('scores', [])
    if len(scores) >= 1:
        return True
    return False

students = data.get('students', [])
# Longitud de lista
print(f'Students with scores: {len(students)}') 
qualified_students = list(filter(students_with_scores, students))
print(f'Students qualified {len(qualified_students)}')

def apply_final_score(student):
    result = statistics.mean(student['scores'])
    student['final_score'] = round(result, 2)
    return student

students_with_final_score = list(map(apply_final_score, qualified_students))
print('\n\n')
for s in students_with_final_score:
    print(f'{s.get("name")} - tiene promedio de {s.get("final_score")}')
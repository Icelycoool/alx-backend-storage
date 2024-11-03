#!/usr/bin/env python3
""""top_students"""


def top_students(mongo_collection):
    """returns all students soretd by average score"""
    students = mongo_collection.find()

    results = []

    for student in students:
        scores = [topic['score'] for topic in student.get('topics', [])]
        average_score = sum(scores) / len(scores) if scores else 0
        student_with_average = {
            '_id': student['_id'],
            'name': student['name'],
            'average_score': average_score,
        }
        results.append(student_with_average)
    
    results.sort(key=lambda x: x['avaerageScore'], reverse=True)

    return results

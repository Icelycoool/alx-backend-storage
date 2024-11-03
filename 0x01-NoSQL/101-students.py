#!/usr/bin/env python3
""""top_students"""


def top_students(mongo_collection):
    """returns all students soretd by average score"""
    students = mongo_collection.find()
    sorted_students = sorted(students, key=lambda student: student['average_score'], reverse=True)
    return sorted_students
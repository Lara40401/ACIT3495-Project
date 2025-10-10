import os
from flask import Flask
import mysql.connector
from pymongo import MongoClient

app = Flask(__name__)
MONGO_CLIENT: MongoClient = MongoClient('mongodb://mongo:27017/')
DB_CONFIG = {
    'host': os.getenv("MYSQL_HOST"),
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'database': os.getenv("MYSQL_DATABASE")
}
def calculations():
    try:
        connector = mysql.connector.connect(**DB_CONFIG)
        cursor = connector.cursor()
        cursor.execute("SELECT course, grade FROM grades")
        data = cursor.fetchall()

        courses_dict = {}
        results = []
        
        for course, grade in data:
            if course not in courses_dict:
                courses_dict[course] = []
            courses_dict[course].append(grade)

        for course, grades in courses_dict.items():
            max_grade = max(grades)
            min_grade = min(grades)
            avg_grade = sum(grades) / len(grades)
            results.append({
                'course': course,
                'max': max_grade,
                'min': min_grade,
                'avg': avg_grade
            })
        return results
    except Exception as e:
        print(f"Error retrieving from db or calculating: {e}")
        return []
    finally:
        cursor.close()
        connector.close()

def store_results(results):
    try:
        mongo_db = MONGO_CLIENT['results_db']
        mongo_collection = mongo_db['subject_stats']
        mongo_collection.delete_many({})
        mongo_collection.insert_many(results)
        return "Ok"
    except Exception as e:
        print(f"Error writing to MongoDB: {e}")
        return "Error writing to MongoDB"

@app.route('/analytics', methods=['POST'])
def analytics():
    results = calculations()
    message = store_results(results)
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
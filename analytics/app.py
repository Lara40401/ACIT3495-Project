import os
import mysql.connector
import pymongo
import time

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE")
}

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
DB_NAME = os.getenv("MONGO_INITDB_DATABASE")

def calculations():
    connector = None
    cursor = None
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
            avg_grade = round(sum(grades) / len(grades), 2)

            results.append({
                "course": course,
                "max": max_grade,
                "min": min_grade,
                "avg": avg_grade
            })
        
        return results
    
    except Exception as e:
        print(f"Error retrieving from db or calculating: {e}")
        return []
    
    finally:
        if connector:
            connector.close()

def store_results(results):
    try:
        client = pymongo.MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@mongo:27017/",authSource=DB_NAME)
        mongo_db = client[DB_NAME]
        mongo_collection = mongo_db["course_stats"]
        mongo_collection.delete_many({})
        mongo_collection.insert_many(results)
    
    except Exception as e:
        print(f"Error writing to MongoDB: {e}")
    
    finally:
        client.close()

def analytics():
    while True:
        results = calculations()
        if results:
            store_results(results)

        # Runs every 10 seconds
        time.sleep(10)

if __name__ == '__main__':
    analytics()

import time
import redis
import mysql.connector

redis_client = redis.Redis(host='localhost', port=6379)
db_connection = mysql.connector.connect(
    host='localhost',
    user='user',
    password='password',
    database='task_db'
)

def process_task(task_id):
    cursor = db_connection.cursor()
    cursor.execute("SELECT task_name FROM Task WHERE id = %s", (task_id,))
    task = cursor.fetchone()

    if task:
        task_name = task[0]
        # Simulating task processing
        time.sleep(5)  # Simulate long-running task
        result = f"Processed {task_name}"
        
        # Update task result in the database
        cursor.execute("UPDATE Task SET status = %s, result = %s WHERE id = %s", ('completed', result, task_id))
        db_connection.commit()
    cursor.close()

def main():
    while True:
        task_id = redis_client.brpop('task_queue', timeout=0)  # Block until a task is available
        if task_id:
            process_task(task_id[1])

if __name__ == '__main__':
    main()

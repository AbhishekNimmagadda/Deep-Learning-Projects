import requests
import psycopg2
from datetime import datetime

# Function to make prediction request and save to database
def save_prediction(input_data):
    try:
        # Make a request to your Flask API endpoint to get prediction
        url = 'http://localhost:5000/predict'  # Adjust URL if necessary
        data = {'input': input_data}
        response = requests.post(url, json=data)

        # Assuming response is JSON with 'prediction' key
        prediction_value = float(response.json()['prediction'][0])
        
        # Im adding a new comment to this code
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname='abhi-db',
            user='postgres',
            password='postgres',
            host='3.80.146.128',
            port='5432'
        )

        # Create a cursor object using the connection
        cursor = conn.cursor()

        # Prepare SQL statement to insert data
        insert_query = """
        INSERT INTO predictions.predictions (input_data, prediction, timestamp)
        VALUES (%s, %s, %s)
        """

        # Execute the SQL statement with data
        timestamp = datetime.utcnow()
        cursor.execute(insert_query, (str(input_data), prediction_value, timestamp))
        
        conn.commit()
        print(f"Saved prediction to database: input_data={input_data}, prediction={prediction_value}, timestamp={timestamp}")

    except requests.exceptions.RequestException as e:
        print(f"Error making request to the prediction API: {e}")
    except psycopg2.Error as e:
        print(f"Database error: {e.pgcode} - {e.pgerror}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure cursor and connection are closed
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    

# Example usage
if __name__ == '__main__':
    input_data = [120.0, 121.5, 122.0, 123.5, 124.0]  # Replace with your input data
    save_prediction(input_data)

from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Function to read names from file
def read_names_from_file():
    try:
        with open('baby_names.txt', 'r') as file:
            names = file.read().splitlines()
        return names
    except FileNotFoundError:
        print("Error: baby_names.txt file not found.")
        return []
    except Exception as e:
        print(f"Error reading baby_names.txt: {e}")
        return []


# List of baby names
baby_names = read_names_from_file()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_name():
    generated_name = random.choice(baby_names)
    return render_template('index.html', generated_name=generated_name)

if __name__ == '__main__':
    app.run(debug=True)

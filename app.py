from flask import Flask, render_template, url_for

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Projects Route
@app.route('/projects')
def projects():
    project_data = [
        {
            "name": "Project 1",
            "description": "Web development project using HTML, CSS, and JavaScript.",
            "image": "image1.jpg",
            "link": "https://link-to-project1.com"
        },
        {
            "name": "Project 2",
            "description": "Full-stack application with Flask and React.",
            "image": "image2.jpg",
            "link": "https://link-to-project2.com"
        },
        {
            "name": "Project 3",
            "description": "Machine learning project focusing on data analysis.",
            "image": "image3.jpg",
            "link": "https://link-to-project3.com"
        },
        {
            "name": "Project 4",
            "description": "AI-based system for predictive analysis with Python and TensorFlow.",
            "image": "image4.jpg",
            "link": "https://link-to-project4.com"
        },
        {
            "name": "Project 5",
            "description": "IoT device for monitoring environmental conditions.",
            "image": "image5.jpg",
            "link": "https://link-to-project5.com"
        }
    ]
    return render_template('projects.html', projects=project_data)

# Profile Route
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Contact Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

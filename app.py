from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

load_dotenv()  

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# rest of your code...
@app.route("/")
def home():
    skills = [
        {
            "name": "HTML/CSS",
            "level": 80,
            "image": "htmlcss.png",
            "color": "#f5622d",
            "score": 8,
        },
        {
            "name": "Javascript",
            "level": 60,
            "image": "javascript.svg",
            "color": "#ffde25",
            "score": 6,
        },
        {
            "name": "Django",
            "level": 90,
            "image": "django.png",
            "color": "#2ba977",
            "score": 9,
        },
        {
            "name": "Davinci Resolve",
            "level": 80,
            "image": "davinci-resolve.png",
            "color": "#383838",
            "score": 8,
        },
        {
            "name": "Figma",
            "level": 50,
            "image": "figma.png",
            "color": "#3075e8",
            "score": 5,
        },
        {
            "name": "Canva",
            "level": 80,
            "image": "canva.png",
            "color": "#3675d9",
            "score": 8,
        },
        {
            "name": "Python",
            "level": 80,
            "image": "python.png",
            "color": "#ffe161",
            "score": 8,
        },
        {
            "name": "C",
            "level": 60,
            "image": "clang.png",
            "color": "#004482",
            "score": 6,
        },
        {
            "name": "C++",
            "level": 70,
            "image": "cpp.png",
            "color": "#00599c",
            "score": 7,
        },
        {
            "name": "Android studio",
            "level": 60,
            "image": "android-studio.png",
            "color": "#eeeeee",
            "score": 6,
        },
        {
            "name": "Firebase",
            "level": 70,
            "image": "firebase.png",
            "color": "#fcca3f",
            "score": 7,
        },
        {
            "name": "sqlite",
            "level": 70,
            "image": "sqlite.png",
            "color": "#6cbde9",
            "score": 7,
        },
    ]

    education = [
        {
            "name": "B.Tech",
            "course": "CSE",
            "year": "2023-2027",
            "institute": "SRM Institute of Science and Technology",
            "image": "srmrmp.webp",
            "location": "Ramapuram, Chennai",
            "score": "GPA: 9.72",
        },
        {
            "name": "Higher Secondary",
            "course": "CS Stream",
            "year": "2021-2023",
            "institute": "SBOA Mat. & Hr. Sec. School",
            "image": "sboa.webp",
            "location": "Anna Nagar, Chennai",
            "score": "HSC +2: 89.17% <br>HSC +1: 84%",
        },
    ]

    themes = ["Full Stack Development", "Video Editing", "Graphic Design"]

    portfolio = [
        {
            "name": "Vendor Management System",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/Vendor-Management-System",
            "tech": "Django REST (Python)",
            "desc": "Provides API for tracking vendor performance metrics. ",
        },
        {
            "name": "Cryck",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/Cryck",
            "tech": "React JS, Solidity",
            "image": "Cryck.jpeg",
            "desc": "Revolutionizing cricket fandom with spatial predictions and immersive engagement with blockchain touch!",
        },
        {
            "name": "Thought Capsule",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/ThoughtCapsule",
            "tech": "Django (Python)",
            "image": "ThoughtCapsule.jpg",
            "desc": "Thought Capsule is a minimalist web platform, enhanced with AI capabilities, designed for capturing, storing, and interpreting personal thoughts, ideas, and moments. ",
        },
        {
            "name": "Synectt",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/SynecttWeb",
            "tech": "Django (Python)",
            "desc": "An event management app for Universities, Colleges and Schools. This project is used to integrate the Participant, Organiser, Sponsor, Control authorities in a single platform. Its right now just a prototype.",
        },
        {
            "name": "Djangy Bay",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/DjangoBay",
            "tech": "Django (Python)",
            "image": "DjangoBay.jpg",
            "desc": "eBay-like e-commerce auction site.",
        },
        {
            "name": "Wiki Online Encyclopedia",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/WikiOnlineEncyclopedia",
            "tech": "Django (Python)",
            "desc": "A Minimal Wikipedia Clone.",
        },
    ]

    return render_template(
        "index.html", skills=skills, education=education, portfolio=portfolio
    )

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Here you can handle the form data, e.g., send an email or store in a database.
    
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

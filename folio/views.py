from django.shortcuts import render

def home(request):
    skills = [
        {'name': 'HTML/CSS', 'level': 80, 'image': 'htmlcss.png', 'color': '#f5622d', 'score': 8},
        {'name': 'Javascript', 'level': 60, 'image': 'javascript.svg', 'color': '#ffde25', 'score': 6},
        {'name': 'Django', 'level': 90, 'image': 'django.png', 'color': '#2ba977', 'score': 9},
        {'name': 'Davinci Resolve', 'level': 80, 'image': 'davinci-resolve.png', 'color': '#383838', 'score': 8},
        {'name': 'Figma', 'level': 50, 'image': 'figma.png', 'color': '#3075e8', 'score': 5},
        {'name': 'Canva', 'level': 80, 'image': 'canva.png', 'color': '#3675d9', 'score': 8},
        {'name': 'Python', 'level': 80, 'image': 'python.png', 'color': '#ffe161', 'score': 8},
        {'name': 'C', 'level': 60, 'image': 'clang.png', 'color': '#004482', 'score': 6},
        {'name': 'C++', 'level': 70, 'image': 'cpp.png', 'color': '#00599c', 'score': 7},
        {'name': 'Android studio', 'level': 60, 'image': 'android-studio.png', 'color': '#eeeeee', 'score': 6},
        {'name': 'Firebase', 'level': 70, 'image': 'firebase.png', 'color': '#fcca3f', 'score': 7},
        {'name': 'sqlite', 'level': 70, 'image': 'sqlite.png', 'color': '#6cbde9', 'score': 7},
    ]

    return render(request, 'folio/index.html', {'skills': skills})
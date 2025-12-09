from django.shortcuts import render, get_object_or_404
from django.http import Http404
import os
import chardet
from .models import Project

# Vue pour la page d'accueil
def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})

# Vue pour la page de contact
def contact(request):
    return render(request, 'projects/contact.html')

# Vue pour le tableau de bord
def dashboard(request):
    categories = [
        {'name': 'Machine Learning', 'url': 'machine_learning'},
        {'name': 'Deep Learning', 'url': 'deep_learning'},
        {'name': 'Développement Web', 'url': 'web_development'},
        {'name': 'Data Ingénierie', 'url': 'data_engineering'},
        {'name': 'Développement Mobile', 'url': 'mobile_development'},
        {'name': 'Stages', 'url': 'internships'},
        {'name': 'Autres Projets Professionnels', 'url': 'other_projects'},
    ]
    return render(request, 'projects/dashboard.html', {'categories': categories})

# Vue pour lister les projets
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

# Vue pour une catégorie spécifique
def category_view(request, category_name):
    projects = Project.objects.filter(category=category_name)
    return render(request, 'projects/category.html', {'projects': projects, 'category_name': category_name})

# ✅ Vue pour afficher un notebook en HTML
def notebook_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    notebook_html_content = "<p>Aucun notebook disponible pour ce projet.</p>"

    if project.notebook_html and os.path.exists(project.notebook_html.path):
        try:
            # ✅ Détection de l'encodage du fichier HTML
            with open(project.notebook_html.path, "rb") as f:
                raw_data = f.read()
                detected_encoding = chardet.detect(raw_data)['encoding']

            # ✅ Lecture avec encodage détecté
            with open(project.notebook_html.path, "r", encoding=detected_encoding) as f:
                notebook_html_content = f.read()

            # ✅ Ajout du CSS pour harmoniser le style
            css_link = '<link rel="stylesheet" href="/static/css/style.css">'
            notebook_html_content = notebook_html_content.replace("</head>", f"{css_link}</head>", 1)

        except UnicodeDecodeError:
            notebook_html_content = "<p>Erreur lors du décodage du fichier Notebook. Essayez de le réenregistrer en UTF-8.</p>"
        except Exception as e:
            notebook_html_content = f"<p>Erreur : {str(e)}</p>"

    return render(request, 'projects/notebook_view.html', {
        'project': project,
        'notebook_html_content': notebook_html_content,
        'category_name': project.category
    })

# Vue pour afficher les détails d'un projet
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'category_name': project.category,
    })

# Vue pour afficher les technologies
def technologies_view(request):
    technologies = {
        "Langages de Programmation": {
            "slug": "langages-de-programmation",
            "items": ["Python", "JavaScript", "SQL", "HTML", "CSS"]
        },
        "Frameworks et Bibliothèques": {
            "slug": "frameworks-et-bibliotheques",
            "items": ["Django", "NumPy", "Pandas", "Scikit-learn", "Matplotlib", "Bootstrap", "Tailwind"]
        },
        "Outils et Plateformes": {
            "slug": "outils-et-plateformes",
            "items": ["Git", "GitHub", "Azure", "AWS"]
        },
        "Domaines Spécifiques": {
            "slug": "domaines-specifiques",
            "items": ["Machine Learning", "Deep Learning", "REST API"]
        },
    }
    return render(request, 'projects/technologies.html', {'technologies': technologies})

# Vue pour afficher les technologies par catégorie
def technologies_category_view(request, category):
    technologies_by_category = {
        "langages-de-programmation": ["Python", "JavaScript", "SQL", "HTML", "CSS"],
        "frameworks-et-bibliotheques": ["Django", "NumPy", "Pandas", "Scikit-learn", "Matplotlib", "Bootstrap", "Tailwind"],
        "outils-et-plateformes": ["Git", "GitHub", "Azure", "AWS"],
        "domaines-specifiques": ["Machine Learning", "Deep Learning", "REST API"]
    }
    technologies = technologies_by_category.get(category)
    if not technologies:
        raise Http404(f"La catégorie '{category}' n'existe pas.")
    return render(request, 'projects/technologies_category.html', {
        'category': category,
        'technologies': technologies
    })
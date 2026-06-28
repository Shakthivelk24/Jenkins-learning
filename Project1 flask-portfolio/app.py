from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# GitHub Profile
GITHUB_URL = "https://github.com/Shakthivelk24"

# LinkedIn Profile
LINKEDIN_URL = "https://www.linkedin.com/in/shakthi-vel-k-b35484343/"

# Projects
PROJECTS = {
    "dropzone": {
        "title": "☁️ DropZone",
        "description": "Cloud-based File Storage System built using the MERN stack with Cloudinary integration.",
        "url": "https://github.com/Shakthivelk24/DropZone",
        "gradient": "linear-gradient(135deg, #00c6ff 0%, #0072ff 100%)"
    },
    "aqualens": {
        "title": "🐟 AquaLens AI",
        "description": "AI-powered Fish Disease Detection using Deep Learning and Computer Vision.",
        "url": "https://github.com/Shakthivelk24/AquaLens-AI",
        "gradient": "linear-gradient(135deg, #43cea2 0%, #185a9d 100%)"
    },
    "magistra": {
        "title": "🎓 Magistra",
        "description": "An AI Teacher Assistant Platform powered by Gemini AI.",
        "url": "https://github.com/Shakthivelk24/Magistra",
        "gradient": "linear-gradient(135deg, #8e2de2 0%, #4a00e0 100%)"
    },
    "2dgame": {
        "title": "🎮 Blue Boy Adventure",
        "description": "A Java-based 2D Platform Adventure Game.",
        "url": "https://github.com/Shakthivelk24/2DGame",
        "gradient": "linear-gradient(135deg, #ff9966 0%, #ff5e62 100%)"
    }
}


@app.context_processor
def inject_globals():
    return {
        "GITHUB_URL": GITHUB_URL,
        "LINKEDIN_URL": LINKEDIN_URL,
        "PROJECTS": PROJECTS,
        "current_year": datetime.now().year
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/project/<project_name>")
def project(project_name):
    project = PROJECTS.get(project_name)

    if not project:
        return "Project Not Found", 404

    return render_template(
        "project.html",
        title=project["title"],
        description=project["description"],
        project_url=project["url"],
        gradient=project["gradient"]
    )


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
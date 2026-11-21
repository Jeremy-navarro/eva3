from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "API DevSecOps Activa y Protegida", 200

@app.route("/hello")
def hello():
    name = escape(request.args.get("name", "Invitado"))
    return f"Hello, {name}!"

@app.after_request
def add_security_headers(response):
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Server"] = "SecureServer"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

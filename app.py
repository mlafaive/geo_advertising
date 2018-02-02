from flask import Flask, render_template
import extensions
import controllers
import config
import hashlib, glob, os

from werkzeug.utils import secure_filename



# Initialize Flask app with the template folder address
app = Flask(__name__)

# Register the controllers
app.register_blueprint(controllers.main)

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host=config.env['host'], port=config.env['port'], debug=True)

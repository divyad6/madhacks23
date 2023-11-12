from flask import Flask, render_template, request
#from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image as img
import os

app = Flask(__name__, template_folder="templates", static_folder="./uploads")

# specify folder to store uploaded images for diff types
#photos = UploadSet("photos", IMAGES)
app.config['UPLOAD_FOLDER'] = 'uploads'
#configure_uploads(app, photos)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_images', methods=['POST'])
def process_images():
    # if request.method == "POST" and "photo" in request.files:
    #     photo = request.files["photo"]
    #     if photo:
    #         # Save the uploaded files
    #         filename = photos.save(photo)

    #         return "File uploaded successfully!"

    # return render_template("upload.html")
    
    if 'file' not in request.files:
        # handle the case where no file is uploaded
        return 'no file part'

    # files = request.files.getlist('file')

    # for file in files:
    #     if 'shirt' in file.filename:  # Checking if the file is a top
    #         img.save(os.path.join(app.config['UPLOAD_FOLDER'], 'tops', file.filename))
    #         #file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'tops', file.filename))
    #     elif 'pants' in file.filename:  # Checking if the file is a bottom
    #         img.save(os.path.join(app.config['UPLOAD_FOLDER'], 'bottoms', file.filename))
    #         #file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'bottoms', file.filename))

    return 'files uploaded successfully'

@app.route('/mix_match.html')
def mix_match():
    top_images = os.listdir(os.path.join(app.config['UPLOAD_FOLDER'], 'tops'))
    bottom_images = os.listdir(os.path.join(app.config['UPLOAD_FOLDER'], 'bottoms'))
    return render_template('mix_match.html', top_images=top_images, bottom_images=bottom_images)

if __name__ == '__main__':
    app.run(debug=True)

from werkzeug.utils import secure_filename
import os
import base64

UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class Item:
    @classmethod
    def allowed_file(cls, filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @classmethod
    def save_img(cls, file):
        decodedFile = base64.b64decode(file)
        import pdb; pdb.set_trace()
        if decodedFile and cls.allowed_file(decodedFile.filename):
           
            filename = secure_filename(decodedFile.filename)
            decodedFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

from werkzeug.utils import secure_filename
from io import BytesIO
from PIL import Image
import os
import base64

os.environ['IMAGE_PATH'] = 'C:/Users/user/Documents/Visual Studio 2019/far-north/static/images'

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class Item:
    @classmethod
    def allowed_file(cls, filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @classmethod
    def save_img(cls, file, name):
        starter = file.find(',')
        image_data = file[starter+1:]
        decoded = BytesIO(base64.b64decode(image_data))
        im = Image.open(decoded)
      
        im.save(f'C:/Users/user/Documents/Visual Studio 2019/far-north/static/images/{name}.jpg')


        # if decodedFile:
        #     filename = secure_filename(decodedFile.filename)
        #     decodedFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

       
        # image_data = bytes(image_data, encoding="ascii")
        # im = Image.open(BytesIO(base64.b64decode(image_data)))
        # im.save('image.jpg')

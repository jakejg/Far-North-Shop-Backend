from werkzeug.utils import secure_filename
from io import BytesIO
from PIL import Image
import os
import base64

os.environ['IMAGE_PATH'] = 'C:/Users/user/Documents/Visual Studio 2019/far-north/static/images'


class Item:
    def __init__(self, description, price, type, img, quantity, name):
        self.description = description
        self.price = price
        self.type = type
        self.img = img
        self.quantity = quantity
        self.name = name

    
    def get_img_name(self):
        """ Extract image name from file name and extension """

        name = self.img
        idx = name.rindex(".")
        return name[:idx]

    @classmethod
    def save_img(cls, base64Image, name):
        """ Decode bas64 image and save in images folder on server """

        starter = base64Image.find(',')
        image_data = base64Image[starter+1:]
        decoded = BytesIO(base64.b64decode(image_data))
        im = Image.open(decoded)
      
        im.save(f'C:/Users/user/Documents/Visual Studio 2019/far-north/static/images/{name}.jpg')


        # if decodedFile:
        #     filename = secure_filename(decodedFile.filename)
        #     decodedFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

       
        # image_data = bytes(image_data, encoding="ascii")
        # im = Image.open(BytesIO(base64.b64decode(image_data)))
        # im.save('image.jpg')

import io
import os
from google.cloud import vision
from google.cloud.vision import types

#Using Google Vision API
client = vision.ImageAnnotatorClient()

#must replace this with a getter for a picture
picture_name = 'test.jpg'
photos_directory = 'Photos'
#gets the path to the targeted picture (must input the name of the picture)
file_name = os.path.join(os.path.dirname(__file__), '..', photos_directory, picture_name)

#opening the file name
with io.open(file_name,'rb') as image_file:
    content = image_file.read();

#getting the image
image = types.Image(content=content)

#getting the response
objects = client.object_localization(image=image).localized_object_annotations

#getting the labels
print('Number of objects found: {}'.format(len(objects)))
for object_ in objects:
    print('\n{} (confidence: {})'.format(object_.name, object_.score))
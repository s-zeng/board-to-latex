import io

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
# Instantiates a client
from google.protobuf.json_format import MessageToDict

client = vision.ImageAnnotatorClient()


def get_text(image_path):
    try:
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
        # Performs text detection on the image file
        response = client.document_text_detection(image=image)
        return MessageToDict(response, preserving_proto_field_name=True)['text_annotations']
    except IOError:
        return None

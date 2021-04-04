import face_recognition
import json
from PIL import Image, ImageDraw

image = face_recognition.load_image_file("group2.png")

face_feature_list = face_recognition.face_landmarks(image)
#print(f"Face Landmarks: {json.dumps(face_feature_list,indent =4)}")

pil_image = Image.fromarray(image)

for index, face_landmark in enumerate(face_feature_list):
    img_draw = ImageDraw.Draw(pil_image,"RGBA")

    img_draw.polygon(face_landmark['top_lip'], fill=(255,0,0, 128))
    img_draw.polygon(face_landmark['bottom_lip'], fill=(255,0,0,128))
    #img_draw.polygon(face_landmark['chin'], fill=(255,192,203,128))
    img_draw.polygon(face_landmark['left_eyebrow'], fill=(0,0,0,128))
    img_draw.polygon(face_landmark['right_eyebrow'], fill=(0,0,0,128))
    img_draw.polygon(face_landmark['nose_bridge'], fill=(0,0,0,128))
    pil_image.show()
    pil_image.save(str(index)+"editedgroup.jpg")
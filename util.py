import joblib
import json
import numpy as np
import base64
import cv2
from wavelet import w2d

__class_name_to_number = {}
__class_number_to_name = {}

__model = None

def classify_image(img_base64_data, file_path = None):
    imgs = get_cropped_image_if_2_eyes(file_path, img_base64_data)
    result = []
    for img in imgs:
        scaled_imgt = cv2.resize(img,(32,32))
        imgt_haar = w2d(img,'db1',5)
        scaled_imgt_haar = cv2.resize(imgt_haar,(32,32))
        combined_img = np.vstack((scaled_imgt.reshape(32*32*3,1),scaled_imgt_haar.reshape(32*32,1)))

        len_img_array = 32*32*3 +32*32
        final = combined_img.reshape(1,len_img_array).astype(float)

        result.append({
            'class': class_number_to_name(int(__model.predict(final)[0])),
            'class_probability': np.round(__model.predict_proba(final)*100,2).tolist()[0],
            'class_dictionary': __class_name_to_number
        })

    return result

def load_artifacts():
    print("Loading Artifacts...start")
    global __class_name_to_number
    global __class_number_to_name

    with open("./Artifacts/class_dictionary.json", "r") as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {v:k for k,v in __class_name_to_number.items()}

    global __model
    if __model is None:
        with open("./Artifacts/saved_model.pkl","rb") as f:
            __model = joblib.load(f)
    print("Loading Artifacts...done")

def get_cv2_image_from_base64_string(b64str):
    '''
    credit: https://stackoverflow.com/questions/33754935/read-a-base-64-encoded-image-from-memory-using-opencv-python-library
    :param uri:
    :return:
    '''
    encoded_data = b64str.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def get_cropped_image_if_2_eyes(image_path, image_base64_data):
    face_cascade = cv2.CascadeClassifier('./openCV/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./openCV/haarcascades/haarcascade_eye.xml')

    if image_path:
        img = cv2.imread(image_path)
    else:
        img = get_cv2_image_from_base64_string(image_base64_data)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    cropped_faces = []
    for (x,y,w,h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            if len(eyes) >= 2:
                cropped_faces.append(roi_color)
    return cropped_faces

def class_number_to_name(class_num):
    return __class_number_to_name[class_num]

def get_b64_test():
    with open("./b64.txt") as f:
        return f.read()
    
if __name__ == "__main__":
    load_artifacts()
    print(classify_image(None, "./ead8314-9d5d-4039-b3b2-f3aba3641296.jpeg"))
   
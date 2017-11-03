from pkg_resources import resource_filename

def pose_predictor_model_location():
    return resource_filename(__name__, "face_landmarks_68.dat")

def pose_predictor_five_point_model_location():
    return resource_filename(__name__, "face_landmarks_5.dat")

def face_recognition_model_location():
    return resource_filename(__name__, "dlib_model.dat")

def cnn_face_detector_model_location():
    return resource_filename(__name__, "face_detector.dat")

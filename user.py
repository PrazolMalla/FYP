#* importing different libraries  
import csv
import copy
import argparse
import itertools
from gtts import gTTS
import os
import pyglet
from io import BytesIO
import threading
from playsound import playsound
import platform
import cv2 as cv
import numpy as np
import mediapipe as mp

from utils import CvFpsCalc
from model import KeyPointClassifier
from collection import get_args,calc_bounding_rect,calc_landmark_list,pre_process_landmark,draw_landmarks,draw_info





def main():
    #******************* Argument parsing ****************************#
    args = get_args()

    cap_device = args.device
    cap_width = args.width
    cap_height = args.height

    use_static_image_mode = args.use_static_image_mode
    min_detection_confidence = args.min_detection_confidence
    min_tracking_confidence = args.min_tracking_confidence

    use_brect = True

    #************** Camera preparation***************************#
    cap = cv.VideoCapture(cap_device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    #************* Model load **********************************#
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=use_static_image_mode,
        max_num_hands=1,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence,
    )

    keypoint_classifier = KeyPointClassifier()

    with open('model/keypoint_classifier/keypoint_classifier_label.csv',
              encoding='utf-8-sig') as f:
        keypoint_classifier_labels = csv.reader(f)
        keypoint_classifier_labels = [
            row[0] for row in keypoint_classifier_labels
        ]
    
    cvFpsCalc = CvFpsCalc(buffer_len=10)

    # history_length = 16

    
    mode = 0

    while True:
        fps = cvFpsCalc.get()

        #******  Process Key (ESC: end) ********************#
        key = cv.waitKey(10)
        if key == 27:  # ESC
            break
        # number, mode = select_mode(key, mode)

        #******************* Camera capture ****************#
        ret, image = cap.read()
        if not ret:
            break
        image = cv.flip(image, 1)  #* Mirror display
        debug_image = copy.deepcopy(image)

        #************* Detection implementation ************#
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True

        #************ processes hand tracking data **************************#
        if results.multi_hand_landmarks is not None:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks,
                                                  results.multi_handedness):
                # *Bounding box calculation
                brect = calc_bounding_rect(debug_image, hand_landmarks)
                # *Landmark calculation
                landmark_list = calc_landmark_list(debug_image, hand_landmarks)

                #* Conversion to relative coordinates / normalized coordinates
                pre_processed_landmark_list = pre_process_landmark(
                    landmark_list)
                
                
                #* Hand sign classification
                hand_sign_id = keypoint_classifier(pre_processed_landmark_list)
                

              
                #* Drawing part
                debug_image = draw_bounding_rect(use_brect, debug_image, brect)
                debug_image = draw_landmarks(debug_image, landmark_list)
                debug_image = draw_info_text(
                    debug_image,
                    brect,
                    handedness,
                    keypoint_classifier_labels[hand_sign_id],
                )
        number=0
        debug_image = draw_info(debug_image, fps, mode,number)

        cv.imshow('Hand Gesture Recognition', debug_image)

    cap.release()
    cv.destroyAllWindows()


def draw_bounding_rect(use_brect, image, brect):
    if use_brect:
        #* Outer rectangle
        cv.rectangle(image, (brect[0], brect[1]), (brect[2], brect[3]),
                     (0, 0, 0), 1)

    return image

sign = " " #* Global variable sign is used to compare with hand_sign_text for the first time
lock = threading.Lock()
def draw_info_text(image, brect, handedness, hand_sign_text):
    cv.rectangle(image, (brect[0], brect[1]), (brect[2], brect[1] - 22),
                 (0, 0, 0), -1)

    info_text = handedness.classification[0].label[0:]
   
    if hand_sign_text != "":
        info_text = info_text + ':' + hand_sign_text
        cv.putText(image, info_text, (brect[0] + 5, brect[1] - 4),
                cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv.LINE_AA)
        
        threading.Thread(target=play_audio_threaded, args=(hand_sign_text,)).start()
    return image

def play_audio_threaded(text):
    global sign
    
    if sign != text:
        
        sign = text
        lock.acquire()
        speech = gTTS(text=text, lang='en', tld='us')
        speech_bytes = BytesIO()
        speech.write_to_fp(speech_bytes)
        speech_bytes.seek(0)
        temp_file = "temp.mp3"
        with open(temp_file, 'wb') as f:
            f.write(speech_bytes.read())
        if platform.system()=="Darwin":
            playsound(temp_file)
        else:
            music = pyglet.media.load(temp_file, streaming=False)
            music.play()
        
        os.remove(temp_file)
        lock.release()

if __name__ == '__main__':
    main()
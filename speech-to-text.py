import speech_recognition 
import os
import cv2
def play_video(word):
        # Check if the video file exists for the given word
    video_file_path = f"video/{word}.mp4"
    if not os.path.exists(video_file_path):
        cap = cv2.VideoCapture("video/idle.mp4")
    else:
        cap = cv2.VideoCapture(video_file_path)
    # Play the video
    

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame,(540,960))
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    

sr = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source2:
    print("Silent Please")

    sr.adjust_for_ambient_noise(source2,duration=2)

    print("Speak now Please")

    audio2 = sr.listen(source2)

    texxt = sr.recognize_google(audio2)

    texxt = texxt.lower()

    print("Did you Say:_ "+texxt)

keywords = list()

keywords = texxt.split()
print(keywords)

for keyword in keywords:
    play_video(keyword)    

cv2.destroyAllWindows()



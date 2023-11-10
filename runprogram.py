from subprocess import call 
def open_sign_to_speech():
    call(['python',"app.py"])

def open_speech_to_sign():
    call(['python','speech-to-text.py'])

def open_main_ui():
    call(['python','ui.py'])
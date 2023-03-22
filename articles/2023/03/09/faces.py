import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def gen_frames():
    camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()
        if not success:
            print("Tarapaty")
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                        
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                
            cv2.imshow('Frame', frame)
            # cv2.imshow('frame', gray)
            if cv2.waitKey(1) == ord('q'):
                break

    camera.release()
    
def main():
    gen_frames()  
            
if __name__ == '__main__':
    main()
import tkinter as tk
from imutils.video import VideoStream
import face_recognition
from imutils import resize
import pickle
import time
import cv2

def camera():
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    time.sleep(2.0)

    while True:
        # grab the frame from the threaded video stream and resize it
        # to 500px (to speedup processing)
        frame = vs.read()
        frame = resize(frame, width=500)

        # convert the input frame from (1) BGR to grayscale (for face
        # detection) and (2) from BGR to RGB (for face recognition)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

        # Display the frame in a Tkinter window
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)
        panel.img = img  # keep a reference to prevent the image from being garbage collected
        panel.config(image=img)
        panel.update_idletasks()

    # Close the OpenCV window and stop the video stream when 'q' is pressed
    cv2.destroyAllWindows()
    vs.stop()

# Create the Tkinter window
parent = tk.Tk()
parent.title("Camera GUI")

# Create a Tkinter frame
frame = tk.Frame(parent)
frame.pack()

# Create "Camera On" button
text_disp = tk.Button(frame, text="Camera On", command=camera)
text_disp.pack(side=tk.LEFT)

# Create "Camera Off" button
exit_button = tk.Button(frame, text="Camera Off", fg="green", command=quit)
exit_button.pack(side=tk.RIGHT)

# Create a Tkinter label to display the video stream
panel = tk.Label(parent)
panel.pack()

# Start the Tkinter event loop
parent.mainloop()

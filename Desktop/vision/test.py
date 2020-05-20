import tkinter
import cv2
from PIL import ImageTk
import PIL.Image, PIL.ImageTk
import time

class App:
 def __init__(self, window, window_title, video_source=0):
  self.window = window
  self.window.title(window_title)
  self.flip = 0
  self.dispW = 640
  self.dispH = 480
  self.video_source ='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(self.flip)+' ! video/x-raw, width='+str(self.dispW)+', height='+str(self.dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'


        # open video source (by default this will try to open the computer webcam)
  self.vid = MyVideoCapture(self.video_source)

# Create a canvas that can fit the above video source size
  self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
  self.canvas.pack()

         # Button that lets the user take a snapshot
  self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
  self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)
 
         # After it is called once, the update method will be automatically called every delay milliseconds
  self.delay = 15
  self.update()
  self.insertImageToCanvas()
  self.window.mainloop()
 
 def snapshot(self):
    fileName = "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S")
 
    self.canvas.postscript(file = fileName + '.ps') 
    # use PIL to convert to PNG 
    img = PIL.Image.open(fileName + '.ps') 
    img.save(fileName + '.png', 'png') 
         # Get a frame from the video source
        # ret, frame = self.vid.get_frame()
 
        # if ret:
        #      cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
 def insertImageToCanvas(self):
   img = PIL.Image.open("images.jpeg")
   img = img.resize((300, 300), PIL.Image.ANTIALIAS)
   img = PIL.ImageTk.PhotoImage(img)  
   self.canvas.create_image(350, 0, image=img, anchor= tkinter.NW)
   self.window.mainloop()

 def update(self):
         # Get a frame from the video source
         ret, frame = self.vid.get_frame()
         if ret:
             self.photo = PIL.Image.fromarray(frame)
             self.photo = self.photo.resize((300,300), PIL.Image.ANTIALIAS)
             self.photo = ImageTk.PhotoImage(image = self.photo)
             self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
 
         self.window.after(self.delay, self.update)

class MyVideoCapture:
     def __init__(self, video_source=0):
         # Open the video source
        #cam= cv2.VideoCapture(camSet)
        print("Chris:  " +  video_source + "\n")
        self.vid = cv2.VideoCapture(video_source, cv2.CAP_GSTREAMER)
        if not self.vid.isOpened():
           raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
     def get_frame(self):
        if self.vid.isOpened():
             ret, frame = self.vid.read()
             if ret:
                # Return a boolean success flag and the current frame converted to BGR
                 return (ret, frame)#cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
             else:
                 return (ret, None)
        else:
             return (ret, None)
 
   # Release the video source when the object is destroyed
     def __del__(self):
      if self.vid.isOpened():
       self.vid.release()
 
 # Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")


import cv2
import numpy as np





# to load Yolo;
net = cv2.dnn.readNet("yolov3/yolov3.weights", "yolov3/yolov3.cfg")



classes = []
with open("yolov3/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()




# have to modify the format of layer_names;hard to understand the errors;
# output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]



colors = np.random.uniform(0, 255, size=(len(classes), 3))




# Loading image
img = cv2.imread("image/people2.jpg")
# img = cv2.resize(img, None, fx=0.4, fy=0.4)
img = cv2.resize(img, None, fx=1, fy=1)
height, width, channels = img.shape






# Detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)


# Showing informations on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)





indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
# indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)



font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[i]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




# print('hello,kitty')
'''
Created by T.S
Rawin Chaisittiporn

'''

import cv2
import numpy as np

cam= cv2.VideoCapture(0)

boundaries = [
	([86, 31, 4], [220, 88, 50]),	
]

while True:
    ret, image=cam.read()
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask = mask)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

            # only proceed if at least one contour was found
        if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                if M["m00"] == 0:
                    M["m00"] = 0.1

                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                # only proceed if the radius meets a minimum size. Correct this value for your obect's size
                if radius > 0.5:
                    cv2.circle(image, (int(x), int(y)), int(radius), (0,255,0), 2)
                    cv2.putText(image," blue", (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,0,0),2)


        cv2.imshow("images", np.hstack([image, output]))
        cv2.waitKey(10)

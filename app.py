import cv2
import mediapipe as mp
import numpy as np


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


cap = cv2.VideoCapture(0)


canvas = None

prev_x, prev_y = 0, 0

# Default color
draw_color = (255, 0, 255)

brush = 6



def get_gesture(hand):

    fingers = []

    # Thumb
    if hand.landmark[4].x < hand.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)


    tips = [8,12,16,20]
    pips = [6,10,14,18]


    for tip,pip in zip(tips,pips):

        if hand.landmark[tip].y < hand.landmark[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)


    total = sum(fingers)


    if total == 5:
        return "OPEN PALM"

    elif total == 0:
        return "FIST"

    elif fingers[1] == 1 and total == 1:
        return "POINT"

    elif fingers[1] == 1 and fingers[2] == 1 and total == 2:
        return "VICTORY"

    elif fingers[0] == 1 and total == 1:
        return "THUMB UP"


    return "UNKNOWN"



while True:

    success, img = cap.read()

    if not success:
        break


    img = cv2.flip(img, 1)


    if canvas is None:
        canvas = np.zeros_like(img)


    rgb = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB
    )


    result = hands.process(rgb)


    gesture = "No Hand"



    if result.multi_hand_landmarks:


        for hand in result.multi_hand_landmarks:


            gesture = get_gesture(hand)


            lm = hand.landmark


            # Index finger position
            x = int(lm[8].x * img.shape[1])
            y = int(lm[8].y * img.shape[0])



            # Draw only with pointing finger

            if gesture == "POINT":


                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y


                cv2.line(
                    canvas,
                    (prev_x, prev_y),
                    (x, y),
                    draw_color,
                    brush
                )


                prev_x, prev_y = x, y


            else:
                prev_x, prev_y = 0, 0



            mp_draw.draw_landmarks(
                img,
                hand,
                mp_hands.HAND_CONNECTIONS
            )



    output = cv2.addWeighted(
        img,
        0.7,
        canvas,
        0.3,
        0
    )


    cv2.putText(
        output,
        "Gesture: " + gesture,
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )


    cv2.putText(
        output,
        "R=Red G=Green B=Blue E=Erase C=Clear Q=Quit",
        (20,75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,255),
        2
    )



    cv2.imshow(
        "AI Air Canvas",
        output
    )



    key = cv2.waitKey(1) & 0xFF


    if key == ord('r'):
        draw_color = (0,0,255)


    elif key == ord('g'):
        draw_color = (0,255,0)


    elif key == ord('b'):
        draw_color = (255,0,0)


    elif key == ord('e'):
        draw_color = (0,0,0)


    elif key == ord('c'):
        canvas = np.zeros_like(img)


    elif key == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
import cv2
import mediapipe as mp
import pyautogui

# Initialize
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

screen_w, screen_h = pyautogui.size()
cap = cv2.VideoCapture(0)

# Smooth mouse
prev_x, prev_y = 0, 0
smooth = 5

def is_finger_up(lm_list, tip, pip):
    return lm_list[tip].y < lm_list[pip].y

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_lms in result.multi_hand_landmarks:
            lm_list = hand_lms.landmark

            # Index finger tip
            ix = lm_list[8].x
            iy = lm_list[8].y

            # Convert to screen coordinates
            cx = int(ix * screen_w)
            cy = int(iy * screen_h)

            # Smooth cursor movement
            mouse_x = prev_x + (cx - prev_x) / smooth
            mouse_y = prev_y + (cy - prev_y) / smooth
            pyautogui.moveTo(mouse_x, mouse_y)
            prev_x, prev_y = mouse_x, mouse_y

            # Gesture detection
            index_up = is_finger_up(lm_list, 8, 6)
            middle_up = is_finger_up(lm_list, 12, 10)

            # Left click: only index up
            if index_up and not middle_up:
                pyautogui.click()
            # Scroll: both index and middle up, move vertically
            if index_up and middle_up:
                # positive dy -> scroll down, negative -> up
                dy = (iy - 0.5) * 40
                pyautogui.scroll(int(-dy))

            # Draw landmarks for visualization
            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("AI Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == 27:   # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()

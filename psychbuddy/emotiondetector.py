import cv2
import time
from deepface import DeepFace
from collections import defaultdict

def detect_emo(duration=60, min_confidence=0.5):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    print(f"Camera feed will run for {duration} seconds with emotion detection.")
    start_time = time.time()

    emotion_durations = defaultdict(float)
    last_emotion = None
    emotion_start_time = None
    recent_emotions = []  
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame.")
            break

        emotion = "Unknown"
        confidence = 0.0

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
            confidence = result[0]['emotion'][emotion]  

            recent_emotions.append((emotion, confidence))
            if len(recent_emotions) > 5:  
                recent_emotions.pop(0)

            emotion_counts = defaultdict(float)
            for e, conf in recent_emotions:
                if conf >= min_confidence:
                    emotion_counts[e] += conf

            if emotion_counts:
                smoothed_emotion = max(emotion_counts, key=emotion_counts.get)
                smoothed_confidence = emotion_counts[smoothed_emotion]

                if smoothed_confidence >= min_confidence:
                    emotion = smoothed_emotion
                else:
                    emotion = "Unknown"

            if last_emotion is not None and last_emotion != emotion:
                duration_since_last_change = time.time() - emotion_start_time
                emotion_durations[last_emotion] += duration_since_last_change

            last_emotion = emotion
            emotion_start_time = time.time()

        except Exception as e:
            print(f"Error in emotion detection: {e}")

        cv2.putText(frame, f"Emotion: {emotion} ({confidence:.2f})", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Psychbuddy Emotion Recognizer", frame)

        elapsed_time = time.time() - start_time
        if elapsed_time > duration:
            print("Time limit reached. Exiting...")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    if last_emotion is not None:
        duration_since_last_change = time.time() - emotion_start_time
        emotion_durations[last_emotion] += duration_since_last_change

    if emotion_durations:
        most_common_emotion = max(emotion_durations, key=emotion_durations.get)
        total_duration = emotion_durations[most_common_emotion]
        print(f"The most common emotion detected based on duration: {most_common_emotion} for {total_duration:.2f} seconds")
    else:
        print("No emotions detected during the session.")

    return most_common_emotion

import cv2
def detect_and_draw_people(frame):
    # detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # analiza person
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8), padding=(8, 8), scale=1.05)

    if len(boxes) > 0:
        # graba el video cuando se detecten personas
        if not hasattr(detect_and_draw_people, "video_writer") or detect_and_draw_people.video_writer is None:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            detect_and_draw_people.video_writer = cv2.VideoWriter('Movimiento_detect.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
        detect_and_draw_people.video_writer.write(frame)
    else:
        # detiene la grabacion si no hay deteccion
        if hasattr(detect_and_draw_people, "video_writer") and detect_and_draw_people.video_writer is not None:
            detect_and_draw_people.video_writer.release()
            detect_and_draw_people.video_writer = None

    # rectangulo en las personas
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame
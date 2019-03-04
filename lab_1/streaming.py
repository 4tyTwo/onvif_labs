import cv2

def formatUrl(protocol, login, password, ip, port, path):
    return protocol + '://' + login + ':' + password + '@' + ip + ':' + str(port) + path

def captureStream(protocol, login, password, ip, port, path, height=320, width=640):
    url = formatUrl(protocol, login, password, ip, port, path)
    print('Capturing video stream from', url)
    cap = cv2.VideoCapture(url)
    cv2.namedWindow('Room 513', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Room 513', width, height)
    # cap = cv2.VideoCapture('rtsp://iigortoporkov:FP72Ainc6pwR@192.168.15.42:554/Streaming/channels/101')
    while(True):
        cap.set(3, height)
        cap.set(4, width)
        ret, frame = cap.read()
        cv2.imshow('Room 513', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

import socket
import struct
import cv2
import numpy

# address = ("192.168.1.158", 12801)
ADDRESS = ("192.168.0.31", 1235)

SURFACE_SIZE = (680, 480)


def run_show_image():

    print("Running image processing")

    s = socket.socket()
    s.connect(ADDRESS)

    try:
        running = True
        while running:
            # receive size
            len_str = s.recv(4)
            size = struct.unpack('!i', len_str)[0]

            print('size:', size)

            # receive string

            img_str = b''

            while size > 0:
                if size >= 4096:
                    data = s.recv(4096)
                else:
                    data = s.recv(size)

                if not data:
                    break

                size -= len(data)
                img_str += data

            print('len:', len(img_str))
            # convert string to surface

            nparr = numpy.fromstring(img_str, numpy.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            #cv2.imwrite("image_processed.png", frame)
            cv2.imshow("CAR 1", frame)
            cv2.waitKey(1)

    except Exception as e:
        print(e)
    finally:
        # exit
        print("Closing socket and exit")
        s.close()

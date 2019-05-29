import struct
import cv2
import numpy

SURFACE_SIZE = (680, 480)


def run_show_image(socket_s):

    print("Running image processing")



    try:
        running = True
        while running:
            # receive size
            len_str = socket_s.recv(4)
            size = struct.unpack('!i', len_str)[0]

            print('size:', size)

            # receive string

            img_str = b''

            while size > 0:
                if size >= 4096:
                    data = socket_s.recv(4096)
                else:
                    data = socket_s.recv(size)

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
        socket_s.close()

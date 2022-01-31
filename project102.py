import cv2

import dropbox


def take_snapshot():
    # initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # read the frames while the camera is on
        ret, frame = videoCaptureObject.read()
        # cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite("NewPicture1.jpg", frame)
        result = False

    # releases the camera
    videoCaptureObject.release()
    # closes all the window that might be opened while this process
    cv2.destroyAllWindows()


take_snapshot()


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)


def main():
    access_token = "65h3xA6UfpAAAAAAAAAAAVlg-W5xRZXpSrft4_i9aQkuYy9XS34J_ZW6-VRrXFtV"
    transferData = TransferData(access_token)

    file_from = "NewPicture1.jpg"
    # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.
    file_to = input("enter the full path to upload to dropbox:- ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
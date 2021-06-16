from GPSPhoto import gpsphoto
import sys

def get_image_metadata(image_ptah:str):
    meta_data = gpsphoto.getGPSData(image_ptah)
    return meta_data

if __name__=='__main__':
    test_path = '/home/ido/Downloads/IMG_20210610_131250.jpg'
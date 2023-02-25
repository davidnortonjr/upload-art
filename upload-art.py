import logging
import os
import argparse

from samsungtvws import SamsungTVWS

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(
                    prog = 'upload-art',
                    description = 'Uploads and selects images on Samsung Frame TVs')
parser.add_argument('image', help = 'Path to the JPEG image file')
parser.add_argument('tv_ip', help = "The TV's IP address. e.g., 192.168.1.39")

args = parser.parse_args()

# TODO: what if you have multiple Frame TVs? do we need to keep track of different tokens?
token_file = os.path.dirname(os.path.realpath(__file__)) + '/tv-token.txt'
tv = SamsungTVWS(host=args.tv_ip, port=8002, token_file=token_file)

file = open(args.image, 'rb')
data = file.read()
item = tv.art().upload(data, file_type='JPEG', matte='none')
tv.art().select_image(item)


# upload-art

Uploads art to Samsung The Frame TV (pre-2022 models).

## Upload Art

```
pip3 install -r requirements.txt
python3 upload-art.py <image_path>

#e.g.:
python3 upload-art.py ~/Desktop/the-japanese-footbridge-claude-monet-1899-1b2747f1.jpg
```

The art should be the correct dimensions (3840x2160) and in JPEG format. This assumes you don't want to use a matte -- I
don't like the look of it with the matte so I just always make them the right dimension. If it's the wrong size, this 
will actually stretch the image to fit the screen which usually looks strange.

It also automatically selects the image.

Lots of great, free art [here](https://useum.org/download-artworks). You just need to resize.

On my network, the TV was available on `samsung.local`. However, if you need to connect via another host or IP, you can 
add the `--host` flag (see usage). You can find TV IP address by looking at your wifi router's admin page, or using the
"Find TVs" instructions below.

Uses the open source project [samsung-tv-ws-api](https://github.com/xchwarze/samsung-tv-ws-api/). There is a lot more 
that library can do (deleting images, setting photo filter, setting matte, changing the channel, opening an app, etc.)

Apparently this is not compatible with model year 2022 and later Frame TVs. :( 

## Find TVs

We can look for TVs using multicast DNS service discovery, assuming it's listening for AirPlay connections:

```
$ python3 find-tvs.py
Press enter to exit...

Found Samsung The Frame, hostname: Samsung.local.
```

# upload-art

## Usage

```
pip3 install -r requirements.txt
python3 upload-art.py <image_path> <frame_tv_ip>

#e.g.:
python3 upload-art.py ~/Desktop/the-japanese-footbridge-claude-monet-1899-1b2747f1.jpg 192.168.1.39
```

The art should be the correct dimensions (3840x2160) and in JPEG format. This assumes you don't want to use a matte -- I
don't like the look of it with the matte so I just always make them the right dimension. If it's the wrong size, this 
will actually stretch the image to fit the screen which usually looks strange.

It also automatically selects the image.

Lots of great, free art [here](https://useum.org/download-artworks). You just need to resize.

I found my TV IP address by looking at my wifi router's admin page.

Uses the open source project [samsung-tv-ws-api](https://github.com/xchwarze/samsung-tv-ws-api/). There is a lot more 
that library can do (deleting images, setting photo filter, setting matte, changing the channel, opening an app, etc.)

Apparently this is not compatible with model year 2022 and later Frame TVs. :( 

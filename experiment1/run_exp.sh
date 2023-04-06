python3 mk_white.py

# hide the lyrics of gravity rides everything in white_grav.ppm
python3 stego_driver.py white.ppm white_grav gravity.txt

# use the lsb expose algorithm to show the changed pixels
python3 lsb_expose.py white_grav.ppm


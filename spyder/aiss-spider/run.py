# -*- coding:utf-8 -*-
from download_info import download_info
from download_pictures import get_info, get_info_imgs, download

if __name__ == 'main':
	# download description of image
	download_info()
	# get infomation of image group
	info = get_info()
	# get the url of each image, save to directory, local file name
	imgs = get_info_imgs(info)
	# using ten threads to download pictures
	download(imgs,processes=10)



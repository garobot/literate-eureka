# script to remove audio from mp4 files

from email.mime import audio
import os
import argparse
from moviepy.editor import VideoFileClip

def main(path):
    video = VideoFileClip(audio)

    video = video.without_audio()
    video.write_videofile()



if __name__ == '__main__':
    path = input("[+] Enter mp4 full filename: ")
    main(path)
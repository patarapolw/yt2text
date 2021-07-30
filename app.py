#!/usr/bin/env python

import os
import subprocess
import sys

from pydub import AudioSegment
import speech_recognition as sr

# import youtube_dl


if __name__ == "__main__":
    os.chdir("./cache")

    filename = os.getenv("AUDIO")
    lang = os.getenv("LANG")

    if not lang:
        lang = "th-TH"

    if not filename:
        for line in (
            subprocess.check_output(["youtube-dl", "-x", sys.argv[1]])
            .decode()
            .split("\n")
        ):
            p1 = "[download] "
            if line.startswith(p1):
                line = line[len(p1) :].rstrip()

                p2 = "Destination: "
                if line.startswith(p2):
                    filename = line[len(p2) :]
                    break

                s2 = " has already been downloaded"
                if line.endswith(s2):
                    filename = line[: -len(s2)]
                    break

    if not filename:
        sys.exit(1)

    audio = AudioSegment.from_file(filename).export(format="wav")
    audio.seek(0)

    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio = r.record(source)
        print(r.recognize_google(audio, language=lang))

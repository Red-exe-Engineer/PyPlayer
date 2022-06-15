# PyPlayer
Created by Wallee#8314/Red-exe-Engineer.

This module was made because I like playsound.
"But wait" I hear you saying "why compete against something you like?"
Well its simple, playsound is over complecated...
I like the simplicity of using it but it's bulky and doesn't work on my current operating system (Raspberry Pi OS 64-Bit Bullseye).
So I made something simple to use, less builky, and with more features.
You can even play videos with it.

Hope you enjoy :D

# INSTALL

```sh
pip install py-media-player
```
or
```sh
pip3 install py-media-player
```

**PyPi:**
https://pypi.org/project/py-media-player/

# USAEGE

```py
# Play audio from a MP3 file
from PyPlayer import playfile

playfile("path/to/file.mp3")
```

```py
# Play video from a MP4 file
from PyPlayer import playfile

playfile("path/to/file.mp4, player="vlc")
```

**ARGUMENTS:**

```
- file: Path to the file that is to be played.
- player: Allows the use of a different audio player (VLC Media Player).
- player_args: Custom arguments to run the player with (Default means either MPV or WM Player depending on the OS).
- wait: Waits for the file to finish playing.
- pathing: Allows for Linux based paths to be used on any system, useful for cross compatability
- win_drive: Select the windows drive to use when pathing.
```

Thanks.

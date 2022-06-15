# Docstring
"""
    ### Created by Wallee#8314/Red-exe-Engineer.

    This module was made because I like playsound.
    "But wait" I hear you saying "why compete against something you like?"
    Well its simple, playsound is over complecated...
    I like the simplicity of using it but it's bulky and doesn't work on my current operating system (Raspberry Pi OS 64-Bit Bullseye).
    So I made something simple to use, less builky, and with more features.
    You can even play videos with it.

    Hope you enjoy :D
"""

# Imports
from subprocess import Popen, PIPE
from os.path import exists, join
from os import uname
from time import sleep

# Define a function to play stuff
def playfile(file:str,
             player:str          = "Default",
             player_args:str     = "",
             wait:bool           = True,
             pathing:bool        = True,
             win_drive:str       = "C"):
    
    # Docstring
    """
        ### A simple function with more advanced features to play media files.

        - file: Path to the file that is to be played.
        - player: Allows the use of a different audio player (VLC Media Player).
        - player_args: Custom arguments to run the player with (Default means either MPV or WM Player depending on the OS).
        - wait: Waits for the file to finish playing.
        - pathing: Allows for Linux based paths to be used on any system, useful for cross compatability
        - win_drive: Select the windows drive to use when pathing.
    """

    # Check if pathing is True
    if pathing:

        # Modify file to be a proper path (Windows/Linux cross compatability)
        file = (win_drive.upper() + ":\\\\" if uname().sysname == "Windows" else "") + join(*file.split("/"))

    # Check if the path exists
    if not exists(file):

        # Raise an error
        raise FileNotFoundError(file)
    
    if player == "Default":
        player = "mvplayer" if uname().sysname == "Windows" else "mpv"

    # Try even though I don't think it needs it
    try:

        # Create a process to play the file
        process = Popen([player, player_args, file], stdout=PIPE, stderr=PIPE)
        
        # Check if wait is True
        if wait:

            # Repeat as long as the process is alive
            while process.poll() is None:

                # Sleep for a small amount of time to preserve resources
                sleep(0.1)
    
    # Wait what I do?
    except Exception as error:

        # Print the error as it would be weird to raise it... I mean who would do that... Okay guilty...
        print(str(error))

# Define an easy way to check the version of the module
def get_version(needs:str = ""):

    # Docstring
    """
        ### Get the current version of PyPlayer.

        - needs: Check the needed version for the program (needs="x.y.z").

        if needs is empty the current version will be returned as a string otherwise True or False will be returned depending on the version.
    """

    version = "1.0.1"

    # Check if needs wasn't specified
    if needs == "":

        # Return version
        return version

    # Check if the number of points in the needs string isn't 3
    if not len(needs.split(".")) == 3:

        # Raise a value error
        raise ValueError

    # Check if the version is greater than needs
    if version[0] >= needs[0] and float(version[2:]) >= float(needs[2:]):

        # Return True
        return True
        
    # Return False
    return False

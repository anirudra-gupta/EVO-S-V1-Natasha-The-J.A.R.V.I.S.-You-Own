from colorama import Fore, Style
import speak


def say_name():
    print(Fore.GREEN + 'My name is EVO' + Style.RESET_ALL)
    speak.speak_only('my name is EVO')


def evo():
    speak.speak('Yes, I\'m here')


# Introduce
def introduce():

    print(Fore.GREEN + """
    I\'m evo.
    I am the voice assistant of this computer.
    I can help you to do your works easily using voice commands.
    """ + Style.RESET_ALL)

    speak.speak_only(
        "I'm evo, I am the voice assistant of this computer. "
        "I can help you to do your works easily using voice commands."
    )

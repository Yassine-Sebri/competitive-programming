"""In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superceded by voice
and digital data communication channels, it still has its use in some applications around the world.

The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as
·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally
capital letters are used. When the message is written in Morse code, a single space is used to separate the
character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code
is ···· · −·−− ·−−− ··− −·· ·."""

def decodeMorse(morse_code):
    morse_code = morse_code.split('   ')
    morse_code = [word.split(' ') for word in morse_code if word != ""]
    print(morse_code)
    morse_code = [[code for code in word if code != ""] for word in morse_code]
    morse_code = ["".join([MORSE_CODE[code] for code in word]) for word in morse_code]
    return " ".join(morse_code)

from string import ascii_letters
import pytest

def delfromtext(text: str):
    
    a = ''
    for char in text:
        if char in ascii_letters or char == ' ':
            a += char         
    return a.lower()


def test_no_change():
          assert delfromtext('кроме букв латинского. алфавита 123/ апраоп! hjjkg') =='      hjjkg', 'text without changes'
    
def test_no_spaces():
        assert delfromtext('кромебуквлатинского.алфавита123/апраоп!hjjkg') =='hjjkg' , 'text without spaces between words'

def test_lathin_instead():
        assert delfromtext('kpome.букв латинского.алфавитa123/ апAаoп! hjjkg') =='kpome a ao hjjkg', 'Latin instead cyrillic'

if __name__ == '__main__':
    pytest.main(['-vv'])
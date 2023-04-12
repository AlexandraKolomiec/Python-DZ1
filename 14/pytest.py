import pytest
import re

def clean_text(text: str) -> str:
        cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
        return cleaned_text.lower()

def test_no_change():
          assert clean_text("hello world") =='hello world', 'text 1'
    
def test_registr():
        assert clean_text("HellO woRld") =='hello world' , 'text 2'

def test_no_punctuation():
        assert clean_text("hello, world...") =='hello world', 'text 3'

def test_language():
        assert clean_text("hello world ворлд") =='hello world ', 'text 4'
    
def test_all():
        assert clean_text("HellO !woRld, ворлд") =='hello world ' , 'text 5' 


if __name__ == '__main__':
    pytest.main(['-vv'])
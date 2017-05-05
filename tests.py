from tracklists import tracklist, main
import pyperclip

aja = """1 Black Cow 5:07
    2 Aja 7:56
    3 Deacon Blues 7:26
    4 Peg 3:58
    5 Home At Last 5:31
    6 I Got The News 5:03
    7 Josie 4:30"""

proper = """1 Black Cow 0:00\n2 Aja 5:07\n3 Deacon Blues 13:03\n4 Peg 20:29\n5 Home At Last 24:27\n6 I Got The News 29:58\n7 Josie 35:01""" 

def test_single_line():
    data = "1 Black Cow 5:07"
    assert tracklist(data) == '1 Black Cow 0:00' 

def test_two_lines():
    data = """1 Black Cow 5:07
    2 Aja 7:56"""
    assert tracklist(data) == '1 Black Cow 0:00\n2 Aja 5:07' 

def test_steely_dan_ada():
    assert tracklist(aja) == """1 Black Cow 0:00\n2 Aja 5:07\n3 Deacon Blues 13:03\n4 Peg 20:29\n5 Home At Last 24:27\n6 I Got The News 29:58\n7 Josie 35:01""" 

def test_aja_with_padding():
    assert tracklist(aja + '\n') == proper

def test_clipboard():
   pyperclip.copy(aja)
   assert main() == proper

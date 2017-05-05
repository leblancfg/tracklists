import sys
sys.path.insert(0, '../tracklists')

from tracklists import tracklist, main
import pyperclip

aja = """1 Black Cow 5:07
    2 Aja 7:56
    3 Deacon Blues 7:26
    4 Peg 3:58
    5 Home At Last 5:31
    6 I Got The News 5:03
    7 Josie 4:30"""

aja_fix = """1 Black Cow 0:00\n2 Aja 5:07\n3 Deacon Blues 13:03\n4 Peg 20:29\n5 Home At Last 24:27\n6 I Got The News 29:58\n7 Josie 35:01""" 

pypy = """1. "Look-Ka Py Py"   3:20 
2. "Rigor Mortis"   2:38
3. "Pungee"   3:01
4. "Thinking"   1:45
5. "This Is My Last Affair"   2:55
6. "Funky Miracle"   2:28
7. "Yeah, You're Right"   2:46
8. "Little Old Money Maker"   2:42
9. "Oh, Calcutta!" 2:45
10. "The Mob"   2:49
11. "9 'Til 5"   2:51
12. "Dry Spell"   2:33"""

def test_single_line():
    data = "1 Black Cow 5:07"
    assert tracklist(data) == '1 Black Cow 0:00' 

def test_two_lines():
    data = """1 Black Cow 5:07
    2 Aja 7:56"""
    assert tracklist(data) == '1 Black Cow 0:00\n2 Aja 5:07' 

def test_steely_dan_ada():
    assert tracklist(aja) == aja_fix

def test_aja_with_padding():
    assert tracklist(aja + '\n') == aja_fix

def test_aja_with_more_padding():
    more_pad = ''.join([line + '\n' for line in aja.split('\n')])
    assert tracklist(more_pad) == aja_fix

def test_clipboard():
   pyperclip.copy(aja)
   assert main() == aja_fix


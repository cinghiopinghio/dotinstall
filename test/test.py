import os
import dotinstall.dotinstall as di

def test_dotfile():
    filename ='../LICENSE'
    a = di.Dotfile(filename)
    assert a.source_file(short=True) == filename

def test_dotfile():
    filename ='LICENSE'
    sdir='../'
    a = di.Dotfile(filename,repo_path=sdir)
    assert a.source_file() == os.path.abspath(sdir + filename)

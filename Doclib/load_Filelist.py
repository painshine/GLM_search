import os

def filelist(filespath='./Doclib/DocFiles/'):
    tem_fl = os.listdir(filespath)
    fl = []
    fnl = []
    for _f in tem_fl:
        fl.append(_f)
        fn = _f.split('_')[1]
        fn = fn.split('.txt')[0]
        
        fnl.append(fn)
    return fl,fnl
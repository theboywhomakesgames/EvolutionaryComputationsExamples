def read():
    f = open('./problem1.dat', 'r')
    f.seek(0)
    whole_file = f.read()
    lines = whole_file.splitlines()
    lines = list(filter(len, lines))

    width = int(lines.pop(0))

    distances = lines[:25]
    flows = lines[25:]
    
    ds = []
    for d in distances:
        dline = []
        for dd in d.split(" "):
            dline.append(int(dd))
        ds.append(dline)

    fs = []
    for f in flows:
        fline = []
        line = f.replace("  ", " ").split(" ")
        line = filter(len, line)
        
        for ff in line:
            fline.append(int(ff))
        fs.append(fline)

    return width, ds, fs
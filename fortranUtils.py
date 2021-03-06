# These are common functions and definitions used by both
# type-to-print and the converter script.

commentCharacters = ['c', 'C', '!', '*']

def split_fortran_line_at_72(line):
    # Commented lines won't be split
    line = line.rstrip()
    lines = [line+"\n"]
    if len(line)>0 and line[0].lower() in commentCharacters:
        return lines
    remain = line[72:]
    while len(remain)>0:
        lines.append("     !" + remain[:66] +"\n")
        remain = remain[66:]
    return lines


from sys import stdin, stdout
from pyperclip import copy as clipcopy
from textwrap import wrap
from datetime import datetime

hsep    = '-'
vsep_l  = '!'
vsep_r  = '!'
decor   = '='
width   = 80
net_width = width - 2 - len(vsep_l + vsep_r)

def pad_text(s, vsep_l = '#', hsep = '-', vsep_r = '#', pad = ' '):
    assert len(hsep) == 1
    assert len(pad) == 1

    net_width = width - 2 - len(vsep_l + vsep_r)
    n_pad_l = ( net_width - len(s) ) / 2
    n_pad_r = net_width - len(s) - n_pad_l

    return vsep_l \
        + pad * n_pad_l \
        + ' ' + s + ' ' \
        + pad * n_pad_r \
        + vsep_r

def hline(vsep_l = '#', hsep = '-', vsep_r = '#'):
    return vsep_l + hsep * (width - len(vsep_l + vsep_r)) + vsep_r

def print_framed(lines):
    from StringIO import StringIO
    out = StringIO()
    for l in lines:
        if l == '--':
            out.write( hline(vsep_l, hsep, vsep_r) + '\n' )
        elif l[:2] == '--':
            out.write( pad_text(l[2:].strip(), vsep_l, hsep, vsep_r, hsep) + '\n' )
        else:
            out.write( pad_text(l, vsep_l, hsep, vsep_r) + '\n' )
    return out.getvalue()

def main():
    lines = [ s.replace('\n','') for s in stdin ]
    stdout.write(print_framed(lines))

parse_tuple_list = lambda buf: [ tuple(s0.strip() for s0 in s.split(':',1)) for s in buf.split(';') ]
def pad_arg_list(buf, sep = ': '):
    lines = list()
    pairs = parse_tuple_list(buf)
    wl = max([ len(l) for l,r in pairs ]) + 1
    wr = max([ len(r) for l,r in pairs ]) + 1
    for l,r in pairs:
        lines.append( ' ' * (wl - len(l)) + l + sep + r + ' ' * (wr - len(r)))
    return lines


def fortran_procedure():
    lines = []

    lines.append('-- ' + raw_input('Procedure name: ').upper())

    for s in wrap(raw_input('Description: '), net_width):
        lines.append(s)

    buf = raw_input('Inputs (separated by \';\') ')
    if len(buf) > 0:
        lines.append('-- INPUTS')
        lines.extend(pad_arg_list(buf))

    buf = raw_input('Outputs (separated by \';\') ')
    if len(buf) > 0:
        lines.append('-- OUTPUTS')
        lines.extend(pad_arg_list(buf))

    buf = raw_input('Return value: ')
    if len(buf) > 0:
        lines.append('-- RETURNS')
        lines.append(buf)

    buf = raw_input('Copyright holder: ')
    if len(buf) > 0:
        lines.append('-- (c) {yr} {n} '.format(yr = datetime.now().year, n = buf))
    else:
        lines.append('--')

    clipcopy(print_framed(lines))



if __name__ == '__main__':
    main()

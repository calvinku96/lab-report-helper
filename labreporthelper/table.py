"""
Helper module for make_tex_table
"""


def make_tex_table(inputlist, outputfile, close=False, **kwargs):
    """
    Parse table from inputlist

    Args:
        inputlist: list
            List to parse
        outputfile: file
            .tex file to write
        **kwargs:
            nonestring: string
                string when objecttype is None
    Returns:
        None
    """
    outputstring = ""
    for e in inputlist:
        for f in e:
            if f is None:
                f = r'\text{{{}}}'.format(
                    str(kwargs.get("nonestring", "None"))
                    )
            outputstring += "$" + str(f) + "$" + "&"
        outputstring = outputstring[:-1]
        outputstring += "\\\\\n"
    outputfile.write(outputstring)
    if close:
        outputfile.close()

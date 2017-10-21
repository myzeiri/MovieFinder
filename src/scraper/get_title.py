from get_next_line import get_next_line

def get_title(text, ref_index, line_count):
    """
        Returns the first movie title string in text using 
        reference as a target. 

        The start of the movie title is line_count number of lines ahead of
        the start of reference. 
    """
    if (ref_index < 0):
        return

    #Move up line_count lines to the start of the movie title
    count = 0
    while count < line_count:
        char = text[ref_index]

        if char == "\n":
            count += 1

        ref_index -= 1

    #print("ref_index = " + str(ref_index + 2))
    return get_next_line(text[ref_index + 2::])

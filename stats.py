def get_num_words(path_to_file):
    with open(path_to_file) as f:
        num_words = len( f.read().split() )
    return num_words
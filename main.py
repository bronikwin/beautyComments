import re

def beauty_comments(data_path:str, size=86, main_symbol='=', text_symbol=' ', comment_pattern='#bc='):
    """
    Hello! It is easy to use beauty comments!
    :param data_path: path to script file
    :param size: line of length
    :param main_symbol: symbol of upper and lower lines
    :param text_symbol: symbol of line with text
    :param comment_pattern: pattern that you use in your script's file to indicate the beauty comment
    :return: file with BEAUTY COMMENTS!
    """
    def create_comment(text, size=86, main_symbol='=', text_symbol=' '):
        up = ''.join([' ' * 4, '# ', main_symbol * (size - 2), '#'])
        low = up
        padding = int((size - 1 - len(text)) / 2)
        main_text = ''.join([' ' * 4, '# ', text_symbol * padding, text, text_symbol * padding, '#'])
        comment = '\n'.join([up, main_text, low])
        return comment
    ok=False
    try:
        data_with_comments = []
        with open(data_path, 'r', encoding='utf-8') as file:
            file = file.read()
            file = file.split(sep='\n')
            for line in file:
                lattice = re.search(comment_pattern, re.sub('\s|\t', '', line))
                if lattice:
                    ok=True
                    text_index = re.search('=', line).end()
                    text = line[text_index:]
                    comment = create_comment(text, size=size, main_symbol=main_symbol, text_symbol=text_symbol)
                    data_with_comments.append(comment)
                else:
                    data_with_comments.append(line)
        if not ok:
            raise KeyError("Sorry! I can't find your comment pattern %s"%comment_pattern)

    except: raise KeyError('Sorry! There is a problem with reading a file %s :(' %data_path)
    try:
        data_with_comments = '\n'.join(data_with_comments)
        with open(data_path, 'w', encoding='utf-8') as file:
            file.write(data_with_comments)
    except: raise KeyError('Sorry! There is a problem with writing a file %s :(' %data_path)

if __name__ == '__main__':
    file_path= r"example_before1.py"
    beauty_comments(file_path,
                    size=86,
                    text_symbol='-',
                    )



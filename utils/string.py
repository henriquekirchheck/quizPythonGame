def line(txt:str = '', totalcaracters:int = 0, upper:bool = False):

    """
    Makes a line before and after the text you write
    :param txt: The text that you will be passing through
    :param totalcaracters: The number of caracters that it will be ocuping (Default = 0)
    :param upper: If the caracters will be on upper case
    """
    if(txt == ''):
        text = '-' * totalcaracters
    elif(totalcaracters < (len(txt) + 2)):
        if(upper == True):
            text = ('{} \n{} \n{}'.format('-' * (len(txt) + 2), txt.upper().center(len(txt) + 2), '-' * (len(txt) + 2)))
        else:    
            text = ('{} \n{} \n{}'.format('-' * (len(txt) + 2), txt.center(len(txt) + 2), '-' * (len(txt) + 2)))
    else:
        if(upper == True):
            text = ('{} \n{} \n{}'.format('-' * totalcaracters, txt.upper().center(totalcaracters), '-' * (totalcaracters)))
        else:    
            text = ('{} \n{} \n{}'.format('-' * totalcaracters, txt.center(totalcaracters), '-' * (totalcaracters)))
    
    print(text)
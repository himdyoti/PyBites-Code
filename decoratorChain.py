
def make_html(htag):
    def deco(fn):
        def wrapper(*arg,**kargs):
            txtt = kargs.get('text')
            if txtt:
                return '<{}>{}</{}>'.format(htag,fn(text=txtt),htag)
            else:
                return '<{}>{}</{}>'.format(htag,fn(),htag)
        return wrapper
    return deco

@make_html('div') 
@make_html('p')        #make_html('p')('<strong>I code with PyBites</strong>')
@make_html('strong')   # make_html('strong')(get_text)
def get_text(text='I code with PyBites'):
    return text
print(get_text())


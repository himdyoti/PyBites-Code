def make_html(htag):
    def deco(fn):
        def wrapper(*arg,**kargs):
            return '<{}>{}</{}>'.format(htag,fn(),htag)
        return wrapper
    return deco

@make_html('div') 
@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text
print(get_text())  
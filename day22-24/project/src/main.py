from functools import wraps


def make_html(element: str):
    '''Decorator that will update plain text with html tags passed in'''
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            return f'<{element}>{function(*args,**kwargs)}</{element}>'
        return wrapper
    return decorator

# @make_html("p")
# @make_html("strong")
def get_text(text="I code with Pybites"):
    return text


def main():
   print(make_html("p")(get_text)("I code with Pybites"))


if __name__ == "__main__":
    main()

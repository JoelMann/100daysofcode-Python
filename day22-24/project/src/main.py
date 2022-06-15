from functools import wraps


def make_html(element: str):
    """Decorator that will update plain text with html tags passed in"""

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return f"<{element}>{function(*args,**kwargs)}</{element}>"

        return wrapper

    return decorator

def get_text(text="I code with Pybites"):
    return text

    
@make_html("strong")
@make_html("p")
def get_text_dec(text="I code with Pybites"):
    return text


def main():
    print(
        make_html("strong")(get_text)((make_html("p")(get_text)("I code with Pybites")))
    )

    print(get_text_dec())

    # both print <strong><p>I code with Pybites</p></strong>


if __name__ == "__main__":
    main()

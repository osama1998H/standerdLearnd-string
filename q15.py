# create html tag

def html_generator(tag: str, content: str, _class="") -> str:
    html = f'<{tag} class="{_class}"> {content} </{tag}>'
    return html


print(html_generator("p", "python loves html"))
print(html_generator("div", "the new jango", "rounded-md"))

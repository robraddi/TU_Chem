```python
# Loads custom.css from working directory to make the notebook more beautiful
from IPython.core.display import HTML
def js():
    g = open("custom/gtag.js", "r").read()
    return HTML(g)
js()
def css_styling():
    styles = open("custom/custom.css", "r").read() #or edit path to custom.css
    return HTML(styles)
#css_styling()

```

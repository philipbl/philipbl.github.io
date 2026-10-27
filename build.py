"""Render index.html from _template.html and the CV data file.

Usage: python build.py [path/to/cv_data.yml] [output.html]
"""
import pathlib
import re
import sys

import jinja2
import yaml

# Site order for publication groups (the CV keeps its own). Unlisted groups
# follow in CV order.
PUB_ORDER = ["Conference Publications", "Journal Articles", "Book Chapters"]


def clean(s):
    r"""Strip the LaTeX that cv_data.yml carries for the PDF.

    >>> clean(r"Kitras\textsuperscript{1,3} \& 49\%")
    'Kitras & 49%'
    """
    s = re.sub(r"\\textsuperscript\{[^}]*\}", "", str(s))
    return s.replace(r"\&", "&").replace(r"\%", "%")


def authors(s):
    """Normalize an author list to "A, B, and C".

    >>> authors(r"Ann Lee, Bo Li\\textsuperscript{2} and Philip Lundrigan")
    'Ann Lee, Bo Li, and Philip Lundrigan'
    >>> authors("Bo Li, Philip Lundrigan")
    'Bo Li and Philip Lundrigan'
    """
    names = [n.strip() for n in clean(s).replace(" and ", ",").split(",") if n.strip()]
    if len(names) > 2:
        return ", ".join(names[:-1]) + ", and " + names[-1]
    return " and ".join(names)


def main(cv_path="../cv/cv_data.yml", out_path="_site/index.html"):
    data = yaml.safe_load(pathlib.Path(cv_path).read_text())
    rank = {name: i for i, name in enumerate(PUB_ORDER)}
    data["publications"].sort(key=lambda g: rank.get(g["name"], len(PUB_ORDER)))
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("."),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters.update(clean=clean, authors=authors)
    html = env.get_template("_template.html").render(data)
    out = pathlib.Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


if __name__ == "__main__":
    main(*sys.argv[1:])

"""Render index.html from _template.html and the CV data file.

Usage: python build.py [path/to/cv_data.yml]
"""
import pathlib
import re
import sys

import jinja2
import yaml
from markupsafe import Markup, escape

MY_NAMES = ("Philip Lundrigan", "Philip B. Lundrigan")


def clean(s):
    r"""Strip the LaTeX that cv_data.yml carries for the PDF.

    >>> clean(r"Kitras\textsuperscript{1,3} \& 49\%")
    'Kitras & 49%'
    """
    s = re.sub(r"\\textsuperscript\{[^}]*\}", "", str(s))
    return s.replace(r"\&", "&").replace(r"\%", "%")


def authors(s):
    """Normalize an author list to "A, B, and C" and bold my name.

    >>> authors(r"Ann Lee, Bo Li\\textsuperscript{2} and Philip Lundrigan")
    Markup('Ann Lee, Bo Li, and <strong>Philip Lundrigan</strong>')
    >>> authors("Bo Li, Philip Lundrigan")
    Markup('Bo Li and <strong>Philip Lundrigan</strong>')
    """
    names = [n.strip() for n in clean(s).replace(" and ", ",").split(",") if n.strip()]
    names = [Markup("<strong>%s</strong>") % n if n in MY_NAMES else escape(n) for n in names]
    if len(names) > 2:
        return Markup(", ").join(names[:-1]) + Markup(", and ") + names[-1]
    return Markup(" and ").join(names)


def main(cv_path="../cv/cv_data.yml"):
    data = yaml.safe_load(pathlib.Path(cv_path).read_text())
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("."),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters.update(clean=clean, authors=authors)
    html = env.get_template("_template.html").render(data)
    pathlib.Path("index.html").write_text(html)


if __name__ == "__main__":
    main(*sys.argv[1:])

philipbl.github.io
==================

Personal webpage, built from `_template.html` and the CV data (`cv_data.yml`) in
the private `philipbl/cv` repo.

GitHub Actions (`.github/workflows/deploy.yml`) builds the CV PDF and the page,
checks links, and deploys to GitHub Pages on every push to `main` and whenever
the cv repo's data changes. Pushes to other branches build and test without
deploying.

To preview locally (expects the cv repo at `../cv`), run `make serve` and open
http://localhost:8000. `make test` runs the doctests and an offline link check
(needs `brew install lychee`).

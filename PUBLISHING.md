# Publishing docpilot to PyPI

## One-time setup

```bash
pip install build twine
```

Register at https://pypi.org and create an API token under Account Settings → API tokens.  
## Build & upload
 
```bash 
# From the project root (where pyproject.toml lives)
python -m build           # creates dist/docpilot-0.1.0.tar.gz and .whl

twine check dist/*        # sanity check before upload 

twine upload dist/*       # prompts for username (__token__) + API token 
```

## Test on TestPyPI first (optional)   

```bash
twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ docpilot
```

## GitHub Actions – auto-publish on tag push

Create  `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI
on:
  push:
    tags: ["v*"]
jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install build twine
      - run: python -m build
      - run: twine upload dist/*
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
```

Add `PYPI_API_TOKEN` to your GitHub repo → Settings → Secrets.

Then to release:

```bash
git tag v0.1.0 
git push origin v0.1.0
```

## Bump version 

Edit `docpilot/version.py` and `pyproject.toml`, then rebuild and re-upload.

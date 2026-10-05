# lab-1mlops# lab-1mlops

This is my first lab for the MLOps course. The calculator itself is tiny on purpose - the real point of the lab was everything around the code: setting up a virtual environment, writing tests two different ways, and getting GitHub to run those tests for me every time I push.

## What's in here

1 `src/calculator.py` - five small functions: add, subtract, multiply, one that combines the first three, and a divide function I added
2 `test/test_pytest.py` - tests written with pytest
3 `test/test_unittest.py` - the same kind of tests written with unittest, so I could compare the two
4 `data/` - empty for now (it has a `.gitkeep` file inside because git won't track an empty folder)
5 `.github/workflows/` - two workflows, one for pytest and one for unittest

## Running it yourself

```
python3 -m venv lab_01
source lab_01/bin/activate
pip install -r requirements.txt
pytest -v
python -m unittest test.test_unittest -v
```

Heads up: `pytest -v` will say 14 tests passed, not 7. That's because pytest also picks up the unittest tests and runs them too. Running unittest on its own gives 7.

## What I changed from the original lab

1 Added `fun5`, which divides two numbers. If you try to divide by zero it raises a `ValueError` instead of crashing.
2 Added tests for division, divide by zero, and negative numbers. The original tests only used small positive numbers, so they couldn't catch much.
3 Updated the GitHub Actions versions. The lab used v2, which GitHub has retired - `upload-artifact@v2` actually makes the workflow fail now.
4 Switched from Python 3.8 to 3.10, since 3.8 is end of life.
5  Made the workflows run on pull requests too, not just pushes. Otherwise CI can't stop a broken change before it gets merged.

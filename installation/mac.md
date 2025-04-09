## 🍎 STEP-BY-STEP: Install Latest Python & Pytest on macOS

---

### ✅ STEP 1: Check if Python is Already Installed

Open **Terminal** and type:

```bash
python3 --version
```

You might see something like:

```
Python 3.9.6
```

If it's **not the latest version** (e.g., `3.13.x`), or you want to **manage multiple versions**, continue below.

---

### ✅ STEP 2: Install `Homebrew` (if not installed)

Homebrew is the Mac package manager. Install it with:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then update brew:

```bash
brew update
```

---

### ✅ STEP 3: Install `pyenv` to Manage Python Versions

```bash
brew install pyenv
```

Then add the following to your shell config file:

#### If you're using **zsh** (default on newer macOS):

```bash
nano ~/.zshrc
```

Add this at the end:

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

Then apply it:

```bash
source ~/.zshrc
```

---

### ✅ STEP 4: Install Latest Python (e.g., 3.13.2)

```bash
pyenv install 3.13.2
```

Make it the global default:

```bash
pyenv global 3.13.2
```

Confirm:

```bash
python --version
# or
python3 --version
```

You should see:

```
Python 3.13.2
```

---

### ✅ STEP 5: Install `pip` (Python’s package manager)

It usually comes with Python, but just in case:

```bash
python3 -m ensurepip --upgrade
```

---

### ✅ STEP 6: Install `pytest`

```bash
pip install pytest
```

Confirm it:

```bash
pytest --version
```

You should see:

```
pytest 8.x.x
```

---

### ✅ STEP 7: Try a Sample Test

1. Create a file `test_example.py`:

```python
# test_example.py
def test_add():
    assert 2 + 2 == 4
```

2. Run the test:

```bash
pytest
```

Expected result:

```
collected 1 item

test_example.py .                                    [100%]

1 passed in 0.01s
```

---

## 🧠 BONUS (Optional): Set `python` Alias to `python3`

To avoid typing `python3`, you can set an alias:

```bash
nano ~/.zshrc
```

Add:

```bash
alias python=python3
alias pip=pip3
```

Then:

```bash
source ~/.zshrc
```

---

## ✅ Done!

You now have:

- ✅ Latest Python via `pyenv`
- ✅ pip installed
- ✅ pytest working
- ✅ Dev environment ready

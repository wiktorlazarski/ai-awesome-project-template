______________________________________________________________________
<div align="center">

# 🤖 AI Awesome Project Template

<p align="center">
  <a href="https://github.com/wiktorlazarski">👋 Author</a>
</p>

______________________________________________________________________

You may want to adjust badge links in a README.md file.

[![ci-testing](https://github.com/wiktorlazarski/ai-awesome-project-template/actions/workflows/ci-testing.yml/badge.svg?branch=master&event=push)](https://github.com/wiktorlazarski/ai-awesome-project-template/actions/workflows/ci-testing.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>


## ⚙️ Setup

**Before setting up a project,** make sure that the `setup.py` script has all setup parameters adjusted and change an `ai_awesome` directory name to your project name. Also, if you want to use conda environment, you may want to change its name in a `conda_env.yml` file. Then, follow the instruction:

```bash
# Clone repo
git clone https://github.com/wiktorlazarski/ai-awesome-project-template.git

# Go to repo directory
cd ai-awesome-project-template

# (Optional) Create virtual environment
python -m venv venv
source ./venv/bin/activate

# Install project in editable mode
pip install -e .

# (Optional but recommended) Install pre-commit hooks to preserve code format consistency
pre-commit install
```

## 🐍 Setup with Anaconda or Miniconda

**Before setting up a project,** make sure that the `setup.py` script has all setup parameters adjusted and change an `ai_awesome` directory name to your project name. Additionally, you may want to change a default (_ai_awesome_env_) conda environment name in a `conda_env.yml` file. Then, follow the instruction:

```bash
# Clone repo
git clone https://github.com/wiktorlazarski/ai-awesome-project-template.git

# Go to repo directory
cd ai-awesome-project-template

# Create and activate conda environment
conda env create -f ./conda_env.yml
conda activate ai_awesome_env

# (Optional but recommended) Install pre-commit hooks to preserve code format consistency
pre-commit install
```

### 🤗 Happy coding !

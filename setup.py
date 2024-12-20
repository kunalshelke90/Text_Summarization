import setuptools

with open("README.md", "rb") as f:
    long_description = f.read().decode("utf-8", errors="ignore")

__version__ = "0.0.1"

REPO_NAME = "Text_Summarization"
AUTHOR_USER_NAME = "kunalshelke90"
SRC_REPO = "Text_Summarization"
AUTHOR_EMAIL = "shelkekunal90@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
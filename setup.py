import setuptools
import os
from rdv.version import __version__


ROOT_DIR = os.path.dirname(__file__)
REQUIREMENTS = [line.strip() for line in open(os.path.join(ROOT_DIR, "requirements.txt")).readlines()]
with open("README.md", "r") as fh:
    LONG_DESC = fh.read()


setuptools.setup(
    name="rdv",
    version=__version__,
    author="Raymon.ai",
    author_email="hello@raymon.ai",
    description="Raymon Data Validation Package.",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    url="https://raymon.ai",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
)

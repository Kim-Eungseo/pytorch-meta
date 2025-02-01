from setuptools import setup, find_packages
from os import path
import sys

from io import open

extras = {
    "tcga": ["pandas~=0.24.0", "academictorrents~=2.1.0", "six~=1.11.0"],
    "test": ["flaky"],
}

here = path.abspath(path.dirname(__file__))

sys.path.insert(0, path.join(here, "torchmeta"))
from version import VERSION

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="torchmeta-maintained",
    version=VERSION,
    description="Dataloaders for meta-learning in Pytorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Eungseo Kim",
    author_email="juniormoo87@gmail.com",
    url="https://github.com/Kim-Eungseo/pytorch-meta",
    keywords=["meta-learning", "pytorch", "few-shot", "few-shot learning"],
    packages=find_packages(exclude=["data", "contrib", "docs", "tests", "examples"]),
    install_requires=[
        "torch>=2.5.0",
        "torchvision>=0.20.0",
        "numpy>=1.14.0,<=1.26.4",
        "Pillow>=7.0.0",
        "h5py",
        "tqdm>=4.0.0",
        "requests",  # Required by Torchvision
        "ordered-set",
    ],
    extras_require=extras,
    package_data={"torchmeta": ["torchmeta/datasets/assets/*"]},
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)

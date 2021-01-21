#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

from setuptools import setup, find_packages

import versioneer


def parse_requirements(path):
    """Parse ``requirements.txt`` at ``path``."""
    requirements = []
    with open(path, "rt") as reqs_f:
        for line in reqs_f:
            line = line.strip()
            if line.startswith("-r"):
                fname = line.split()[1]
                inner_path = os.path.join(os.path.dirname(path), fname)
                requirements += parse_requirements(inner_path)
            elif line != "" and not line.startswith("#"):
                if line.startswith("-e"):
                    url, name = line.split()[1].split("#egg=", 1)
                    requirements.append("%s @ %s" % (name, url))
                else:
                    requirements.append(line)
    return requirements


with open("README.md") as readme_file:
    readme = readme_file.read()

install_requirements = parse_requirements("requirements/base.txt")

setup(
    author="Manuel Holtgrewe, Dieter Beule",
    author_email="manuel.holtgrewe@bihealth.de, dieter.beule@bihealth.de",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.6",
        # "Programming Language :: Python :: 3.7",
        # "Programming Language :: Python :: 3.8",
    ],
    entry_points={},
    description="RODEOS main documentation",
    install_requires=install_requirements,
    license="MIT license",
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="irods",
    name="rodeos",
    packages=find_packages(include=["rodeos"]),
    url="https://github.com/bihealth/rodeos",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
)

from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in my_advika/__init__.py
from my_advika import __version__ as version

setup(
	name="my_advika",
	version=version,
	description="For MyAdvika",
	author="Faiyaz",
	author_email="faiyaz@avtutoring.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name='akriti',
	version='0.1.0',
	author="Ayush Shenoy",
	author_email="masala_man@protonmail.com",
	description="Generate patterns with modified Game of Life rules",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/masala-man/akriti",
	packages=setuptools.find_packages(),
	install_requires=[
        "click==8.0.1",
        "colorama==0.4.4",
        "commonmark==0.9.1",
        "cycler==0.10.0",
        "kiwisolver==1.3.1",
        "matplotlib==3.4.2",
        "numpy==1.21.1",
        "Pillow==8.3.1",
        "pyfiglet==0.8.post1",
        "Pygments==2.9.0",
        "pyparsing==2.4.7",
        "PyQt5==5.15.4",
        "PyQt5-Qt5==5.15.2",
        "PyQt5-sip==12.9.0",
        "python-dateutil==2.8.2",
        "rich==10.7.0",
        "six==1.16.0",
        "termcolor==1.1.0",
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
	entry_points={
		'console_scripts': [
			'akriti = akriti.main:cli',
		],
	}
)

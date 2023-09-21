import setuptools

VERSION = "0.1.0"
PACKAGE_NAME = "process"
AUTHOR = "Valerio Luzzi, Marco Renzi"
EMAIL = "valerio.luzzi@gecosistema.com, marco.renzi@gecosistema.com"
GITHUB = f"https://github.com/valluzzi/{PACKAGE_NAME}.git"
DESCRIPTION = "An utils functions package"

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    license='MIT',
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    url=GITHUB,
    packages=setuptools.find_packages("src"),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pygeoapi"]
)

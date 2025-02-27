import setuptools

VERSION = '1.0.0'
PACKAGE_NAME = "html-py-pkg"
AUTHOR = "Tommaso Redaelli"
EMAIL = "tommasoredaelli276@gmail.com"
GITHUB = f"https://github.com/PMG-t/html-py-pkg.git"
DESCRIPTION = "Query a db in a chatbot like way"

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
    package_data={
        "mypackage": ["assets/*"],  # Indica i file extra da includere
    },
    install_requires=[
        
    ]
)
import setuptools
 
setuptools.setup(
    name="notica-common",
    version="0.0.1",
    author="Junho Lee",
    author_email="lee_junho@cyberagent.co.jp",
    description="Used for the notica project.",
    url="https://github.com/CyberAgent-Infosys/notica-common",
    packages=setuptools.find_packages(),
    install_requires = [
        'pymysql==1.0.2',
        'boto3==1.20.45'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9.8",
        "Operating System :: OS Independent",
    ]
)

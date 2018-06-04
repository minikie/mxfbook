from setuptools import setup, find_packages

setup(
    name             = 'mxfbook',
    version          = '0.1.11',
    description      = 'python financial book',
    author           = 'montrix',
    author_email     = 'master@montrix.co.kr',
    url              = 'https://www.montrix.co.kr/mxfbook',
    download_url     = 'https://www.montrix.co.kr/mxfbook/download/0.1.0.tar.gz',
    install_requires = [ ],
    packages         = find_packages(exclude = ['venv', 'sample', 'server']),
    keywords         = ['book', 'finance'],
    python_requires  = '>=2.7',
    package_data     =  { },
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 2.7'
    ]
)
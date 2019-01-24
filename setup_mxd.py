from setuptools import setup, find_packages

setup(
    name             = 'mxd',
    version          = '0.1.2',
    description      = 'python library for mxdex',
    author           = 'montrix',
    author_email     = 'master@montrix.co.kr',
    url              = 'https://www.montrix.co.kr/mxdex',
    download_url     = 'https://www.montrix.co.kr/mxdex/download/mxdex_0.1.0.tar.gz',
    install_requires = [ ],
    packages         = find_packages(exclude = ['venv', 'sample', 'server', 'mxfbook']),
    keywords         = ['book', 'finance'],
    python_requires  = '>=2.7',
    package_data     =  { },
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 2.7'
    ]
)
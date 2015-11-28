from setuptools import setup,find_packages


with open('fabric_fixes/version.py') as fin: exec(fin)

setup(
    name='fabric-fixes',
    version=__version__,

    packages=find_packages(),
    
    # dependencies
    install_requires=['fabric'],
    
    # PyPI MetaData
    author='Adam Kerz',
    author_email='github@kerz.id.au',
    description='Fixes for various deficiencies of fabric',
    license='BSD 3-Clause',
    keywords='fabric',
    url='http://github.com/adamkerz/fabric-fixes',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ),
)

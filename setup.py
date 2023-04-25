from setuptools import setup, find_packages

setup(
    name='aniquote',
    version='1.0.0',
    description='A Python package to generate famous quotes from various anime characters.',
    url='https://github.com/MandarKelkarOfficial/aniquotes.git',
    author='Mandar Kelkar',
    author_email='mandarkelkarofficial@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='anime quotes character famous',
    packages=find_packages(),
    install_requires=[
       
    ],
    python_requires= '>= 3.6',
    py_modules=['aniquote'],
    # entry_points={
    #     'console_scripts': [
    #         'aniquote=aniquote.main:main',
    #     ],
    # },
    package_dir={'':'aniquote'}
)

from setuptools import setup

with open('Readme.md') as fh:
    long_description = fh.read()

setup(
        name='betterjira',
        version='0.1.0',
        description='Work with Jira using human-readable field names, not custom field ids',
        url='https://github.com/jamesbroadhead/betterjira',
        author='James Broadhead',
        author_email='jamesbroadhead+pypi@gmail.com',
        py_modules=["betterjira"],
        package_dir={'': 'src'},
        classifiers=[
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",

            ],
        long_description=long_description,
        long_description_content_type='text/markdown',

)


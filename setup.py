from setuptools import setup

setup(
    name='py-html-json-reporter',
    packages=['py_html_json_reporter'],
    version='1.0.0',
    description='This Library Generate a HTML and JSON report for your Nose Unit Tests',
    long_description=open('README.md', 'r').read(),
    author='Pankaj Kumar Nayak',
    author_email='nayakpankaj2015@gmail.com',
    license='MIT',
    install_requires=['jinja2'],
    package_data={
        'py_html_json_reporter': ['templates/report.html']
    },
    url='https://github.com/pankajnayak1994/py-html-json-reporter',
    download_url='https://github.com/pankajnayak1994/py-html-json-reporter',
    keywords=['nose2', 'testing', 'reporting', 'pytest'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ]
)

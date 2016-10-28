from setuptools import setup, find_packages

setup(name='pythontools',
      version=pythontools.__version__,
      description='Useful python tools',
      long_description="",
      author='Bongsoo Suh',
      author_email='bongsoo.suh@gmail.com',
      url='https://github.com/bongsoos/pythontools/',
      license='MIT',
      packages=find_packages,
      install_requires=['numpy','scipy','matplotlib'],
      zip_safe=False)

from setuptools import setup

setup(name='YourAppName',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
      author_email='example@example.com',
      url='https://www.python.org/community/sigs/current/distutils-sig',
      install_requires=['Flask','flask-wtf', 'unirest', 'wtforms', 'bokeh==0.12.4', 'Flask-PyMongo'],
      )

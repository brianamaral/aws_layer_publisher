from setuptools import setup, find_packages


setup(name='layer_builder',
      version='0.1',
      description='AWS Lambda Layer publisher',
      author='Flying Circus',
      url = 'https://github.com/brianamaral/aws_layer_publisher',
      license='MIT',
      packages=['layer_builder'],
      entry_points={
        'console_scripts': ['build_layer = layer_builder.handle:handle'],
    },
    
      zip_safe=False)
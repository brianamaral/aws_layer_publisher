from setuptools import setup, find_packages


setup(name='layer_builder',
      version='0.1',
      description='The funniest joke in the world',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['layer_builder'],
      entry_points={
        'console_scripts': ['build_layer = layer_builder.handle:handle'],
    },
    
      zip_safe=False)
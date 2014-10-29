from setuptools import setup, find_packages

setup(
    name='viper',
    author='jaegeral',
    version='1.0',
    author_email='mail@alexanderjaeger.de',
    description='Viper Maltego',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)

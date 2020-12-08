from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import pathlib
from subprocess import check_call

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')
install_requires = (here / 'install_requires').read_text(encoding='utf-8').split('\n')

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        check_call('python install_scripts.py'.split())

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        check_call('python install_scripts.py'.split())

setup(
    name='visualize_transformers',
    version='0.0.1',
    author='Apteryx Labs LLC',
    author_email='matthew@apteryxlabs.com',
    desctiption='For visualizing the saliency of transformer inputs on transformer outputs.',
    long_description = long_description,
    long_description_content_type='text/markdown',
    url='git@github.com:apteryxlabs/visualize_transformers.git',
    python_requires='>=3.7',
    keywords='transformers, visualization',
    project_urls = {
            'Website' : 'https://github.com/apteryxlabs/visualize_transformers'
        },
    package_dir = {'': 'src'},
    packages = find_packages(where='src'),
    install_requires = install_requires,
    cmdclass={
            'develop': PostDevelopCommand,
            'install': PostInstallCommand,
        }
)
    
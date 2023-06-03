import os
from glob import glob
from setuptools import setup

package_name = 'autonomy_algo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # (os.path.join('share/' + package_name, glob('launch/*.launch.py')))
        # (os.path.join('share/' + package_name, glob('autonomy_algo/states/*.py')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='camwolff',
    maintainer_email='36940948+camwolff02@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'autonomy_algo = {package_name}.autonomy_algo:main',
            f'naive_algo = {package_name}.naive_algo:main',
            f'autonomy_cli = {package_name}.autonomy_cli:main',
        ],
    },
)

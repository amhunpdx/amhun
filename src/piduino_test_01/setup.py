from setuptools import find_packages, setup

package_name = 'piduino_test_01'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lac',
    maintainer_email='your.email@example.com',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'publisher = piduino_test_01.publisher:main',
	'subscriber = piduino_test_01.subscriber:main',
        ],
    },
)

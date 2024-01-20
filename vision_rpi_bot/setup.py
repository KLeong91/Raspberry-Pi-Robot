from setuptools import find_packages, setup

package_name = 'vision_rpi_bot'

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
    maintainer='kleong91',
    maintainer_email='kleong91@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_rpi_node = vision_rpi_bot.publisher:main',   #added entry point for publisher
            'subscriber_rpi_node = vision_rpi_bot.subscriber:main'    #and subscriber
        ],
    },
)

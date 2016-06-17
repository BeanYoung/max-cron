from setuptools import setup

setup(
    name='MaxCron',
    version='0.0.1',
    url='https://github.com/BeanYoung/max-cron',
    license='MIT',
    author='BeanYoung',
    author_email='beanyoung.cn@gmail.com',
    description='',
    py_modules=['maxcron'],
    install_requires=[
        'click==6.6',
        'PyYAML==3.11',
        'requests==2.10.0'
    ],
    entry_points='''
        [console_scripts]
        maxcron=maxcron:cli
    ''',
)

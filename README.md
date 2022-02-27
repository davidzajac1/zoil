# ZOil

![Language](https://img.shields.io/badge/Language-Python-success?style=flat)
![License](https://img.shields.io/badge/License-MIT-informational?style=flat)
![Version](https://img.shields.io/badge/Version-0.0.3-informational?style=flat)

ZOil is a python library used to generate random Oil and Gas data. Most Oil and Gas data is either propreitary or costly to aquire. ZOil lets you quickly generate an unlimited amount of production data that can be used to for testing, anonymization and much more. ZOil was inspired by the [`Faker`](https://github.com/joke2k/faker) library.

## Installation

```bash
pip install zoil
```

## Usage

ZOil generates random production data using the `get_production_data` shown below with default keyword arguements

```python
zoil.get_production_data(start_date=datetime(year=1950,month=1,day=1), end_date=datetime.now(), qio_min=100, qio_max=2500, qig_min=500, qig_max=5000, qiw_min=100, qiw_max=2500)
    
"""
get_production_data generates a dictionary containing random production data.

:param granularity: 'monthly' | 'daily' Granularity of data
:param start_date: The start date of the production history
:param end_date: The end date of the production history
:param qio_min: The minimum initial oil production rate
:param qio_max: The maximum initial oil production rate
:param qig_min: The minimum initial gas production rate
:param qig_max: The maximum initial gas production rate
:param qiw_min: The minimum initial water production rate
:param qiw_max: The maximum initial water production rate
:return: A dictionary containing random production data
"""
```


See the example below to visualize a random wells production decline curve using [`pandas`](https://github.com/pandas-dev/pandas) and [`matplotlib`](https://github.com/matplotlib/matplotlib)

```python
from zoil import get_production_data
import matplotlib.pyplot as plt
import pandas as pd

production_data = get_production_data()

df = pd.DataFrame(production_data)

df.plot(x='date'
        , y=['oil', 'gas', 'water']
        , color=['green','red','blue']
        , title='Production History for a Random Well'
        , xlabel='Date'
        , ylabel='Production'
    )

plt.show()
```


Each time the `get_production_data` function is called a new dictionary of production data will be generated. The occasional halts in production are to represent workovers where the well is shut-in for repair for sometime.


<p align="center">
  <img width="auto" src="https://github.com/davidzajac1/zoil/blob/main/img/example_well.png?raw=true">
</p>

## To Do

- Make data more chaotic and realistic

- Create more keyword arguements

- Create new functions for other types of data (drilling, logging, etc.)

## Contribute

For any bugs, issues, suggestions please create an Issue or a Pull Request. 

## License
ZOil is released under the MIT License. See the bundled [LICENSE](https://github.com/davidzajac1/zoil/blob/main/LICENSE) file for details.
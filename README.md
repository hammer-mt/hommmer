# hommmer

A simple Marketing Mix Modeling library in Python.

## Quick start

### 1. Install the library

> `pip install hommmer`

### 2. Build the model

```
# import the library
import hommmer as mmm

# list media columns
media = ['facebook_spend', 'google_spend', 'tiktok_spend']

# build the model
model = mmm.build(
  'duff.csv',
  'beer_sales',
  media
)
```

#### Required

- **path**: the location of the file with your data
- **target**: the column with your conversions or conversion value
- **media**: a list of the columns with media spend

#### Optional

- **type**: label your target as 'conversions' or 'value'. default: 'conversions'
- **date**: the name of the date column. default: 'date'
- **format**: the format of the date column. default: 'YYYY-MM-DD'

Provide at least 1 year of weekly data where the `date` column is the start of the week (Monday).

### 3. Use the results

```
# show the charts and metrics
model.show()

# save locally to png and csv
model.save()
```

### Other features

Our solution is fully automated, but if you want to build a model manually, or use our helper functions for cleaning data, you can import from our sublibraries.

```python
import hommmer as mmm
from mmm.helpers import transpose
from mmm.features import adstocks
from mmm.charts import accuracy
from mmm.metrics import nrsme
from mmm.models import linear
```

## About hommmer

Most Marketing Mix Models (MMM) are built in Excel, because that's simpler than running a script. But there are things you can't do in Excel, like automatically building 1,130 models to see which one works best. We'd like MMM to be in the hands of more people, but that can't happen if you need to be a nuclear physicist to use it.

Most modeling libraries, like [Statsmodels](https://www.statsmodels.org/stable/index.html), [SciKit Learn](https://scikit-learn.org/stable/) and [Facebook's Robyn](https://facebookexperimental.github.io/Robyn/), are grown in a lab by scientists. They offer complex configuration options and advanced algorithms to cater for the smartest people at the biggest companies spending millions on marketing, who can afford to spend 3-6 months on a solution.

`hommmer` is built for the rest of us. The everyman (or woman) modeling hobbyist, for which MMM is just one of many jobs on the todo list. It's designed to be simple to use, but powerful underneath, without getting you into trouble. Over-simplifying things will annoy the statisticians (Doh!), but it'll make allocating budget quick and easy.

## Design Principles:

### 1. Excel is the operating system

Full compatability with Excel / GSheets / CSV for importing and exporting.

### 2. Don't make me think

All user input should be treated as error. Everything needs a good default.

### 3. Good is better than great

Where there's a choice between optimization and usefullness, take the latter.

## Contributors

These people are building `hommmer` for fun in their spare time. Cheers! 🍻

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://twitter.com/hammer_mt"><img src="https://avatars.githubusercontent.com/u/5264596?s=96&v=4" width="100px;" alt=""/><br /><sub><b>hammer-mt</b></sub></a><br /><a href="https://github.com/hammer-mt/hommmer/commits?author=hammer-mt" title="Code">💻</a></td>
    
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## Sources

Here's where we got our inspiration from.

- [Python/STAN Implementation of Multiplicative Marketing Mix Model](https://towardsdatascience.com/python-stan-implementation-of-multiplicative-marketing-mix-model-with-deep-dive-into-adstock-a7320865b334)
- [Facebook Robyn](https://facebookexperimental.github.io/Robyn/)
- [Bayesian Media Mix Modeling using PyMC3, for Fun and Profit](https://engineering.hellofresh.com/bayesian-media-mix-modeling-using-pymc3-for-fun-and-profit-2bd4667504e6)
- [Bayesian Methods for Media Mix Modeling with Carryover and
  Shape Effects](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46001.pdf)
- [Bayesian Methods for Hackers](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)
- [Statistical Rethinking: A Bayesian Course Using R and Stan](https://github.com/rmcelreath/statrethinking_winter2019)
- [A Hierarchical Bayesian Approach to Improve Media Mix Models Using Category Data](https://research.google/pubs/pub45999/)
- [Introduction to Bayesian Methods for MMM](https://getrecast.com/bayesian-methods-for-mmm/)
- [Feature Selection For Machine Learning in Python](https://machinelearningmastery.com/feature-selection-machine-learning-python/)
- [The Five Linear Regression Assumptions: Testing on the Kaggle Housing Price Dataset](https://boostedml.com/2018/08/testing-linear-regression-assumptions-the-kaggle-housing-price-dataset.html)
- [A Complete Guide To Linear Regression In Python](<[https://](https://www.listendata.com/2018/01/linear-regression-in-python.html)>)
- [Advertising Adstock – Concept & Formula]([)](https://analyticsartist.wordpress.com/2013/11/02/calculating-adstock-effect/)
- [Advertising Diminishing Returns & Saturation](https://analyticsartist.wordpress.com/2015/03/08/advertising-diminishing-returns-saturation/)
- [Building and Validating Media Mix Models](https://github.com/mecommerce/ThirdLove-Tech-Blog/blob/master/Media_Mix_Model/ThirdLove_MMM_Whitepaper.pdf)
- [Market Mix Modeling using Sales data](https://www.kaggle.com/imdineshgrewal/market-mix-modeling-using-sales-data)
- [Multiple Regression with Google Sheets XL Miner](https://www.youtube.com/watch?v=YhBU92eyNRo)
- [DT MART: Market Mix Modeling](https://www.kaggle.com/datatattle/dt-mart-market-mix-modeling)
- [How to create a basic Marketing Mix Model in scikit-learn](https://practicaldatascience.co.uk/machine-learning/how-to-create-a-basic-marketing-mix-model-in-scikit-learn)

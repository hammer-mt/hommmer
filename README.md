# hommmer

A simple Marketing Mix Modeling library in Python.

\*\*\* **_NOTE: this library is in alpha and not yet working._** \*\*\*

## Quick start

### 1. Install the library

> `pip install hommmer`

### 2. Build the model

```
# import the library
import hommmer as mmm

# download example data
mmm.load_duff()

# list media columns
media = ['facebook', 'google', 'tiktok']

# build the model
model = mmm.build('duff.csv', 'sales', media)
```

#### Required

- **path**: the location of the file with your data
- **target**: the column with your conversions or conversion value
- **media**: a list of the columns with media spend

#### Optional

- **organic**: a list of the organic columns. default: everything not listed in `media`.
- **date**: the column with your date labels (YYYY-MM-DD). default: `date`
- **verbose**: see what the model is doing by printing logs. default: `False`
- **override**: use custom settings for aspects of the model. default: `{}`

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
from hommmer.cleaners import transpose
from hommmer.features import adstocks
from hommmer.charts import accuracy
from hommmer.metrics import nrsme
from hommmer.models import Linear
```

## About Marketing Mix Modeling

Marketing Mix Modeling (MMM) was introduced in the 1960s to match spikes and dips in sales to actions taken in marketing. No user data required - it's privacy-friendly, adblocker-proof and works across all channels (even offline).

What used to be a 3-6 month, $50k+ job for the Fortune 500, is now an always-on, automated source of truth for startups like [Harry's](https://ladder.io/blog/attribution-technique), [HelloFresh](https://engineering.hellofresh.com/bayesian-media-mix-modeling-using-pymc3-for-fun-and-profit-2bd4667504e6) and [Monday․com](https://www.youtube.com/watch?v=p-YbHMCUycw). Even Facebook and Google are getting in on the game with [research papers](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46001.pdf) and [open-source projects](https://facebookexperimental.github.io/Robyn/).

## About hommmer

Most modeling libraries, like [Statsmodels](https://www.statsmodels.org/stable/index.html), [SciKitLearn](https://scikit-learn.org/stable/) and [Facebook's Robyn](https://facebookexperimental.github.io/Robyn/), cater to statisticians and data scientists. They offer complex configuration options and advanced algorithms only accessible to the biggest companies spending millions on marketing, who can afford to spend 3-6 months on a solution.

So most Marketing Mix Modeling by small businesses and startups is [done in Excel](https://www.saxifrage.xyz/post/econometrics-gsheets). But there are things you can't do in Excel, like automatically building 1,130 models to see which one works best. We'd like MMM to be in the hands of more people, but that can't happen if you need to be a nuclear physicist to use it.

`hommmer` is built for the rest of us. The 'everyman' (of any gender) modeling hobbyist, for which MMM is just one of many jobs on the todo list. It's designed to be simple to use, but powerful underneath, without getting you into trouble. Over-simplifying things will annoy the statisticians (Doh!), but it'll make allocating budget quick and easy.

## Design Principles:

### 1. Excel is the operating system

Full compatability with Excel / GSheets / CSV for importing and exporting.

### 2. Don't make me think

All user input should be treated as error. Everything needs a good default.

### 3. Good is better than great

Where there's a choice between optimization and usefullness, take the latter.

### 4. Better data beats fancier algorithms

We focus on helper functions to clean data, and treat algorithms as commodities.

### 5. We know less than the client

Assume the client knows what they're doing, then try to prove otherwise.

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

# PeaksValleys

Consider you have a list containing multiple numbers. By using ***PeaksValleys*** package, you can find and detect peaks and valleys.


## Screenshots

![PeaksValleys Screenshot](https://user-images.githubusercontent.com/8419324/134659955-6ad34a8a-df35-4c7c-bdf5-de7e0bb6e643.png)


## Usage

```python
from PeaksValleys import detectPeaksValleys
import random
import pandas as pd


randItems = random.sample(range(1, 200), 100)
data = {
    'Numbers': randItems
}
df = pd.DataFrame(data=data)

print(detectPeaksValleys(df['Numbers'], 21, 8))
```

As you see, `detectPeaksValleys` has 3 parameters:
```python
detectPeaksValleys(dataframeSeries, rollingNumber, averageSize):
```

1. `dataframeSeries` is series created by `pandas` package
2. `rollingNumber` is a number for smoothing numbers sequence (the higher number, the smoother sequence)
3. `averageSize` is a count of numbers creating an interval for detecting peaks and valleys (the less number, the more peaks and valleys)


## License

[MIT](https://choosealicense.com/licenses/mit/)

  
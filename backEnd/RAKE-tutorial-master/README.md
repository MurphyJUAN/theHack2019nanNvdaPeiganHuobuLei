# RAKE
---

A Python implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm as described in: Rose, S., Engel, D., Cramer, N., & Cowley, W. (2010). Automatic Keyword Extraction from Individual Documents. In M. W. Berry & J. Kogan (Eds.), Text Mining: Theory and Applications: John Wiley & Sons.

The source code is released under the MIT License.

## Installing rake

To install rake as a package, run:

`python setup.py install`

## Example use

```python
from nlp_rake import rake

stoppath = 'data/stoplists/SmartStoplist.txt'

rake_object = rake.Rake(stoppath, 5, 3, 4)

sample_file = open("data/docs/fao_test/w2167e.txt", 'r', encoding="iso-8859-1")
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print("Keywords:", keywords)
```

# 2022-12-26
# Run this in a Jupyter Notebook where just the second cell can be run iteratively 
# The `values` list is copy-pasted from the santabot script. Make sure it's up-to-date.

# First Cell

import random

values = {
  ("Papa", "A"),
  ("Eric", "B"),
  ("Jennie", "B"),
  ("Avery", "B"),
  ("Carsten", "B"),
  ("Drew", "B"),
  ("Jon", "C"),
  ("Beth", "C"),
  ("Elizabeth", "C"),
  ("Sarah", "C"),
  ("Mark", "C"),
  ("Paul", "D"),
  ("Kim", "D"),
  ("Sascha", "D"),
}

family = [v[0] for v in values]
random.shuffle(family)


# Second Cell

print(family.pop())
print(f'remaining {len(family)} of {len(values)}')

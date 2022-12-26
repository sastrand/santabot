# Top Cell

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


# Next cell

print(family.pop())
print(f'remaining {len(family)} of {len(values)}')

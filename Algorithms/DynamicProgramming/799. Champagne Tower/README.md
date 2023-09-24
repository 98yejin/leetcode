# 799. Champagne Tower

1. initialize a 2D array

- 0th row : 1 glass
- 1th row : 2 glasses

so [0.0] * (i+1) glasses are in the row

```python
glasses = []
for i in range(query_row +1):
  glasses.append([0.0]*(i+1))
```

2. pour the champagne

```python
glasses[0][0] = poured # top glass
```

3. iterate through each row and glass

- When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.
  - overflow = (glasses[i][j] - 1.0) / 2.0
- `(1, 1) -> (2, 1) (2, 2)`
  - `(i, j) -> (i+1, j), (i+1, j+1)`

4. one glass can't hold more than 1.0

- min(1.0 glasses[query_row][query_glass])
- maybe more than 1.0 champagne poured onto the floor.. :(
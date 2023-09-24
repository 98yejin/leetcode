class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0.0]*(i+1)for i in range(query_row + 1)]
        glasses[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if glasses[i][j] >= 1.0:
                    overflow = (glasses[i][j] - 1.0) / 2.0
                    if i + 1 <= query_row:
                        glasses[i+1][j] += overflow
                        glasses[i+1][j+1] += overflow
        return min(1.0, glasses[query_row][query_glass])

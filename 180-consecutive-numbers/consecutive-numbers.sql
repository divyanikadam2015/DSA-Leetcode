SELECT DISTINCT Num AS ConsecutiveNums
FROM (
    SELECT Num,
           LAG(Num, 1) OVER (ORDER BY Id) AS Prev1,
           LAG(Num, 2) OVER (ORDER BY Id) AS Prev2
    FROM Logs
) AS T
WHERE Num = Prev1 AND Num = Prev2;
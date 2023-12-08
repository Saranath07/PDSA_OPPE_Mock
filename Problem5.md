# Shortest Circular Route

A traveler made a travel plan which starts from city `s`. Due to time limitations, he decided to choose the shortest circular route that returns to the starting city `s` without using any road twice in the route. The route need not visit all cities.



Write a Function `shortestCircularRoute(WList, S)` that accepts a weighted adjacency list **wList** for the connected two-way road network of $n$ cities, labeled $0$ to $n-1$ and another parameter `s` which represents the start city. The function returns the total distance of the shortest circular route from city `s`.

**Note**: You are guaranteed that there is always at least one circular route.



**Hint**: Observe that a circular route from S consists of a road from S to a neighbour U followed by a path back from U to S that does not use the road (U, S).



```
WList = {
	source_index : [(destination_index, distance),
	(destination_index, distance),  
	....
	....
	source_index : [(destination_index, distance),
	(destination_index, distance)]
}
```



## Sample Input 1

```python
6 #n- number of nodes (cities) labeled 0 to 5
[(2,0,11), (5,0,12), (5,3,52), (5,1,17), (4,1,14), (3, 4,13), (2,3,10)] # edges (roads between city with distance)
0 #S source index (start city)
```

![img](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/m4.png)
### HW1

## Q1

The runtime for the given data is as follow:


Size / Time(ms) | Naive 3 sum | Smart 3 sum 
:-: | :-: | :-: 
8 | 0.02 | 0.05 
32 | 0.50 |      1.00      
128 | 31.25 | 15.62 
512 | 2109.38jj | 406.25 
1024 | 17062.50 | 1812.50 
4096 | 1124015.63 | 35343.75 
4196 | 1215734.38 | 39203.13 
8192 | 9034207.23 | 155703.13 

For naive 3 sum, when the size is double, the runtime is $2^3$ times longer, e.g., when size is changed from 4096 to 8192, the runtime is 8.3 times longer, which shows it has $O(N^3)$  growth rate


![image-20200209114311383](.\image-20200209114311383.png)

For smart 3 sum, when the size is double, the runtime is $2^2log2$ times longer, e.g., when size is changed from 4096 to 8192, the runtime is 4.4 times longer, which shows it has $O(N^2logN)$  growth rate

![image-20200209114144512](.\image-20200209114144512.png)

## Q2

The runtime for the given data is as follow:

| Size / Time(ms) | Quick Find | Quick Union | Weighted Quick Union |
| :-------------: | :--------: | :---------: | :------------------: |
|        8        |    3.13    |    0.23     |         0.24         |
|       32        |   12.22    |    0.20     |         0.22         |
|       128       |   48.12    |    0.31     |         0.30         |
|       512       |   188.55   |    0.52     |         0.61         |
|      1024       |   386.26   |    0.89     |         1.02         |
|      4096       |  1503.79   |    3.47     |         3.81         |
|      8192       |  2659.27   |    14.10    |         7.97         |

For quick find, **union()** is $O(N)$, **find()** is $O(1)$,and **read()** N data with each one conduct both **union** and **find**, that is $O(M*(N+1))$, so overall the algorithm has $O(N^2)$. For example, when size is changed from 1024 to 4096, the runtime is $3.89\approx4$ times, 

![image-20200209121303659](.\image-20200209121303659.png)

For quick union, the result shows a very small growth rate on small size data, but as the size grow, the growth rate is close to $O(N^2)$. The reason is as more points are involved, the *root* would be "deeper" to reach.

![image-20200209123907292](.\image-20200209123907292.png)

![image-20200209125649008](.\image-20200209125649008.png)

## Q3







## Q4

For this question, the algorithm use two local variants to store the maximum value and the minimum value during the iteration. I use *numpy.random.randint(low,high,len)* from **numpy** to generate random data with different length to test my implementation.

| Size/Time(ms) | Farthest pair |
| :-----------: | :-----------: |
|      128      |     0.15      |
|      512      |     0.12      |
|     1024      |     0.20      |
|     4096      |     0.64      |
|     8192      |     1.24      |
|     16384     |     2.45      |
|     32768     |     4.60      |
|     65536     |     9.39      |


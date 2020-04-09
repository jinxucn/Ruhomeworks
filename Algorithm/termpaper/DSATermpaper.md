# Several Solutions for String Searching

###### DATA STRUCTURES & ALGORITHMS TERM PAPER

###### Jin Xu, Rutgers University





**String Searching** algorithm refers to finding if there is any occurrence of a sting pattern within a given text. More advanced algorithms could also tell where the pattern appears, count the number of occurrences or replace the occurrences with new pattern. This paper gives a discussion about several solutions for string searching including Brute force matching, Rabin Karp algorithm, KMP algorithm, Boyer Moore algorithm and Sunday algorithm. The main goal is to analyze their performances and complexities.









**Contents**

[toc]







## 1 Introduction

A string searching problem can be defined as follows:

- Given a text: an array $T[0..n]$
- A pattern: an array $P[0..m]$, where $m \leq n$
- Every elements in $T$ and $P$ belong to an alphabet $Σ$
- Searching if there is a shift $s$, makes $T[s...s+m]=P[0...m]$ where $0 \leq s \leq n-m$

In normal cases, the pattern is considered to be relatively short, usually it is a word, while the text  could be relatively long, for example an article. So the performance of a algorithm is highly related to the length of the text and the pattern.

Also the alphabet is very essential to the problem. For example, matching an English word in an English article is much easier to do the same thing in other languages, because the length of code unit is variable in many languages.

For most string searching algorithm, in order to speed up the performance, we usually have some preprocessing work to do so the over all performance should consider the preprocessing part and the matching part.



## 2 Brute force matching

### 2.1 Implementation

Brute-force string matching is also called naive string matching. The idea is to compare each substring for every position in the text, and it does not have any preprocessing.

```pseudocode
#n for the length of T and m for the length of P
brute_force(T,P)
  for s from 0 to n-m
  	if T[s...s+m] = P[0...m] then match
  	else mismatch
```

### 2.2 Analysis

Obviously, this method is easy to implement and straightforward. It does not need any preprocessing and extra space. The time complexity is $O(MN)$, and the worst case, occurs when the pattern is the last substring of the text, is also $O(MN)$.



## 3 Rabin-Karp algorithm

### 3.1 Implementation

Instead of compare pattern with the substring directly, Rabin-Karp algorithm improves the brute-force matching by using the idea of hash function, that is if the hash value of pattern is not equal to the substring's, they must mismatch. So we compare the hash values first, if match then do the brute-force matching in case of the conflict of hash function.

```pseudocode
if hash(P) = hash(substring)
  if P[0...m] = substring[0...m] then match
else mismatch
```

The hash function is defined as follows:

- Taking a string with length $M$ as an M-digit base-R number, where $R$ is the size of the alphabet $Σ$
- Convert it into a integer by calculating its polynomial value, taking $R$ as $x$  and each digit as the coefficient 
- Use Horner's rule to speed up the calculation
- Use modular-Q operation to avoid large number calculation, where $Q$ is a random prime

```pseudocode
hash(s,m,r,Q)
  let result = 0
  for each letter of s[0...m]
    result = (r*result + letter) mod Q
  return result
```

Now we can calculate each substring of the text with the length of the pattern. However, if we da the hashing separately, it would cost much more time than brute-force matching. 

So here Rabin-Karp algorithm picks a clever trick to compute the hash value for the $t_{i+1}$ substring based on that of the $t_i$. The basic idea is to remove the leading digit and add the trailing digit. That is:
$$
t_{i+1} = (t_i - T[i]R^{M-1})R+T[i+m]
$$
Overall, the pseudocode is as follows:

```pseudocode
RK_matching(pattern,text)
  let Q = a random prime
  compute hash_pattern = hash(pattern)
  compute hash_s = hash(first substring with length of pattern)
	for each substring of text
	  if hash_pattern = hash_s
		brute_force_matching(pattern,substring)
      else
		renew hash_s = ((hash_s - text[i]*pow(d,M-1) mod Q)*R +T[i+M]) mod Q
```

### 3.2 Analysis

At the preprocessing part, we only do two hashings, which is $O(M)$. 

During the matching, each hash values comparison and renewing the hash values are $O(1)$, and if all the hash values are distinguish, which is the best case and most likely the average case, it totally takes $O(N)$ time.

The worst case of Rabin-Karp algorithm is $O(MN)$, which occurs when the hash values of every substrings are exactly the same resulting in $N$ times false positive comparisons.  

Also, Rabin-Karp algorithm use $O(2M)$ extra memory to store hash values.



## 4 KMP algorithm

### 4.1 Implementation

KMP algorithm, named after Knuth, Morris, and Pratt, is considered to be one of the greatest algorithms in computer science. The basic idea is to utilize the information of matched letters when a mismatch is detected and shift the matching window to skip those letters that would anyway mismatch.

Consider the following situation: 
$$
\begin{align}
TEXT:\qquad & \boldsymbol{ABC} DABDABCAB\\
PATTERN:\qquad & \boldsymbol{ABC} AB
\end{align}
$$
When $ABC$ is already match and $E$ is mismatch, we know that it would always mismatch $ABCD$ with $BCAB$, so we can skip those letters:
$$
\begin{align}
TEXT:\qquad  ABC&DABDABCAB\\
PATTERN:\qquad \quad \quad \ & ABCAB
\end{align}
$$
$$
\begin{align}
TEXT:\qquad  ABCD&\boldsymbol{AB} D\boldsymbol{AB}CAB\\
PATTERN:\qquad \qquad \quad \, \, & \boldsymbol{AB} C\boldsymbol{AB}
\end{align}
$$
And if in the pattern a prefix is also a suffix and they both match, we should jump to the suffix:

$$
\begin{align}
TEXT:\qquad  ABCDABD&\boldsymbol{ABCAB}\\
PATTERN:\qquad \qquad \qquad \quad \ \ & \boldsymbol{ABCAB}
\end{align}
$$
To implement this functionality, an array **lps[]** is used to stored the property of the pattern. It has the following characteristics:

- lps[0] = 0
- lps[i] is the length of the longest substring in pattern[0...i] that is both a prefix and a suffix

Take $ABCAB$ as an example:

1. lps[0] = 0
2. lps[1] = 0, because in "AB", prefix is "A"; suffix is "B", the longest one is 0
3. lps[2] = 0, because in "ABC", prefixes: {"A","AB"}, suffixes: {"BC","C"}, the longest one is 0
4. lps[3] = 1, because in "ABCA", prefixes: {"A","AB","ABC"}, suffixes: {"BCA","CA","A"}, the longest one is 1
5. lps[4] = 2, because in "ABCAB", prefixes: {"A","AB","ABC","ABCA"}, suffixes: {"BCAB","CAB","AB","B"}, the longest one is 2

Pseudocode: 

```pseudocode
lps(P)
  let lps = new Array(P.length)
  set lps[0] = 0
  let k = 0 as the length of a prefix
  let i = 1 for looping through P
  looping i, suffix through P
    if trail of suffix is equal to the trail of the prefix
      store k in lps and increse i, suffix
    else if prefix with length k is not a suffix
      if prefix with length k-1 is a suffix
      	try current suffix with previous prefix in next loop
      else if no prefix is a suffix
        inscese i, suffix in next loop
  return lps
```

With the lps array, the matching part is similar to brute-force matching:

```pseudocode
KMP_matching(P,T)
  let i, j for indexing P,T
  get lps of P
  looping until one of i,j reach P's,T's bound
    if P[i] = T[j] then i++,j++
    else
      if i != 0 try i = lps[i-1], the previous prefix match or not
      else if  i = 0, when no prefix works, just increse k for next substring
    if i = P.length then match
    else mismatch
```

### 4.2 Analysis

The performance of KMP algorithm is highly depend on the pattern. 

When the pattern have very few prefix that may also be its suffix, the lps array is sparse or empty(all zero), the matching and the preprocessing is faster.

When the pattern have lots of proper prefix, extremely when all the characters are the same, the lps array is more "full", leading to a longer time for matching.

However, it is clear that there is no double loop in the algorithm, which means even the worst case is $O(N)$.

In more detail, the overall time complexity is between $O(M+N) \sim O(2M+2N)$,  $O(M)$ for preprocessing and $O(N)$ for matching.

The best case occurs when lps is empty. And the worst case occurs in situations like matching "AAAA" in "AAABAAAB...".

Also, $O(M)$ extra memory is needed.



## 5 Boyer-Moore Algorithm

### 5.1 Implementation

Similar to KMP algorithm, Boyer-Moore algorithm also has an efficient way to skip those unnecessary comparisons and jump multiple characters at every loop. The main deference is that Boyer-Moore algorithm matches the pattern from the last character to the very beginning, which brings out the **Bad Character Heuristic**.

If we have a mismatch, also called a bad character, at the trail of the pattern with a character that does not exist in the pattern:
$$
\begin{align}
TEXT:\qquad  ABCD&\boldsymbol{E}ABCABCDA\\
PATTERN:\qquad    ABCD&\boldsymbol{A}
\end{align}
$$
Here, since there is no any "E" in the pattern (or consider at position j = -1), we should shift the pattern to the position after E, which is $4-(-1) = 5$:
$$
\begin{align}
TEXT:\qquad  ABCDE&ABCA\boldsymbol{B}CDA\\
PATTERN:\qquad \qquad \qquad  &ABCD\boldsymbol{A}
\end{align}
$$
And a mismatch occurs but "B" do exist in the pattern at position j = 2, so we shift to where it would match, which is $4-2 = 3$:
$$
\begin{align}
TEXT:\qquad  ABCDEABC&\boldsymbol{ABCDA}\\
PATTERN:\qquad \qquad \qquad \qquad \; &\boldsymbol{ABCDA}
\end{align}
$$

Therefore we can conclude the Bad Character Heuristic: 

**shift = the mismatch position occurs in pattern - the last position of bad character shows up in the pattern** 

Bad character heuristic only takes the advantage of the information of the "existing character positions" of the pattern. Like KMP algorithm, we can also utilize the "suffix/prefix" information, that is the **Good Suffix Heuristic**. 

If a suffix is matched and it is also a prefix of the pattern, it is called a good suffix:
$$
\begin{align}
TEXT:\qquad  ABAB&\boldsymbol{DA}BCDA\\
PATTERN:\qquad \ \ \   ABC&\boldsymbol{DA}
\end{align}
$$
Here "D" is the bad character, bad character shift is 1, but it would be better if we just shift the prefix to the suffix. In this case, "A" is a good suffix, position is 4, the last time it appears at j = 0, so shift is $4 - 0 = 4$:
$$
\begin{align}
TEXT:\qquad  ABABD&\boldsymbol{ABCDA}\\
PATTERN:\qquad \qquad \qquad   &\boldsymbol{ABCDA}
\end{align}
$$

The same, we conclude the Good Suffix Heuristic:

- **shift = the position of good suffix - the last position it appears.**
- the position of good suffix is consider to be the last character of it, e.g.,  "AB" is a good suffix of "ABCAB",  then its position is 4.
-  the last position it appeared is also consider to be the last character, e.g., "AB" is a good suffix of "ABCAB",  then last time it appears at 1.

At every step, Boyer-Moore algorithm takes the maximum of bad character shift and good suffix shift in order to get the optimal shift. 

To implement it, an array is required to record all the occurrences of characters for the pattern:

```pseudocode
occurrence_map(P,∑)
  let map = new Array(P.length)
  for each character x in ∑
    map[x] = 0
  for j from 1 to P.length
    map[P[j]] = j
  return map
```

Also, an array to remember each good suffix:

```pseudocode
good_suffix(P)
  let suffix = new Array(P.length).default(-1)
  for each suffix SF as P[i...P.length-1]
    if SF is also a preffix
      suffix[SF.length] = SF.position
  return suffix
```

Note that suffix array is like {-1,2,-1,-1,-1}, which means a suffix with length j has a corresponding prefix at position suffix[j]. For example, suffix "A" in "AAABA" has length of 1, and last time it appears at j = 2.

The matching function:

```pseudocode
BM_matching(P,T,∑)
  let bcmap = occurrence_map(P,∑)
  let gsuffix = good_suffix(P)
  for each substring S of T
    from the right to left compare S and P
      if all characters match then match
      else shift S based on max ( gsuffix[length of matched suffix], mismatch position - bcmap[last time it appears] )
```

### 5.2 Analysis

Matching from the right to the left makes Boyer-Moore algorithm really fast. In normal cases, the longer the pattern is, the faster it would be. 

In preprocessing part, it has $O(|∑|+M)$ for alphabet setting and occurrence recording, and another $O(M)$ for good suffix table.

During the matching, it takes $O(N)$ on average. The worst case occurs when the situation is like: matching "BAAAA" in "AAAAAAA...", having a $O(MN)$.

However, the best case is $O(N/M)$! The best case occurs in situation when bad character is always the last character and has no occurrence in the pattern. 

Generally speaking, Boyer-Moore algorithm is 3-5 times faster than KMP algorithm in real situation thanks to few repeat of characters in a word in human language causing lots of mismatch at the trail of the word and shift fast, which makes it widely used in editor applications.

Typically, an $O(|∑|+M)$ extra memory is needed.



## 6 Sunday algorithm

### 6.1 Implementation

From Boyer-Moore algorithm we have seen the powerful Bad Character Heuristic, which allows large scale shifting of the matching window. Sunday algorithm, named after Daniel Sunday, use the same idea and makes some improvements on it.

The strategy of Sunday algorithm is surprisingly simple:

Matching from the left to the right, until a mismatch occurs, focus on the first character C that outside of the matching window:

- If C has no occurrence within the pattern, then shift = M - (-1), skipping a whole matching window.
- Otherwise, shift = M - last position C appears in pattern.

Here is an example:
$$
\begin{align}
TEXT:\qquad  &\boldsymbol{AB}CAEABCABDA\\
PATTERN:\qquad    &\boldsymbol{AB}DA
\end{align}
$$
We have a mismatch at "C" with "D", so we focus on "E": it has no occurrence in the pattern, so we shift $4-(-1) =5$ and skip a whole window, because substrings with a  "E" would anyway mismatches:
$$
\begin{align}
TEXT:\qquad ABCAE &\boldsymbol{AB}CABDA\\
PATTERN:\qquad \qquad \qquad  &\boldsymbol{AB}DA
\end{align}
$$
Again a mismatch with "C" and "D", we focus on "B": id does appear at j = 1 in pattern, so we shift $4-1 =3$:
$$
\begin{align}
TEXT:\qquad ABCAEABC &\boldsymbol{ABDA}\\
PATTERN:\qquad \qquad \qquad \qquad \;  &\boldsymbol{ABDA}
\end{align}
$$
To implement it, we use the same *occurrence_map* function as Boyer More algorithm , except a little change:

```
occurrence_map(P,∑)
  let map = new Array(P.length)
  for each character x in ∑
    map[x] = -1				# change 0 to -1 for no occurrence letters
  for j from 1 to P.length
    map[P[j]] = j
  return map
```

The matching function is as follow:

```pseudocode
Sunday_matching(P,T,∑)
  let shift = occurrence_map(P,∑)
  for each substring S of T
    from the right to the left compare S and P
      if all characters match then match
      else shift S based on shift[the first character outside of the window]
```

### 6.2 Analysis

Sunday algorithm is quite similar to Boyer-Moore algorithm.

It takes $O(|∑|+M)$ time for preprocessing, and use $O(|∑|)$ extra memory.

The worst case of matching is also $O(MN)$, it happens in situations like: matching "AAAA" in "BAAABAAA...".

The average performance is $O(N)$ and the best case is also $O(N/M)$. 

Technically speaking, Sunday algorithm is slightly faster than Boyer-Moore algorithm because it has a relatively greater shift.



## 7 Conclusion

### 7.1 Comparison

To summarize,  the following table shows the performances for the algorithms discussed above:

|  Algorithm  |  Preprocessing   | Average Matching | Best Matching | Worst Matching | Extra memory |
| :---------: | :--------------: | :--------------: | :-----------: | :------------: | :----------: |
| Brute force |        /         | $O(MN)$          | $O(MN)$       | $O(MN)$        |      /       |
| Rabin-Karp  |      $O(M)$      | $O(N+M)$         | $O(N)$     | $O(MN)$        |   $O(2M)$    |
|     KMP     | $O(M)\sim O(2M)$ | $O(N)$         | $O(N)$      | $O(2N)$     |    $O(M)$    |
| Boyer-Moore |   $O(|∑|+2M)$    | $O(N)$         | $O(N/M)$      | $O(MN)$        |  $O(|∑|+M)$  |
| Sunday | $O(|∑|+M)$   |  $O(N)$  | $O(N/M)$ | $O(MN)$ | $O(|∑|)$ |

### 7.2 Use cases, advantages and disadvantages

**Brute force** matching, literally, is the slowest but the basic way to search a pattern even though it needs no preprocessing and extra memory. However, for those cases when the pattern is only one single character( or 2 at most), it could be the best method. For example, many programing languages use this method for the built-in *indexOf* function of string operation.

**Rabin-Karp** algorithm is at an embarrassing position. It faster but not as fast as other advanced algorithms, so it may not be a good choice to use Rabin-Karp algorithm in normal string searching problems. But the idea is worth to be extended. If in the case when the memory space cost is not a problem and only matching part matters, we can actually store every substring in advanced to speedup the matching. This algorithm would work very well with huge amount of data and super large hash map. For example, it is adoptable in plagiarism checking problem.

**KMP** algorithm, in short, is fast and stable. It always has $O(N)$ under any situation, which means it could be the best choice in any situation, since we do not need to worry about the performance. If we have little knowledge about the pattern and the text, KMP algorithm would never fail us.

**Boyer-Moore** algorithm and **Sunday** algorithm trade the runtime in worst case for a faster performance in best or average cases. Generally speaking, they could be 3-5 times faster than KMP algorithm on average, while in the worst case they could be the slowest two. Surprisingly, we do can rely on them in terms of string searching for human language. The reason is that most of the words (for example in English) have few repeats or overlaps, therefore long scale shift is possible within the algorithms. That why many editor software use Boyer-Moore or Sunday to implement their word searching functionality. 



## 8 References

1. Sedgewick, R. & Wayne, K., 2011. *Algorithms*. 4th ed. Addison-Wesley Professional.
2. Knuth, D & Morris, J. H. & Pratt, V. 1977. *Fast pattern matching in strings*. SIAM Journal on Computing. 6 (2): 323–350. 
3. Karp, R. M. & Rabin, M. O. 1987. *Efficient randomized pattern-matching algorithms*. IBM Journal of Research and Development. 31 (2): 249–260.
4. Boyer, R. S. & Moore, J. S. 1977. *A Fast String Searching Algorithm*. Comm. ACM. New York: Association for Computing Machinery. 20 (10): 762–772.
5. Hume A. & Sunday D. 1991. *Fast String Searching*. Software, Practice and Experience. 21 (11): 1221–1248.

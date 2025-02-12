# CMPS 2200  Recitation 02

**Name (Team Member 1):**Viraj Choksi  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.
The recurrence relation W(n) = aW(n/b) + f(n) can be analyzed using the Master Theorem. When f(n) = 1, the recurrence follows the case where c = 0 and log_b(a) > 0, leading to a complexity of O(n^(log_b(a))). For example, when a = 2 and b = 2, we get W(n) = O(n). When f(n) = log(n), it behaves similarly, as the logarithmic term does not significantly impact the recurrence, resulting in the same O(n^(log_b(a))) complexity. However, when f(n) = n, the comparison with n^(log_b(a)) determines whether W(n) follows O(n^(log_b(a))), O(n log n), or O(n). For a = 2, b = 2, and f(n) = n, we get W(n) = O(n log n). Empirical results confirm these theoretical findings, as computations for different n values show linear growth for f(n) = 1 and f(n) = log(n), while f(n) = n grows at a higher rate, consistent with O(n log n). Thus, our results align with theoretical expectations, demonstrating the applicability of the Master Theorem in analyzing this recurrence.

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 
The asymptotic behavior of W(n) depends on the relationship between c (from f(n) = n^c) and log_b(a) (from the recurrence W(n) = aW(n/b) + f(n)). Using the Master Theorem:
- If c < log_b(a), then the recurrence is dominated by the recursive term, and W(n) = O(n^(log_b(a))).
- If c > log_b(a), then the work function dominates, and W(n) = O(n^c).
- If c = log_b(a), then both terms contribute equally, and W(n) = O(n^c * log(n)).
For example, if we have W(n) = 2W(n/2) + n, then:
- log_2(2) = 1, so if f(n) = n^c with c < 1, then W(n) = O(n).
- If f(n) = n^c with c > 1, then W(n) = O(n^c).
- If f(n) = n, then c = log_2(2), so W(n) = O(n log n).

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 
The span, S(n), represents the longest path of dependencies in a recursive algorithm with parallelism, following the recurrence:
S(n) = S(n / b) + f(n)
Asymptotic Analysis:
f(n) = 1 → Expands to O(log n)
f(n) = log n → Forms an arithmetic sum of logs, yielding O(log^2 n)
f(n) = n → Geometric sum, leading to O(n)
Empirical Confirmation:
Implementing span_calc and testing across various n-values confirmed these trends. S(n) = O(log n), O(log^2 n), and O(n) as expected, verifying the theoretical analysis.
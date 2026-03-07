*This project has been created as part of the 42 curriculum by selouizg*

# Push_swap

## Description

**Push_swap** is an algorithmic sorting project from the 42 curriculum.  
The goal is to sort a list of integers using two stacks (`A` and `B`) and a limited set of operations, while minimizing the total number of instructions.

The challenge is not only to make the program work, but to make it efficient.

### Performance Targets

- Sort **100 numbers** in fewer than **700 operations**
- Sort **500 numbers** in fewer than **5500 operations**

This project is a deep introduction to:

- Sorting algorithms
- Algorithmic complexity (Big O notation)
- Optimization strategies
- Stack data structures
- Low-level memory management in C
- Performance-driven problem solving

---

## Allowed Operations

The program uses only the following operations:

- `sa`, `sb`, `ss` — swap
- `pa`, `pb` — push
- `ra`, `rb`, `rr` — rotate
- `rra`, `rrb`, `rrr` — reverse rotate

Every instruction counts.  
The objective is to sort using the smallest number of operations possible.

---

## Algorithmic Strategy

### 1️⃣ Pre-Sorting Using Insertion Sort (Value-Based Approach)

Before applying the chunk algorithm, I copied all input values into a standard C array and sorted this array using **Insertion Sort**.

I did **not** transform the numbers into indexes.

Instead, I worked directly with the original integer values.

The sorted array was used only as a reference to:

- Determine chunk boundaries (minimum and maximum values of each chunk range)
- Compare values during stack traversal
- Decide whether a value belongs to the current chunk

The stack nodes always stored and manipulated the **real integer values**, not normalized ranks.

This required careful comparison logic when checking whether:

- A value belongs to the current chunk
- A value is the maximum in Stack B
- A rotation direction is optimal

Working directly with values increased the algorithmic complexity slightly, but it strengthened my understanding of how chunk boundaries operate on real datasets.

---

### 2️⃣ Chunk-Based Sorting Algorithm

Instead of sorting elements one by one, I divided the dataset into **chunks**.

For example:

- 100 numbers → ~6 chunks  
- 500 numbers → ~13–14 chunks  

#### Phase 1 — Push Chunks to Stack B

- Iterate through Stack A
- If the element value belongs to the current chunk range → `pb`
- Rotate Stack B when necessary to maintain structure
- Continue until all chunks are pushed to Stack B

This creates a controlled distribution in Stack B.

By pushing smaller ranges progressively, Stack B forms a semi-ordered structure that reduces the number of rotations required during reconstruction.

---

#### Phase 2 — Push Back in Descending Order

- Find the largest element currently in Stack B
- Choose between `rb` and `rrb` depending on which is cheaper
- Bring the element to the top
- Use `pa` to push it back to Stack A
- Repeat until Stack B is empty

Stack A becomes fully sorted in ascending order.

---

## Optimization Strategy

To reach the required limits (700 / 5500 operations), I focused on:

- Calculating efficient chunk sizes
- Minimizing unnecessary rotations
- Choosing between `ra` and `rra` based on element position
- Rotating Stack B strategically during pushes
- Always bringing the closest maximum to the top in Phase 2
- Reducing redundant movements
- Avoiding unnecessary full stack scans

The main difficulty of this project was not sorting correctly —  
it was minimizing the number of operations.

---

## AI Usage & Learning Process

AI was used strictly as a **learning and analytical assistant**, not as a code generator.

I used AI to:

- Understand deeply how the chunk algorithm works
- Analyze why pushing smaller values first improves structure
- Study optimization strategies to stay under:
  - 700 operations (100 numbers)
  - 5500 operations (500 numbers)
- Clarify time complexity concepts
- Explore alternative chunk strategies
- Understand rotation cost optimization
- Improve algorithmic reasoning

I did **not**:

- Copy full implementations
- Generate my project automatically
- Paste AI-generated solutions blindly

All structural decisions, implementation logic, testing, and debugging were done manually.

AI supported my understanding, but the final solution was designed and written by me.

---

## Makefile Rules

The project includes a complete Makefile with the following rules:

- `make`  
  Compiles the project and generates the executable `push_swap`.

- `make clean`  
  Removes all object files (`.o`) generated during compilation.

- `make fclean`  
  Removes object files and the executable.

- `make re`  
  Performs `fclean` followed by `make` (full rebuild).

The Makefile respects 42 standards:

- No unnecessary relinking
- Proper dependency management
- Clear separation between compilation and cleaning rules

---

## Compilation & Usage

### Compile

```bash
make
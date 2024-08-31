# **Funk**
**FUNK** is a comprehensive tool for numerical analysis of functions. Polynomial approximation allows for estimating a function's value at specific points, while the numerical differentiation feature facilitates the calculation of its derivatives. These functionalities, with an intuitive interface and precise results, make FUNK an invaluable tool for students, researchers, and professionals requiring numerical calculations in various fields.

# **Installation**
Following the repository download, please confirm that you possess the requirements to guarantee the program's functionality. A prerequisite for implementing the FUNK application is the installation of Python, the foundational programming language. The requisite Python libraries for its operation are as follows: 

- **NumPy:** A fundamental package for numerical computations, providing efficient operations on arrays and matrices.
- **SymPy:** A library for symbolic mathematics, used to manipulate and simplify mathematical expressions.
- **Flet:** A framework for building cross-platform desktop and web applications with a simple and declarative syntax.
- **Matplotlib:** A plotting library for creating static, animated, and interactive visualizations.

To install these libraries, you can use pip, the Python package manager. Open your terminal or command prompt and run the following command:
```
pip install numpy sympy flet matplotlib
```

# **How to use:** 
The main menu offers two primary functions upon startup: Taylor series calculations and numerical differentiation. 

## **Taylor series**
1. Enter an arbitrary mathematical function f(x).  
2. Determine the degree n of the Taylor polynomial that will be used to approximate the function. 
3. Specify a point around which the approximation will be made.  
4. Evaluate the function at a specific point x to obtain the theoretical value. 

_Once these data are entered, FUNK:_
* Creates a graph that visualizes the function.
* Calculates the value of the polynomial at point x, providing the experimental and theoretical value of the approximation.
* Determines the relative error between the theoretical and experimental values, allowing for evaluation of the approximation's accuracy.

import streamlit as st
# Title and caption
st.title("Functions in Python")
st.caption("Understanding the building blocks of reusable code in Python")

# Intro paragraph
st.markdown(
    """
    In Python, **functions** are blocks of organized and reusable code that perform a specific task.
    They make your programs easier to manage, more readable, and reduce repetition.
    Using functions allows you to divide your code into logical sections.
    """
)

# Divider
st.divider()

# Section: Defining a Function
st.subheader("Defining a Function")

st.markdown(
    """
    A function in Python is defined using the `def` keyword followed by the function name and parentheses `()`.

    **Syntax:**
    ```python
    def function_name(parameters):
        # block of code
        return value
    ```
    """
)

# Example function
st.markdown("**Example:**")
st.code(
    """
def greet(name):
    return "Hello, " + name + "!"

# Calling the function
message = greet("Sandhya")
print(message)
    """,
    language="python"
)

st.markdown(
    " **Output:** `Hello, Sandhya!`"
)

# Divider
st.divider()

# Section: Types of Functions
st.subheader("Types of Functions in Python")

st.markdown(
    """
    1. **Built-in Functions:** These come pre-defined in Python (e.g., `len()`, `print()`, `sum()`).
    2. **User-defined Functions:** These are created by programmers to perform specific tasks.
    3. **Lambda Functions:** Anonymous, single-line functions defined using the `lambda` keyword.
    """
)

# Example of a lambda function
st.markdown("**Example of a Lambda Function:**")
st.code(
    """
square = lambda x: x * x
print(square(5))
    """,
    language="python"
)

st.markdown("➡️ **Output:** `25`")

# Divider
st.divider()

# Section: Importance
st.subheader("Why Are Functions Important?")

st.markdown(
    """
    ✅ Improve **code reusability**  
    ✅ Make programs **easier to test and debug**  
    ✅ Enhance **readability and structure**  
    ✅ Reduce **repetition** in code  
    """
)


# Unclosed File Resource Leak in Python
This repository demonstrates a common but easily overlooked error in Python: failing to close a file after opening it.  The `bug.py` file shows the erroneous code, which fails to explicitly close the opened file. This can lead to resource exhaustion and unexpected behavior.

The `bugSolution.py` file provides the corrected code, using `with open(...) as f:` to ensure the file is properly closed even if exceptions occur.

This example is crucial to highlight the importance of proper resource management in Python programming.
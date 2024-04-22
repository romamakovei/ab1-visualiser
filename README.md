# AB1 Visualiser

AB1 Visualiser is a Python program designed to visualize chromatogram data obtained after Sanger sequencing. 

## Installation & Getting Started
Python 3.11 must be already installed.

1. Create and activate virtual environment:
   ```shell
   python -m venv venv # Or python3 -m venv venv for some operating systems
   venv\Scripts\activate # For Windows
   source venv/bin/activate # For Linux, MacOS
   ```
2. Install the necessary libraries:
   ```shell
   pip install biopython
   pip install matplotlib
   pip install flet
   ```

## How to Run visualiser
Run the main script:
   ```shell
   python ab1_DNA_visualiser.py # Or python3 ab1_DNA_visualiser.py for some operating systems
   ```
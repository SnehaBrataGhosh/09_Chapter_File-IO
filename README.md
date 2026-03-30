Chapter 9 – File I/O

Overview
This folder contains programs that practice reading and writing files in Python. It covers basic open/read/write patterns, append mode, using the with-statement, and small exercises that store results in text files (high scores, multiplication tables, and log searching).

Concepts Covered
- Opening files in read/write/append modes ("r", "w", "a")
- Reading file content using read(), readline(), and readlines()
- Writing using write() and writelines()
- Using with open(...) to automatically close files
- Basic text replacement in files using str.replace()
- Creating multiple output files programmatically
- Searching text files for keywords and reporting line numbers

Code Highlights
- Read examples showing full read, single line read, and reading all lines
- Write examples showing overwrite vs append, and writing multiple lines at once
- with-statement demo that writes and then reads the same file
- Practice scripts:
  - Random “game score” with a persistent high score saved in HighScore.txt
  - Generating multiplication tables (1–29) into separate files under Tables/
  - Replacing a word inside a text file (Hey.txt)
  - Scanning a log file (log.txt) to check whether “python” appears, including line-number reporting

Learning Outcome
I learned the basics of working with files safely, especially using the with-statement. I also practiced using file I/O to make small utilities that save results and work with real text data.

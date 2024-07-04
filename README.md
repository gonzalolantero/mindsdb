# Report for Assignment 1

## Project chosen

Name: MindsDB --  https://github.com/mindsdb/mindsdb
My repository URL: https://github.com/gonzalolantero/mindsdb

Number of lines of code: ~114.5 KLOC 
Tool used to count it: lizard

![Screenshot 2024-07-04 at 12.10.25](https://hackmd.io/_uploads/BJgESeND0.png)


Programming language: Python

## Coverage measurement

### Existing tool

Used tool: Coverage.py

![Screenshot 2024-07-04 at 12.11.10](https://hackmd.io/_uploads/B1O8rlNwC.png)



### Your own coverage tool

The coverage tool operates through various functions that initialize, mark, and report the coverage of branches within certain functions. To achieve thorough branch coverage, the tool must consider both the "if" and "else" branches in the code. Consequently, I introduced "invisible" else statements (empty else statements with a mark_branch) to ensure that each branch is accounted for whenever a conditional statement is encountered.

For context, I made some helper functions to help me with the instrumentation:

![Screenshot 2024-06-24 at 17.08.13](https://hackmd.io/_uploads/Bk6xn-vLA.png)
These functions are later called in code screenshots and referred to.

#### Function 1: configure_logging

1. Coverage initialisation:

![Screenshot 2024-07-04 at 12.11.52](https://hackmd.io/_uploads/H1E5HlEPA.png)


2. Code with instrumentation:

![Screenshot 2024-07-04 at 12.12.05](https://hackmd.io/_uploads/BkJiHxNvA.png)


3. Coverage results output by the instrumentation:

![Screenshot 2024-07-04 at 10.23.50](https://hackmd.io/_uploads/r1hiSg4vR.png)



#### Function 2: getLogger

1. Coverage initialisation:

![Screenshot 2024-07-04 at 12.15.33](https://hackmd.io/_uploads/HyJO8eNDC.png)


2. Code with instrumentation:

![Screenshot 2024-07-04 at 12.15.44](https://hackmd.io/_uploads/SJW9UlNPA.png)


3. Coverage results output by the instrumentation: 

![Screenshot 2024-07-04 at 12.15.56](https://hackmd.io/_uploads/S1fn8xVwA.png)



## Coverage improvement

### Individual tests

#### Test 1: configure_logging

1. Example Usage: 

![Screenshot 2024-07-04 at 12.18.53](https://hackmd.io/_uploads/H1zXwgNwR.png)


2. Old coverage results: 

![Screenshot 2024-07-04 at 10.23.50](https://hackmd.io/_uploads/r1hiSg4vR.png)

3. New coverage results:

![Screenshot 2024-07-04 at 12.19.48](https://hackmd.io/_uploads/SJPUvg4wA.png)


4. Coverage improvement explanation:
The coverage improved and reached 100% by making sure that both the if and else branch were being tested. To reach the if-statement, I had to reset to allow a reconfiguration (logging_initialized = False)

#### Test 2: get_logger

1. Example Usage:

![Screenshot 2024-07-04 at 11.42.37](https://hackmd.io/_uploads/ByOdDx4wR.png)

![Screenshot 2024-07-04 at 12.21.02](https://hackmd.io/_uploads/H1yiwxNwR.png)


2. Old coverage results: 

![Screenshot 2024-07-04 at 12.15.56](https://hackmd.io/_uploads/S1fn8xVwA.png)

3. New coverage results:

![Screenshot 2024-07-04 at 12.22.26](https://hackmd.io/_uploads/rkLlOgNPR.png)


4. Coverage improvement explanation:
The coverage improved and reached 100% by making sure that both the if and else branch were being tested. To reach the if-statement, I had to log pre-made messages (logger.debug(), logger.info(), logger.warning()...)

## Overall

### Overall input log.py
Overall, for configure_logging and get_logger, I measured the change in the overall branch coverage using the Coverage.py tool. There was a branch coverage improvement as it shows an increase in the overall branch coverage from 57% to 59%. 

### Old Coverage Results

![Screenshot 2024-07-04 at 10.19.30](https://hackmd.io/_uploads/H10WdxEw0.png)


### New Coverage Results

![Screenshot 2024-07-04 at 11.07.44](https://hackmd.io/_uploads/Hyo8ux4DA.png)


### Tests added for configure_logging

![Screenshot 2024-07-04 at 12.24.59](https://hackmd.io/_uploads/Sy6YdeNvA.png)


### Tests added for get_logger

![Screenshot 2024-07-04 at 11.10.01](https://hackmd.io/_uploads/S1nq_x4wR.png)



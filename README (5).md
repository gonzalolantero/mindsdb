# Report for Assignment 1

## Project chosen

Name: MindsDB --  https://github.com/mindsdb/mindsdb
My repository URL: https://github.com/gonzalolantero/mindsdb

Number of lines of code: ~114.5 KLOC 
Tool used to count it: lizard
![image](https://hackmd.io/_uploads/ry4UCRmvC.png)

Programming language: Python

## Coverage measurement

### Existing tool

Used tool: Coverage.py

![image](https://hackmd.io/_uploads/BktULlXvA.png)


### Your own coverage tool

The coverage tool operates through various functions that initialize, mark, and report the coverage of branches within certain functions. To achieve thorough branch coverage, the tool must consider both the "if" and "else" branches in the code. Consequently, I introduced "invisible" else statements (empty else statements with a mark_branch) to ensure that each branch is accounted for whenever a conditional statement is encountered.

For context, I made some helper functions to help me with the instrumentation:
![Screenshot 2024-06-24 at 17.08.13](https://hackmd.io/_uploads/Bk6xn-vLA.png)
These functions are later called in code screenshots and referred to.

#### Function 1: configure_logging

1. Coverage initialisation:
![image](https://hackmd.io/_uploads/SkyLekEw0.png)

2. Code with instrumentation:
![image](https://hackmd.io/_uploads/rJxue1Nw0.png)

3. Coverage results output by the instrumentation:
![Screenshot 2024-07-04 at 10.23.50](https://hackmd.io/_uploads/BJBEW14PA.png)


#### Function 2: get_logging

1. Coverage initialisation:
![image](https://hackmd.io/_uploads/H11tWJEDA.png)

2. Code with instrumentation:
![image](https://hackmd.io/_uploads/rJ0n-JEvC.png)

3. Coverage results output by the instrumentation: 
![image](https://hackmd.io/_uploads/SJktzkEDR.png)


## Coverage improvement

### Individual tests

#### Test 1: configure_logging

1. Example Usage: 
![image](https://hackmd.io/_uploads/HkFo41EPR.png)

2. Old coverage results: 
![Screenshot 2024-07-04 at 10.23.50](https://hackmd.io/_uploads/BJBEW14PA.png)

3. New coverage results:
![image](https://hackmd.io/_uploads/BJlGVy4wC.png)

4. Coverage improvement explanation:
The coverage improved and reached 100% by making sure that both the if and else branch were being tested. To reach the if-statement, I had to reset to allow a reconfiguration (logging_initialized = False)

#### Test 2: get_logger

1. Example Usage:
![image](https://hackmd.io/_uploads/r1KjXyVwR.png)
![image](https://hackmd.io/_uploads/SyIpAJEw0.png)
![image](https://hackmd.io/_uploads/rJO6CkVDC.png)
![image](https://hackmd.io/_uploads/H1KCEyVvR.png)

2. Old coverage results: 
![image](https://hackmd.io/_uploads/SJktzkEDR.png)

3. New coverage results:
![image](https://hackmd.io/_uploads/B1YbBkNP0.png)

4. Coverage improvement explanation:
The coverage improved and reached 100% by making sure that both the if and else branch were being tested. To reach the if-statement, I had to log pre-made messages (logger.debug(), logger.info(), logger.warning()...)

## Overall

### Overall input log.py
Overall, for configure_logging and get_logger, I measured the change in the overall branch coverage using the Coverage.py tool. There was a branch coverage improvement as it shows an increase in the overall branch coverage from 57% to 59%. 

### Old Coverage Results
![Screenshot 2024-07-04 at 10.19.30](https://hackmd.io/_uploads/BJggB8yNvA.png)

### New Coverage Results
![image](https://hackmd.io/_uploads/HJWtUkVDR.png)

### Tests added for configure_logging
![image](https://hackmd.io/_uploads/S1K1vyVvR.png)

### Tests added for _put_to_database
![image](https://hackmd.io/_uploads/rJdbP1VDA.png)


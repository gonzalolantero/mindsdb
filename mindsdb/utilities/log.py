import logging
import os
from logging.config import dictConfig

logging_initialized = False

branch_coverage = {}

def initialize_coverage(func_name, num_branches):
    branch_coverage[func_name] = [False] * num_branches

def mark_branch(func_name, branch_id):
    branch_coverage[func_name][branch_id] = True

def report_coverage():
    total_branches = 0
    reached_branches = 0
    
    for func_name, branches in branch_coverage.items():
        func_total = len(branches)
        func_reached = sum(branches)
        
        total_branches += func_total
        reached_branches += func_reached
        
        coverage_percentage = (func_reached / func_total) * 100 if func_total > 0 else 0
        
        print(f"Coverage for {func_name}:")
        for i, reached in enumerate(branches):
            print(f"  Branch {i}: {'Reached! ✅' if reached else 'Not Reached ❌'}")
        print(f"  Function coverage: {coverage_percentage:.2f}%\n")
    
    overall_coverage = (reached_branches / total_branches) * 100 if total_branches > 0 else 0
    print(f"Overall branch coverage: {overall_coverage:.2f}%")

initialize_coverage("configure_logging", 2)

initialize_coverage("get_logger", 2)

class ColorFormatter(logging.Formatter):

    green = "\x1b[32;20m"
    default = "\x1b[39;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s %(processName)15s %(levelname)-8s %(name)s: %(message)s"

    FORMATS = {
        logging.DEBUG: logging.Formatter(green + format + reset),
        logging.INFO: logging.Formatter(default + format + reset),
        logging.WARNING: logging.Formatter(yellow + format + reset),
        logging.ERROR: logging.Formatter(red + format + reset),
        logging.CRITICAL: logging.Formatter(bold_red + format + reset),
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        return log_fmt.format(record)

def configure_logging():
    mindsdb_level = os.environ.get("MINDSDB_LOG_LEVEL", None)
    if mindsdb_level is not None:
        mark_branch("configure_logging", 0)
        mindsdb_level = getattr(logging, mindsdb_level)
    else:
        mark_branch("configure_logging", 1)
        mindsdb_level = logging.INFO

    logging_config = dict(
        version=1,
        formatters={"f": {"()": ColorFormatter}},
        handlers={
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "f",
            }
        },
        loggers={
            "": {  # root logger
                "handlers": ["console"],
                "level": logging.WARNING,
            },
            "__main__": {
                "level": mindsdb_level,
            },
            "mindsdb": {
                "level": mindsdb_level,
            },
            "alembic": {
                "level": mindsdb_level,
            },
        },
    )
    dictConfig(logging_config)


# I would prefer to leave code to use logging.getLogger(), but there are a lot of complicated situations
# in MindsDB with processes being spawned that require logging to be configured again in a lot of cases.
# Using a custom logger-getter like this lets us do that logic here, once.
def getLogger(name=None):
    """
    Get a new logger, configuring logging first if it hasn't been done yet.
    """
    global logging_initialized
    if not logging_initialized:
        mark_branch("get_logger", 0)
        configure_logging()
        logging_initialized = True
    else:
        mark_branch("get_logger", 1)

    return logging.getLogger(name)


if __name__ == "__main__":
    #test for get_logger branch 0 & configure_logging branch 1
    logger = getLogger()
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

    #test for configure_logging branch 0:
    os.environ["MINDSDB_LOG_LEVEL"] = "DEBUG"
    logging_initialized = False 
    logger = getLogger()

    #test for get_logger branch 1:
    logger = getLogger()

report_coverage()
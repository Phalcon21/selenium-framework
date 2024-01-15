import csv
import inspect
import logging
import softest


class Utils(softest.TestCase):

    def custom_logger(logLevel: str = logging.DEBUG):
        # Set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        fh = logging.FileHandler("reports/automation.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    def read_data_from_csv(filename: str):
        datalist = []
        csvdata = open(filename, "r")
        reader = csv.reader(csvdata)
        next(reader)
        for rows in reader:
            datalist.append(rows)
        return datalist

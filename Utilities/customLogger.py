# solution2
import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(r'.\demo\automation.log')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger







# import os
# import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         # Define the log directory and file path
#         # log_dir = './Logs'
#         # log_file = 'automation.log'
#         # log_path = os.path.join(log_dir, log_file)
#         #
#         # # Ensure the log directory exists
#         # if not os.path.exists(log_dir):
#         #     os.makedirs(log_dir)
#
#         # Avoid duplicate log handlers
#         # if not logging.getLogger().handlers:
#             # Configure logging
#             logging.basicConfig(
#                 filename='.//Logs//automation.log',
#                 format='%(asctime)s : %(levelname)s : %(message)s',
#                 datefmt='%m%d%y %I:%M:%S %p',
#                 level=logging.INFO
#             )
#
#             logger = logging.getLogger()
#             return logger

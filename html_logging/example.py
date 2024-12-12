import logging

from html_logger_initializer import HtmlLoggerInitializer

if __name__ == '__main__':
    class ExampleLogging:
        def run_some_function_example(self):
            HtmlLoggerInitializer.create(logger_name="my_logger", logs_path="c:\\temp\\logs", is_create_new_folder=True,
                                         max_bytes=1024 * 1024 * 2)
            my_logger = logging.getLogger("my_logger")
            for a in range(4000):
                my_logger.debug(f"debug message {a} " * 2)
                my_logger.info(f"info message {a} " * 22)
                my_logger.warning(f"warning message {a} " * 6)
                my_logger.error(f"error message {a} " * 8)

    ExampleLogging().run_some_function_example()

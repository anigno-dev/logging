# Logging Library
## HTML Logging
Generate a rolling files with html format that enable to filter log messages by severity

## Class: HtmlRollingAppender
Purpose
Handles log file rotation for .html files.
Ensures logs are stored in a human-readable HTML format for easier visualization in web browsers.
Writes the initial HTML structure (from HTML_PRETEXT) to each new log file.
Constructor (__init__)
Parameters:
logs_path:

Directory path where log files will be stored.
The directory is created if it does not exist.
log_file_prefix:

Prefix for the log files (default: "log").
Each log file will follow the naming format: <prefix>.<index>.html.
max_bytes:

Maximum size of a log file before rotation occurs (default: 2 MB).
backup_count:

Maximum number of log files to retain (default: 999).
encoding:

File encoding (default: "utf-8").
delay:

If True, defers file opening until the first log event.
Key Operations:
File Path Initialization:

Creates the specified log directory if it doesn’t exist.
Initializes the first log file as <prefix>.000.html.
HTML Header:

Writes HTML_PRETEXT to the newly created log file to initialize the HTML structure.
Base Filename:

Stores the base path (logs_path + log_file_prefix) for use during file rotation.
Method: doRollover()
Purpose:
Handles file rotation when the current log file exceeds the max_bytes size.

Process:
Close Current Stream:

Closes the current log file stream if it’s open.
Update File Index:

Increments the file index (next_file_ext) for the new log file.
Wraps around to 0 if the number of backups exceeds backup_count.
Open New Log File:

Creates and opens a new log file with the updated index.
Writes HTML_PRETEXT to ensure the new file maintains proper HTML structure.
Method: emit(record)
Purpose:
Handles logging of individual records.

Process:
Calls the parent emit() method to write the log message to the current file.
Ensures proper HTML formatting for each log record.
Features and Benefits
1. Log Rotation
Ensures log files don't grow indefinitely by capping their size (max_bytes).
Automatically manages old logs using the backup_count mechanism.
2. HTML Formatting
Every log file is an HTML document, initialized with HTML_PRETEXT for styling or formatting.
Makes log files easier to read in a browser compared to plain text.
3. Automatic Directory Management
Ensures the logs_path exists before creating log files.
4. Modular and Extendable
Built on Python’s logging system, making it compatible with standard logging configurations.


## Class: HtmlLoggerInitializer
Purpose
Simplifies the creation of a logging system.
Provides:
HTML rolling log files with structured formatting.
Console output for real-time feedback.
Supports file-based log rotation with customizable file size and backup limits.
Static Method: create()
Purpose
Initializes and configures a logger with:

HTML log file handler: Writes logs to rotating HTML files.
Console handler: Outputs logs to the terminal.
Parameters
logger_name:

The name of the logger to register in Python's logging system.
Used to uniquely identify and retrieve the logger.
logs_path:

The directory where log files will be stored (default: "logs").
is_create_new_folder:

If True, creates a new subdirectory for each logger run, based on the current date, time, and hostname.
If False, appends a timestamp to the log file names instead.
max_bytes:

Maximum size (in bytes) for each log file before it rotates (default: 2 MB).
Key Operations
Logger Setup:

Retrieves or creates a logger with the given logger_name.
Sets its log level to DEBUG to capture detailed logs.
Timestamped File and Folder Naming:

Generates a unique identifier for the logs using:
Current date and time (datetime.now()).
Hostname of the machine (socket.gethostname()).
Millisecond precision timestamp.
Depending on is_create_new_folder:
Creates a subdirectory for logs.
Or prefixes log files with the timestamp.
HTML File Handler:

Creates an instance of HtmlRollingAppender, a custom log handler for rotating HTML logs.
Stores log files in the determined path, using the specified max_bytes limit and up to 999 backups.
Console Handler:

Uses StreamHandler to send logs to the console (sys.stdout).
Provides real-time feedback during application runtime.
Formatting:

FORMATTER_TEXT_HTML (HTML log files): Ensures HTML logs are formatted as structured documents.
FORMATTER_TEXT (Console): Provides plain-text log formatting for better readability.
Handler Assignment:

Attaches both the HTML file handler and the console handler to the logger.
HTML and Console Handlers
HTML Rolling Appender:

Handles log rotation and ensures the files are in HTML format.
Makes logs readable in web browsers.
Stream Handler:

Outputs logs to the terminal for immediate visibility during execution.

Benefits
User-Friendly Logs:

HTML logs are easily navigable and presentable in a browser.
Console logs ensure immediate visibility for debugging.
File Rotation:

Prevents logs from growing indefinitely by limiting file size and maintaining backups.
Timestamped Organization:

Ensures logs from different runs are easily distinguishable.
Customizable and Extendable:

Parameters like max_bytes, backup_count, and logs_path can be adjusted for specific needs.


## Simple logging
### Purpose
Quickly set up a Python logger for console output with consistent formatting and severity-based log filtering.
Ensures that log messages include additional metadata, such as timestamps, severity levels, function names, and line numbers.
Code Explanation
Imports
logging: Core Python module for logging functionality.
sys: Provides access to standard input, output, and error streams.
SeverityPaddingFormatter:
A custom formatter class (likely defined in severity_padding_formatter) to control the format of log messages.
### Class: SimpleLogger
__init__ Method
Purpose: Initializes and configures a logger with a specific name and log level.
Parameters
name:

The unique identifier for the logger.
Multiple loggers can coexist, each with a different name.
level:

The severity level of the logs to handle (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
Determines the minimum severity of log messages that will be processed.

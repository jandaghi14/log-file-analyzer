# Log File Analyzer

A Python application that efficiently processes large log files using generators for memory-efficient log analysis and filtering.

## Features

- Memory-efficient log file processing using Python generators
- Parse log entries with timestamp, level, and message extraction
- Filter logs by level (INFO, WARNING, ERROR)
- Generator chaining for efficient data pipeline
- Comprehensive test coverage with pytest
- Handles large files without loading entire content into memory

## Technologies Used

- **Python 3.7+**
- **Generators** - Memory-efficient iteration
- **pytest** - Testing framework
- **File I/O** - Reading log files line by line

## How It Works

### Generators Used:

1. **`read_log_lines(filename)`** - Yields log lines one at a time
   - Opens file and reads line by line
   - Memory efficient for large files

2. **`filter_by_level(lines, level)`** - Filters logs by level
   - Takes a generator of lines
   - Yields only lines matching specified level

3. **`parse_log_entry(line)`** - Parses individual log entries
   - Extracts timestamp, level, and message
   - Returns structured dict

4. **`analyze_logs(filename, level=None)`** - Main analyzer
   - Chains generators together
   - Returns parsed and optionally filtered logs

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/log-file-analyzer.git
cd log-file-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Analyze all logs:
```python
from log_analyzer import analyze_logs

# Get all logs
all_logs = analyze_logs("sample.log")
for log in all_logs:
    print(log)
```

### Filter by log level:
```python
# Get only ERROR logs
errors = analyze_logs("sample.log", level="ERROR")
for error in errors:
    print(error)

# Get only WARNING logs
warnings = analyze_logs("sample.log", level="WARNING")
```

### Run the demo:
```bash
python log_analyzer.py
```

## Log Format

The analyzer expects logs in this format:
```
YYYY-MM-DD HH:MM:SS LEVEL Message text
```

Example:
```
2025-12-30 10:15:23 INFO User logged in: user123
2025-12-30 10:16:45 ERROR Database connection failed
```

## Running Tests

Run all tests:
```bash
pytest test_log_analyzer.py -v
```

Test coverage includes:
- Reading log lines with generator
- Parsing log entries
- Filtering by log level
- Full log analysis (all logs)
- Full log analysis (filtered)

## Project Structure

```
log-file-analyzer/
├── log_analyzer.py          # Main analyzer with generators
├── test_log_analyzer.py     # Test suite
├── sample.log              # Sample log file
├── requirements.txt        # Dependencies
└── README.md              # Documentation
```

## Why Generators?

Generators are perfect for log file analysis because:
- **Memory Efficient**: Process one line at a time, not entire file
- **Scalable**: Works with GB-sized log files
- **Fast**: Lazy evaluation, only process what you need
- **Chainable**: Combine multiple generators in a pipeline

## Real-World Applications

- Server log analysis
- Application debugging
- Security audit log processing
- Performance monitoring
- Error tracking and reporting

## Future Enhancements

- Support multiple log formats
- Real-time log monitoring
- Statistical analysis (error rates, patterns)
- Export to CSV/JSON
- Regex-based filtering
- Date range filtering
- Visualization dashboard

## License

MIT License
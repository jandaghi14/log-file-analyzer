'''
test_read_log_lines - Test that generator yields lines
test_parse_log_entry - Test parsing a single line
test_filter_by_level - Test filtering by ERROR
test_analyze_logs_all - Test getting all logs
test_analyze_logs_filtered - Test filtering by level
'''
import pytest
from unittest.mock import patch , Mock
from log_analyzer import read_log_lines , filter_by_level , parse_log_entry , analyze_logs

def test_read_log_lines():
    lines = read_log_lines('sample.log')
    lines = list(lines)
    assert len(lines) == 10
    assert "User logged in: user123" in lines[0]

def test_parse_log_entry():
    lines = read_log_lines('sample.log')
    a = parse_log_entry(next(lines))
    assert a['message'] == 'User logged in: user123'
    a = parse_log_entry(next(lines))
    assert a['message'] == 'Database connection failed'
def test_filter_by_level():
    lines = read_log_lines('sample.log')
    filter_line = list(filter_by_level(lines , 'INFO'))
    assert 'User logged in: user123' in filter_line[0]
    
def test_analyze_logs_all():
    result = analyze_logs('sample.log' , None)
    assert len(result) == 10
    
def test_analyze_logs_filtered():
    result = analyze_logs('sample.log' , 'INFO')
    assert len(result) == 4
    
    
    
    
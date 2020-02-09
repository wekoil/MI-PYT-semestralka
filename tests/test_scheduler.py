from src.scheduler import Scheduler
import pytest

def test_create_event_with_wrong_date(capsys):
    with pytest.raises(Exception) as excinfo:
        Scheduler.create_event('test', 'test')
    cp = capsys.readouterr()
    assert not cp.out
    assert 'Could not match input to any of' in str(excinfo.value)

def test_create_event(capsys):
    Scheduler.create_event('test', '2021-01-30 19:25:00')
    cp = capsys.readouterr()
    assert not cp.err

def test_read_nonexistring_calendar(capsys):
    sch = Scheduler()
    with pytest.raises(Exception) as excinfo:
        sch.read_calendar(file='non_existring_file.extension')
    cp = capsys.readouterr()
    assert not cp.out
    assert 'No such file or directory:' in str(excinfo.value)

def test_read_empty_calendar(capsys):
    sch = Scheduler()
    with pytest.raises(Exception) as excinfo:
        sch.read_calendar(file='tests/empty.ics')
    cp = capsys.readouterr()
    assert not cp.out
    assert 'Multiple calendars in one file are not supported by this method.' in str(excinfo.value)

def test_load_no_events_calendar(capsys):
    sch = Scheduler()
    sch.load_calendar(calendar_file='tests/no_events.ics')
    events = sch.get_events()
    p = capsys.readouterr()
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err
    assert not events

def test_load_some_events_calendar(capsys):
    sch = Scheduler()
    sch.load_calendar(calendar_file='tests/some_events.ics')
    events = sch.get_events()
    p = capsys.readouterr()
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err
    assert events

def test_process_sms(capsys):
    sch = Scheduler()
    event = Scheduler.create_event('test', '2221-01-30 19:25:00', how='SMS')

    with pytest.raises(Exception) as excinfo:
        sch.process_event(event)

    events = sch.get_events()
    p = capsys.readouterr()
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err
    assert not events

def test_process_mail(capsys):
    sch = Scheduler()
    event = Scheduler.create_event('test', '2221-01-30 19:25:00', how='mail')

    sch.process_event(event)

    events = sch.get_events()
    p = capsys.readouterr()
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err
    assert events
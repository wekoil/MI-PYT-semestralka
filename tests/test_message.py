from src.message import Mail, Slack, WhatsApp, Message
import pytest

def test_mail(capsys):
    Message.set_config_files('credentials.cfg', 'config.cfg')
    Mail.send()
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err

def test_mail_wrong_smtp(capsys):
    Message.set_config_files('credentials.cfg', 'tests/config_wrong_smtp.cfg')
    with pytest.raises(Exception) as excinfo:
        Mail.send()
    assert 'service not known' in str(excinfo.value) or '[Errno 11001] getaddrinfo failed' in str(excinfo.value)
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err

def test_mail_wrong_sender(capsys):
    Message.set_config_files('credentials.cfg', 'tests/config_wrong_sender.cfg')
    with pytest.raises(Exception) as excinfo:
        Mail.send()
    assert 'Username and Password not accepted.' in str(excinfo.value)
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err

def test_mail_wrong_password(capsys):
    Message.set_config_files('credentials_example.cfg', 'config.cfg')
    with pytest.raises(Exception) as excinfo:
        Mail.send()
    assert 'Username and Password not accepted.' in str(excinfo.value)
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err

def test_slack(capsys):
    Message.set_config_files('credentials.cfg', 'config.cfg')
    Slack.send()
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err

def test_slack_wrong_channel(capsys):
    Message.set_config_files('credentials.cfg', 'tests/config_wrong_channel.cfg')
    with pytest.raises(Exception) as excinfo:
        Slack.send()
    assert 'The server responded with: {\'ok\': False, \'error\': \'channel_not_found\'}' in str(excinfo.value)
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err

def test_slack_wrong_password(capsys):
    Message.set_config_files('credentials_example.cfg', 'config.cfg')
    with pytest.raises(Exception) as excinfo:
        Slack.send()
    assert 'The server responded with: {\'ok\': False, \'error\': \'invalid_auth\'}' in str(excinfo.value)
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err

def test_whatsapp(capsys):
    Message.set_config_files('credentials.cfg', 'config.cfg')
    WhatsApp.send()
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err

def test_whatsapp_wrong_SID(capsys):
    Message.set_config_files('credentials_example.cfg', 'config.cfg')
    with pytest.raises(Exception) as excinfo:
        WhatsApp.send()
    assert 'Unable to create record: The requested resource /2010-04-01/Accounts/PLACE_HERE_YOUR_SID/Messages.json was not found' in str(excinfo.value)
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err

def test_whatsapp_wrong_sender(capsys):
    Message.set_config_files('credentials.cfg', 'tests/config_wrong_sender.cfg')
    with pytest.raises(Exception) as excinfo:
        WhatsApp.send()
    assert 'Unable to create record: Twilio could not find a Channel with the specified From address' in str(excinfo.value)
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err

def test_whatsapp_wrong_token(capsys):
    Message.set_config_files('tests/credentials_wrong.cfg', 'config.cfg')
    with pytest.raises(Exception) as excinfo:
        WhatsApp.send()
    assert 'HTTP 401 error: Unable to create record: Authenticate' in str(excinfo.value)
    cp = capsys.readouterr()
    assert not cp.out
    assert not cp.err
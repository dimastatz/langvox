import pytest

import audiotrace


def test_version_exposed():
    assert isinstance(audiotrace.__version__, str)


def test_analyze_not_implemented():
    with pytest.raises(NotImplementedError):
        audiotrace.analyze("call.wav")


def test_batch_not_implemented():
    with pytest.raises(NotImplementedError):
        audiotrace.batch(["call1.wav", "call2.wav"])

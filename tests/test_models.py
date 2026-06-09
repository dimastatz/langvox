from audiotrace import CallReport, Transcript, Turn


def test_callreport_defaults():
    report = CallReport()
    assert report.quality.overall_score == 0.0
    assert report.events.outcome == "completed"
    assert report.events.drop_off_turn is None
    assert report.transcript.turns == []


def test_callreport_roundtrip():
    report = CallReport(
        transcript=Transcript(
            full_text="hello",
            turns=[Turn(speaker="agent", text="hello", start_ms=0, end_ms=500)],
        )
    )
    restored = CallReport.model_validate(report.model_dump())
    assert restored.transcript.turns[0].speaker == "agent"
    assert restored.transcript.full_text == "hello"

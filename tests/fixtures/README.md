# Test fixtures

Golden audio and other fixtures used by the test suite.

## `premier_phone_call_30s.mp3`

A 30-second customer-service phone call (service rep + customer), used as
golden data for transcription, diarization, quality, and sentiment tests.

- **Format:** MP3, 48 kHz, stereo, 128 kbps, 30.0 s (~470 KB)
- **Source:** Deepgram "Premier Phone Services" demo sample — the opening of a
  customer call, published by Deepgram for developer testing.
  Original (full ~10 min call): <https://www.datocms-assets.com/96965/1687565980-premier_broken-phone.mp3>
- **Provenance:** trimmed to the first 30 s with no re-encoding (stream copy),
  preserving the original audio exactly:

  ```bash
  ffmpeg -ss 0 -t 30 -i premier_broken-phone.mp3 -c copy premier_phone_call_30s.mp3
  ```

> Note: this clip originates from Deepgram's publicly published demo sample.
> It is included here for testing/illustration with attribution. If you
> redistribute AudioTrace commercially, confirm the sample's terms with the
> original publisher first.

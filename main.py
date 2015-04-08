__author__ = 'Shadow'

import telemetry.loader
import telemetry.errors

try:

    loader = telemetry.loader.TelemetryLoader()
    loader.load_file('motec', 'data/Rally.ld').read_head()


except (telemetry.errors.TelemetryError, telemetry.errors.LoaderError) as e:
    print("Exception: "+e.value)
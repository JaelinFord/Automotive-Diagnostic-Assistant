diagnostics = {
    "no_start": {
        "question": "Does the engine crank?",
        "yes": "check_fuel",
        "no": "check_battery"
    },
    "check_battery": {
        "question": "Are dashboard lights dim or off?",
        "yes": "battery_issue",
        "no": "starter_issue"
    },
    "check_fuel": {
        "question": "Do you hear the fuel pump?",
        "yes": "check_ignition",
        "no": "fuel_pump_issue"
    },
    "check_ignition": {
        "question": "Is there spark at the spark plugs?",
        "yes": "unknown_issue",
        "no": "ignition_issue"
    },
    "check_engine_light": {
        "question": "Is the vehicle experiencing noticeable performance issues (rough idle, stalling, loss of power)?",
        "yes": "check_engine_severe",
        "no": "check_engine_scan"
    },
    "check_engine_severe": {
        "question": "Is the check engine light flashing?",
        "yes": "misfire_issue",
        "no": "sensor_issue"
    },
    "check_engine_scan": {
        "question": "Do you have access to an OBD-II scanner?",
        "yes": "read_codes",
        "no": "recommend_scan_tool"
    },
    "read_codes": {
        "question": "Are there misfire-related codes (e.g., P0300)?",
        "yes": "misfire_issue",
        "no": "emissions_issue"
    },

    # Results
    "battery_issue": {
        "result": "Battery voltage may be low. Test battery and replace if necessary."
    },
    "starter_issue": {
        "result": "Starter motor may be faulty. Inspect starter and connections."
    },
    "fuel_pump_issue": {
        "result": "Fuel pump may not be working. Check fuel pump and relay."
    },
    "ignition_issue": {
        "result": "Ignition system failure. Check spark plugs and ignition coils."
    },
    "unknown_issue": {
        "result": "Issue unclear. Further diagnostics required. Escalate to Level 2 support."
    },
    "misfire_issue": {
        "result": "Engine misfire detected. Inspect spark plugs, ignition coils, and fuel injectors. Immediate attention recommended."
    },
    "sensor_issue": {
        "result": "Possible sensor-related issue. Inspect MAF, O2 sensors, and wiring connections."
    },
    "emissions_issue": {
        "result": "Emissions-related fault detected. Check O2 sensors, catalytic converter, and fuel system."
    },
    "recommend_scan_tool": {
        "result": "OBD-II scan required. Retrieve diagnostic trouble codes before proceeding. Escalate if unavailable."
    }
}

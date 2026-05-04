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
    }
}

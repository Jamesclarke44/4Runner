ENGINE_PERFORMANCE = {

    "ignition_inspection": {
        "category": "Engine Performance",
        "subcategory": "Ignition",
        "section": "Ignition System - On-Vehicle Inspection",
        "specs": {
            "spark_plug": {
                "recommended": "DENSO SK16HR11",
                "electrode_gap_new": "1.0 to 1.1 mm (0.0394 to 0.0433 in.)",
                "electrode_gap_max_used": "1.3 mm (0.0512 in.)",
                "insulation_resistance": "10 MΩ or higher"
            }
        },
        "tools": [
            "Spark plug socket",
            "Megohmmeter",
            "Spark plug cleaner",
            "Feeler gauge"
        ],
        "workflow": [
            "",
            "=== IGNITION SYSTEM - ON-VEHICLE INSPECTION ===",
            "",
            "1. PERFORM SPARK TEST",
            "",
            "   a. Check for DTCs.",
            "   NOTE: If any DTC is output, perform the troubleshooting procedures for that DTC.",
            "",
            "   b. Check if sparks occur.",
            "   c. Remove the 6 spark plugs.",
            "   d. Install the spark plug to the ignition coil assembly and connect the",
            "      ignition coil assembly connector.",
            "   e. Disconnect the fuel pump ECU connector.",
            "   f. Ground the spark plug.",
            "   g. Visually check that sparks occur while the engine is being cranked.",
            "",
            "   NOTE: Be sure to ground the spark plug when checking.",
            "   NOTE: Replace the ignition coil assembly if it receives an impact.",
            "   NOTE: Do not crank the engine for more than 2 seconds.",
            "",
            "   h. Check that the ignition coil assembly connector is securely connected.",
            "",
            "   RESULT:",
            "   NG → Connect securely, then retest",
            "   OK → Go to next step",
            "",
            "   i. Perform a spark test on each ignition coil assembly.",
            "   j. If there is a cylinder where sparks do not occur, replace its ignition",
            "      coil assembly with one from a cylinder where sparks occur normally.",
            "   k. Crank the engine and visually check that sparks occur at the cylinder.",
            "",
            "   RESULT:",
            "   OK → Replace ignition coil assembly",
            "   NG → Go to next step",
            "",
            "   l. Inspect the spark plug.",
            "   m. Replace the spark plug with a known good one.",
            "   n. Perform spark test again.",
            "",
            "   RESULT:",
            "   OK → Replace spark plug",
            "   NG → Go to next step",
            "",
            "   o. Check power supply to ignition coil assembly.",
            "      - Turn the ignition switch to ON.",
            "      - Check that there is battery voltage at the ignition coil assembly",
            "        positive (+) terminal.",
            "",
            "   RESULT:",
            "   NG → Check wiring between ignition switch and ignition coil assembly",
            "   OK → Go to next step",
            "",
            "   p. Check the VVT sensor for intake side.",
            "   q. Check the VVT sensor for exhaust side.",
            "   r. Check the crankshaft position sensor.",
            "   s. Install the 6 spark plugs.",
            "   t. Connect the fuel pump ECU connector.",
            "",
            "2. INSPECT SPARK PLUG",
            "",
            "   a. Check the electrode.",
            "   b. Using a megohmmeter, measure the insulation resistance.",
            "",
            "   Standard Insulation Resistance:",
            "   Spark plug (terminal part) - Body ground: 10 MΩ or higher",
            "",
            "   c. If a megohmmeter is not available, perform this simple inspection:",
            "      - Quickly accelerate the engine to 4000 rpm 5 times.",
            "      - Remove the spark plug.",
            "      - Visually check the spark plug.",
            "      - If the electrode is dry, the spark plug is functioning properly.",
            "      - If the electrode is damp, proceed to the next step.",
            "",
            "   d. Check the spark plug for any damage on its threads and insulator.",
            "      - If there is damage, replace the spark plug.",
            "",
            "   Recommended Spark Plug: DENSO SK16HR11",
            "",
            "   e. Clean the spark plugs.",
            "   f. Check the spark plug electrode gap.",
            "",
            "   Maximum electrode gap for used spark plug: 1.3 mm (0.0512 in.)",
            "   If the gap is more than the maximum, replace the spark plug.",
            "",
            "   Electrode gap for new spark plug: 1.0 to 1.1 mm (0.0394 to 0.0433 in.)"
        ]
    },
    "spark_plug_removal": {
        "category": "Engine Performance",
        "subcategory": "Ignition",
        "section": "Spark Plug - Removal",
        "tools": [
            "Spark plug socket (14 mm)",
            "Socket set",
            "Extensions",
            "Torque wrench"
        ],
        "references": {
            "v_bank_cover": "V-Bank Cover Removal",
            "air_tube": "Air Tube Removal",
            "no1_emission_control_valve": "No. 1 Emission Control Valve Set Removal",
            "no2_air_tube": "No. 2 Air Tube Removal",
            "no2_emission_control_valve": "No. 2 Emission Control Valve Set Removal"
        },
        "workflow": [
            "",
            "=== SPARK PLUG - REMOVAL ===",
            "",
            "1. REMOVE V-BANK COVER",
            "   → Refer to V-Bank Cover Removal",
            "",
            "2. REMOVE AIR CLEANER CAP AND HOSE",
            "",
            "   a. Disconnect the mass air flow meter connector, vacuum hose and",
            "      ventilation hose and detach the 4 clamps.",
            "   b. Loosen the clamp.",
            "   c. Unfasten the 4 hook clamps, and then remove the bolt and air",
            "      cleaner cap and hose.",
            "",
            "3. REMOVE AIR TUBE",
            "   → Refer to Air Tube Removal",
            "",
            "4. REMOVE NO. 1 EMISSION CONTROL VALVE SET",
            "   → Refer to No. 1 Emission Control Valve Set Removal",
            "",
            "5. REMOVE NO. 2 AIR TUBE",
            "   → Refer to No. 2 Air Tube Removal",
            "",
            "6. REMOVE NO. 2 EMISSION CONTROL VALVE SET",
            "   → Refer to No. 2 Emission Control Valve Set Removal",
            "",
            "7. REMOVE IGNITION COIL ASSEMBLY",
            "",
            "   a. Disconnect the 6 ignition coil assembly connectors.",
            "   b. Remove the 6 bolts and 6 ignition coil assemblies.",
            "",
            "8. REMOVE SPARK PLUG",
            "",
            "   a. Remove the 6 spark plugs."
        ]
    },
    "v_bank_cover_removal": {
        "category": "Engine Performance",
        "subcategory": "Engine Covers",
        "section": "V-Bank Cover - Removal",
        "tools": ["None"],
        "workflow": [
            "",
            "=== V-BANK COVER - REMOVAL ===",
            "",
            "1. REMOVE V-BANK COVER",
            "",
            "   a. Raise the front of the V-bank cover to detach the 2 pins.",
            "   b. Detach the 2 V-bank cover hooks from the bracket.",
            "   c. Remove the V-bank cover.",
            "",
            "   *1  Pin",
            "   *2  V-bank Cover Hook"
        ]
    },
    "air_tube_removal": {
        "category": "Engine Performance",
        "subcategory": "Air Intake",
        "section": "Air Tube - Removal",
        "tools": [
            "Socket set",
            "Wrench"
        ],
        "workflow": [
            "",
            "=== AIR TUBE - REMOVAL ===",
            "",
            "1. REMOVE AIR TUBE",
            "",
            "   a. Remove the 2 bolts, 2 nuts and air tube.",
            "   b. Remove the 2 gaskets from the air tube.",
            "",
            "   NOTE: Be careful not to damage the installation surfaces of the gaskets."
        ]
    },
    "no1_emission_control_valve_removal": {
        "category": "Engine Performance",
        "subcategory": "Emissions",
        "section": "No. 1 Emission Control Valve Set - Removal",
        "tools": [
            "Socket set",
            "Wrench"
        ],
        "workflow": [
            "",
            "=== NO. 1 EMISSION CONTROL VALVE SET - REMOVAL ===",
            "",
            "1. REMOVE NO. 1 EMISSION CONTROL VALVE SET",
            "",
            "   a. Disconnect the No. 1 emission control valve set connector.",
            "   b. Disconnect the No. 1 air hose from the No. 1 emission control valve set.",
            "   c. Remove the 3 nuts and No. 1 emission control valve set."
        ]
    },
    "spark_plug_installation": {
        "category": "Engine Performance",
        "subcategory": "Ignition",
        "section": "Spark Plug - Installation",
        "torque": {
            "spark_plug": "18 N·m (184 kgf·cm, 13 ft·lbf)",
            "ignition_coil_bolts": "10 N·m (102 kgf·cm, 7 ft·lbf)",
            "air_cleaner_bolt": "5.0 N·m (51 kgf·cm, 44 in·lbf)",
            "air_cleaner_clamp": "5.0 N·m (51 kgf·cm, 44 in·lbf)"
        },
        "tools": [
            "Spark plug socket (14 mm)",
            "Torque wrench",
            "Socket set",
            "Extensions"
        ],
        "references": {
            "no2_emission_control_valve": "No. 2 Emission Control Valve Set Installation",
            "no2_air_tube": "No. 2 Air Tube Installation",
            "no1_emission_control_valve": "No. 1 Emission Control Valve Set Installation",
            "air_tube": "Air Tube Installation",
            "v_bank_cover": "V-Bank Cover Installation"
        },
        "workflow": [
            "",
            "=== SPARK PLUG - INSTALLATION ===",
            "",
            "1. INSTALL SPARK PLUG",
            "",
            "   a. Install the 6 spark plugs.",
            "      Torque: 18 N·m (184 kgf·cm, 13 ft·lbf)",
            "",
            "2. INSTALL IGNITION COIL ASSEMBLY",
            "",
            "   a. Install the 6 ignition coil assemblies with the 6 bolts.",
            "      Torque: 10 N·m (102 kgf·cm, 7 ft·lbf)",
            "   b. Connect the 6 ignition coil connectors.",
            "",
            "3. INSTALL NO. 2 EMISSION CONTROL VALVE SET",
            "   → Refer to No. 2 Emission Control Valve Set Installation",
            "",
            "4. INSTALL NO. 2 AIR TUBE",
            "   → Refer to No. 2 Air Tube Installation",
            "",
            "5. INSTALL NO. 1 EMISSION CONTROL VALVE SET",
            "   → Refer to No. 1 Emission Control Valve Set Installation",
            "",
            "6. INSTALL AIR TUBE",
            "   → Refer to Air Tube Installation",
            "",
            "7. INSTALL AIR CLEANER CAP AND HOSE",
            "",
            "   a. Install the air cleaner cap and hose.",
            "",
            "      *a  Top",
            "      *b  Front",
            "      *c  RH",
            "      *d  Align cutout portion of hose with protrusion of throttle",
            "      *e  Paint Mark",
            "",
            "   b. Install the air cleaner cap and hose with the bolt and fasten the",
            "      4 hook clamps.",
            "      Torque: 5.0 N·m (51 kgf·cm, 44 in·lbf)",
            "",
            "   c. Tighten the clamp.",
            "      Torque: 5.0 N·m (51 kgf·cm, 44 in·lbf)",
            "",
            "   d. Attach the 4 clamps and connect the ventilation hose, vacuum hose",
            "      and mass air flow meter connector.",
            "",
            "   HINT: The direction of the hose clamp is indicated in the illustration.",
            "",
            "8. INSTALL V-BANK COVER",
            "   → Refer to V-Bank Cover Installation"
        ]
    },
    "no2_emission_control_valve_installation": {
        "category": "Engine Performance",
        "subcategory": "Emissions",
        "section": "No. 2 Emission Control Valve Set - Installation",
        "torque": {
            "mounting_nuts": "21 N·m (214 kgf·cm, 15 ft·lbf)"
        },
        "tools": [
            "Socket set",
            "Torque wrench"
        ],
        "workflow": [
            "",
            "=== NO. 2 EMISSION CONTROL VALVE SET - INSTALLATION ===",
            "",
            "1. INSTALL NO. 2 EMISSION CONTROL VALVE SET",
            "",
            "   a. Install the No. 2 emission control valve set with the 3 nuts.",
            "      Torque: 21 N·m (214 kgf·cm, 15 ft·lbf)",
            "",
            "   b. Align the paint mark with the projection and connect the No. 1 air hose.",
            "",
            "      *1  Paint Mark",
            "      *2  Projection",
            "      *a  Upper",
            "      *b  LH Side",
            "",
            "   HINT: Make sure the direction of the hose clamp is as shown in the",
            "   illustration.",
            "",
            "   c. Connect the No. 2 emission control valve set connector."
        ]
    },
    "no2_air_tube_installation": {
        "category": "Engine Performance",
        "subcategory": "Air Intake",
        "section": "No. 2 Air Tube - Installation",
        "torque": {
            "bolts_nuts": "10 N·m (102 kgf·cm, 7 ft·lbf)"
        },
        "tools": [
            "Socket set",
            "Torque wrench"
        ],
        "workflow": [
            "",
            "=== NO. 2 AIR TUBE - INSTALLATION ===",
            "",
            "1. INSTALL NO. 2 AIR TUBE",
            "",
            "   a. Install 2 new gaskets to the No. 2 air tube.",
            "",
            "      *1  New Gasket",
            "      *2  No. 2 Air Tube",
            "",
            "   NOTE: Be careful not to damage the installation surfaces of the gaskets.",
            "",
            "   b. Install the No. 2 air tube with the 2 bolts and 2 nuts.",
            "      Torque: 10 N·m (102 kgf·cm, 7 ft·lbf)"
        ]
    },
    "no1_emission_control_valve_installation": {
        "category": "Engine Performance",
        "subcategory": "Emissions",
        "section": "No. 1 Emission Control Valve Set - Installation",
        "torque": {
            "mounting_nuts": "21 N·m (214 kgf·cm, 15 ft·lbf)"
        },
        "tools": [
            "Socket set",
            "Torque wrench"
        ],
        "workflow": [
            "",
            "=== NO. 1 EMISSION CONTROL VALVE SET - INSTALLATION ===",
            "",
            "1. INSTALL NO. 1 EMISSION CONTROL VALVE SET",
            "",
            "   a. Install the No. 1 emission control valve set with the 3 nuts.",
            "      Torque: 21 N·m (214 kgf·cm, 15 ft·lbf)",
            "",
            "   b. Align the paint mark with the projection and connect the No. 1 air hose.",
            "",
            "      *1  Projection",
            "      *2  Paint Mark",
            "      *a  RH Side",
            "      *b  Upper",
            "",
            "   HINT: Make sure the direction of the hose clamp is as shown in the",
            "   illustration.",
            "",
            "   c. Connect the No. 1 emission control valve set connector."
        ]
    },
    "v_bank_cover_installation": {
        "category": "Engine Performance",
        "subcategory": "Engine Covers",
        "section": "V-Bank Cover - Installation",
        "tools": ["None"],
        "workflow": [
            "",
            "=== V-BANK COVER - INSTALLATION ===",
            "",
            "1. INSTALL V-BANK COVER",
            "",
            "   a. Attach the 2 V-bank cover hooks to the bracket.",
            "   b. Align the 2 V-bank cover grommets with the 2 pins and press down",
            "      on the V-bank cover to attach the pins.",
            "",
            "   *1  Pin",
            "   *2  Hook"
        ]
    },
    "air_tube_installation": {
        "category": "Engine Performance",
        "subcategory": "Air Intake",
        "section": "Air Tube - Installation",
        "torque": {
            "bolts_nuts": "10 N·m (102 kgf·cm, 7 ft·lbf)"
        },
        "tools": [
            "Socket set",
            "Torque wrench"
        ],
        "workflow": [
            "",
            "=== AIR TUBE - INSTALLATION ===",
            "",
            "1. INSTALL AIR TUBE",
            "",
            "   a. Install 2 new gaskets to the air tube.",
            "",
            "      *1  New Gasket",
            "      *2  Air Tube",
            "",
            "   NOTE: Be careful not to damage the installation surfaces of the gaskets.",
            "",
            "   b. Install the air tube with the 2 bolts and 2 nuts.",
            "      Torque: 10 N·m (102 kgf·cm, 7 ft·lbf)"
        ]
    },
    "no2_air_tube_removal": {
        "category": "Engine Performance",
        "subcategory": "Air Intake",
        "section": "No. 2 Air Tube - Removal",
        "tools": [
            "Socket set",
            "Wrench"
        ],
        "workflow": [
            "",
            "=== NO. 2 AIR TUBE - REMOVAL ===",
            "",
            "1. REMOVE NO. 2 AIR TUBE",
            "",
            "   a. Remove the 2 bolts, 2 nuts and No. 2 air tube.",
            "   b. Remove the 2 gaskets from the No. 2 air tube.",
            "",
            "   NOTE: Be careful not to damage the installation surfaces of the gaskets."
        ]
    },
    "no2_emission_control_valve_removal": {
        "category": "Engine Performance",
        "subcategory": "Emissions",
        "section": "No. 2 Emission Control Valve Set - Removal",
        "tools": [
            "Socket set",
            "Wrench"
        ],
        "workflow": [
            "",
            "=== NO. 2 EMISSION CONTROL VALVE SET - REMOVAL ===",
            "",
            "1. REMOVE NO. 2 EMISSION CONTROL VALVE SET",
            "",
            "   a. Disconnect the No. 2 emission control valve set connector.",
            "   b. Disconnect the No. 3 air hose.",
            "   c. Remove the 3 nuts and No. 2 emission control valve set."
        ]
    }

}
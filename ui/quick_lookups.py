import streamlit as st

def render(data):
    st.subheader("⚡ Quick Lookups")

    tab1, tab2, tab3 = st.tabs(["🛢 Fluids", "📐 Specs", "🔧 Procedures"])

    with tab1:
        st.markdown("## 🛢 Fluid Capacities & Specifications")

        fluids = [
            {
                "name": "Engine Oil",
                "applications": [
                    {
                        "label": "With Filter",
                        "capacity": "6.6 qts / 6.24 L",
                        "spec": "SAE 0W-20 (ILSAC GF-5 multigrade)",
                        "note": "0W-20 is best for fuel economy and cold starts. If unavailable, 5W-20 may be used but must be replaced with 0W-20 at next change."
                    },
                    {
                        "label": "Without Filter",
                        "capacity": "6.0 qts / 5.67 L",
                        "spec": "SAE 0W-20 (ILSAC GF-5 multigrade)"
                    }
                ]
            },
            {
                "name": "Automatic Transmission Fluid",
                "applications": [
                    {
                        "label": "Reference Capacity",
                        "capacity": "11.3 qts / 10.69 L",
                        "spec": "Toyota Genuine ATF WS",
                        "note": "⚠️ Using fluid other than ATF WS may cause shift deterioration, lock-up vibration, and transmission damage."
                    }
                ]
            },
            {
                "name": "Engine Coolant",
                "applications": [
                    {
                        "label": "System Capacity",
                        "capacity": "11.1 qts / 10.5 L",
                        "spec": "Toyota Super Long Life Coolant (pink)",
                        "note": "DO NOT use plain water alone. Use ethylene glycol-based non-silicate, non-amine, non-nitrate, non-borate coolant with long-life hybrid organic acid technology."
                    }
                ]
            },
            {
                "name": "Differential Gear Oil",
                "applications": [
                    {
                        "label": "Rear - Without Diff Lock",
                        "capacity": "2.9 qts / 2.74 L",
                        "spec": "Toyota Genuine Differential Gear Oil LT SAE 75W-85 GL-5"
                    },
                    {
                        "label": "Rear - With Diff Lock",
                        "capacity": "2.8 qts / 2.64 L",
                        "spec": "Toyota Genuine Differential Gear Oil LT SAE 75W-85 GL-5"
                    }
                ]
            },
            {
                "name": "Brake Fluid",
                "applications": [
                    {
                        "label": "System",
                        "capacity": "N/A",
                        "spec": "SAE J1703 or FMVSS No. 116 DOT 3"
                    }
                ]
            },
            {
                "name": "Power Steering Fluid",
                "applications": [
                    {
                        "label": "System",
                        "capacity": "N/A",
                        "spec": "ATF DEXRON II or DEXRON III"
                    }
                ]
            },
            {
                "name": "A/C Compressor Oil",
                "applications": [
                    {
                        "label": "Approximate Capacity",
                        "capacity": "4.6 oz / 0.13 L",
                        "spec": "PAG 46"
                    }
                ]
            },
            {
                "name": "A/C Refrigerant",
                "applications": [
                    {
                        "label": "Approximate Capacity",
                        "capacity": "1.21 lbs / 0.54 kg",
                        "spec": "HFC-134a (R-134a)"
                    }
                ]
            },
            {
                "name": "Fuel Tank",
                "applications": [
                    {
                        "label": "Capacity",
                        "capacity": "23.0 gal / 87.06 L"
                    }
                ]
            },
            {
                "name": "Windshield Washer Fluid",
                "applications": [
                    {
                        "label": "Capacity",
                        "capacity": "N/A",
                        "spec": "Washer Fluid"
                    }
                ]
            }
        ]

        for fluid in fluids:
            with st.expander(f"**{fluid['name']}**"):
                for app in fluid["applications"]:
                    st.markdown(f"**{app['label']}**")
                    st.write(f"Capacity: {app.get('capacity', 'N/A')}")
                    st.write(f"Spec: {app.get('spec', '—')}")
                    if "note" in app:
                        st.info(app["note"])
                    st.markdown("---")

    with tab2:
        st.markdown("## 📐 Common Specs")
        st.info("Common specifications coming soon.")

    with tab3:
        st.markdown("## 🔧 Quick Procedures")
        st.info("Quick procedures coming soon.")
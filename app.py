import streamlit as st
import requests
import streamlit.components.v1 as components

# Page configuration & styling
st.set_page_config(page_title="📱 Hack Buddy", page_icon="🔒", layout="wide")

# Custom CSS for background color and general styling
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    button {
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for navigation
st.sidebar.title("🛠️ Tools")
tool_choice = st.sidebar.radio("Choose a tool:", [
    "Network Scanner",
    "Generate detailed Report and Analysis"
])

# Define webhook URLs
# generate_scan_url = "https://nervous-chicken-40.hooks.n8n.cloud/webhook-test/074ab947-e085-4c30-8d20-1dc1811b7e2b"
generate_scan_url="https://nervous-chicken-40.hooks.n8n.cloud/webhook/074ab947-e085-4c30-8d20-1dc1811b7e2b"
# ai_report_url = "https://nervous-chicken-40.hooks.n8n.cloud/webhook-test/1704b691-f9a7-47fe-8387-64833f31daf3"
ai_report_url="https://nervous-chicken-40.hooks.n8n.cloud/webhook/1704b691-f9a7-47fe-8387-64833f31daf3"

# -------------------- Tool: Network Scanner --------------------
if tool_choice == "Network Scanner":
    st.title("🔒 Network Vulnerability & NMAP Service Scanner")
    st.markdown("This dashboard automates Nmap scans and returns reports via n8n webhooks.")

    st.markdown("""
### Network Vulnerability & NMAP Service Scanner

The **Network Vulnerability & NMAP Service Scanner** is a smart, AI-assisted security tool that automates and enhances network scanning using Nmap.

It uses **AI to intelligently trigger and analyze Nmap scans** via secure webhooks, generating a detailed service scan report that identifies:
- Open ports
- Running services
- Possible network vulnerabilities

This allows you to assess your network posture in real time with minimal manual effort.
""")

    if "nmap_report" not in st.session_state:
        st.session_state.nmap_report = None
        st.session_state.nmap_meta = None

    if st.button("⚙️ Auto Generate Nmap Service Scan Report"):
        st.info("Invoking service scan webhook...")
        try:
            resp = requests.post(generate_scan_url, json=None)
            content_type = resp.headers.get('Content-Type', '')

            if 'application/json' in content_type:
                result = resp.json()
                if isinstance(result, list) and result:
                    meta = result[0]
                    file_resp = requests.get(generate_scan_url, stream=True)
                    file_bytes = file_resp.content

                    st.session_state.nmap_report = file_bytes
                    st.session_state.nmap_meta = meta
                    st.success("✅ Service scan report metadata received!")
                else:
                    st.warning("Unexpected JSON format received.")
            else:
                file_bytes = resp.content
                st.session_state.nmap_report = file_bytes
                st.session_state.nmap_meta = {
                    "fileName": "service_scan_report.html" if 'text/html' in content_type else "service_scan_report",
                    "mimeType": content_type
                }
                st.success("✅ Raw service scan report received!")
        except Exception as ex:
            st.error(f"Exception during webhook call: {str(ex)}")

    # Show saved Nmap scan result
    if st.session_state.nmap_report:
        meta = st.session_state.nmap_meta or {}
        mime_type = meta.get("mimeType", "text/html")
        file_name = meta.get("fileName", "report.html")

        if mime_type.startswith("text/html"):
            html_content = st.session_state.nmap_report.decode("utf-8")
            st.markdown("### 📄 Service Scan HTML Report")
            components.html(html_content, height=600, scrolling=True)

        st.download_button(
            label="📥 Download Nmap Report",
            data=st.session_state.nmap_report,
            file_name=file_name,
            mime=mime_type
        )

# -------------------- Tool: AI-Generated Report --------------------
elif tool_choice == "Generate detailed Report and Analysis":
    st.title("📁 Download AI Generated Report")
    st.markdown("This section fetches the AI-generated vulnerability and patch management report.")
    st.markdown("""
### AI-Generated Vulnerability & Patch Management Report

This tool uses **AI-driven automation** to fetch a comprehensive vulnerability and patch status report tailored for stakeholders and IT teams.

It outlines:
- Executive summary of your security posture
- Common vulnerability types and remediation status
- Patch compliance trends and risk analysis
- Actionable recommendations for mitigation

The report is generated through intelligent workflows and offers a ready-to-download document, simplifying communication and decision-making around cybersecurity efforts.
""")

    if "ai_report" not in st.session_state:
        st.session_state.ai_report = None

    if st.button("📥 Fetch Detailed AI Report"):
        st.info("Retrieving AI-generated report...")
        try:
            response = requests.post(ai_report_url)
            content_type = response.headers.get("Content-Type", "")

            if "application/json" in content_type:
                data = response.json()
                if isinstance(data, list) and len(data) > 0 and "output" in data[0]:
                    st.session_state.ai_report = data[0]["output"]
                    st.success("✅ Report retrieved successfully!")
                else:
                    st.warning("No 'output' field found in the JSON response.")
            else:
                st.warning("Unexpected response format. Expected JSON with an 'output' field.")
        except Exception as e:
            st.error(f"Error fetching the report: {str(e)}")

    if st.session_state.ai_report:
        st.markdown("### 📄 Vulnerability & Patch Analysis")
        st.markdown(st.session_state.ai_report)

        st.download_button(
            label="📥 Download Report as Markdown",
            data=st.session_state.ai_report,
            file_name="ai_detailed_vulnerability_report.md",
            mime="text/markdown"
        )
st.markdown("""
<hr style="margin-top: 3rem; margin-bottom: 1rem;">
<div style="text-align: center; font-size: 0.9rem; color: gray;">
    Made by <strong>Ankur Kumar Muduli</strong>
</div>
""", unsafe_allow_html=True)


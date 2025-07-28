import streamlit as st
import requests
import time

st.set_page_config(page_title="Policy Explainer Agent", page_icon="📜", layout="centered")

st.title("📜 Policy Explainer Agent")
st.markdown("Explain complex healthcare policies in simple terms, with real-world examples.")

st.divider()

query = st.text_input("🔍 Ask your question", placeholder="e.g. What does this policy say about emergency care?")

if st.button("Explain Policy"):
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Processing your request..."):
            try:
                start_time = time.time()
                response = requests.post("http://localhost:8000/explain_policy", json={"query": query})
                elapsed = time.time() - start_time

                if response.status_code == 200:
                    data = response.json()
                    st.success(f"✅ Explanation ready in {elapsed:.2f}s")

                    st.subheader("📘 Simplified Explanation")
                    st.write(data.get("simplified", "No simplified explanation returned."))

                    st.subheader("📝 Real-Life Examples")
                    st.write(data.get("examples", "No examples returned."))

                    # Optional download
                    output = f"Question: {query}\n\nSimplified:\n{data.get('simplified')}\n\nExamples:\n{data.get('examples')}"
                    st.download_button("💾 Download Explanation", data=output, file_name="policy_explanation.txt")

                else:
                    st.error(f"❌ API returned status code {response.status_code}")
            except Exception as e:
                st.error(f"💥 Error: Could not connect to the backend.\n\n{e}")

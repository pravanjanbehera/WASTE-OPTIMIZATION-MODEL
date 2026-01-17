import streamlit as st
from PIL import Image
import random

# --- STYLE & UI CONFIGURATION ---
st.set_page_config(page_title="Eco-Smart Waste Analyzer", layout="centered")

def apply_custom_branding():
    """Injects custom CSS for unique styling to avoid template-looks."""
    st.markdown("""
        <style>
        .report-card { padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .red-spot { background-color: #ffe3e3; border-left: 5px solid #ff4b4b; color: #b91c1c; }
        .yellow-spot { background-color: #fff9e6; border-left: 5px solid #facc15; color: #854d0e; }
        .green-spot { background-color: #f0fdf4; border-left: 5px solid #22c55e; color: #166534; }
        </style>
    """, unsafe_allow_html=True)

# --- CORE LOGIC MODULE ---
class WasteIntelligence:
    def __init__(self):
        # Human-curated dataset for environmental impact
        self.impact_db = {
            "Plastic Bottle": {"risk": 7, "type": "Recyclable", "desc": "Takes 450 years to decompose."},
            "Hazardous Waste": {"risk": 10, "type": "Bio-Hazard", "desc": "High infection risk; toxic if leaked."},
            "Organic Waste": {"risk": 1, "type": "Organic", "desc": "Perfect for composting; low footprint."},
            "Old Battery": {"risk": 9, "type": "Electronic", "desc": "Contains heavy metals like Lead/Lithium."},
            "Cardboard Box": {"risk": 2, "type": "", "desc": "Highly recyclable and biodegradable."},
            "Aluminium Can": {"risk": 4, "type": "Metal", "desc": "Infinitely recyclable with low energy."}
        }

    def simulate_vision_analysis(self, img):
        """Mocking the ML Model prediction for the demo interface."""
        # In a production app, you'd use: model.predict(img)
        prediction = random.choice(list(self.impact_db.keys()))
        return prediction

    def get_hotspot_marking(self, score):
        """Determines the visual safety level based on toxicity."""
        if score >= 8: return "🔴 RED HOTSPOT", "red-spot"
        if 4 <= score <= 7: return "🟡 YELLOW HOTSPOT", "yellow-spot"
        return "🟢 GREEN HOTSPOT", "green-spot"

# --- MAIN APP INTERFACE ---
def run_app():
    apply_custom_branding()
    engine = WasteIntelligence()

    st.title("🎯 Intelligent Waste Segregator")
    st.write("Upload a photo of waste to analyze its environmental harm and hotspot level.")

    # 1. User Upload Section
    uploaded_file = st.file_uploader("Choose a waste image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Snapshot", use_container_width=True)
        
        with st.spinner("Analyzing toxicity levels..."):
            # 2. Logic Execution
            label = engine.simulate_vision_analysis(img)
            data = engine.impact_db[label]
            status_text, css_class = engine.get_hotspot_marking(data['risk'])

            # 3. Visual Output
            st.subheader(f"Analysis Result: {label}")
            
            st.markdown(f"""
                <div class="report-card {css_class}">
                    <h3>{status_text}</h3>
                    <p><b>Environmental Risk Score:</b> {data['risk']}/10</p>
                    <p><b>Category:</b> {data['type']}</p>
                    <p><b>Impact:</b> {data['desc']}</p>
                </div>
            """, unsafe_allow_html=True)

            # Circular Economy Recommendation
            st.info(f"💡 **Recommendation:** This item should be handled as **{data['type']}**. "
                    f"Check local {data['type'].lower()} guidelines to reduce landfill impact.")

if __name__ == "__main__":
    run_app()
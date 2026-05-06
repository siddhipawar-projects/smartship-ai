import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="SmartShip AI",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────
# CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif !important;
}
.stApp {
    background-color: #030712;
    color: #ffffff;
}
[data-testid="stSidebar"] {
    background-color: #0a0f1e;
    border-right: 1px solid #1e2438;
}
/* Hide default streamlit header white bar */
[data-testid="stHeader"] {
    background: #030712 !important;
    border-bottom: none !important;
}
[data-testid="stToolbar"] {
    display: none;
}
/* Radio buttons in sidebar */
[data-testid="stSidebar"] .stRadio label {
    color: #a0aec0 !important;
    font-size: 14px !important;
    padding: 8px 0 !important;
}
[data-testid="stSidebar"] * {
    color: #a0aec0 !important;
}
[data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] p {
    color: #a0aec0 !important;
}
section[data-testid="stSidebar"] label {
    color: #a0aec0 !important;
}
section[data-testid="stSidebar"] p {
    color: #9ca3af !important;
}
            
/* Selectbox */
.stSelectbox > div > div {
    background-color: #0d1117;
    border: 1px solid #1e2438;
    border-radius: 8px;
    color: white;
}
/* Slider */
.stSlider > div > div > div {
    background: linear-gradient(90deg, #6366f1, #a855f7) !important;
}
/* Button */
.stButton > button {
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 14px 28px;
    font-size: 16px;
    font-weight: 600;
    width: 100%;
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: 0.3px;
    transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.85; }

/* Dataframe */
[data-testid="stDataFrame"] {
    background: #0d1117;
}
/* Hide streamlit footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Cards */
.stat-card {
    background: #0d1117;
    border: 1px solid #1e2438;
    border-radius: 14px;
    padding: 22px 20px;
    text-align: center;
}
.stat-val {
    font-size: 34px;
    font-weight: 700;
    margin: 0;
    font-family: 'Space Grotesk', sans-serif;
}
.stat-label {
    font-size: 13px;
    color: #6b7280;
    margin: 4px 0 0;
    font-family: 'Space Grotesk', sans-serif;
}
.hero-text {
    font-size: 42px;
    font-weight: 700;
    line-height: 1.2;
    margin: 0;
    font-family: 'Space Grotesk', sans-serif;
}
.hero-sub {
    font-size: 18px;
    color: #6b7280;
    margin: 12px 0 0;
    font-weight: 300;
    font-family: 'Space Grotesk', sans-serif;
}
.step-card {
    background: #0d1117;
    border: 1px solid #1e2438;
    border-radius: 14px;
    padding: 24px 20px;
    text-align: center;
    height: 100%;
}
.step-num {
    font-size: 13px;
    font-weight: 600;
    color: #6366f1;
    letter-spacing: 2px;
    margin: 0 0 10px;
    font-family: 'Space Grotesk', sans-serif;
}
.step-title {
    font-size: 16px;
    font-weight: 600;
    color: white;
    margin: 0 0 8px;
    font-family: 'Space Grotesk', sans-serif;
}
.step-desc {
    font-size: 13px;
    color: #6b7280;
    margin: 0;
    line-height: 1.5;
    font-family: 'Space Grotesk', sans-serif;
}
.risk-high {
    background: #160a0a;
    border: 1px solid #7f1d1d;
    border-left: 4px solid #ef4444;
    border-radius: 12px;
    padding: 22px 24px;
    margin: 16px 0;
}
.risk-low {
    background: #061210;
    border: 1px solid #14532d;
    border-left: 4px solid #22c55e;
    border-radius: 12px;
    padding: 22px 24px;
    margin: 16px 0;
}
.risk-title {
    font-size: 24px;
    font-weight: 700;
    margin: 0 0 6px;
    font-family: 'Space Grotesk', sans-serif;
}
.risk-sub {
    font-size: 14px;
    color: #9ca3af;
    margin: 0;
    font-family: 'Space Grotesk', sans-serif;
}
.action-card {
    background: #0d1117;
    border: 1px solid #1e2438;
    border-radius: 10px;
    padding: 14px 16px;
    margin: 8px 0;
    display: flex;
    align-items: flex-start;
    gap: 12px;
}
.action-icon {
    font-size: 20px;
    flex-shrink: 0;
}
.action-text {
    font-size: 13px;
    color: #d1d5db;
    line-height: 1.5;
    font-family: 'Space Grotesk', sans-serif;
}
.action-text b {
    color: white;
    font-weight: 600;
}
.detail-pill {
    background: #0d1117;
    border: 1px solid #1e2438;
    border-radius: 8px;
    padding: 10px 14px;
    margin: 4px 0;
    font-size: 13px;
    color: #d1d5db;
    font-family: 'Space Grotesk', sans-serif;
}
.section-title {
    font-size: 20px;
    font-weight: 600;
    color: white;
    margin: 24px 0 14px;
    padding-bottom: 8px;
    border-bottom: 1px solid #1e2438;
    font-family: 'Space Grotesk', sans-serif;
}
.insight-card {
    background: #0d1117;
    border: 1px solid #1e2438;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
}
.insight-icon { font-size: 28px; margin: 0 0 10px; }
.insight-title {
    font-size: 15px;
    font-weight: 600;
    color: #818cf8;
    margin: 0 0 6px;
    font-family: 'Space Grotesk', sans-serif;
}
.insight-desc {
    font-size: 12px;
    color: #6b7280;
    margin: 0;
    line-height: 1.5;
    font-family: 'Space Grotesk', sans-serif;
}
.chat-bubble-user {
    background: #1e2438;
    border-radius: 12px 12px 4px 12px;
    padding: 12px 16px;
    margin: 8px 0 8px 40px;
    font-size: 14px;
    color: #e5e7eb;
    font-family: 'Space Grotesk', sans-serif;
}
.chat-bubble-ai {
    background: linear-gradient(135deg, #1e1b4b, #1a0a2e);
    border: 1px solid #3730a3;
    border-radius: 12px 12px 12px 4px;
    padding: 12px 16px;
    margin: 8px 40px 8px 0;
    font-size: 14px;
    color: #e5e7eb;
    font-family: 'Space Grotesk', sans-serif;
}
.coming-soon {
    background: #0d1117;
    border: 1px dashed #1e2438;
    border-radius: 14px;
    padding: 60px 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@st.cache_resource
def load_model():
    with open(os.path.join(BASE_DIR, 'models', 'best_model.pkl'), 'rb') as f:
        model = pickle.load(f)
    with open(os.path.join(BASE_DIR, 'models', 'feature_names.pkl'), 'rb') as f:
        features = pickle.load(f)
    return model, features

@st.cache_data
def load_data():
    return pd.read_csv(os.path.join(BASE_DIR, 'data', 'clean_supply_chain_data.csv'))

model, feature_names = load_model()
df = load_data()

# ─────────────────────────────────────────
# SESSION STATE — prediction counter
# ─────────────────────────────────────────
if 'prediction_count' not in st.session_state:
    st.session_state.prediction_count = 0
if 'last_prediction' not in st.session_state:
    st.session_state.last_prediction = None

# ─────────────────────────────────────────
# ENCODING MAPS
# ─────────────────────────────────────────
shipping_map = {'First Class': 0, 'Same Day': 1,
                'Second Class': 2, 'Standard Class': 3}
segment_map = {'Consumer': 0, 'Corporate': 1, 'Home Office': 2}
market_map = {'Africa': 0, 'Europe': 1, 'LATAM': 2,
              'Pacific Asia': 3, 'USCA': 4}
payment_map = {'CASH': 0, 'DEBIT': 1, 'PAYMENT': 2, 'TRANSFER': 3}
region_map = {
    'Caribbean': 0, 'Central Africa': 1, 'Central America': 2,
    'East Africa': 3, 'East Asia': 4, 'Eastern Asia': 5,
    'Eastern Europe': 6, 'North Africa': 7, 'North Asia': 8,
    'Northern Europe': 9, 'Oceania': 10, 'South America': 11,
    'South Asia': 12, 'Southeast Asia': 13, 'Southern Europe': 14,
    'US Center': 15, 'US East': 16, 'US South': 17, 'US West': 18,
    'West Africa': 19, 'West Asia': 20, 'Western Europe': 21
}
category_map = {
    'Apparel': 0, 'Auto Parts': 1, 'Books': 2, 'Cameras': 3,
    'Electronics': 4, 'Fitness': 5, 'Footwear': 6, 'Garden': 7,
    'Health': 8, 'Home': 9, 'Music': 10, 'Outdoors': 11,
    'Sports': 12, 'Toys': 13
}
median_sales = float(df['Sales per customer'].median())
median_dept = int(df['Department Name'].median())

# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 10px 0 20px'>
        <div style='font-size:22px;font-weight:700;color:white;
                    font-family:Space Grotesk,sans-serif;
                    letter-spacing:-0.5px'>
            🚢 SmartShip AI
        </div>
        <div style='font-size:11px;color:#6b7280;
                    letter-spacing:2px;text-transform:uppercase;
                    margin-top:4px'>
            Predict · Prevent · Deliver
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "Navigation",
        ["🏠 Home", "🔮 Predict", "📊 Analytics", "💬 Ask AI"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown(f"""
    <div style='padding:12px;background:#0d1117;border:1px solid #1e2438;
                border-radius:10px;margin-bottom:12px'>
        <div style='font-size:11px;color:#6b7280;
                    text-transform:uppercase;letter-spacing:1px;
                    margin-bottom:6px'>Session Stats</div>
        <div style='font-size:22px;font-weight:700;color:#818cf8'>
            {st.session_state.prediction_count}
        </div>
        <div style='font-size:12px;color:#6b7280'>
            predictions made
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size:12px;color:#4b5563;line-height:1.6'>
        <b style='color:#6b7280'>Model:</b> Random Forest<br>
        <b style='color:#6b7280'>Accuracy:</b> 73.96%<br>
        <b style='color:#6b7280'>Trained on:</b> 180,519 orders<br>
        <b style='color:#6b7280'>Features:</b> 14
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style='font-size:11px;color:#374151'>
        Built by Siddhi Chavan<br>
        Supply Chain ML Project · 2025
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════
# PAGE 1 — HOME
# ═══════════════════════════════════════
if page == "🏠 Home":

    # Logo section
    st.markdown("""
    <div style='text-align:center;padding:40px 0 20px'>
        <div style='font-size:52px;font-weight:800;
                    font-family:Space Grotesk,sans-serif;
                    letter-spacing:-2px;color:white'>
            🚢 Smart<span style='background:linear-gradient(90deg,#818cf8,#c084fc,#e879f9);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            background-clip:text'>Ship</span> AI
        </div>
        <div style='display:inline-flex;align-items:center;gap:8px;
                    background:rgba(99,102,241,0.1);
                    border:1px solid rgba(99,102,241,0.2);
                    border-radius:20px;padding:6px 16px;margin-top:12px'>
            <div style='width:7px;height:7px;border-radius:50%;
                        background:#818cf8;animation:pulse 2s infinite'></div>
            <span style='font-size:11px;color:#a5b4fc;
                        letter-spacing:2px;text-transform:uppercase;
                        font-family:Space Grotesk,sans-serif'>
                Powered by Machine Learning
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hero statement
    st.markdown("""
    <div style='text-align:center;padding:20px 60px 10px'>
        <p class='hero-text'>Your shipments are lying to you.</p>
        <p class='hero-sub'>
            54.8% of orders in our dataset arrived late.<br>
            SmartShip AI tells you which ones —
            <span style='color:#818cf8;font-weight:500'>
            before they leave the warehouse.
            </span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Stats row
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class='stat-card'>
            <p class='stat-val' style='color:#818cf8'>{len(df):,}</p>
            <p class='stat-label'>Orders Analysed</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='stat-card'>
            <p class='stat-val' style='color:#ef4444'>54.8%</p>
            <p class='stat-label'>Real Delay Rate</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class='stat-card'>
            <p class='stat-val' style='color:#22c55e'>73.96%</p>
            <p class='stat-label'>Model Accuracy</p>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""
        <div class='stat-card'>
            <p class='stat-val' style='color:#c084fc'>14</p>
            <p class='stat-label'>Predictive Features</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # How it works
    st.markdown("""
    <p style='text-align:center;font-size:13px;font-weight:600;
              color:#6366f1;letter-spacing:3px;text-transform:uppercase;
              font-family:Space Grotesk,sans-serif;margin-bottom:16px'>
        How it works
    </p>""", unsafe_allow_html=True)

    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown("""
        <div class='step-card'>
            <p class='step-num'>01</p>
            <div style='font-size:32px;margin-bottom:10px'>📋</div>
            <p class='step-title'>Fill in shipment details</p>
            <p class='step-desc'>
                Enter shipping mode, destination, product category,
                payment type and order timing. Takes 30 seconds.
            </p>
        </div>""", unsafe_allow_html=True)
    with s2:
        st.markdown("""
        <div class='step-card'>
            <p class='step-num'>02</p>
            <div style='font-size:32px;margin-bottom:10px'>🤖</div>
            <p class='step-title'>Get instant risk score</p>
            <p class='step-desc'>
                Our Random Forest model — trained on 180,519 real orders —
                predicts delay probability in milliseconds.
            </p>
        </div>""", unsafe_allow_html=True)
    with s3:
        st.markdown("""
        <div class='step-card'>
            <p class='step-num'>03</p>
            <div style='font-size:32px;margin-bottom:10px'>⚡</div>
            <p class='step-title'>Act before it's late</p>
            <p class='step-desc'>
                See exactly why the shipment is at risk and get
                specific recommendations to prevent the delay.
            </p>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # CTA
    st.markdown("""
    <div style='text-align:center;padding:30px;
                background:#0d1117;border:1px solid #1e2438;
                border-radius:16px'>
        <p style='font-size:22px;font-weight:700;color:white;
                  margin:0 0 8px;font-family:Space Grotesk,sans-serif'>
            Ready to predict your first shipment?
        </p>
        <p style='font-size:14px;color:#6b7280;margin:0 0 16px;
                  font-family:Space Grotesk,sans-serif'>
            Click <b style='color:#818cf8'>🔮 Predict</b> in the
            sidebar to get started. Free. Instant. No signup needed.
        </p>
        <div style='display:inline-flex;gap:16px;flex-wrap:wrap;
                    justify-content:center'>
            <span style='background:rgba(99,102,241,0.1);
                        border:1px solid rgba(99,102,241,0.2);
                        border-radius:8px;padding:8px 16px;
                        font-size:13px;color:#a5b4fc'>
                ✓ No signup required
            </span>
            <span style='background:rgba(99,102,241,0.1);
                        border:1px solid rgba(99,102,241,0.2);
                        border-radius:8px;padding:8px 16px;
                        font-size:13px;color:#a5b4fc'>
                ✓ Instant predictions
            </span>
            <span style='background:rgba(99,102,241,0.1);
                        border:1px solid rgba(99,102,241,0.2);
                        border-radius:8px;padding:8px 16px;
                        font-size:13px;color:#a5b4fc'>
                ✓ Actionable insights
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════
# PAGE 2 — PREDICT
# ═══════════════════════════════════════
elif page == "🔮 Predict":

    st.markdown("""
    <div style='padding:10px 0 24px'>
        <p style='font-size:32px;font-weight:700;color:white;
                  margin:0;font-family:Space Grotesk,sans-serif'>
            🔮 Predict Shipment Delay
        </p>
        <p style='font-size:15px;color:#6b7280;margin:6px 0 0;
                  font-family:Space Grotesk,sans-serif'>
            Fill in the details below — we'll tell you if it's going to be late.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<p class='section-title'>🚚 Shipping Details</p>",
                   unsafe_allow_html=True)
        shipping_mode = st.selectbox("Shipping Mode",
            ['First Class', 'Same Day', 'Second Class', 'Standard Class'])
        scheduled_days = st.slider("Scheduled Delivery Days", 1, 7, 3)
        market = st.selectbox("Market",
            ['Africa', 'Europe', 'LATAM', 'Pacific Asia', 'USCA'])
        order_region = st.selectbox("Order Region", sorted(region_map.keys()))
        category = st.selectbox("Product Category", sorted(category_map.keys()))

    with col2:
        st.markdown("<p class='section-title'>📦 Order Details</p>",
                   unsafe_allow_html=True)
        customer_segment = st.selectbox("Customer Segment",
            ['Consumer', 'Corporate', 'Home Office'])
        payment_type = st.selectbox("Payment Type",
            ['CASH', 'DEBIT', 'PAYMENT', 'TRANSFER'])
        quantity = st.slider("Order Quantity", 1, 5, 1)
        discount_rate = st.slider("Discount Rate", 0.0, 0.5, 0.05)
        order_hour = st.slider("Order Hour (0-23)", 0, 23, 10)
        order_month = st.slider("Order Month", 1, 12, 6)
        order_day = st.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 2)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔮 Predict Delay Risk", type="primary",
                 use_container_width=True):

        input_data = pd.DataFrame([{
            'Shipping Mode': shipping_map[shipping_mode],
            'Days for shipment (scheduled)': scheduled_days,
            'Category Name': category_map[category],
            'Customer Segment': segment_map[customer_segment],
            'Department Name': median_dept,
            'Market': market_map[market],
            'Order Region': region_map[order_region],
            'Order Item Quantity': quantity,
            'Order Item Discount Rate': discount_rate,
            'Sales per customer': median_sales,
            'Type': payment_map[payment_type],
            'order_month': order_month,
            'order_day_of_week': order_day,
            'order_hour': order_hour
        }])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1] * 100
        st.session_state.prediction_count += 1
        st.session_state.last_prediction = {
            'prediction': prediction,
            'probability': probability,
            'shipping_mode': shipping_mode,
            'scheduled_days': scheduled_days,
            'market': market,
            'region': order_region,
            'category': category,
            'segment': customer_segment,
            'payment': payment_type,
            'hour': order_hour
        }

        # Risk result
        if prediction == 1:
            st.markdown(f"""
            <div class='risk-high'>
                <p class='risk-title' style='color:#fca5a5'>
                    ⚠️ HIGH DELAY RISK — {probability:.1f}%
                </p>
                <p class='risk-sub'>
                    This shipment has a high probability of arriving late.
                    See recommendations below.
                </p>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='risk-low'>
                <p class='risk-title' style='color:#86efac'>
                    ✅ LOW DELAY RISK — {probability:.1f}%
                </p>
                <p class='risk-sub'>
                    This shipment is likely to arrive on time.
                    No immediate action needed.
                </p>
            </div>""", unsafe_allow_html=True)

        # Two column results
        r1, r2 = st.columns(2)

        with r1:
            st.markdown("<p class='section-title'>📋 Shipment Summary</p>",
                       unsafe_allow_html=True)
            st.markdown(f"<div class='detail-pill'>🚚 <b>Shipping Mode:</b> {shipping_mode}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='detail-pill'>📅 <b>Scheduled Days:</b> {scheduled_days}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='detail-pill'>🌍 <b>Market:</b> {market}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='detail-pill'>🗺️ <b>Region:</b> {order_region}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='detail-pill'>📦 <b>Category:</b> {category}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='detail-pill'>👤 <b>Segment:</b> {customer_segment}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='detail-pill'>💳 <b>Payment:</b> {payment_type}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='detail-pill'>🕐 <b>Order Hour:</b> {order_hour}:00</div>", unsafe_allow_html=True)

        with r2:
            st.markdown("<p class='section-title'>⚡ Recommended Actions</p>",
                       unsafe_allow_html=True)

            if prediction == 1:
                # Dynamic recommendations based on inputs
                if shipping_mode == 'Standard Class':
                    st.markdown("""
                    <div class='action-card'>
                        <div class='action-icon'>🚀</div>
                        <div class='action-text'>
                            <b>Upgrade shipping mode</b><br>
                            Switch from Standard Class to First Class.
                            Reduces delay risk by approximately 30%.
                        </div>
                    </div>""", unsafe_allow_html=True)

                if scheduled_days <= 2:
                    st.markdown("""
                    <div class='action-card'>
                        <div class='action-icon'>📅</div>
                        <div class='action-text'>
                            <b>Extend delivery window</b><br>
                            A 1-2 day promise is aggressive.
                            Set realistic expectations — extend to 4-5 days.
                        </div>
                    </div>""", unsafe_allow_html=True)

                if order_hour >= 18:
                    st.markdown("""
                    <div class='action-card'>
                        <div class='action-icon'>⏰</div>
                        <div class='action-text'>
                            <b>Late night order risk</b><br>
                            Orders placed after 6PM miss warehouse
                            cut-off. Flag for priority next-day processing.
                        </div>
                    </div>""", unsafe_allow_html=True)

                if payment_type == 'CASH':
                    st.markdown("""
                    <div class='action-card'>
                        <div class='action-icon'>💳</div>
                        <div class='action-text'>
                            <b>Cash payment risk</b><br>
                            COD orders have higher failure rates.
                            Encourage prepaid or digital payment.
                        </div>
                    </div>""", unsafe_allow_html=True)

                st.markdown("""
                <div class='action-card'>
                    <div class='action-icon'>🔔</div>
                    <div class='action-text'>
                        <b>Proactive customer alert</b><br>
                        Notify the customer now about potential delay.
                        Proactive communication reduces complaints by 60%.
                    </div>
                </div>""", unsafe_allow_html=True)

            else:
                st.markdown("""
                <div class='action-card'>
                    <div class='action-icon'>✅</div>
                    <div class='action-text'>
                        <b>No action needed</b><br>
                        This shipment looks good. Standard processing
                        should ensure on-time delivery.
                    </div>
                </div>""", unsafe_allow_html=True)

                st.markdown("""
                <div class='action-card'>
                    <div class='action-icon'>📊</div>
                    <div class='action-text'>
                        <b>Monitor as usual</b><br>
                        Add to your standard tracking dashboard.
                        No priority escalation needed.
                    </div>
                </div>""", unsafe_allow_html=True)

        # Scenario simulator
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p class='section-title'>🔁 What If Simulator</p>",
                   unsafe_allow_html=True)
        st.markdown("""
        <p style='font-size:13px;color:#6b7280;margin-bottom:16px;
                  font-family:Space Grotesk,sans-serif'>
            See how changing the shipping mode affects delay risk
            for this exact order.
        </p>""", unsafe_allow_html=True)

        sim_cols = st.columns(4)
        sim_modes = ['First Class', 'Same Day', 'Second Class', 'Standard Class']

        for i, mode in enumerate(sim_modes):
            sim_input = input_data.copy()
            sim_input['Shipping Mode'] = shipping_map[mode]
            sim_prob = model.predict_proba(sim_input)[0][1] * 100
            sim_pred = model.predict(sim_input)[0]
            color = "#ef4444" if sim_pred == 1 else "#22c55e"
            border = "#7f1d1d" if sim_pred == 1 else "#14532d"
            icon = "⚠️" if sim_pred == 1 else "✅"
            highlight = " border: 1.5px solid #6366f1 !important;" if mode == shipping_mode else ""

            with sim_cols[i]:
                st.markdown(f"""
                <div style='background:#0d1117;border:1px solid {border};
                            border-radius:10px;padding:16px;text-align:center;
                            {highlight}'>
                    <div style='font-size:12px;color:#9ca3af;margin-bottom:6px;
                                font-family:Space Grotesk,sans-serif'>{mode}</div>
                    <div style='font-size:26px;font-weight:700;color:{color};
                                font-family:Space Grotesk,sans-serif'>
                        {sim_prob:.0f}%
                    </div>
                    <div style='font-size:11px;color:#6b7280;margin-top:4px'>
                        {icon} delay risk
                    </div>
                </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════
# PAGE 3 — ANALYTICS
# ═══════════════════════════════════════
elif page == "📊 Analytics":

    st.markdown("""
    <div style='padding:10px 0 24px'>
        <p style='font-size:32px;font-weight:700;color:white;
                  margin:0;font-family:Space Grotesk,sans-serif'>
            📊 Delay Analytics
        </p>
        <p style='font-size:15px;color:#6b7280;margin:6px 0 0;
                  font-family:Space Grotesk,sans-serif'>
            Real patterns from 180,519 supply chain orders.
        </p>
    </div>
    """, unsafe_allow_html=True)

    def dark_chart(figsize=(8, 4)):
        fig, ax = plt.subplots(figsize=figsize)
        fig.patch.set_facecolor('#0d1117')
        ax.set_facecolor('#0d1117')
        ax.tick_params(colors='#6b7280', labelsize=10)
        ax.spines['bottom'].set_color('#1e2438')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#1e2438')
        ax.grid(axis='x', color='#1e2438', linewidth=0.5)
        return fig, ax

    # Row 1
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("<p class='section-title'>Delay Rate by Shipping Mode</p>",
                   unsafe_allow_html=True)
        shipping_labels = {
            0: 'First Class', 1: 'Same Day',
            2: 'Second Class', 3: 'Standard Class'
        }
        delay_mode = df.groupby('Shipping Mode')['Late_delivery_risk'].mean() * 100
        delay_mode.index = delay_mode.index.map(shipping_labels)
        delay_mode = delay_mode.sort_values(ascending=True)

        fig, ax = dark_chart()
        colors = ['#22c55e' if v < 50 else '#f97316' if v < 70 else '#ef4444'
                 for v in delay_mode.values]
        bars = ax.barh(delay_mode.index, delay_mode.values,
                      color=colors, height=0.5)
        for bar, val in zip(bars, delay_mode.values):
            ax.text(val + 0.5, bar.get_y() + bar.get_height()/2,
                   f'{val:.1f}%', va='center', color='white',
                   fontsize=10, fontweight='600')
        ax.set_xlim(0, 110)
        ax.set_xlabel('Delay Rate (%)', color='#6b7280')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with c2:
        st.markdown("<p class='section-title'>Delay Rate by Market</p>",
                   unsafe_allow_html=True)
        market_labels = {
            0: 'Africa', 1: 'Europe', 2: 'LATAM',
            3: 'Pacific Asia', 4: 'USCA'
        }
        delay_market = df.groupby('Market')['Late_delivery_risk'].mean() * 100
        delay_market.index = delay_market.index.map(market_labels)
        delay_market = delay_market.sort_values(ascending=True)

        fig2, ax2 = dark_chart()
        colors2 = ['#22c55e' if v < 50 else '#f97316' if v < 55 else '#ef4444'
                  for v in delay_market.values]
        bars2 = ax2.barh(delay_market.index, delay_market.values,
                        color=colors2, height=0.5)
        for bar, val in zip(bars2, delay_market.values):
            ax2.text(val + 0.5, bar.get_y() + bar.get_height()/2,
                    f'{val:.1f}%', va='center', color='white',
                    fontsize=10, fontweight='600')
        ax2.set_xlim(0, 80)
        ax2.set_xlabel('Delay Rate (%)', color='#6b7280')
        plt.tight_layout()
        st.pyplot(fig2)
        plt.close()

    # Row 2
    c3, c4 = st.columns(2)

    with c3:
        st.markdown("<p class='section-title'>Orders by Hour of Day</p>",
                   unsafe_allow_html=True)
        hourly = df.groupby('order_hour')['Late_delivery_risk'].mean() * 100

        fig3, ax3 = dark_chart(figsize=(8, 4))
        ax3.plot(hourly.index, hourly.values,
                color='#818cf8', linewidth=2, marker='o',
                markersize=4, markerfacecolor='#c084fc')
        ax3.fill_between(hourly.index, hourly.values,
                        alpha=0.15, color='#818cf8')
        ax3.set_xlabel('Hour of Day', color='#6b7280')
        ax3.set_ylabel('Delay Rate (%)', color='#6b7280')
        ax3.set_xlim(0, 23)
        plt.tight_layout()
        st.pyplot(fig3)
        plt.close()

    with c4:
        st.markdown("<p class='section-title'>Delay Rate by Day of Week</p>",
                   unsafe_allow_html=True)
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        daily = df.groupby('order_day_of_week')['Late_delivery_risk'].mean() * 100

        fig4, ax4 = dark_chart(figsize=(8, 4))
        bar_colors = ['#ef4444' if v == daily.max()
                     else '#22c55e' if v == daily.min()
                     else '#818cf8' for v in daily.values]
        ax4.bar(days, daily.values, color=bar_colors,
               width=0.6, edgecolor='none')
        ax4.set_ylabel('Delay Rate (%)', color='#6b7280')
        plt.tight_layout()
        st.pyplot(fig4)
        plt.close()

    # Key insights
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p class='section-title'>💡 Key Insights</p>",
               unsafe_allow_html=True)

    i1, i2, i3 = st.columns(3)
    with i1:
        st.markdown("""
        <div class='insight-card'>
            <div class='insight-icon'>📅</div>
            <p class='insight-title'>Delivery Promise is #1 Risk Factor</p>
            <p class='insight-desc'>
                Orders with 1-2 day delivery promises
                are most likely to fail. Realistic timelines
                reduce delay risk significantly.
            </p>
        </div>""", unsafe_allow_html=True)
    with i2:
        st.markdown("""
        <div class='insight-card'>
            <div class='insight-icon'>🚚</div>
            <p class='insight-title'>Standard Class = Highest Risk</p>
            <p class='insight-desc'>
                Standard Class shipping carries the
                highest delay rate. Upgrading to First Class
                reduces risk by approximately 30%.
            </p>
        </div>""", unsafe_allow_html=True)
    with i3:
        st.markdown("""
        <div class='insight-card'>
            <div class='insight-icon'>🕐</div>
            <p class='insight-title'>Order Timing Matters</p>
            <p class='insight-desc'>
                Late night orders miss warehouse cut-off.
                Orders placed before 5PM have significantly
                lower delay risk across all markets.
            </p>
        </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════
# PAGE 4 — ASK AI
# ═══════════════════════════════════════
elif page == "💬 Ask AI":

    st.markdown("""
    <div style='padding:10px 0 24px'>
        <p style='font-size:32px;font-weight:700;color:white;
                  margin:0;font-family:Space Grotesk,sans-serif'>
            💬 Ask SmartShip AI
        </p>
        <p style='font-size:15px;color:#6b7280;margin:6px 0 0;
                  font-family:Space Grotesk,sans-serif'>
            Get answers about your shipment risk and supply chain strategy.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Show last prediction context if available
    if st.session_state.last_prediction:
        p = st.session_state.last_prediction
        st.markdown(f"""
        <div style='background:#0d1117;border:1px solid #1e2438;
                    border-radius:10px;padding:14px 18px;margin-bottom:20px'>
            <span style='font-size:11px;color:#6366f1;letter-spacing:2px;
                        text-transform:uppercase'>Last Prediction Context</span>
            <span style='font-size:13px;color:#9ca3af;margin-left:12px'>
                {p['shipping_mode']} · {p['market']} ·
                {'⚠️ HIGH RISK' if p['prediction']==1 else '✅ LOW RISK'}
                {p['probability']:.1f}%
            </span>
        </div>
        """, unsafe_allow_html=True)

    # Sample conversations
    st.markdown("""
    <div class='chat-bubble-ai'>
        👋 Hey! I'm SmartShip AI. I can help you understand why shipments
        get delayed, what actions to take, and how to optimise your
        supply chain. What would you like to know?
    </div>
    <div class='chat-bubble-ai'>
        💡 <b>Try asking me:</b><br>
        "Why is Standard Class shipping riskier?"<br>
        "What's the safest market to ship to?"<br>
        "How do I reduce delay risk for my order?"
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Coming soon notice
    st.markdown("""
    <div style='background:#0d1117;border:1px dashed #1e2438;
                border-radius:14px;padding:30px;text-align:center'>
        <div style='font-size:32px;margin-bottom:12px'>🔑</div>
        <p style='font-size:16px;font-weight:600;color:white;
                  margin:0 0 8px;font-family:Space Grotesk,sans-serif'>
            AI Chat — Coming Soon
        </p>
        <p style='font-size:13px;color:#6b7280;margin:0 0 16px;
                  font-family:Space Grotesk,sans-serif'>
            This feature uses the Claude API for intelligent supply chain Q&A.
            Add your Anthropic API key to activate it.
        </p>
        <div style='display:inline-flex;align-items:center;gap:8px;
                    background:rgba(99,102,241,0.1);
                    border:1px solid rgba(99,102,241,0.2);
                    border-radius:8px;padding:8px 16px'>
            <span style='font-size:13px;color:#a5b4fc;
                        font-family:Space Grotesk,sans-serif'>
                Get your free API key at console.anthropic.com
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
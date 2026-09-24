import streamlit as st
import urllib.parse

# ページ全体の設定
st.set_page_config(
    page_title="Multi-Affiliate Hub", 
    page_icon="💎", 
    layout="centered"
)

# --- スタイリッシュ化のための洗練されたカスタムCSS ---
st.markdown("""
<style>
    /* 全体の背景とパディング調整 */
    .stApp {
        background-color: #f8fafc;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    /* カッコいいグラデーション・メインタイトル */
    .hero-container {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #db2777 100%);
        padding: 1.8rem 1.2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.3);
    }
    .hero-title {
        font-size: 1.6rem;
        font-weight: 800;
        margin: 0;
        color: white;
        letter-spacing: -0.02em;
    }
    .hero-subtitle {
        font-size: 0.8rem;
        opacity: 0.9;
        margin-top: 0.4rem;
        margin-bottom: 0;
    }
    /* セクションカード */
    .modern-card {
        background: #ffffff;
        padding: 1.2rem;
        border-radius: 14px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        margin-bottom: 1rem;
        border: 1px solid #f1f5f9;
    }
</style>
""", unsafe_allow_html=True)

# --- 洗練されたヒーローヘッダー ---
st.markdown("""
<div class="hero-container">
    <p class="hero-title">💎 Multi-Affiliate Hub</p>
    <p class="hero-subtitle">エラー知らず！次世代マルチリンク生成ツール</p>
</div>
""", unsafe_allow_html=True)

# サイドバー：アフィリエイトIDの設定
with st.sidebar:
    st.header("⚙️ アフィリエイト設定")
    rakuten_aff_id = st.text_input("楽天アフィリエイトID", value="104c3008.67310065.104c3009.a677faf7")
    amazon_tag = st.text_input("Amazon アソシエイトID (例: xxx-22)", value="")
    st.info("💡 あなたのIDを保存しておけば、すべての生成リンクに自動で反映されます。")

# メイン入力エリア
st.markdown("<p style='font-weight: 700; color: #1e293b; margin-bottom: 0.5rem;'>🔍 紹介したいアイテムの入力</p>", unsafe_allow_html=True)
input_text = st.text_input("アイテム名やURLを入力", "Xiaomi", label_visibility="collapsed", placeholder="例：北海道スイーツ、Anker、Xiaomi など")

st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
generate_btn = st.button("🚀 収益リンクを一発生成する", use_container_width=True)

if generate_btn:
    if not input_text.strip():
        st.warning("商品名またはURLを入力してください。")
    else:
        clean_input = input_text.strip()
        encoded_query = urllib.parse.quote(clean_input)
        
        # モールごとの検索・アフィリエイトリンクの構築
        rakuten_link = f"https://hb.afl.rakuten.co.jp/hgc/{rakuten_aff_id}/?pc={urllib.parse.quote('https://search.rakuten.co.jp/search/mall/' + clean_input + '/')}"
        
        tag_param = f"&tag={amazon_tag}" if amazon_tag else ""
        amazon_link = f"https://www.amazon.co.jp/s?k={encoded_query}{tag_param}"
        
        yahoo_link = f"https://shopping.yahoo.co.jp/search?p={encoded_query}"

        st.success(f"「{clean_input}」のリンクを生成しました！")
        st.markdown("<div style='margin-top: 0.5rem;'></div>", unsafe_allow_html=True)

        # 1. 楽天市場カード
        st.markdown(f"""
        <div class="modern-card">
            <div style="font-weight: 700; color: #bf0000; font-size: 0.9rem; margin-bottom: 0.4rem;">🛒 楽天市場（アフィリエイト）</div>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("Rakuten Link", value=rakuten_link, key="rak_out", label_visibility="collapsed")
        st.markdown(f"[👉 楽天でチェックする]({rakuten_link})")

        # 2. Amazonカード
        st.markdown(f"""
        <div class="modern-card" style="margin-top: 1rem;">
            <div style="font-weight: 700; color: #d97706; font-size: 0.9rem; margin-bottom: 0.4rem;">📦 Amazon（アソシエイト）</div>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("Amazon Link", value=amazon_link, key="amz_out", label_visibility="collapsed")
        st.markdown(f"[👉 Amazonでチェックする]({amazon_link})")

        # 3. Yahoo!カード
        st.markdown(f"""
        <div class="modern-card" style="margin-top: 1rem;">
            <div style="font-weight: 700; color: #e11d48; font-size: 0.9rem; margin-bottom: 0.4rem;">🛍️ Yahoo!ショッピング</div>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("Yahoo Link", value=yahoo_link, key="yah_out", label_visibility="collapsed")
        st.markdown(f"[👉 Yahoo!でチェックする]({yahoo_link})")
        
        st.markdown("---")

        # SNSやブログ用のまとめテキスト
        st.markdown("<p style='font-weight: 700; color: #1e293b;'>✍️ SNS・ブログ用コピペ文面</p>", unsafe_allow_html=True)
        share_text = f"""＼ 今日のイチオシ！ ／
{clean_input} をチェック✨

▼ 楽天市場はこちら
{rakuten_link}

▼ Amazonはこちら
{amazon_link}

▼ Yahoo!ショッピングはこちら
{yahoo_link}
"""
        st.text_area("コピペ用テキスト", share_text, height=140, label_visibility="collapsed")

# フッター
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.75rem;'>© 2026 Multi-Affiliate Hub</p>", unsafe_allow_html=True)

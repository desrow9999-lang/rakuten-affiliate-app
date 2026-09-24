import streamlit as st
import urllib.parse

# ページ全体の設定
st.set_page_config(
    page_title="Rakuten Threads Generator", 
    page_icon="🛍️", 
    layout="centered"
)

# --- スタイリッシュ化のためのカスタムCSS ---
st.markdown("""
<style>
    .stApp {
        background-color: #f8fafc;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    .hero-container {
        background: linear-gradient(135deg, #bf0000 0%, #ff4500 100%);
        padding: 1.5rem 1rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(191, 0, 0, 0.2);
    }
    .hero-title {
        font-size: 1.5rem;
        font-weight: 800;
        margin: 0;
        color: white;
    }
    .hero-subtitle {
        font-size: 0.8rem;
        opacity: 0.9;
        margin-top: 0.3rem;
        margin-bottom: 0;
    }
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

# --- ヘッダー ---
st.markdown("""
<div class="hero-container">
    <p class="hero-title">🛍️ 楽天 Threads ジェネレーター</p>
    <p class="hero-subtitle">商品名から楽天アフィリエイトリンク＆スレッズ投稿文を秒速作成</p>
</div>
""", unsafe_allow_html=True)

# サイドバー：アフィリエイトIDの設定
with st.sidebar:
    st.header("⚙️ 設定")
    rakuten_aff_id = st.text_input("楽天アフィリエイトID", value="104c3008.67310065.104c3009.a677faf7")
    st.info("💡 あなたのIDがすべてのリンクに自動で反映されます。")

# メイン入力エリア
st.markdown("<p style='font-weight: 700; color: #1e293b; margin-bottom: 0.5rem;'>🔍 紹介したいアイテム名を入力</p>", unsafe_allow_html=True)
input_text = st.text_input("アイテム名", "Xiaomi POCO F9 Ultra", label_visibility="collapsed", placeholder="例：北海道 スイーツ、ワイヤレスイヤホン など")

st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
generate_btn = st.button("🚀 楽天リンク＆スレッズ文面を一発生成", use_container_width=True)

if generate_btn:
    if not input_text.strip():
        st.warning("アイテム名を入力してください。")
    else:
        clean_input = input_text.strip()
        
        # 楽天アフィリエイトリンクの構築
        rakuten_link = f"https://hb.afl.rakuten.co.jp/hgc/{rakuten_aff_id}/?pc={urllib.parse.quote('https://search.rakuten.co.jp/search/mall/' + clean_input + '/')}"

        st.success(f"「{clean_input}」のデータを生成しました！")
        st.markdown("<div style='margin-top: 0.5rem;'></div>", unsafe_allow_html=True)

        # 1. 楽天リンクカード
        st.markdown(f"""
        <div class="modern-card">
            <div style="font-weight: 700; color: #bf0000; font-size: 0.9rem; margin-bottom: 0.4rem;">🛒 楽天アフィリエイトリンク</div>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("Rakuten Link", value=rakuten_link, key="rak_out", label_visibility="collapsed")
        st.markdown(f"[👉 楽天で商品ページをチェックする]({rakuten_link})")

        st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

        # 2. スレッズ用自動生成テキスト
        st.markdown(f"""
        <div class="modern-card">
            <div style="font-weight: 700; color: #000000; font-size: 0.9rem; margin-bottom: 0.4rem;">🧵 スレッズ（Threads）用 投稿文</div>
        </div>
        """, unsafe_allow_html=True)
        
        threads_text = f"""これめちゃ気になってる…！✨
{clean_input}

機能もデザインも良すぎて、お気に入りに追加しちゃった🥰
みんなはもうチェックした？

詳細はこちら👇
{rakuten_link}

#PR #楽天市場 #お買い物メモ #{clean_input.replace(' ', '')}"""

        st.text_area("スレッズ用コピペ文面", threads_text, height=180, label_visibility="collapsed")
        st.info("💡 上のボックスをコピーして、そのままスレッズに貼り付けるだけでOKです！")

# フッター
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.75rem;'>© 2026 楽天 Threads ジェネレーター</p>", unsafe_allow_html=True)

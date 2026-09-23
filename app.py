import streamlit as st
import urllib.parse

# ページ全体の設定
st.set_page_config(
    page_title="Multi-Affiliate Hub", 
    page_icon="💎", 
    layout="centered"
)

# --- スタイリッシュ化のためのカスタムCSSデザイン ---
st.markdown("""
<style>
    /* 全体のフォント・背景の雰囲気 */
    .stApp {
        background-color: #f8f9fa;
    }
    /* グラデーションタイトル */
    .main-title {
        font-size: 1.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        line-height: 1.2;
    }
    .sub-title {
        color: #64748b;
        font-size: 0.85rem;
        margin-bottom: 1.5rem;
    }
    /* カードデザイン */
    .affiliate-card {
        background: #ffffff;
        padding: 1.2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        margin-bottom: 1.2rem;
        border: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# --- ヘッダー部分 ---
st.markdown('<p class="main-title">💎 Multi-Affiliate Hub</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">スマートに収益リンクを生成する、次世代アフィリエイトツール</p>', unsafe_allow_html=True)

# サイドバー：アフィリエイトIDの設定
with st.sidebar:
    st.header("⚙️ アフィリエイト設定")
    rakuten_aff_id = st.text_input("楽天アフィリエイトID", value="104c3008.67310065.104c3009.a677faf7")
    amazon_tag = st.text_input("Amazon アソシエイトID (例: xxx-22)", value="")
    st.info("💡 あなたのIDを保存しておけば、すべての生成リンクに自動で反映されます。")

# メイン入力エリア
st.markdown("### 🔍 商品の変換・リンク生成")
input_text = st.text_input("紹介したい商品の「名前」または「通常のURL」を入力", "Xiaomi")

if st.button("🚀 収益リンクを一発生成する", use_container_width=True):
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

        st.success("✨ 各モールの収益化リンクを生成しました！")
        st.markdown("---")

        # スタイリッシュなカード枠でそれぞれのリンクを表示
        st.markdown(f"""
        <div class="affiliate-card">
            <div style="font-weight: 700; color: #1e293b; margin-bottom: 8px; font-size: 1rem;">📦 対象アイテム: <span style="color: #6366f1;">{clean_input}</span></div>
            <hr style="margin: 10px 0; border: 0; border-top: 1px solid #f1f5f9;">
            
            <p style="margin: 8px 0 4px 0; font-weight: 600; color: #bf0000; font-size: 0.9rem;">🛒 楽天市場（アフィリエイトリンク）</p>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("Rakuten Link", value=rakuten_link, key="rakuten_out", label_visibility="collapsed")
        st.markdown(f"[👉 楽天で確認・購入する]({rakuten_link})")

        st.markdown(f"""
        <div class="affiliate-card" style="margin-top: 15px;">
            <p style="margin: 0 0 4px 0; font-weight: 600; color: #ff9900; font-size: 0.9rem;">📦 Amazon（検索＆アソシエイト）</p>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("Amazon Link", value=amazon_link, key="amazon_out", label_visibility="collapsed")
        st.markdown(f"[👉 Amazonで確認・購入する]({amazon_link})")

        st.markdown(f"""
        <div class="affiliate-card" style="margin-top: 15px;">
            <p style="margin: 0 0 4px 0; font-weight: 600; color: #ff0033; font-size: 0.9rem;">🛍️ Yahoo!ショッピング</p>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("Yahoo Link", value=yahoo_link, key="yahoo_out", label_visibility="collapsed")
        st.markdown(f"[👉 Yahoo!で確認・購入する]({yahoo_link})")
        
        st.markdown("---")

        # SNSやブログ用のまとめテキスト
        st.markdown("### ✍️ SNS・ブログ用コピペ文面")
        share_text = f"""＼ 今日のイチオシ！ ／
{clean_input} をチェック✨

▼ 楽天市場はこちら
{rakuten_link}

▼ Amazonはこちら
{amazon_link}

▼ Yahoo!ショッピングはこちら
{yahoo_link}
"""
        st.text_area("以下の文章をコピーしてSNSやブログに貼り付けられます", share_text, height=150)

# フッター
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.8rem;'>© 2026 Multi-Affiliate Hub | Powered by Streamlit</p>", unsafe_allow_html=True)

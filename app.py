import streamlit as st
import urllib.parse

# ページ全体の設定
st.set_page_config(
    page_title="一撃マルチアフィリエイト・ジェネレーター", 
    page_icon="💰", 
    layout="centered"
)

# --- スタイリッシュ化のためのカスタムCSS ---
st.markdown("""
<style>
    .main-title {
        font-size: 2.0rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF8008 0%, #FFC837 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
    }
    .card {
        background: #ffffff;
        padding: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        margin-bottom: 1.2rem;
        border: 1px solid #eaeaea;
    }
    .success-box {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- ヘッダー部分 ---
st.markdown('<p class="main-title">💰 一撃マルチアフィリエイト・ツール</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">エラー知らず！URLや商品名から、主要3モールの収益リンクを同時に一発生成</p>', unsafe_allow_html=True)

# サイドバー：アフィリエイトIDの設定
with st.sidebar:
    st.header("⚙️ アフィリエイト設定")
    # 先ほど取得したアフィリエイトIDを初期値に設定
    rakuten_aff_id = st.text_input("楽天アフィリエイトID (またはトマレ等)", value="104c3008.67310065.104c3009.a677faf7")
    amazon_tag = st.text_input("Amazon アソシエイトID (例: xxx-22)", value="")
    yahoo_vc_id = st.text_input("もしも/バリューコマース等 (任意)", value="")
    st.info("💡 あなたのIDを保存しておけば、すべての生成リンクに自動で反映されます。")

# メイン入力エリア
st.markdown("### 🔗 商品の変換・リンク生成")
input_text = st.text_input("紹介したい商品の「名前」または「通常のURL」を入力", "北海道 お取り寄せ スイーツ")

if st.button("🚀 収益リンクを一発生成する", use_container_width=True):
    if not input_text.strip():
        st.warning("商品名またはURLを入力してください。")
    else:
        clean_input = input_text.strip()
        encoded_query = urllib.parse.quote(clean_input)
        
        # モールごとの検索・アフィリエイトリンクの構築
        # 1. 楽天市場（楽天アフィリエイトIDを付与）
        rakuten_link = f"https://hb.afl.rakuten.co.jp/hgc/{rakuten_aff_id}/?pc={urllib.parse.quote('https://search.rakuten.co.jp/search/mall/' + clean_input + '/')}"
        
        # 2. Amazon（アソシエイトタグを付与）
        tag_param = f"&tag={amazon_tag}" if amazon_tag else ""
        amazon_link = f"https://www.amazon.co.jp/s?k={encoded_query}{tag_param}"
        
        # 3. Yahoo!ショッピング
        yahoo_link = f"https://shopping.yahoo.co.jp/search?p={encoded_query}"

        st.success("✨ 各モールの収益化リンクを生成しました！")
        st.markdown("---")

        # 結果表示カード
        st.markdown(f"""
        <div class="card">
            <h4 style="margin-top:0; color:#333;">📦 対象キーワード・商品: <b>{clean_input}</b></h4>
            <hr style="margin:10px 0; border:0; border-top:1px solid #eee;">
            
            <p style="margin-bottom:5px; font-weight:600; color:#BF0000;">1. 楽天市場（アフィリエイトリンク）</p>
            <input type="text" value="{rakuten_link}" readonly style="width:100%; padding:8px; border-radius:6px; border:1px solid #ddd; background:#fafafa; font-size:0.8rem; margin-bottom:10px;">
            <a href="{rakuten_link}" target="_blank" style="display:inline-block; background:#BF0000; color:white; padding:6px 14px; border-radius:15px; text-decoration:none; font-size:0.85rem; font-weight:600; margin-bottom:15px;">🛒 楽天で確認・購入</a>

            <p style="margin-bottom:5px; font-weight:600; color:#FF9900;">2. Amazon（検索＆アソシエイト）</p>
            <input type="text" value="{amazon_link}" readonly style="width:100%; padding:8px; border-radius:6px; border:1px solid #ddd; background:#fafafa; font-size:0.8rem; margin-bottom:10px;">
            <a href="{amazon_link}" target="_blank" style="display:inline-block; background:#232F3E; color:white; padding:6px 14px; border-radius:15px; text-decoration:none; font-size:0.85rem; font-weight:600; margin-bottom:15px;">📦 Amazonで確認・購入</a>

            <p style="margin-bottom:5px; font-weight:600; color:#FF0033;">3. Yahoo!ショッピング</p>
            <input type="text" value="{yahoo_link}" readonly style="width:100%; padding:8px; border-radius:6px; border:1px solid #ddd; background:#fafafa; font-size:0.8rem; margin-bottom:10px;">
            <a href="{yahoo_link}" target="_blank" style="display:inline-block; background:#FF0033; color:white; padding:6px 14px; border-radius:15px; text-decoration:none; font-size:0.85rem; font-weight:600;">🛍️ Yahoo!で確認・購入</a>
        </div>
        """, unsafe_allow_html=True)
        
        # SNSやブログ用のまとめテキストも自動生成
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
        st.text_area("以下の文章をコピーして、X（Twitter）やInstagram、ブログに貼り付けられます", share_text, height=150)

# フッター
st.markdown("---")
st.markdown("<p style='text-align: center; color: #aaa; font-size: 0.8rem;'>© 2026 一撃マルチアフィリエイト・ツール | Powered by Streamlit</p>", unsafe_allow_html=True)

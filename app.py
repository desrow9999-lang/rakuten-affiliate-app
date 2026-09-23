import streamlit as st
import urllib.parse

# ページ全体の設定
st.set_page_config(
    page_title="一撃マルチアフィリエイト・ジェネレーター", 
    page_icon="💰", 
    layout="centered"
)

# --- ヘッダー部分 ---
st.title("💰 一撃マルチアフィリエイト・ツール")
st.markdown("エラー知らず！URLや商品名から、主要3モールの収益リンクを同時に一発生成します。")

# サイドバー：アフィリエイトIDの設定
with st.sidebar:
    st.header("⚙️ アフィリエイト設定")
    rakuten_aff_id = st.text_input("楽天アフィリエイトID", value="104c3008.67310065.104c3009.a677faf7")
    amazon_tag = st.text_input("Amazon アソシエイトID (例: xxx-22)", value="")
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
        rakuten_link = f"https://hb.afl.rakuten.co.jp/hgc/{rakuten_aff_id}/?pc={urllib.parse.quote('https://search.rakuten.co.jp/search/mall/' + clean_input + '/')}"
        
        tag_param = f"&tag={amazon_tag}" if amazon_tag else ""
        amazon_link = f"https://www.amazon.co.jp/s?k={encoded_query}{tag_param}"
        
        yahoo_link = f"https://shopping.yahoo.co.jp/search?p={encoded_query}"

        st.success("✨ 各モールの収益化リンクを生成しました！")
        st.markdown("---")

        # 1. 楽天市場
        st.markdown("##### 🛒 楽天市場（アフィリエイトリンク）")
        st.text_input("Rakuten Link", value=rakuten_link, key="rakuten_out", label_visibility="collapsed")
        st.markdown(f"[👉 楽天で確認・購入する]({rakuten_link})", unsafe_allow_html=True)

        st.markdown("")

        # 2. Amazon
        st.markdown("##### 📦 Amazon（検索＆アソシエイト）")
        st.text_input("Amazon Link", value=amazon_link, key="amazon_out", label_visibility="collapsed")
        st.markdown(f"[👉 Amazonで確認・購入する]({amazon_link})", unsafe_allow_html=True)

        st.markdown("")

        # 3. Yahoo!ショッピング
        st.markdown("##### 🛍️ Yahoo!ショッピング")
        st.text_input("Yahoo Link", value=yahoo_link, key="yahoo_out", label_visibility="collapsed")
        st.markdown(f"[👉 Yahoo!で確認・購入する]({yahoo_link})", unsafe_allow_html=True)
        
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
st.markdown("<p style='text-align: center; color: #aaa; font-size: 0.8rem;'>© 2026 一撃マルチアフィリエイト・ツール | Powered by Streamlit</p>", unsafe_allow_html=True)

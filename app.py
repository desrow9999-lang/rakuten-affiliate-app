import streamlit as st
import requests

# ページ全体の設定
st.set_page_config(
    page_title="楽天ラグジュアリーセレクト | 智能ポイ活カタログ", 
    page_icon="✨", 
    layout="centered"
)

# --- スタイリッシュ化のためのカスタムCSS ---
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #BF0000 0%, #FF416C 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #666;
        font-size: 0.95rem;
        margin-bottom: 2rem;
    }
    .product-card {
        background: #ffffff;
        padding: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        margin-bottom: 1.2rem;
        border: 1px solid #eaeaea;
    }
    .price-tag {
        color: #BF0000;
        font-size: 1.25rem;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# --- ヘッダー部分 ---
st.markdown('<p class="main-title">✨ 楽天ラグジュアリーセレクト</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">トレンドと欲しいモノをスマートに繋ぐ、次世代アフィリエイト・カタログ</p>', unsafe_allow_html=True)

# サイドバー：認証・設定情報
with st.sidebar:
    st.header("⚙️ システム設定")
    # ここには元の形式のアプリケーションID（またはお持ちの通常のID）を設定します
    app_id = st.text_input("アプリケーションID", value="cd4566ea-c2e9-462d-8e63-01b1eec844b8")
    affiliate_id = st.text_input("アフィリエイトID", value="104c3008.67310065.104c3009.a677faf7")
    st.info("💡 アプリケーションIDを入力してください。")

# メイン検索エリア
st.markdown("### 🔍 スマートアイテム検索")
keyword = st.text_input("「気になるキーワードを入力してください」（例：北海道スイーツ、Xiaomi、プロテイン）", "北海道 スイーツ")

col1, col2 = st.columns([3, 1])
with col1:
    search_btn = st.button("✨ カタログを生成する", use_container_width=True)

if search_btn:
    clean_app_id = app_id.strip() if app_id else ""
    clean_aff_id = affiliate_id.strip() if affiliate_id else ""
    clean_keyword = keyword.strip() if keyword else ""

    if not clean_app_id or not clean_aff_id:
        st.warning("アプリケーションIDとアフィリエイトIDを入力してください。")
    else:
        # APIのエンドポイント（最も互換性の高いバージョンに変更）
        url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170428"
        
        params = {
            "applicationId": clean_app_id,
            "affiliateId": clean_aff_id,
            "keyword": clean_keyword,
            "format": "json",
            "hits": 6
        }

        with st.spinner("🌟 楽天のトレンドデータを同期中..."):
            try:
                res = requests.get(url, params=params)
                
                if res.status_code == 200:
                    data = res.json()
                    items = data.get("Items", [])
                    
                    if not items:
                        st.info("該当するアイテムが見つかりませんでした。別のキーワードでお試しください。")
                    else:
                        st.success(f"「{clean_keyword}」の厳選アイテムをピックアップしました！")
                        st.markdown("---")
                        
                        for item_wrapper in items:
                            item = item_wrapper["Item"]
                            item_name = item["itemName"]
                            item_price = item["itemPrice"]
                            item_url = item.get("affiliateUrl") or item["itemUrl"]
                            image_url = item["mediumImageUrls"][0]["imageUrl"] if item["mediumImageUrls"] else ""
                            
                            st.markdown(f"""
                            <div class="product-card">
                                <table>
                                    <tr>
                                        <td style="width: 110px; vertical-align: top; padding-right: 15px;">
                                            <img src="{image_url}" width="100" style="border-radius: 8px; object-fit: cover;">
                                        </td>
                                        <td style="vertical-align: top;">
                                            <div style="font-weight: 600; font-size: 0.95rem; margin-bottom: 8px; color: #333;">{item_name}</div>
                                            <div class="price-tag">¥{item_price:,}</div>
                                        </td>
                                    </tr>
                                </table>
                                <div style="text-align: right; margin-top: 10px;">
                                    <a href="{item_url}" target="_blank" style="background-color: #BF0000; color: white; padding: 6px 16px; border-radius: 20px; text-decoration: none; font-size: 0.85rem; font-weight: 600;">🛒 詳細・購入を見る</a>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                else:
                    st.error(f"APIエラー (コード: {res.status_code})")
                    try:
                        err_json = res.json()
                        st.code(str(err_json))
                    except:
                        st.text(res.text)
            except Exception as e:
                st.error(f"通信例外エラー: {e}")

# フッター
st.markdown("---")
st.markdown("<p style='text-align: center; color: #aaa; font-size: 0.8rem;'>© 2026 楽天ラグジュアリーセレクト | Powered by Streamlit & Rakuten Web Service</p>", unsafe_allow_html=True)

import streamlit as st
import requests

st.set_page_config(page_title="楽天アフィリエイト・カタログメーカー", page_icon="💰", layout="centered")

st.title("💰 楽天アフィリエイト・自動カタログメーカー")
st.write("取得したAPIを使って、アフィリエイトリンク付きのアイテムを検索できます！")

# 先ほど取得したIDを初期値として設定（もちろんサイドバーで書き換えられるようにしてもOKです）
app_id = st.sidebar.text_input("アプリケーションID", value="7e0200d6-45fe-4b28-be71-8711baaa5e7c", type="password")
affiliate_id = st.sidebar.text_input("アフィリエイトID", value="104c3008.67310065.104c3009.a677faf7")

# 検索キーワード
keyword = st.text_input("検索したい商品のキーワード（例：キャンプ用品、お取り寄せ スイーツ、プロテイン）", "北海道 スイーツ")

if st.button("🔍 楽天から商品を探してアフィリエイトリンクを作る"):
    if not app_id or not affiliate_id:
        st.warning("アプリケーションIDとアフィリエイトIDを入力してください。")
    else:
        # 楽天商品検索APIのエンドポイント
        url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601"
        params = {
            "applicationId": app_id,
            "affiliateId": affiliate_id,
            "keyword": keyword,
            "format": "json",
            "hits": 5
        }
        
        try:
            res = requests.get(url, params=params)
            if res.status_code == 200:
                data = res.json()
                items = data.get("Items", [])
                
                if not items:
                    st.info("該当する商品が見つかりませんでした。別のキーワードを試してみてください。")
                else:
                    st.success(f"「{keyword}」のヒット商品（上位5件）を取得しました！")
                    st.markdown("---")
                    
                    for item_wrapper in items:
                        item = item_wrapper["Item"]
                        col1, col2 = st.columns([1, 2])
                        with col1:
                            st.image(item["mediumImageUrls"][0]["imageUrl"], width=120)
                        with col2:
                            st.subheader(item["itemName"])
                            st.write(f"価格: **{item['itemPrice']:,}円**")
                            # 楽天APIが自動生成したアフィリエイトリンク
                            aff_url = item.get("affiliateUrl") or item["itemUrl"]
                            st.markdown(f"[🛒 楽天市場でチェック・購入する]({aff_url})", unsafe_allow_html=True)
                        st.markdown("---")
                        
                    st.info("💡 このリンクを経由して購入されると、あなたにアフィリエイト報酬が入る仕組みが完成しています！")
            else:
                st.error(f"APIの取得に失敗しました（ステータスコード: {res.status_code}）。入力内容をご確認ください。")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")

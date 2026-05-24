import pandas as pd
from datetime import datetime
from models.base import SessionLocal
from models.stock import Stock
from models.transaction import Transaction

def import_csv(filepath: str):
    # CSVを読み込む（SBI証券のフォーマット）
    df = pd.read_csv(
        filepath,
        encoding="shift-jis",
        skiprows=8,        # ヘッダー情報をスキップ
        header=0,
    )

    session = SessionLocal()

    try:
        for _, row in df.iterrows():
            # 銘柄の登録（すでに存在する場合はスキップ）
            stock = session.query(Stock).filter_by(code=str(row["銘柄コード"])).first()
            if not stock:
                stock = Stock(
                    code   = str(row["銘柄コード"]),
                    name   = str(row["銘柄"]),
                    market = str(row["市場"]),
                )
                session.add(stock)
                session.flush()  # stock.idを確定させる

            # 取引種別の判定
            raw_type = str(row["取引"])
            if "買" in raw_type:
                transaction_type = "buy"
            elif "売" in raw_type:
                transaction_type = "sell"
            else:
                transaction_type = "dividend"

            # 取引の登録
            transaction = Transaction(
                stock_id         = stock.id,
                transaction_type = transaction_type,
                quantity         = int(row["約定数量"]),
                price            = float(row["約定単価"]),
                amount           = int(str(row["受渡金額/決済損益"]).replace(",", "")),
                account_type     = str(row["預り"]).strip(),
                commission       = None,
                date             = datetime.strptime(str(row["約定日"]), "%Y/%m/%d").date(),
            )
            session.add(transaction)

        session.commit()
        print(f"インポート完了：{len(df)}件の取引を登録しました")

    # except Exception as e:
    #     session.rollback()
    #     print(f"エラーが発生しました：{e}")

    except Exception as e:
        session.rollback()
        import traceback
        traceback.print_exc()
        print(f"エラーが発生しました：{e}")

    finally:
        session.close()
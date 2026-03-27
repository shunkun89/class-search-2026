from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Excelデータ読み込み
df = pd.read_excel("2026クラス検索データ.xlsx")

@app.route("/", methods=["GET", "POST"])
def search():
    result = None
    error = None

    if request.method == "POST":
        number = request.form["exam_number"]

        if not number.isdigit():
            error = "受験番号は数字で入力してください。"
        else:
            number = int(number)
            row = df[df["受験番号"] == number]

            if not row.empty:
                result = {
                    "class": row.iloc[0]["クラス"],
                    "number": row.iloc[0]["出席番号"]
                }
            else:
                error = "該当する受験番号が見つかりません。"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

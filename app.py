from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_excel("2026クラス検索データ.xlsx", dtype=str)

@app.route("/", methods=["GET", "POST"])
def search():
    result = None
    error = None

    if request.method == "POST":
        number = request.form["exam_number"]
        birth = request.form["birth_date"]

        if not number.isdigit() or not birth.isdigit() or len(birth) != 8:
            error = "受験番号と生年月日（8桁）を正しく入力してください。"
        else:
            row = df[(df["受験番号"] == number) & (df["生年月日"] == birth)]

            if not row.empty:
               result = {
    "sei": row.iloc[0]["姓"],
    "mei": row.iloc[0]["名"],
    "school": row.iloc[0]["中学校名"],
    "class": row.iloc[0]["クラス"],
    "number": row.iloc[0]["出席番号"],
    "room": row.iloc[0]["教室"]
}
            else:
                error = "受験番号または生年月日が正しくありません。"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

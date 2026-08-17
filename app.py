from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

MODEL_PATH = "model_klasifikasi_jeruk.joblib"
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None
    error = None

    form = {
        "berat": "",
        "diameter": "",
        "tebal_kulit": "",
        "kadar_gula": "",
        "asal_daerah": "",
        "warna": "",
        "musim_panen": ""
    }

    if request.method == "POST":
        form.update({
            key: request.form.get(key, "").strip()
            for key in form
        })

        try:
            # IMPORTANT:
            # These columns and their order follow the X definition
            # in the uploaded notebook.
            data_baru = pd.DataFrame([{
                "berat": float(form["berat"]),
                "diameter": float(form["diameter"]),
                "tebal_kulit": float(form["tebal_kulit"]),
                "kadar_gula": float(form["kadar_gula"]),
                "asal_daerah": form["asal_daerah"],
                "warna": form["warna"].lower(),
                "musim_panen": form["musim_panen"].lower()
            }], columns=[
                "berat", "diameter", "tebal_kulit", "kadar_gula",
                "asal_daerah", "warna", "musim_panen"
            ])

            prediction = model.predict(data_baru)[0]
            result = str(prediction)

            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba(data_baru)[0]
                confidence = max(probabilities) * 100

        except Exception as e:
            error = (
                "Data tidak dapat diproses. Pastikan angka dan kategori "
                "sesuai dengan data training. Detail: " + str(e)
            )

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        error=error,
        form=form
    )


if __name__ == "__main__":
    app.run(debug=True)

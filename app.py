from flask import Flask, render_template, request, jsonify

from ice_breaker import icebreak_main

app = Flask(__name__)


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    person_info, profile_pic_url = icebreak_main(name=name)

    return jsonify(
        {
            "summary": person_info.summary,
            "interests": person_info.interest,
            "facts": person_info.facts,
            "ice_breakers": person_info.ice_breakers,
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

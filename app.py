import os
from flask import Flask

app = Flask(__name__)
COUNT_FILE = "/data/count.txt"

@app.route("/")
def hello():
    if not os.path.exists("/data"):
        os.makedirs("/data")

    count = 0
    if os.path.exists(COUNT_FILE):
        count = int(open(COUNT_FILE).read())

    count += 1
    open(COUNT_FILE, "w").write(str(count))

    name = os.getenv("NAME", "Docker")

    return f"Hello {name}! Visit #{count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
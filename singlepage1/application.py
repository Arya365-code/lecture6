from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla tempor, felis eget laoreet suscipit, dui libero ultricies enim, non pretium massa lectus vitae justo. Cras eu sapien tincidunt, gravida lectus id, ultricies elit. Phasellus fringilla arcu id congue semper. Phasellus et elit scelerisque, pellentesque lorem et, condimentum eros. ",
         "Ut quis elementum ipsum. Quisque et enim vehicula tellus rhoncus posuere ut ac nulla. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur blandit purus varius orci accumsan ornare. Donec ex orci, commodo eget nibh eget, semper pellentesque neque.",
         "Sed velit ipsum, pellentesque vitae quam quis, elementum maximus lectus. Nulla a lorem dui. Curabitur efficitur sem in dui dignissim, eu blandit elit fermentum. Nulla in pulvinar magna. Cras aliquam tortor ut tempor sollicitudin. Maecenas in semper sem. Nullam lorem justo, venenatis ut diam eu, venenatis scelerisque sem. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed risus elit, sagittis sit amet enim ut, maximus posuere turpis. Nam et risus aliquet, bibendum magna eget, rutrum metus. Aliquam blandit tempor mi dictum sagittis. Sed porttitor aliquet finibus. Suspendisse commodo elit non sem varius congue."

@app.route("/first")
def first():
  return texts[0]

@app.route("/second")
def second():
  return texts[1]

@app.route("/third")
def third():
  return texts[2]

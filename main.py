from flask import Flask, redirect, request, render_template, session
import os
import codecs
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



@app.route('/')
def index():

	#index_base_file = codecs.open("templates/index.html", "r", "utf-8")



	chat_storage_file = codecs.open("data/chat_file.txt", "r", "utf-8")

	chat = chat_storage_file.read()

	index1 = f"""

<!doctype html>
<html lang="fr">

<head>
  <meta charset="utf-8">
  <title>Anon Palace</title>
  <link rel="stylesheet" href="{{{{ url_for('static', filename='style/mainpage.css')}}}}">
</head>

<body>


  <div id="title_box">
    <p id="title">

                                        _____      _                
     /\\                               |  __ \\    | |               
    /  \\   _ __   ___  _ __    ______  | |__) |_ _| | __ _  ___ ___ 
   / /\\ \\ | '_ \\ / _ \\| '_ \\  |______| |  ___/ _` | |/ _` |/ __/ _ \
  / ____ \\| | | | (_) | | | |          | |  | (_| | | (_| | (_|  __/
 /_/    \\_\\_| |_|\\___/|_| |_|          |_|   \\__,_|_|\\__,_|\\___\\___|
                                                                    

    </p>
  </div>

<div id="presentation_box">
  <p id="presentation">
    Anon-Palace is an anonymous forum where you can share your knowledge without caring   <br>
    about your identity and safety.
  </p>
  
</div>

<div id="shoutbox">
  <p id="chat">
    {chat}
  </p>
</div>

<center><div id="message_field">
  <form autocomplete="off" action="api/send" method="post" id="send_form">
  <input type="text" name="msg_field" id="msg_field" autocomplete=“false” required>
  <input type="submit" hidden />
</div>
</center>

</body>

</html>
		
	"""

	index_file = codecs.open("templates/index.html", "w", "utf-8")

	index_file.write(index1)

	chat_storage_file.close()
	index_file.close()


	return render_template("index.html")


@app.route('/api/send', methods=['POST', 'GET'])
def sendMessage():	
	if request.method == "POST":
		msg = request.form['msg_field']
		chat_storage_file = open("data/chat_file.txt", "a+")
		chat_storage_file.write((f"@admin : {msg} <br>"))
		chat_storage_file.close()
		return redirect("http://muzulab.local:1336/", code=302)


@app.route('/api/register')
def registerAPI():
  return redirect("http://muzulab.local:1336/", code=302)

@app.route('/login', methods =['GET', 'POST'])
def login():
  return "index"


@app.route('/login/logout')
def logout():
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
  return "index"




@app.route('/admin/delete', methods=["POST"])
def clearChat():
  if request.method == "POST":
    password = request.json["password"]
    if len(str(password)) == 0:
      print("blank pwd")
      return redirect("http://muzulab.local:1336/", code=302)
    else:
      if str(password) == "motdepassetressecurise":
        print("valid pwd")
        index1 = f"""

<!doctype html>
<html lang="fr">

<head>
  <meta charset="utf-8">
  <title>Anon Palace</title>
  <link rel="stylesheet" href="{{{{ url_for('static', filename='style/mainpage.css')}}}}">
</head>

<body>


  <div id="title_box">
    <p id="title">

                                        _____      _                
     /\\                               |  __ \\    | |               
    /  \\   _ __   ___  _ __    ______  | |__) |_ _| | __ _  ___ ___ 
   / /\\ \\ | '_ \\ / _ \\| '_ \\  |______| |  ___/ _` | |/ _` |/ __/ _ \
  / ____ \\| | | | (_) | | | |          | |  | (_| | | (_| | (_|  __/
 /_/    \\_\\_| |_|\\___/|_| |_|          |_|   \\__,_|_|\\__,_|\\___\\___|
                                                                    

    </p>
  </div>

<div id="presentation_box">
  <p id="presentation">
    Anon-Palace is an anonymous forum where you can share your knowledge without caring   <br>
    about your identity and safety.
  </p>
  
</div>

<div id="shoutbox">
  <p id="chat">
    @AppolyonBot : Chat Cleared !
  </p>
</div>

<center><div id="message_field">
  <form autocomplete="off" action="api/send" method="post" id="send_form">
  <input type="text" name="msg_field" id="msg_field" autocomplete=“false” required>
  <input type="submit" hidden />
</div>
</center>

</body>

</html>
    
  """
        index_file = codecs.open("templates/index.html", "w", "utf-8")
        index_file.write(index1)
        index_file.close()
        return redirect("http://muzulab.local:1336/", code=302)
      else:
        print("wrong pwd")
        return redirect("http://muzulab.local:1336/", code=302)
  else:
    return "wrong method"

if __name__ == "__main__":
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host="0.0.0.0", port=1336)
from flask import Flask, request, render_template
from stories import story


# next we create flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = "abcdefg"


@app.route('/')
def show_home_form():
    p= story.prompts
    return render_template("form.html", prom=p)

@app.route('/story')
def show_story():
    s = story.generate(request.args)
    return render_template("story.html", my_story=s)

# ans = {"verb": "eat", "noun": "mango","place":"limgrave","adjective":"scary","plural_noun":"pirates"}
# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )


# @app.route('/greet')
# def get_greeting():
#     username = request.args["username"]
#     nasty_thing = choice(insults)
#     return render_template("greet.html", username=username, insult=nasty_thing)


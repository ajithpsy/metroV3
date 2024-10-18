from flask import Flask
app=Flask(__name__)
@app.roule
def home:
    if __name__
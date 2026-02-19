import sys
import os

sys.path.append(os.getcwd())

from Flasky import create_app

app=create_app()



if __name__ == "__main__":
    app.run(debug=True)
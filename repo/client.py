from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def main():

    r1 = requests.get("http://vcm-3608.vm.duke.edu:5000/name")
    print (r1.text)

    r2 = requests.get("http://vcm-3608.vm.duke.edu:5000/hello/Enoch")
    print (r2.text)

    r3 = requests.post("http://vcm-3608.vm.duke.edu:5000/distance",
                       json={"a": [2,4],"b": [5,6]})

    distance = r3.json()
    print (distance)

    return

if __name__ == "__main__":
    main()
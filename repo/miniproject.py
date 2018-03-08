from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/name", methods=["GET"])
def name():
    """ Return string of name to the collar

    :return nm: name in dictionary
    """
    nm = {
         "name": "Enoch"
         }
    return jsonify(nm)

@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    """ Return string of message to the collar


    :param name: URL input name
    :return: message greeting the name inputted
    """
    msg = {
          "message": "Hello there, {0}".format(name)
           }
    return jsonify(msg)

@app.route("/distance", methods=["POST"])
def distance():
    """ Returns inputted coordinates and the calculated distance to caller


    :return: dictionary containing coordinates and calculated distance
    """
    r = request.get_json()
    diff = calc_distance(r["a"], r["b"])

    result = {
             "distance": diff,
             "a": r["a"],
             "b": r["b"]
    }

    return jsonify(result)

def calc_distance(coord_1, coord_2):
    """ Calculates the distance between the two inputted coordinates

    :param coord_1: First coordinate
    :param coord_2: Second coordinate
    :return: Returns distance between the two coordinates
    """
    diff = ((coord_1[0] - coord_2[0])**2 + (coord_1[1] - coord_2[1])**2)**0.5

    return diff

if __name__ == "__main__":
    app.run(host="127.0.0.1")
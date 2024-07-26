from flask import Flask, request, jsonify

app = Flask("My Internship app")

examples = [
    {"id": 0, "title": "Example 1", "body": "First example in the list"},
    {"id": 1, "title": "Example 2", "body": "Second example in the list"},
    {"id": 2, "title": "Example 3", "body": "Third example in the list"},
]

@app.route("/")
def index():
    return "Welcome to my app!"

@app.route("/example/<int:id>", methods=["POST"])
def my_example(id):
    if id < 0:
        return jsonify(error="invalid id, must be above 0!"), 400
    return jsonify(userId=id)

@app.route("/examples", methods=["GET"])
def get_examples():
    return jsonify(examples=examples)

@app.route("/examples", methods=["POST"])
def post_example():
    data = request.json   
    data["id"] = len(examples)
    examples.append(data)
    return jsonify(data), 200

@app.route("/examples/<int:id>", methods=["PUT"])
def put_example(id):
    data = request.json
    for example in examples:
        if example["id"] == id:
            example["title"] = data.get("title", example["title"])
            example["body"] = data.get("body", example["body"])
            return jsonify(example), 200 
            #jsonify: converts Python dictionaries to JSON format to be sent as HTTP responses 
            #200 is the status code 

@app.route("/examples/<int:id>", methods=["PATCH"])
def patch_example(id):
    data = request.json
    for example in examples:
        if example["id"] == id:
            example.update(data)
            return jsonify(example), 200

@app.route("/examples/<int:id>", methods=["DELETE"])
def delete_example(id):
    global examples
    examples = [example for example in examples if example["id"] != id]
    return jsonify(message="Example deleted"), 200

if __name__ == "__main__":
    app.run(debug=True)

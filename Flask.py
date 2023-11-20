from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (replace with a database in a real-world scenario)
books = [
    {"id": 1, "book_name": "Book1", "author": "Author1", "publisher": "Publisher1"},
    {"id": 2, "book_name": "Book2", "author": "Author2", "publisher": "Publisher2"},
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        return jsonify({"book": book})
    else:
        return jsonify({"message": "Book not found"}), 404

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "book_name": data["book_name"],
        "author": data["author"],
        "publisher": data["publisher"],
    }
    books.append(new_book)
    return jsonify({"message": "Book created successfully"}), 201

# Update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        data = request.get_json()
        book.update({
            "book_name": data["book_name"],
            "author": data["author"],
            "publisher": data["publisher"],
        })
        return jsonify({"message": "Book updated successfully"})
    else:
        return jsonify({"message": "Book not found"}), 404

# Delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [item for item in books if item["id"] != book_id]
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
    
from typing import Dict, List


def get_books_users_dict(users_books_dict: Dict[str, List]) -> Dict[str, List]:
    """
    Args:
        dictionary of the form {user: List(books)}
    Returns:
        dictionary of the form {book: List[users]}
    """

    books_users_dict = {}
    for user, books in users_books_dict.items():
        for book in books:
            books_users_dict.setdefault(book, []).append(user)
    return books_users_dict


if __name__ == "__main__":
    import pprint as pp

    users_books_dict = {
        "Alice": ["book1", "book2", "book3"],
        "Bob": ["book3", "book4", "book2", "book5"],
        "Mary": ["book1", "book2", "book8"],
        "Joe": ["book8"],
    }

    books_users_dict = get_books_users_dict(users_books_dict)
    pp.pprint(books_users_dict)

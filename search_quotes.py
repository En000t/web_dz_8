from models import Quote, Author

while True:
    user_input = input("Введіть команду: ").strip()

    if user_input.startswith("name:"):
        author_name = user_input[len("name:"):].strip()
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(quote.quote)
        else:
            print("Автор не знайдений.")

    elif user_input.startswith("tag:"):
        tag = user_input[len("tag:"):].strip()
        quotes = Quote.objects(tags=tag)
        for quote in quotes:
            print(quote.quote)

    elif user_input.startswith("tags:"):
        tags = [t.strip() for t in user_input[len("tags:"):].split(",")]
        quotes = Quote.objects(tags__in=tags)
        for quote in quotes:
            print(quote.quote)

    elif user_input.lower() == "exit":
        break

    else:
        print("Невідома команда.")

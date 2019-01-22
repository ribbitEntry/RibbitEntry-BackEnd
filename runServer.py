import os

from server import create_app

if __name__ == '__main__':
    app = create_app()

    if 'SECRET_KEY' not in os.environ:
        print("[WARNING] SECRET KEY NOT FOUNDED IN ENVIRONMENT VARIABLE")

    app.run('0.0.0.0', port=5000, debug=True)

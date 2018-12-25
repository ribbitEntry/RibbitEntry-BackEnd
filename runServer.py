from server import create_app, register_extensions

app = create_app()

register_extensions(app)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

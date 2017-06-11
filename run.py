# Run a test server.
import exampleapp

app = exampleapp.create_app()

app.config.update({
    "DEBUG": True,
    "USE_RELOADER": True
})

app.run(host='0.0.0.0', port=5000)

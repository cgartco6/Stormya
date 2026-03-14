from flask import Flask, render_template, request, jsonify

from stormy.core.ai_engine import AIEngine

engine = AIEngine()   # singleton-ish for now

def create_app():
    app = Flask(
        __name__,
        static_folder='../../web/static',
        template_folder='../../web/templates'
    )

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/chat', methods=['POST'])
    def chat():
        data = request.get_json(silent=True) or {}
        message = data.get('message', '').strip()

        if not message:
            return jsonify({"error": "No message provided"}), 400

        result = engine.process(message)
        return jsonify(result)

    @app.route('/api/status')
    def status():
        return jsonify({
            "status": "online",
            "engine": engine.name,
            "memory_items": len(engine.memory)
        })

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

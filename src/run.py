from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # Permite acesso externo no Docker
        port=5000,       # Porta padrão
        debug=False      # Desativa debug em produção
    )
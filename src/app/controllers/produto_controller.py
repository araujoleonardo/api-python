from flask import jsonify, request
from app.models.produto import Produto
from app import db

class ProdutoController:
    @staticmethod
    def criar():
        dados = request.get_json()
        
        if not dados or 'nome' not in dados or 'preco' not in dados:
            return jsonify({'erro': 'Dados incompletos'}), 400
        
        novo_produto = Produto(
            nome=dados['nome'],
            preco=dados['preco'],
            descricao=dados.get('descricao', '')
        )
        
        db.session.add(novo_produto)
        db.session.commit()
        
        return jsonify(novo_produto.to_dict()), 201

    @staticmethod
    def listar():
        produtos = Produto.query.all()
        return jsonify([produto.to_dict() for produto in produtos])

    @staticmethod
    def obter(id):
        produto = Produto.query.get_or_404(id)
        return jsonify(produto.to_dict())

    @staticmethod
    def atualizar(id):
        produto = Produto.query.get_or_404(id)
        dados = request.get_json()
        
        if 'nome' in dados:
            produto.nome = dados['nome']
        if 'preco' in dados:
            produto.preco = dados['preco']
        if 'descricao' in dados:
            produto.descricao = dados['descricao']
        
        db.session.commit()
        return jsonify(produto.to_dict())

    @staticmethod
    def deletar(id):
        produto = Produto.query.get_or_404(id)
        db.session.delete(produto)
        db.session.commit()
        return jsonify({'mensagem': 'Produto deletado com sucesso'})
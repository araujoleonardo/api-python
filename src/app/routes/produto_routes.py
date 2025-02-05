from flask import Blueprint
from app.controllers.produto_controller import ProdutoController

bp = Blueprint('produtos', __name__)

bp.route('/produtos', methods=['POST'])(ProdutoController.criar)
bp.route('/produtos', methods=['GET'])(ProdutoController.listar)
bp.route('/produtos/<int:id>', methods=['GET'])(ProdutoController.obter)
bp.route('/produtos/<int:id>', methods=['PUT'])(ProdutoController.atualizar)
bp.route('/produtos/<int:id>', methods=['DELETE'])(ProdutoController.deletar)
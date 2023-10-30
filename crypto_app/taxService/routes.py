from flask import Blueprint, request, jsonify

tax = Blueprint('tax', __name__)


@tax.route('/calculate_tax', methods=['POST'])
def calculate_tax():
    data = request.get_json()

    selling_time = data.get('sellingTime')
    sold_asset = data.get('soldAsset')
    sold_quantity = data.get('soldQuantity')
    spot_price = data.get('spotPrice')

    print(selling_time, sold_asset, sold_quantity, spot_price)

    return jsonify(selling_time, sold_asset, sold_quantity, spot_price)
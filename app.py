from flask import Flask, request, jsonify
from flask_cors import CORS
from services.transfer_service import TransferService
from middleware.auth_middleware import auth_required
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

transfer_service = TransferService()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/api/v1/transfers', methods=['POST'])
@auth_required
def create_transfer():
    try:
        data = request.get_json()
        
        if not data or not all(k in data for k in ['from_account', 'to_account', 'amount']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        transfer = transfer_service.create_transfer(
            from_account=data['from_account'],
            to_account=data['to_account'],
            amount=data['amount']
        )
        
        return jsonify({
            'id': transfer.id,
            'status': transfer.status,
            'created_at': transfer.created_at.isoformat()
        }), 201
        
    except Exception as e:
        logger.error(f'Error creating transfer: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/v1/transfers/<transfer_id>', methods=['GET'])
@auth_required
def get_transfer(transfer_id):
    try:
        transfer = transfer_service.get_transfer(transfer_id)
        
        if not transfer:
            return jsonify({'error': 'Transfer not found'}), 404
        
        return jsonify({
            'id': transfer.id,
            'from_account': transfer.from_account,
            'to_account': transfer.to_account,
            'amount': transfer.amount,
            'status': transfer.status,
            'created_at': transfer.created_at.isoformat()
        })
        
    except Exception as e:
        logger.error(f'Error retrieving transfer: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False) 
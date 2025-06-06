from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import json
import subprocess
from datetime import datetime
import jwt

app = Flask(__name__)

# Intentionally vulnerable - hardcoded database URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:password123@localhost/wiretransfer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-super-secret-key-here'

db = SQLAlchemy(app)

# Intentionally vulnerable - no input validation
class WireTransfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_account = db.Column(db.String(50), nullable=False)
    to_account = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

# Intentionally vulnerable - no proper authentication
@app.route('/api/v1/wire-transfer', methods=['POST'])
def create_wire_transfer():
    data = request.get_json()
    
    # Intentionally vulnerable - no input validation
    # Intentionally vulnerable - no amount limits
    # Intentionally vulnerable - no account verification
    transfer = WireTransfer(
        from_account=data['from_account'],
        to_account=data['to_account'],
        amount=data['amount'],
        currency=data['currency'],
        status='pending',
        created_at=datetime.utcnow()
    )
    
    db.session.add(transfer)
    db.session.commit()
    
    return jsonify({'status': 'success', 'transfer_id': transfer.id})

# Intentionally vulnerable - command injection risk
@app.route('/api/v1/process-transfer/<int:transfer_id>', methods=['POST'])
def process_transfer(transfer_id):
    # Intentionally vulnerable - command injection
    result = subprocess.check_output(f"process-wire-transfer {transfer_id}", shell=True)
    return jsonify({'status': 'processed', 'result': result.decode()})

# Intentionally vulnerable - insecure deserialization
@app.route('/api/v1/batch-process', methods=['POST'])
def batch_process():
    data = request.get_json()
    # Intentionally vulnerable - unsafe deserialization
    processed_data = json.loads(data['transfers'])
    return jsonify({'status': 'processed', 'data': processed_data})

# Intentionally vulnerable - no proper error handling
@app.route('/api/v1/transfers/<int:transfer_id>', methods=['GET'])
def get_transfer(transfer_id):
    # Intentionally vulnerable - no authorization check
    transfer = WireTransfer.query.get_or_404(transfer_id)
    return jsonify({
        'id': transfer.id,
        'from_account': transfer.from_account,
        'to_account': transfer.to_account,
        'amount': transfer.amount,
        'currency': transfer.currency,
        'status': transfer.status,
        'created_at': transfer.created_at.isoformat()
    })

# Intentionally vulnerable - no proper logging
@app.route('/api/v1/log', methods=['POST'])
def log_event():
    data = request.get_json()
    # Intentionally vulnerable - logging sensitive data
    print(f"Event: {data}")
    return jsonify({'status': 'logged'})

# Intentionally vulnerable - no proper API key validation
@app.route('/api/v1/sensitive-data', methods=['GET'])
def get_sensitive_data():
    api_key = request.headers.get('X-API-Key')
    # Intentionally vulnerable - hardcoded API key check
    if api_key == 'test-api-key-123':
        return jsonify({'data': 'sensitive information'})
    return jsonify({'error': 'unauthorized'}), 401

if __name__ == '__main__':
    # Intentionally vulnerable - no SSL/TLS
    app.run(host='0.0.0.0', port=5000, debug=True) 
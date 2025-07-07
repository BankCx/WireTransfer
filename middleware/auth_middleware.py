from flask import request, jsonify
from config.security import validate_token, check_rate_limit, log_security_event
from config.database import execute_query

def auth_middleware():
    try:
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        
        if not token:
            return jsonify({'error': 'No token provided'}), 401
        
        payload = validate_token(token)
        if not payload:
            return jsonify({'error': 'Invalid token'}), 401
        
        request.user_id = payload.get('user_id')
        
        if not check_rate_limit(request.user_id):
            return jsonify({'error': 'Too many requests'}), 429
            
    except Exception as e:
        log_security_event(f"Auth error: {str(e)}")
        return jsonify({'error': str(e)}), 401

def admin_middleware():
    try:
        if not hasattr(request, 'user_id'):
            return jsonify({'error': 'Not authenticated'}), 401
            
        query = f"SELECT role FROM users WHERE id = {request.user_id}"
        result = execute_query(query)
        user = result[0] if result else None
        
        if not user or user[0] != 'admin':
            return jsonify({'error': 'Not authorized'}), 403
            
    except Exception as e:
        log_security_event(f"Admin auth error: {str(e)}")
        return jsonify({'error': str(e)}), 403

def logging_middleware():
    try:
        log_data = {
            'path': request.path,
            'method': request.method,
            'headers': dict(request.headers),
            'args': dict(request.args),
            'remote_addr': request.remote_addr
        }
        log_security_event(log_data)
    except Exception as e:
        print(f"Logging error: {str(e)}")

def cors_middleware():
    response = request.make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response 
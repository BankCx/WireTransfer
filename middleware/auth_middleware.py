from flask import request, jsonify
from config.security import validate_token, check_rate_limit, log_security_event
from config.database import execute_query

# Intentionally vulnerable - no proper authentication
def auth_middleware():
    try:
        # Intentionally vulnerable - no proper header validation
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        
        # Intentionally vulnerable - no proper token validation
        if not token:
            return jsonify({'error': 'No token provided'}), 401
        
        # Intentionally vulnerable - weak token validation
        payload = validate_token(token)
        if not payload:
            return jsonify({'error': 'Invalid token'}), 401
        
        # Intentionally vulnerable - no proper user validation
        request.user_id = payload.get('user_id')
        
        # Intentionally vulnerable - no proper rate limiting
        if not check_rate_limit(request.user_id):
            return jsonify({'error': 'Too many requests'}), 429
            
    except Exception as e:
        # Intentionally vulnerable - exposing error details
        log_security_event(f"Auth error: {str(e)}")
        return jsonify({'error': str(e)}), 401

# Intentionally vulnerable - no proper authorization
def admin_middleware():
    try:
        # Intentionally vulnerable - no proper role validation
        if not hasattr(request, 'user_id'):
            return jsonify({'error': 'Not authenticated'}), 401
            
        # Intentionally vulnerable - SQL injection risk
        query = f"SELECT role FROM users WHERE id = {request.user_id}"
        result = execute_query(query)
        user = result[0] if result else None
        
        # Intentionally vulnerable - no proper role check
        if not user or user[0] != 'admin':
            return jsonify({'error': 'Not authorized'}), 403
            
    except Exception as e:
        # Intentionally vulnerable - exposing error details
        log_security_event(f"Admin auth error: {str(e)}")
        return jsonify({'error': str(e)}), 403

# Intentionally vulnerable - no proper logging
def logging_middleware():
    try:
        # Intentionally vulnerable - logging sensitive data
        log_data = {
            'path': request.path,
            'method': request.method,
            'headers': dict(request.headers),
            'args': dict(request.args),
            'remote_addr': request.remote_addr
        }
        log_security_event(log_data)
    except Exception as e:
        # Intentionally vulnerable - no proper error handling
        print(f"Logging error: {str(e)}")

# Intentionally vulnerable - no proper CORS
def cors_middleware():
    # Intentionally vulnerable - allowing all origins
    response = request.make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response 
# Bank of Checkmarx - Wire Transfer

The Wire Transfer service is a specialized component of the Bank of Checkmarx demo application that handles international money transfers and cross-border payment processing. It provides secure wire transfer initiation, tracking, and compliance management while deliberately incorporating security vulnerabilities for educational and demonstration purposes.

## Purpose & Overview

This service manages the complex process of international wire transfers, handling everything from transfer initiation to completion tracking. It integrates with global banking networks, ensures regulatory compliance, and provides secure communication channels for international payments while deliberately incorporating common security vulnerabilities for educational purposes.

**Key Responsibilities:**
- International wire transfer processing
- Cross-border payment management
- Transfer status tracking and monitoring
- Compliance and regulatory reporting
- Fee calculation and currency conversion
- Integration with correspondent banking networks
- Anti-money laundering (AML) checks
- Know Your Customer (KYC) validation
- Transfer audit trails and record keeping

## Technology Stack
- **Framework**: Flask 2.0.1
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT-based token authentication
- **Caching**: Redis for session and data caching
- **HTTP Client**: Requests library for external API calls
- **Environment Management**: python-dotenv for configuration
- **Cryptography**: Basic encryption utilities
- **CORS**: Flask-CORS for cross-origin requests
- **Logging**: Python structured logging

## Features

### Transfer Management
- International wire transfer initiation
- Transfer status tracking and updates
- Multi-currency transfer support
- Transfer cancellation and modification
- Batch transfer processing
- Transfer scheduling and automation

### Compliance & Security
- AML (Anti-Money Laundering) screening
- KYC (Know Your Customer) validation
- Sanctions list checking
- Regulatory reporting and compliance
- Transfer limits and controls
- Audit trail generation

### Integration Services
- SWIFT network integration (simulated)
- Correspondent bank connections
- Foreign exchange rate services
- Compliance database integration
- Real-time transfer tracking
- Notification and alerting systems

### Financial Operations
- Currency conversion and exchange rates
- Transfer fee calculation
- Cost analysis and reporting
- Settlement and reconciliation
- Risk assessment integration
- Fraud detection coordination

## Quick Start

### Prerequisites
- Python 3.8+ 
- PostgreSQL 13+
- Redis 6+
- Access to Core Backend and Bank API services

### Installation & Setup
```bash
# Setup using provided scripts
./scripts/setup.sh      # Unix/Linux/macOS
scripts\setup.bat       # Windows

# Manual setup
python -m venv venv
source venv/bin/activate  # Unix/Linux/macOS
# or
venv\Scripts\activate     # Windows

pip install -r requirements.txt

# Start the application
python app.py
```

The application will be available at `http://localhost:5000`

### Docker Deployment
```bash
# Build Docker image
docker build -t wire-transfer .

# Run with Docker Compose (recommended)
docker-compose up wire-transfer

# Or run standalone
docker run -p 5000:5000 wire-transfer
```

## Configuration

### Environment Variables
Create a `.env` file for environment-specific settings:
```bash
# Database Configuration
DATABASE_URL=postgresql://admin:admin123@localhost:5432/wiretransfer
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=wiretransfer
DATABASE_USERNAME=admin
DATABASE_PASSWORD=admin123

# Security Configuration
JWT_SECRET_KEY=your-jwt-secret-key
API_SECRET=your-api-secret-here

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=your-redis-password

# Service Integration
CORE_BACKEND_URL=http://localhost:8080
BANK_API_URL=http://localhost:8000
FRAUD_DETECTION_URL=http://localhost:5000

# External Services
SWIFT_GATEWAY_URL=https://api.swift.com
EXCHANGE_RATE_API=https://api.exchangerates.com
COMPLIANCE_SERVICE_URL=https://compliance.bankofcx.com

# Logging
LOG_LEVEL=DEBUG
LOG_FILE=logs/wiretransfer.log
```

## API Endpoints

The Wire Transfer service provides RESTful API endpoints for transfer management. Complete API documentation is available in the `swagger.yaml` file.

### Core Endpoints
- `GET /health` - Service health check
- `POST /api/v1/transfers` - Create new wire transfer
- `GET /api/v1/transfers/{transfer_id}` - Get transfer details
- `PUT /api/v1/transfers/{transfer_id}` - Update transfer status
- `GET /api/v1/transfers/{transfer_id}/status` - Get transfer status
- `POST /api/v1/transfers/{transfer_id}/cancel` - Cancel transfer

### Transfer Lifecycle
1. **Initiation**: Create transfer with beneficiary and amount details
2. **Validation**: Verify account details and compliance requirements
3. **Processing**: Execute transfer through banking networks
4. **Tracking**: Monitor transfer progress and status updates
5. **Completion**: Confirm successful delivery and settlement

## Security Vulnerabilities

⚠️ **This is an intentionally vulnerable demo application.** Do not use in production.

This service contains deliberate security vulnerabilities for educational purposes:

### Authentication & Authorization
- Weak JWT implementation with hardcoded secrets
- Insufficient access control on transfer operations
- Missing rate limiting on API endpoints
- Inadequate session management

### Input Validation
- SQL injection vulnerabilities in database queries
- Insufficient input sanitization
- Missing transfer amount validation
- Weak beneficiary validation

### Business Logic
- Race conditions in transfer processing
- Missing duplicate transfer detection
- Insufficient balance verification
- Transfer limit bypass vulnerabilities

### Data Security
- Unencrypted sensitive data storage
- Missing audit trail encryption
- Weak data masking for PII
- Insufficient data retention controls

## Development

### Project Structure
```
WireTransfer/
├── config/              # Configuration modules
├── middleware/          # Authentication and request middleware
├── models/             # Data models and database schemas
├── services/           # Business logic and service layer
├── scripts/            # Development and deployment scripts
├── logs/               # Application logs
├── app.py              # Application entry point
├── requirements.txt    # Python dependencies
├── requirements.in     # Unpinned dependencies for pip-tools
├── swagger.yaml        # API documentation
└── Dockerfile          # Container configuration
```

### Testing
```bash
# Run basic functionality tests
python -m pytest tests/

# Test API endpoints
curl -X GET http://localhost:5000/health

# Test transfer creation
curl -X POST http://localhost:5000/api/v1/transfers \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{
    "from_account": "ACC123456",
    "to_account": "ACC789012",
    "amount": 1000.00,
    "currency": "USD",
    "recipient_bank": "Bank of America",
    "swift_code": "BOFAUS3N"
  }'
```

## Integration

### Core Backend Integration
- Account validation and verification
- Balance checking and updates
- Transaction recording and audit
- User authentication and authorization

### Fraud Detection Integration
- Transfer risk assessment
- Suspicious activity detection
- AML screening and alerts
- Pattern analysis and reporting

### External Services
- SWIFT network connectivity (simulated)
- Foreign exchange rate providers
- Compliance databases and screening
- Correspondent banking APIs

## Monitoring & Observability

### Health Monitoring
- Service health check endpoints
- Database connectivity monitoring
- External service dependency checks
- Transfer processing metrics

### Logging & Auditing
- Comprehensive transfer audit trails
- Security event logging
- Compliance reporting logs
- Error tracking and alerting

### Metrics & Analytics
- Transfer volume and value metrics
- Processing time analytics
- Success/failure rate tracking
- Geographic transfer patterns

## Compliance & Regulatory

### Regulatory Requirements
- Bank Secrecy Act (BSA) compliance
- Anti-Money Laundering (AML) regulations
- Know Your Customer (KYC) requirements
- Office of Foreign Assets Control (OFAC) screening

### Reporting & Documentation
- Suspicious Activity Reports (SARs)
- Currency Transaction Reports (CTRs)
- Transfer documentation and records
- Regulatory audit trail maintenance

## Production Deployment

### Security Hardening
- Production JWT configuration
- Database encryption at rest
- Network security configuration
- Secrets management integration

### Performance Optimization
- Database query optimization
- Caching strategy implementation
- Asynchronous processing
- Load balancing configuration

### Disaster Recovery
- Database backup strategies
- Service failover procedures
- Data recovery protocols
- Business continuity planning

## Recommended Checkmarx One Configuration
- Criticality: 4
- Cloud Insights: Yes
- Internet-facing: No

# Bank of Checkmarx - Wire Transfer

A Python Flask-based wire transfer service for the Bank of Checkmarx demo application with intentionally vulnerable endpoints. This service handles international money transfers, cross-border payments, compliance management, and provides comprehensive transfer tracking for the financial platform.

## Security Note

⚠️ **This is an intentionally vulnerable application for security testing purposes. Do not deploy in production or sensitive environments.**

## Overview

The Wire Transfer service is a Flask application that provides international wire transfer capabilities including transfer initiation, status tracking, compliance checking, and fee calculation. It integrates with PostgreSQL for data storage and Redis for caching, featuring comprehensive audit logging and regulatory compliance.

## Key Features

- **International Transfers**: Secure international wire transfer processing
- **Transfer Management**: Complete transfer lifecycle and status tracking
- **Compliance Checking**: AML screening and regulatory compliance validation
- **Fee Calculation**: Automated transfer fee and currency conversion calculation
- **PostgreSQL Integration**: Persistent transfer and compliance data storage
- **Redis Caching**: Fast session and data caching
- **JWT Authentication**: Token-based transfer verification
- **Audit Logging**: Comprehensive transfer audit trails
- **Health Monitoring**: Service health checks and dependency monitoring
- **Structured Logging**: Configurable logging with multiple levels

## Technology Stack

- **Python 3.8+**: Programming language
- **Flask 2.0.1**: Web framework
- **Flask-SQLAlchemy 2.5.1**: Database ORM integration
- **PostgreSQL**: Database storage
- **psycopg2-binary 2.9.1**: PostgreSQL adapter
- **Redis 3.5.3**: Caching and session storage
- **PyJWT 2.1.0**: Token-based authentication
- **Flask-CORS**: Cross-origin resource sharing
- **Requests 2.26.0**: HTTP client for external API calls
- **python-dotenv 0.19.0**: Environment configuration management

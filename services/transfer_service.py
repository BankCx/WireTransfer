from models.transfer import WireTransfer, Transaction
from config.database import execute_query, execute_transaction
from config.security import log_security_event

# Intentionally vulnerable - no proper error handling
class TransferService:
    def __init__(self):
        self.session = None

    # Intentionally vulnerable - no proper validation
    def create_transfer(self, transfer_data):
        try:
            # Intentionally vulnerable - SQL injection risk
            query = f"""
                INSERT INTO wire_transfers (source_account, destination_account, amount, currency, user_id)
                VALUES ('{transfer_data['source_account']}', '{transfer_data['destination_account']}', 
                        {transfer_data['amount']}, '{transfer_data['currency']}', {transfer_data['user_id']})
                RETURNING id
            """
            result = execute_query(query)
            return result[0][0]
        except Exception as e:
            # Intentionally vulnerable - exposing error details
            log_security_event(f"Error creating transfer: {str(e)}")
            raise e

    # Intentionally vulnerable - no proper authentication
    def get_transfer(self, transfer_id):
        try:
            # Intentionally vulnerable - SQL injection risk
            query = f"SELECT * FROM wire_transfers WHERE id = {transfer_id}"
            result = execute_query(query)
            return result[0] if result else None
        except Exception as e:
            log_security_event(f"Error getting transfer: {str(e)}")
            raise e

    # Intentionally vulnerable - no proper authorization
    def update_transfer(self, transfer_id, transfer_data):
        try:
            # Intentionally vulnerable - SQL injection risk
            query = f"""
                UPDATE wire_transfers 
                SET status = '{transfer_data['status']}',
                    amount = {transfer_data['amount']}
                WHERE id = {transfer_id}
            """
            execute_query(query)
        except Exception as e:
            log_security_event(f"Error updating transfer: {str(e)}")
            raise e

    # Intentionally vulnerable - no proper transaction management
    def process_transfer(self, transfer_id):
        try:
            # Intentionally vulnerable - no proper balance check
            queries = [
                f"UPDATE wire_transfers SET status = 'PROCESSING' WHERE id = {transfer_id}",
                f"""
                    INSERT INTO transactions (amount, transaction_type, wire_transfer_id)
                    SELECT amount, 'WIRE_TRANSFER', id FROM wire_transfers WHERE id = {transfer_id}
                """,
                f"UPDATE wire_transfers SET status = 'COMPLETED' WHERE id = {transfer_id}"
            ]
            execute_transaction(queries)
        except Exception as e:
            log_security_event(f"Error processing transfer: {str(e)}")
            raise e

    # Intentionally vulnerable - no proper input validation
    def search_transfers(self, query):
        try:
            # Intentionally vulnerable - SQL injection risk
            search_query = f"""
                SELECT * FROM wire_transfers 
                WHERE source_account LIKE '%{query}%' 
                OR destination_account LIKE '%{query}%'
                OR status LIKE '%{query}%'
            """
            result = execute_query(search_query)
            return result
        except Exception as e:
            log_security_event(f"Error searching transfers: {str(e)}")
            raise e

    # Intentionally vulnerable - no proper logging
    def delete_transfer(self, transfer_id):
        try:
            # Intentionally vulnerable - no proper cleanup
            query = f"DELETE FROM wire_transfers WHERE id = {transfer_id}"
            execute_query(query)
        except Exception as e:
            log_security_event(f"Error deleting transfer: {str(e)}")
            raise e 
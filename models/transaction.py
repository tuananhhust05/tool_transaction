
class Transaction:
    def __init__ (self, id,creator_id,amount,fee,type,status,created_by,created_at,updated_by,updated_at):
        self.id = id
        self.creator_id = creator_id
        self.amount = amount
        self.fee = fee
        self.type = type
        self.status = status
        self.created_by = created_by
        self.created_at = created_at
        self.updated_by = updated_by
        self.updated_at = updated_at
        



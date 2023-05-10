
class Transaction:
    def __init__ (self, id,status,amount,fee_settlement,fee_refund,received_amount,settle_date,created_date,creator_id,stripe_id,type):
        self.id = id
        self.status = status
        self.amount = amount
        self.fee_settlement = fee_settlement
        self.fee_refund = fee_refund
        self.received_amount = received_amount
        self.settle_date = settle_date
        self.created_date = created_date
        self.creator_id = creator_id
        self.stripe_id = stripe_id
        self.type = type 



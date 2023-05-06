INSERT INTO ecom.transaction (id,creator_id,amount,fee,type,status,created_by,created_at,updated_by,updated_at)
VALUES (2,1,1,1,'ATM_CARD','pending',1,'1998-01-23 12:45:56',1,'1998-01-23 12:45:56');


UPDATE ecom.transaction SET  status ='settled' WHERE id = 1;
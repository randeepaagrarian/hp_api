ALTER TABLE contract_installment
ADD interest DECIMAL(13,2) NOT NULL DEFAULT 0
AFTER amount;

ALTER TABLE contract_installment
ADD default_interest DECIMAL(13,2) NOT NULL DEFAULT 0
AFTER interest;

ALTER TABLE contract_installment 
CHANGE amount capital DECIMAL(13,2) NOT NULL;
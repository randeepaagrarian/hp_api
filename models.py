# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessLayer(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'access_layer'


class AccessLayerValues(models.Model):
    access_layer = models.ForeignKey(AccessLayer, models.DO_NOTHING, primary_key=True)
    value = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'access_layer_values'
        unique_together = (('access_layer', 'value'),)


class AdminLogs(models.Model):
    username = models.CharField(max_length=32)
    url = models.CharField(max_length=64)
    date = models.DateTimeField()
    method = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'admin_logs'


class Banking(models.Model):
    officer = models.ForeignKey('User', models.DO_NOTHING, db_column='officer')
    region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region')
    territory = models.ForeignKey('Territory', models.DO_NOTHING, db_column='territory')
    bank = models.CharField(max_length=64)
    branch = models.CharField(max_length=64)
    amount = models.IntegerField()
    date = models.DateTimeField()
    sys_date = models.DateTimeField()
    source_document = models.CharField(max_length=360)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banking'


class Contract(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')
    id_1 = models.CharField(unique=True, max_length=32)
    id_2 = models.CharField(max_length=32, blank=True, null=True)
    model = models.ForeignKey('Model', models.DO_NOTHING)
    contract_batch = models.ForeignKey('ContractBatch', models.DO_NOTHING)
    recovery_officer = models.ForeignKey('User', models.DO_NOTHING, db_column='recovery_officer')
    sale = models.ForeignKey('Sale', models.DO_NOTHING, blank=True, null=True)
    customer_name = models.CharField(max_length=128)
    customer_address = models.CharField(max_length=128)
    customer_contact = models.CharField(max_length=15)
    guarantor1_name = models.CharField(max_length=128, blank=True, null=True)
    guarantor1_address = models.CharField(max_length=128, blank=True, null=True)
    guarantor1_contact = models.CharField(max_length=15, blank=True, null=True)
    guarantor2_name = models.CharField(max_length=128, blank=True, null=True)
    guarantor2_address = models.CharField(max_length=128, blank=True, null=True)
    guarantor2_contact = models.CharField(max_length=15, blank=True, null=True)
    edit_lock = models.IntegerField()
    closed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contract'


class ContractBanking(models.Model):
    date = models.DateField()
    sys_date = models.DateTimeField()
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='username')
    contract_chassis_no = models.CharField(max_length=32)
    bank = models.CharField(max_length=32, blank=True, null=True)
    branch = models.CharField(max_length=32, blank=True, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    tr_no = models.CharField(max_length=8)
    contract_banking_type = models.ForeignKey('ContractBankingType', models.DO_NOTHING)
    source_document = models.CharField(max_length=360)

    class Meta:
        managed = False
        db_table = 'contract_banking'


class ContractBankingType(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'contract_banking_type'


class ContractBatch(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'contract_batch'


class ContractComment(models.Model):
    contract = models.ForeignKey(Contract, models.DO_NOTHING)
    installment = models.ForeignKey('ContractInstallment', models.DO_NOTHING, blank=True, null=True)
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='username')
    date = models.DateTimeField()
    text = models.CharField(max_length=2048)
    commitment = models.IntegerField()
    due_date = models.DateTimeField(blank=True, null=True)
    fulfilled = models.IntegerField()
    fulfilled_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contract_comment'


class ContractHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    date_in = models.DateTimeField()
    modified_by = models.ForeignKey('User', models.DO_NOTHING, db_column='modified_by')
    date = models.DateTimeField()
    user = models.CharField(max_length=16)
    id_1 = models.CharField(max_length=32)
    id_2 = models.CharField(max_length=32, blank=True, null=True)
    model_id = models.CharField(max_length=64)
    contract_batch_id = models.IntegerField()
    recovery_officer = models.CharField(max_length=16)
    sale_id = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=128)
    customer_address = models.CharField(max_length=128)
    customer_contact = models.CharField(max_length=15)
    guarantor1_name = models.CharField(max_length=128, blank=True, null=True)
    guarantor1_address = models.CharField(max_length=128, blank=True, null=True)
    guarantor1_contact = models.CharField(max_length=15, blank=True, null=True)
    guarantor2_name = models.CharField(max_length=128, blank=True, null=True)
    guarantor2_address = models.CharField(max_length=128, blank=True, null=True)
    guarantor2_contact = models.CharField(max_length=15, blank=True, null=True)
    edit_lock = models.IntegerField()
    closed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contract_history'
        unique_together = (('id', 'date_in', 'modified_by'),)


class ContractInstallment(models.Model):
    contract = models.ForeignKey(Contract, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    due_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contract_installment'


class ContractInstallmentHistory(models.Model):
    date_in = models.DateTimeField()
    changed_by = models.ForeignKey('User', models.DO_NOTHING, db_column='changed_by')
    change_reason = models.CharField(max_length=1024)
    contract_installment = models.ForeignKey(ContractInstallment, models.DO_NOTHING)
    contract = models.ForeignKey(Contract, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    due_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contract_installment_history'


class ContractInstallmentPayment(models.Model):
    contract_installment = models.ForeignKey(ContractInstallment, models.DO_NOTHING)
    contract_receipt = models.ForeignKey('ContractReceipt', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    issued_user = models.ForeignKey('User', models.DO_NOTHING, db_column='issued_user')
    issued_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contract_installment_payment'


class ContractReceipt(models.Model):
    date = models.DateField()
    contract = models.ForeignKey(Contract, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    tr_number = models.CharField(max_length=32, blank=True, null=True)
    tr_book_number = models.CharField(max_length=32, blank=True, null=True)
    issued_user = models.ForeignKey('User', models.DO_NOTHING, db_column='issued_user')
    issued_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contract_receipt'


class Dealer(models.Model):
    dealer_type = models.ForeignKey('DealerType', models.DO_NOTHING)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    telephone = models.CharField(max_length=64)
    territory = models.ForeignKey('Territory', models.DO_NOTHING)
    exclusive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dealer'


class DealerType(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'dealer_type'


class DeliveryDocument(models.Model):
    delivery_document_type = models.ForeignKey('DeliveryDocumentType', models.DO_NOTHING)
    dealer = models.ForeignKey(Dealer, models.DO_NOTHING)
    from_dealer = models.ForeignKey(Dealer, models.DO_NOTHING)
    date = models.DateTimeField()
    issuer = models.CharField(max_length=32)
    notes = models.CharField(max_length=1024, blank=True, null=True)
    officer_responsible = models.CharField(max_length=32)
    officer_telephone = models.IntegerField()
    vehicle_no = models.CharField(max_length=32)
    driver_name = models.CharField(max_length=32)
    driver_nic = models.CharField(max_length=32)
    driver_telephone = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'delivery_document'


class DeliveryDocumentType(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'delivery_document_type'


class Designation(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'designation'


class Driver(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    telephone_no = models.CharField(max_length=45)
    emergency_contact_name = models.CharField(max_length=45)
    emergency_contact_relation = models.CharField(max_length=45)
    image = models.CharField(max_length=360, blank=True, null=True)
    dob = models.DateField()

    class Meta:
        managed = False
        db_table = 'driver'


class Expense(models.Model):
    date = models.DateTimeField()
    sys_date = models.DateTimeField()
    username = models.CharField(max_length=16)
    description = models.CharField(max_length=512, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expense'


class ExpenseItem(models.Model):
    expense = models.ForeignKey(Expense, models.DO_NOTHING)
    expense_type = models.ForeignKey('ExpenseType', models.DO_NOTHING)
    amount = models.IntegerField()
    description = models.CharField(max_length=512, blank=True, null=True)
    bill_received = models.IntegerField()
    bill_received_date = models.DateField(blank=True, null=True)
    bill_received_marked_by = models.CharField(max_length=16, blank=True, null=True)
    bill_paid = models.IntegerField()
    bill_paid_date = models.DateField(blank=True, null=True)
    bill_paid_marked_by = models.CharField(max_length=16, blank=True, null=True)
    rejected = models.IntegerField()
    rejected_date = models.DateField(blank=True, null=True)
    rejected_marked_by = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expense_item'


class ExpenseType(models.Model):
    name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'expense_type'


class FieldVisit(models.Model):
    date = models.DateTimeField()
    sys_date = models.DateTimeField()
    officer = models.ForeignKey('User', models.DO_NOTHING, db_column='officer')
    region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region')
    territory = models.ForeignKey('Territory', models.DO_NOTHING, db_column='territory')
    start_meter = models.IntegerField()
    end_meter = models.IntegerField()
    location = models.CharField(max_length=100)
    field_visit_criteria = models.ForeignKey('FieldVisitCriteria', models.DO_NOTHING)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_visit'


class FieldVisitCriteria(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'field_visit_criteria'


class FieldVisitInquiry(models.Model):
    field_visit = models.ForeignKey(FieldVisit, models.DO_NOTHING)
    customer_name = models.CharField(max_length=64)
    customer_telephone = models.IntegerField()
    customer_nic = models.CharField(max_length=16)
    customer_address = models.CharField(max_length=64)
    model = models.ForeignKey('Model', models.DO_NOTHING, db_column='model')
    inquiry = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'field_visit_inquiry'


class MachineryBanking(models.Model):
    banking = models.ForeignKey(Banking, models.DO_NOTHING)
    chassis_no = models.CharField(max_length=64)
    receipt_number = models.CharField(max_length=64)
    payment_type = models.ForeignKey('PaymentType', models.DO_NOTHING, db_column='payment_type')

    class Meta:
        managed = False
        db_table = 'machinery_banking'


class MainStock(models.Model):
    delivery_document = models.ForeignKey(DeliveryDocument, models.DO_NOTHING)
    model = models.ForeignKey('Model', models.DO_NOTHING)
    primary_id = models.CharField(primary_key=True, max_length=32)
    secondary_id = models.CharField(unique=True, max_length=32)
    price = models.IntegerField()
    sold = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'main_stock'
        unique_together = (('primary_id', 'secondary_id'),)


class Model(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=8)
    primary_name = models.CharField(max_length=32)
    secondary_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'model'


class Notification(models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=64)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notification'


class Organization(models.Model):
    organization_type = models.ForeignKey('OrganizationType', models.DO_NOTHING)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'organization'


class OrganizationType(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'organization_type'


class OrganizationalVisit(models.Model):
    date = models.DateTimeField()
    sys_date = models.DateTimeField()
    officer = models.ForeignKey('User', models.DO_NOTHING, db_column='officer')
    region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region')
    territory = models.ForeignKey('Territory', models.DO_NOTHING, db_column='territory')
    start_meter = models.IntegerField()
    end_meter = models.IntegerField()
    organization_type = models.ForeignKey(OrganizationType, models.DO_NOTHING)
    organization_name = models.CharField(max_length=100)
    organization_name_fk = models.IntegerField()
    location = models.CharField(max_length=100)
    purpose = models.CharField(max_length=512)
    outcome = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organizational_visit'


class OrganizationalVisitInquiry(models.Model):
    organizational_visit = models.ForeignKey(OrganizationalVisit, models.DO_NOTHING)
    customer_name = models.CharField(max_length=64)
    customer_telephone = models.IntegerField()
    customer_nic = models.CharField(max_length=16)
    customer_address = models.CharField(max_length=64)
    model = models.ForeignKey(Model, models.DO_NOTHING, db_column='model')
    inquiry = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'organizational_visit_inquiry'


class OrganizationalVisitStock(models.Model):
    organizational_visit = models.ForeignKey(OrganizationalVisit, models.DO_NOTHING)
    model = models.ForeignKey(Model, models.DO_NOTHING)
    chassis_no = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'organizational_visit_stock'


class PaymentType(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'payment_type'


class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'region'


class Route(models.Model):
    driver = models.ForeignKey(Driver, models.DO_NOTHING)
    supporter = models.ForeignKey('Supporter', models.DO_NOTHING, blank=True, null=True)
    vehicle_number = models.CharField(max_length=16)
    route_pass_id = models.CharField(max_length=32)
    source_documents = models.CharField(max_length=64, blank=True, null=True)
    route_start_time = models.DateTimeField()
    route_end_time = models.DateTimeField()
    start_meter = models.IntegerField()
    end_meter = models.IntegerField()
    start_location = models.CharField(max_length=45)
    end_location = models.CharField(max_length=45)
    document_front = models.CharField(max_length=180, blank=True, null=True)
    sys_time = models.DateTimeField()
    billed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'route'


class RouteInvoice(models.Model):
    date = models.DateField()
    issuer = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'route_invoice'


class RouteInvoiceContents(models.Model):
    invoice = models.ForeignKey(RouteInvoice, models.DO_NOTHING)
    route = models.ForeignKey(Route, models.DO_NOTHING)
    rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'route_invoice_contents'


class Sale(models.Model):
    deleted = models.IntegerField()
    officer = models.ForeignKey('User', models.DO_NOTHING, db_column='officer')
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='region')
    territory = models.ForeignKey('Territory', models.DO_NOTHING, db_column='territory')
    date = models.DateTimeField()
    sys_date = models.DateTimeField()
    location = models.CharField(max_length=32)
    chassis_no = models.CharField(max_length=32)
    customer_name = models.CharField(max_length=64)
    customer_address = models.CharField(max_length=128)
    customer_contact = models.CharField(max_length=16)
    model = models.ForeignKey(Model, models.DO_NOTHING, db_column='model')
    invoice_no = models.CharField(max_length=16, blank=True, null=True)
    price = models.CharField(max_length=16)
    sale_type = models.ForeignKey('SaleType', models.DO_NOTHING, db_column='sale_type')
    institute = models.CharField(max_length=64, blank=True, null=True)
    advance = models.CharField(max_length=16)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    location_fk = models.ForeignKey(Dealer, models.DO_NOTHING, db_column='location_fk', blank=True, null=True)
    verified = models.IntegerField()
    verified_by = models.ForeignKey('User', models.DO_NOTHING, db_column='verified_by', blank=True, null=True)
    verified_on = models.DateTimeField(blank=True, null=True)
    sale_completed = models.IntegerField()
    sale_completed_type = models.ForeignKey('SaleCompletedType', models.DO_NOTHING, blank=True, null=True)
    sale_completed_remarks = models.CharField(max_length=2048, blank=True, null=True)
    sale_completed_by = models.ForeignKey('User', models.DO_NOTHING, db_column='sale_completed_by', blank=True, null=True)
    sale_completed_on = models.DateTimeField(blank=True, null=True)
    commision_paid = models.IntegerField()
    commission_paid_remarks = models.CharField(max_length=2048, blank=True, null=True)
    commission_paid_marked_by = models.ForeignKey('User', models.DO_NOTHING, db_column='commission_paid_marked_by', blank=True, null=True)
    commission_paid_marked_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale'


class SaleComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, models.DO_NOTHING)
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='username')
    date = models.DateTimeField()
    text = models.CharField(max_length=2048, blank=True, null=True)
    attachment = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_comment'


class SaleCompletedType(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'sale_completed_type'


class SaleHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    date_in = models.DateTimeField()
    modified_by = models.ForeignKey('User', models.DO_NOTHING, db_column='modified_by')
    deleted = models.IntegerField()
    officer = models.CharField(max_length=16)
    region = models.IntegerField()
    territory = models.IntegerField()
    date = models.DateTimeField()
    sys_date = models.DateTimeField()
    location = models.CharField(max_length=32)
    chassis_no = models.CharField(max_length=32)
    customer_name = models.CharField(max_length=64)
    customer_address = models.CharField(max_length=128)
    customer_contact = models.CharField(max_length=16)
    model = models.CharField(max_length=64)
    invoice_no = models.CharField(max_length=16, blank=True, null=True)
    price = models.CharField(max_length=16)
    sale_type = models.IntegerField()
    institute = models.CharField(max_length=64, blank=True, null=True)
    advance = models.CharField(max_length=16)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    location_fk = models.IntegerField(blank=True, null=True)
    verified = models.IntegerField()
    verified_by = models.CharField(max_length=32, blank=True, null=True)
    verified_on = models.DateTimeField(blank=True, null=True)
    sale_completed = models.IntegerField()
    sale_completed_type_id = models.IntegerField(blank=True, null=True)
    sale_completed_remarks = models.CharField(max_length=2048, blank=True, null=True)
    sale_completed_by = models.CharField(max_length=32, blank=True, null=True)
    sale_completed_on = models.DateTimeField(blank=True, null=True)
    commision_paid = models.IntegerField()
    commission_paid_remarks = models.CharField(max_length=2048, blank=True, null=True)
    commission_paid_marked_by = models.ForeignKey('User', models.DO_NOTHING, db_column='commission_paid_marked_by', blank=True, null=True)
    commission_paid_marked_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_history'
        unique_together = (('id', 'date_in', 'modified_by'),)


class SaleType(models.Model):
    name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'sale_type'


class SaleWatch(models.Model):
    sale = models.ForeignKey(Sale, models.DO_NOTHING)
    content = models.CharField(max_length=2048)
    date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')
    closed = models.IntegerField()
    closed_by = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_watch'


class Service(models.Model):
    date = models.DateTimeField()
    issue = models.CharField(max_length=256)
    sale = models.ForeignKey(Sale, models.DO_NOTHING, blank=True, null=True)
    sale_date = models.DateField(blank=True, null=True)
    chassis_no = models.CharField(max_length=32, blank=True, null=True)
    model = models.ForeignKey(Model, models.DO_NOTHING, blank=True, null=True)
    meter = models.IntegerField(blank=True, null=True)
    meter_type = models.CharField(max_length=8, blank=True, null=True)
    customer_name = models.CharField(max_length=64, blank=True, null=True)
    customer_contact = models.IntegerField(blank=True, null=True)
    current_address = models.CharField(max_length=64, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, models.DO_NOTHING, blank=True, null=True)
    technician = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    work_sheet = models.CharField(max_length=128, blank=True, null=True)
    work_sheet_uploaded_by = models.ForeignKey('User', models.DO_NOTHING, db_column='work_sheet_uploaded_by', blank=True, null=True)
    work_sheet_uploaded_on = models.DateTimeField(blank=True, null=True)
    technician_allocated = models.IntegerField()
    technician_allocated_by = models.ForeignKey('User', models.DO_NOTHING, db_column='technician_allocated_by', blank=True, null=True)
    technician_allocated_on = models.DateTimeField(blank=True, null=True)
    service_completed = models.IntegerField()
    service_completed_remarks = models.CharField(max_length=128, blank=True, null=True)
    service_completed_by = models.ForeignKey('User', models.DO_NOTHING, db_column='service_completed_by', blank=True, null=True)
    service_completed_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class ServiceComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, models.DO_NOTHING)
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='username')
    date = models.DateTimeField()
    text = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'service_comment'


class ServiceTechnicianChangeHistory(models.Model):
    date_in = models.DateTimeField()
    service = models.ForeignKey(Service, models.DO_NOTHING)
    changed_by = models.ForeignKey('User', models.DO_NOTHING, db_column='changed_by')
    technician = models.ForeignKey('User', models.DO_NOTHING)
    technician_allocated_by = models.ForeignKey('User', models.DO_NOTHING, db_column='technician_allocated_by')
    technician_allocated_on = models.DateTimeField(blank=True, null=True)
    reason = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'service_technician_change_history'


class SparePartsBanking(models.Model):
    banking = models.ForeignKey(Banking, models.DO_NOTHING)
    invoice_number = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'spare_parts_banking'


class StockHistory(models.Model):
    delivery_document = models.ForeignKey(DeliveryDocument, models.DO_NOTHING)
    model = models.ForeignKey(Model, models.DO_NOTHING)
    primary_id = models.CharField(primary_key=True, max_length=32)
    secondary_id = models.CharField(max_length=32)
    price = models.IntegerField()
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stock_history'
        unique_together = (('primary_id', 'secondary_id', 'date_in'),)


class Supporter(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    telephone_no = models.CharField(max_length=45)
    emergency_contact_name = models.CharField(max_length=45)
    emergency_contact_relation = models.CharField(max_length=45)
    image = models.CharField(max_length=360, blank=True, null=True)
    dob = models.DateField()

    class Meta:
        managed = False
        db_table = 'supporter'


class Task(models.Model):
    created = models.DateTimeField()
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='username')
    due = models.DateTimeField()
    complete = models.IntegerField()
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'


class TaskComment(models.Model):
    task = models.ForeignKey(Task, models.DO_NOTHING)
    date = models.DateTimeField()
    text = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'task_comment'


class Telephonenumbers(models.Model):
    idtelephonenumbers = models.AutoField(primary_key=True)
    telephone1 = models.CharField(max_length=45, blank=True, null=True)
    telephone2 = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'telephonenumbers'
        unique_together = (('idtelephonenumbers', 'user'),)


class Territory(models.Model):
    id = models.IntegerField(primary_key=True)
    region = models.ForeignKey(Region, models.DO_NOTHING)
    name = models.CharField(max_length=32)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'territory'


class User(models.Model):
    id = models.AutoField()
    username = models.CharField(primary_key=True, max_length=16)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=64, blank=True, null=True)
    active = models.IntegerField()
    name = models.CharField(max_length=64)
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='region')
    territory = models.ForeignKey(Territory, models.DO_NOTHING, db_column='territory', blank=True, null=True)
    profile_pic = models.CharField(max_length=128, blank=True, null=True)
    token_an = models.CharField(max_length=32)
    birthday = models.DateField(blank=True, null=True)
    designation = models.CharField(max_length=32, blank=True, null=True)
    designation_fk = models.ForeignKey(Designation, models.DO_NOTHING, db_column='designation_fk')
    profile = models.IntegerField()
    application_form = models.CharField(max_length=128, blank=True, null=True)
    change_password = models.IntegerField()
    last_password_change = models.DateTimeField(blank=True, null=True)
    password_reset_request_date = models.DateTimeField(blank=True, null=True)
    password_reset_request_ip = models.CharField(max_length=32, blank=True, null=True)
    login_enabled = models.IntegerField()
    telephone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserAccess(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, primary_key=True)
    access_layer = models.ForeignKey(AccessLayer, models.DO_NOTHING)
    access_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_access'
        unique_together = (('user', 'access_layer'),)


class UserNotification(models.Model):
    notification = models.ForeignKey(Notification, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user')
    checked = models.IntegerField()
    read_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_notification'

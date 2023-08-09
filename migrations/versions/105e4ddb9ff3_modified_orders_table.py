"""modified orders table

Revision ID: 105e4ddb9ff3
Revises: 
Create Date: 2023-08-09 01:23:59.488659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '105e4ddb9ff3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('amount', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('mpesa_receipt_number', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('merchant_request_id', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('checkout_request_id', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('result_code', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('result_desc', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('order_status', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('phone_number', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('transaction_date', sa.DateTime(), nullable=True))
        batch_op.drop_column('status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_column('transaction_date')
        batch_op.drop_column('phone_number')
        batch_op.drop_column('order_status')
        batch_op.drop_column('result_desc')
        batch_op.drop_column('result_code')
        batch_op.drop_column('checkout_request_id')
        batch_op.drop_column('merchant_request_id')
        batch_op.drop_column('mpesa_receipt_number')
        batch_op.drop_column('amount')

    # ### end Alembic commands ###

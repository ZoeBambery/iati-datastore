"""Add transaction fields

Revision ID: 3dd506d98d0
Revises: ce28b6ebf50
Create Date: 2013-04-11 16:08:27.464159

"""

# revision identifiers, used by Alembic.
revision = '3dd506d98d0'
down_revision = 'ce28b6ebf50'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('budget', u'value_amount', existing_type=sa.INTEGER(), 
                    type_=sa.NUMERIC(), nullable=False)

    op.add_column('transaction', sa.Column('description', sa.Unicode(), nullable=True))
    op.add_column('transaction', sa.Column('receiver_org_activity_id',
                   sa.Unicode(), nullable=True))
    op.add_column('transaction', sa.Column('receiver_org_ref', sa.Unicode(),
                   sa.ForeignKey('organisation.ref'), nullable=True))
    op.add_column('transaction', sa.Column('receiver_org_text', sa.Unicode(),
                   nullable=True))
    op.alter_column('transaction', u'value_amount', existing_type=sa.INTEGER(),
                    type_=sa.NUMERIC(), nullable=False)
    op.add_column('transaction', sa.Column('provider_org_activity_id',
                   sa.Unicode(), nullable=True))
    op.add_column('transaction', sa.Column('provider_org_ref', sa.Unicode(),
                   sa.ForeignKey('organisation.ref'), nullable=True))
    op.add_column('transaction', sa.Column('provider_org_text',
                   sa.Unicode(), nullable=True))
    op.add_column('transaction', sa.Column('ref', sa.Unicode(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transaction', 'ref')
    op.drop_column('transaction', 'provider_org_text')
    op.drop_column('transaction', 'provider_org_ref')
    op.drop_column('transaction', 'provider_org_activity_id')
    op.drop_column('transaction', 'receiver_org_text')
    op.drop_column('transaction', 'receiver_org_ref')
    op.drop_column('transaction', 'receiver_org_activity_id')
    op.alter_column('budget', u'value_amount',
               existing_type=sa.NUMERIC(),
               type_=sa.INTEGER(),
               nullable=True)
    op.alter_column('transaction', u'value_amount',
               existing_type=sa.NUMERIC(),
               type_=sa.INTEGER(),
               nullable=False)
    op.drop_column('transaction', 'description')
    ### end Alembic commands ###

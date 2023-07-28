import cloudinary

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:SHAR0007@localhost/farmer_to_consumer_app'
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://sharoun:SHAR0007@localhost/farmer_to_consumer_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    cloudinary.config(
        cloud_name='dlgspxpwr',
        api_key='162229873424843',
        api_secret='PK64yfEbGdYzy7syywRCAhLOYGc'
    )
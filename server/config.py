import cloudinary

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/farmers_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    cloudinary.config(
        cloud_name='dlgspxpwr',
        api_key='162229873424843',
        api_secret='PK64yfEbGdYzy7syywRCAhLOYGc'
    )

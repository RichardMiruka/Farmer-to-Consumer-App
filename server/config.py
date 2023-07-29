import cloudinary

class Config:
    #SQLALCHEMY_DATABASE_URI = 'postgresql://richard:PHnUn9tYFVnLaIiw0dugeXqiYUIrWSdB@dpg-cie29q59aq0ce39k53sg-a.ohio-postgres.render.com/bird_app_h6ml'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@192.168.100.16/farmer-to-consumer-app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    cloudinary.config(
        cloud_name='dlgspxpwr',
        api_key='162229873424843',
        api_secret='PK64yfEbGdYzy7syywRCAhLOYGc'
    )
    
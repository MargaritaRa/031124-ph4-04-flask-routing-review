#!/usr/bin/env python3

from app import app
from models import db, Meme
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Meme.query.delete()

        memes = []

        m = Meme(img_url="https://images-ext-1.discordapp.net/external/dJicYorfrVqn0N9z3YQ6fRttI-aMYjy6iedZy4enWxM/%3Ffit%3D700%252C700/https/www.rd.com/wp-content/uploads/2023/04/Hilarious-Cat-Memes-7.jpg?format=webp&width=641&height=641", caption="self care")
        memes.append(m)

        m = Meme(img_url="https://images-ext-1.discordapp.net/external/B8mf8L4sZwjuU2QepNLbPdJ8tXNZk53lRm9fWRp6bak/https/i.redd.it/dfe2ym46fd0d1.jpeg?format=webp&width=514&height=641", caption="me")
        memes.append(m)

        m = Meme(img_url="https://images-ext-1.discordapp.net/external/nMOHpwhshFjsH3B7UTWOStqW6YIN7lbmIc3ee3EZOkk/%3Fq%3Dtbn%3AANd9GcTx3AaNukEA_HVs8Q0B_o5frQefG8brKaWZ6Q%26usqp%3DCAU/https/encrypted-tbn0.gstatic.com/images?format=webp", caption="rico suavcat")
        memes.append(m)

        m = Meme(img_url="https://images-ext-1.discordapp.net/external/2tywKRCeyHf6dfBzQw5_4FMZ3PszEVMhzhlET6tqLCo/https/i.kym-cdn.com/entries/icons/original/000/041/742/cover3.jpg?format=webp&width=1139&height=641", caption="this cat sucks at ping pong")
        memes.append(m)

        m = Meme(img_url="https://media.discordapp.net/attachments/1174721029583667270/1239952905352646786/gztuoyu9zva61.png?ex=6644cba1&is=66437a21&hm=ff87964c92fe72d4bcf0d9c84a3af7d4a945f3da5f661538dcaa8add19d5b6e4&=&format=webp&quality=lossless&width=823&height=641", caption="everything is connected")
        memes.append(m)

        m = Meme(img_url="https://media.discordapp.net/attachments/1174721029583667270/1239953145711300659/1gumqz9n3yq61.png?ex=6644cbdb&is=66437a5b&hm=a5cae0299859dd7c1a15b87411a893872632943d6f18b8fed4cc69a37e93d029&=&format=webp&quality=lossless&width=504&height=640", caption="no comment")
        memes.append(m)

        db.session.add_all(memes)
        db.session.commit()

        print("Seeding complete!")



# use for testing file
